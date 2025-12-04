import argparse
import os
import sys
import time
from typing import List

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    print("[ERROR] Falta playwright. Instala con: pip install playwright && python -m playwright install chromium", file=sys.stderr)
    sys.exit(1)

PUBLIC_ROUTES = [
    ("index", "/"),
    ("login", "/login"),
    ("registro", "/registro"),
    ("servicios", "/servicios"),
    ("especialidades", "/especialidades"),
    ("atencion", "/atencion"),
    ("contactenos", "/contactenos"),
    ("historia_gerontologica", "/historia_gerontologica"),
    ("paciente", "/paciente"),
    ("dashboard", "/Dashboards"),
    ("terminos", "/terminos"),
    ("somos", "/somos"),
]

ADMIN_ROUTES = [
    ("administrador", "/administrador"),
    ("lista_usuarios", "/lista_usuarios"),
    ("formulario_usuario", "/admin_user_create"),
    # Borrado típico: necesita id, se omite captura directa
]

LOGIN_PATH = "/login"  # Ajustar si difiere
LOGIN_USERNAME_FIELD = "usuario"
LOGIN_PASSWORD_FIELD = "contrasena"


def parse_args():
    p = argparse.ArgumentParser(description="Captura automática de pantallas de rutas Django usando Playwright.")
    p.add_argument("--base-url", default="http://127.0.0.1:8000", help="Base URL del servidor en ejecución")
    p.add_argument("--out-dir", default="docs/images", help="Directorio de salida para PNG")
    p.add_argument("--viewport-width", type=int, default=1280)
    p.add_argument("--viewport-height", type=int, default=900)
    p.add_argument("--wait-ms", type=int, default=500, help="Tiempo de espera tras cargar la página")
    p.add_argument("--include-admin", action="store_true", help="Incluye rutas de administración tras login")
    p.add_argument("--admin-user", default=os.getenv("ADMIN_USER"), help="Usuario admin para login (si se incluye admin)")
    p.add_argument("--admin-pass", default=os.getenv("ADMIN_PASS"), help="Contraseña admin para login")
    p.add_argument("--full-page", action="store_true", help="Captura página completa")
    p.add_argument("--headless", action="store_true", help="Forzar modo headless (por defecto GUI si está disponible)")
    return p.parse_args()


def ensure_out_dir(path: str):
    os.makedirs(path, exist_ok=True)


def login_if_needed(page, base_url: str, user: str, pwd: str):
    if not user or not pwd:
        print("[WARN] Credenciales admin no provistas; se omiten rutas admin.")
        return False
    login_url = base_url.rstrip("/") + LOGIN_PATH
    print(f"[INFO] Intentando login en {login_url}")
    page.goto(login_url)
    # Verificar campos
    try:
        page.fill(f"input[name='{LOGIN_USERNAME_FIELD}']", user)
        page.fill(f"input[name='{LOGIN_PASSWORD_FIELD}']", pwd)
        page.click("button[type='submit']")
        page.wait_for_timeout(700)
    except Exception as e:
        print(f"[ERROR] Falló el login: {e}")
        return False
    return True


def capture_routes(page, routes: List[tuple], base_url: str, out_dir: str, wait_ms: int, full_page: bool):
    for name, path in routes:
        url = base_url.rstrip("/") + path
        print(f"[CAPTURE] {name}: {url}")
        try:
            page.goto(url)
            page.wait_for_timeout(wait_ms)
            # Espera extra si hay carruseles / gráficos
            if name in {"index", "dashboard"}:
                page.wait_for_timeout(1000)
            screenshot_path = os.path.join(out_dir, f"{name}.png")
            page.screenshot(path=screenshot_path, full_page=full_page)
            print(f"[OK] Guardado {screenshot_path}")
        except Exception as e:
            print(f"[FAIL] {name} -> {e}")


def main():
    args = parse_args()
    ensure_out_dir(args.out_dir)

    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=args.headless)
        context = browser.new_context(viewport={"width": args.viewport_width, "height": args.viewport_height})
        page = context.new_page()

        # Capturas públicas
        capture_routes(page, PUBLIC_ROUTES, args.base_url, args.out_dir, args.wait_ms, args.full_page)

        # Capturas admin (opcional)
        if args.include_admin:
            if login_if_needed(page, args.base_url, args.admin_user, args.admin_pass):
                capture_routes(page, ADMIN_ROUTES, args.base_url, args.out_dir, args.wait_ms, args.full_page)
            else:
                print("[WARN] No se capturan rutas admin por fallo de login.")

        browser.close()
    print("[DONE] Capturas completadas.")


if __name__ == "__main__":
    main()
