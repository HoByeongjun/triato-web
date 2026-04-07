import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });

// Serve dist folder
import { createServer } from 'http';
import { readFileSync, existsSync } from 'fs';
import { join, extname } from 'path';

const mimeTypes = { '.html': 'text/html', '.css': 'text/css', '.js': 'application/javascript', '.svg': 'image/svg+xml', '.jpg': 'image/jpeg', '.png': 'image/png', '.woff2': 'font/woff2', '.xml': 'application/xml' };

const server = createServer((req, res) => {
  let filePath = join(process.cwd(), 'dist', req.url === '/' ? 'index.html' : req.url);
  if (!existsSync(filePath)) { res.writeHead(404); res.end(); return; }
  const ext = extname(filePath);
  res.writeHead(200, { 'Content-Type': mimeTypes[ext] || 'application/octet-stream' });
  res.end(readFileSync(filePath));
});

await new Promise(r => server.listen(4321, r));

await page.goto('http://localhost:4321', { waitUntil: 'networkidle' });
await page.screenshot({ path: 'screenshots/before-full.png', fullPage: true });
await page.screenshot({ path: 'screenshots/before-hero.png' });

console.log('Screenshots saved');
server.close();
await browser.close();
