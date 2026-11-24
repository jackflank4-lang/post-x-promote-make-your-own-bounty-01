// main.ts — post-x-promote-make-your-own-bounty-01
// Copies POST.json from the repository root to the output directory.
// That is all it has to do: the house reads the post itself from X,
// so nothing else the program writes about the post counts.
import { readFileSync, writeFileSync, mkdirSync } from "node:fs";
import { join } from "node:path";

const botDir = process.env.MAKEFUN_BOT_DIR ?? ".";
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "out";

const src = join(botDir, "POST.json");
const text = readFileSync(src, "utf8");
const post = JSON.parse(text);
const urlPattern = /^https:\/\/(x\.com|twitter\.com)\/[^/]+\/status\/\d+$/;
if (typeof post !== "object" || post === null || typeof post.url !== "string") {
  throw new Error("POST.json must be an object with a string url");
}
if (!urlPattern.test(post.url)) {
  throw new Error(
    `POST.json url must be an X post address (https://x.com/<handle>/status/<id>), got: ${post.url}`,
  );
}
mkdirSync(outDir, { recursive: true });
writeFileSync(join(outDir, "POST.json"), JSON.stringify(post) + "\n", "utf8");
console.log("wrote", join(outDir, "POST.json"));
