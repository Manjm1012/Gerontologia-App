"""Genera un PDF `manual_usuario.pdf` combinando el contenido del manual y las capturas.

Requisitos:
    pip install fpdf2 pillow

Uso:
    python scripts/build_manual_pdf.py \
        --manual manual_usuario.md \
        --images-dir docs/images \
        --output manual_usuario.pdf \
        --title "Manual Usuario Gerontologia-App" \
        --skip-missing

Opciones:
  --skip-missing  No falla si faltan imágenes; las omite.
  --image-order   Un archivo de texto (una imagen por línea) para ordenar.

El script intenta leer las líneas con ![Texto](ruta) del markdown para
ordenar las imágenes si existe esa sección; de lo contrario usa un orden
predefinido.
"""

from __future__ import annotations
import argparse
import os
import re
from typing import List

try:
    from fpdf import FPDF
except ImportError:  # pragma: no cover
    raise SystemExit("Falta fpdf2. Instala con: pip install fpdf2")

try:
    from PIL import Image
except ImportError:  # pragma: no cover
    raise SystemExit("Falta Pillow. Instala con: pip install pillow")

DEFAULT_ORDER = [
    "index.png",
    "login.png",
    "registro.png",
    "servicios.png",
    "especialidades.png",
    "atencion.png",
    "contactenos.png",
    "historia_gerontologica.png",
    "paciente.png",
    "administrador.png",
    "lista_usuarios.png",
    "formulario_usuario.png",
    "confirmar_borrado.png",
    "dashboard.png",
    "terminos.png",
    "somos.png",
]

IMG_PATTERN = re.compile(r"!\[(?P<label>[^\]]+)\]\((?P<path>[^)]+)\)")


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Construcción de PDF con capturas y markdown.")
    p.add_argument("--manual", default="manual_usuario.md", help="Ruta del archivo markdown del manual")
    p.add_argument("--images-dir", default="docs/images", help="Directorio con las capturas")
    p.add_argument("--output", default="manual_usuario.pdf", help="Nombre del PDF de salida")
    p.add_argument("--title", default="Manual Usuario", help="Título de portada")
    p.add_argument("--skip-missing", action="store_true", help="Omite imágenes que no existan")
    p.add_argument("--image-order", help="Archivo de texto con orden personalizado de imágenes")
    return p.parse_args()


def load_manual(path: str) -> str:
    if not os.path.isfile(path):
        return ""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def extract_images_from_markdown(md: str, images_dir: str) -> List[str]:
    found = []
    for match in IMG_PATTERN.finditer(md):
        rel = match.group("path").strip()
        # Normalizar y solo considerar si apunta dentro del images_dir
        if rel.startswith(images_dir):
            name = os.path.basename(rel)
            found.append(name)
    return found


def read_order_file(path: str) -> List[str]:
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


def mm_for_image(image_path: str, max_w_mm: float, max_h_mm: float) -> tuple[float, float]:
    with Image.open(image_path) as im:
        w_px, h_px = im.size
    # Asumir 96 dpi -> 1 px = 0.264583 mm
    w_mm = w_px * 0.264583
    h_mm = h_px * 0.264583
    ratio = min(max_w_mm / w_mm, max_h_mm / h_mm, 1.0)
    return w_mm * ratio, h_mm * ratio


def build_pdf(manual_md: str, images: List[str], images_dir: str, output: str, title: str, skip_missing: bool):
    pdf = FPDF(format="A4")
    pdf.set_auto_page_break(auto=True, margin=15)

    # Portada
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 24)
    pdf.cell(0, 20, title, ln=1, align="C")
    pdf.set_font("Helvetica", size=12)
    pdf.multi_cell(0, 8, "Manual generado automáticamente. Contiene capturas de pantallas clave del sistema.")

    # Sección texto inicial (resumen)
    if manual_md:
        pdf.add_page()
        pdf.set_font("Helvetica", "B", 16)
        pdf.cell(0, 12, "Resumen Manual (Extracto)", ln=1)
        pdf.set_font("Helvetica", size=10)
        # Limitar a primeras 120 líneas para evitar PDF enorme
        lines = manual_md.splitlines()[:120]
        pdf.multi_cell(0, 5, "\n".join(lines))

    # Imágenes
    for img_name in images:
        img_path = os.path.join(images_dir, img_name)
        if not os.path.isfile(img_path):
            if skip_missing:
                continue
            else:
                raise FileNotFoundError(f"Falta imagen: {img_path}")
        pdf.add_page()
        pdf.set_font("Helvetica", "B", 14)
        pdf.cell(0, 10, img_name, ln=1)
        max_w, max_h = 190.0, 250.0  # Margenes
        w_mm, h_mm = mm_for_image(img_path, max_w, max_h)
        x = (210 - w_mm) / 2  # centrar horizontal (A4 width=210mm)
        y = (297 - h_mm) / 2  # centrar vertical
        pdf.image(img_path, x=x, y=y, w=w_mm, h=h_mm)

    pdf.output(output)
    print(f"[OK] PDF generado: {output}")


def main():
    args = parse_args()
    manual_md = load_manual(args.manual)

    if args.image_order:
        images = read_order_file(args.image_order)
    else:
        # Intentar leer orden desde markdown; si no, usar default
        extracted = extract_images_from_markdown(manual_md, args.images_dir)
        images = extracted if extracted else DEFAULT_ORDER

    build_pdf(manual_md, images, args.images_dir, args.output, args.title, args.skip_missing)


if __name__ == "__main__":
    main()
