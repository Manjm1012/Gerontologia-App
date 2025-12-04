#!/usr/bin/env node
/**
 * Captura automática de pantallas usando Playwright (Node).
 * Requiere: npm i -D playwright && npx playwright install chromium
 */
const { program } = require('commander');
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const PUBLIC_ROUTES = [
  ["index", "/"],
  ["login", "/login"],
  ["registro", "/registro"],
  ["servicios", "/servicios"],
  ["especialidades", "/especialidades"],
  ["atencion", "/atencion"],
  ["contactenos", "/contactenos"],
  ["historia_gerontologica", "/historia_gerontologica"],
  ["paciente", "/paciente"],
  ["dashboard", "/Dashboards"],
  ["terminos", "/terminos"],
  ["somos", "/somos"],
];

const ADMIN_ROUTES = [
  ["administrador", "/administrador"],
  ["lista_usuarios", "/lista_usuarios"],
  ["formulario_usuario", "/admin_user_create"],
];

program
  .option('--baseUrl <url>', 'Base URL', 'http://127.0.0.1:8000')
  .option('--outDir <dir>', 'Directorio salida', 'docs/images')
  .option('--width <n>', 'Viewport width', '1280')
  .option('--height <n>', 'Viewport height', '900')
  .option('--waitMs <n>', 'Espera tras carga', '500')
  .option('--fullPage', 'Captura página completa')
  .option('--includeAdmin', 'Incluir rutas admin')
  .option('--adminUser <u>', 'Usuario admin')
  .option('--adminPass <p>', 'Password admin')
  .parse(process.argv);

const opts = program.opts();

function ensureOutDir(dir) {
  fs.mkdirSync(dir, { recursive: true });
}

async function loginIfNeeded(page) {
  if (!opts.includeAdmin) return false;
  if (!opts.adminUser || !opts.adminPass) {
    console.log('[WARN] Credenciales admin no provistas, se omiten rutas admin');
    return false;
  }
  const loginUrl = opts.baseUrl.replace(/\/$/, '') + '/login';
  console.log('[INFO] Login en', loginUrl);
  await page.goto(loginUrl);
  try {
    await page.fill("input[name='usuario']", opts.adminUser);
    await page.fill("input[name='contrasena']", opts.adminPass);
    await page.click('button[type="submit"]');
    await page.waitForTimeout(800);
    return true;
  } catch (e) {
    console.log('[ERROR] Falló el login:', e.message);
    return false;
  }
}

async function captureRoutes(page, routes) {
  for (const [name, route] of routes) {
    const url = opts.baseUrl.replace(/\/$/, '') + route;
    console.log('[CAPTURE]', name, url);
    try {
      await page.goto(url);
      await page.waitForTimeout(Number(opts.waitMs));
      if (name === 'index' || name === 'dashboard') await page.waitForTimeout(1000);
      const filePath = path.join(opts.outDir, name + '.png');
      await page.screenshot({ path: filePath, fullPage: !!opts.fullPage });
      console.log('[OK]', filePath);
    } catch (e) {
      console.log('[FAIL]', name, e.message);
    }
  }
}

(async () => {
  ensureOutDir(opts.outDir);
  const browser = await chromium.launch();
  const context = await browser.newContext({ viewport: { width: Number(opts.width), height: Number(opts.height) } });
  const page = await context.newPage();

  await captureRoutes(page, PUBLIC_ROUTES);
  const logged = await loginIfNeeded(page);
  if (logged) await captureRoutes(page, ADMIN_ROUTES);

  await browser.close();
  console.log('[DONE] Capturas completadas.');
})();
