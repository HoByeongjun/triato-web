import { chromium } from 'playwright';

const sites = [
  { name: 'stripe', url: 'https://stripe.com' },
  { name: 'vercel', url: 'https://vercel.com' },
  { name: 'notion', url: 'https://www.notion.com' },
  { name: 'anthropic', url: 'https://anthropic.com' },
  { name: 'figma', url: 'https://figma.com' },
  { name: 'cal', url: 'https://cal.com' },
  { name: 'linear', url: 'https://linear.app' },
  { name: 'toss', url: 'https://toss.im' },
  { name: 'channel', url: 'https://channel.io/ko' },
  { name: 'daangn', url: 'https://www.daangn.com' },
  { name: 'astrowind', url: 'https://astrowind.vercel.app/' },
  { name: 'astroship', url: 'https://astroship.web3templates.com/' },
  { name: 'astroship-pro', url: 'https://astroship-pro.web3templates.com/' },
];

const browser = await chromium.launch();

for (const site of sites) {
  try {
    const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
    await page.goto(site.url, { waitUntil: 'domcontentloaded', timeout: 15000 });
    await page.waitForTimeout(2000);
    await page.screenshot({ path: `reference/${site.name}-hero.png` });
    await page.screenshot({ path: `reference/${site.name}-full.png`, fullPage: true });
    await page.close();
    console.log(`✓ ${site.name}`);
  } catch (e) {
    console.log(`✗ ${site.name}: ${e.message}`);
  }
}

await browser.close();
console.log('Done.');
