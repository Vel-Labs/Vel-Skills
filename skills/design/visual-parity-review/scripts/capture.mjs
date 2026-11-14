#!/usr/bin/env node
// Capture pages for a visual parity review.
// Run from a project that has Playwright installed (it is resolved from the current
// directory, not from this file):
//   node /path/to/capture.mjs plan.json
// plan.json: { "out": "shots", "shots": [
//   { "name": "home-dark", "url": "http://127.0.0.1:5173/#home", "width": 1440,
//     "height": 1640, "scheme": "dark", "fullPage": true, "waitMs": 1500,
//     "steps": [{ "click": "Open demo workspace" }, { "hash": "#home" }] } ] }
// A step is { "click": "<accessible button name>" }, { "hash": "#route" } or { "wait": ms }.
import { createRequire } from "node:module";
import { mkdirSync, readFileSync } from "node:fs";
import { join, resolve } from "node:path";

const require = createRequire(join(process.cwd(), "noop.js"));
const { chromium } = require("playwright");
const plan = JSON.parse(readFileSync(process.argv[2], "utf8"));
const out = resolve(plan.out || "shots");
mkdirSync(out, { recursive: true });

const browser = await chromium.launch();
for (const shot of plan.shots) {
  const context = await browser.newContext({
    viewport: { width: shot.width, height: shot.height },
    colorScheme: shot.scheme || "light",
  });
  const page = await context.newPage();
  await page.goto(shot.url);
  await page.waitForTimeout(shot.waitMs ?? 1200);
  for (const step of shot.steps || []) {
    if (step.click) {
      const target = page.getByRole("button", { name: step.click });
      if (await target.count()) await target.first().click();
    }
    if (step.hash) await page.evaluate((h) => (location.hash = h), step.hash);
    await page.waitForTimeout(step.wait ?? 800);
  }
  const file = join(out, `${shot.name}.png`);
  await page.screenshot({ path: file, fullPage: shot.fullPage ?? true });
  console.log(file);
  await context.close();
}
await browser.close();
