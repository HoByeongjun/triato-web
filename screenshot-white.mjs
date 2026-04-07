import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });

import { createServer } from 'http';
import { readFileSync, existsSync } from 'fs';
import { join, extname } from 'path';

const mimeTypes = { '.html': 'text/html', '.css': 'text/css', '.js': 'application/javascript', '.svg': 'image/svg+xml', '.jpg': 'image/jpeg', '.png': 'image/png', '.ico': 'image/x-icon', '.woff2': 'font/woff2', '.xml': 'application/xml', '.avif': 'image/avif', '.webp': 'image/webp' };

const server = createServer((req, res) => {
  let url = req.url.split('?')[0];
  let filePath = join(process.cwd(), 'dist', url === '/' ? 'index.html' : url);
  if (!existsSync(filePath)) { res.writeHead(404); res.end(); return; }
  const ext = extname(filePath);
  res.writeHead(200, { 'Content-Type': mimeTypes[ext] || 'application/octet-stream' });
  res.end(readFileSync(filePath));
});

await new Promise(r => server.listen(4322, r));

await page.goto('http://localhost:4322', { waitUntil: 'networkidle' });
await page.waitForTimeout(1000);

await page.screenshot({ path: 'screenshots/white-v1-full.png', fullPage: true });
await page.screenshot({ path: 'screenshots/white-v1-hero.png' });

console.log('White version screenshots saved');
server.close();
await browser.close();
