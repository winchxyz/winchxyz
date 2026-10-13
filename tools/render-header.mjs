// Renders tools/header.html to assets/header-light.png and assets/header-dark.png.
// Usage: node tools/render-header.mjs
// Needs playwright-core: installed next to this repo, or PLAYWRIGHT_CORE set to its index.mjs as a file:// URL.
import fs from 'fs';
import path from 'path';
import { fileURLToPath, pathToFileURL } from 'url';

const { chromium } = await import(process.env.PLAYWRIGHT_CORE || 'playwright-core');
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const base = path.join(process.env.LOCALAPPDATA, 'ms-playwright');
const dir = fs.readdirSync(base).filter(d => d.startsWith('chromium-') && !d.includes('headless')).sort().pop();
const browser = await chromium.launch({ executablePath: path.join(base, dir, 'chrome-win64', 'chrome.exe'), headless: true });
const page = await browser.newPage({ viewport: { width: 1280, height: 320 }, deviceScaleFactor: 2 });
const url = pathToFileURL(path.join(root, 'tools', 'header.html')).href;
for (const theme of ['light', 'dark']) {
  await page.goto(`${url}?${theme}`, { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  await page.waitForFunction(() => window.__done);
  await page.screenshot({ path: path.join(root, 'assets', `header-${theme}.png`) });
  console.log('wrote', theme);
}
await browser.close();
