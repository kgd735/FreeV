#!/usr/bin/env node
/** 检测 free-vpn-db.yaml 中所有官网 URL 的可达性。
 * 用法: node scripts/check-urls.js [--output DIR]
 * 输出 JSON 报告到 stdout，并可选写入 DIR/check-YYYYMMDD-HHMMSS.json
 * 退出码：0=全部可达，1=有失败项
 */
const fs = require("node:fs");
const path = require("node:path");
const yaml = require("js-yaml");

const DB_PATH = path.join(__dirname, "..", "free-vpn-db.yaml");

async function check(url, timeoutMs = 20000) {
  const result = { url, ok: false, status: null, error: null };
  const ctrl = new AbortController();
  const timer = setTimeout(() => ctrl.abort(), timeoutMs);
  try {
    const resp = await fetch(url, {
      signal: ctrl.signal,
      headers: { "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36" },
      redirect: "follow",
    });
    result.status = resp.status;
    result.ok = resp.status >= 200 && resp.status < 400;
    // 消费 body 以释放连接
    await resp.arrayBuffer();
  } catch (err) {
    result.error = `${err.name}: ${err.message}`;
  } finally {
    clearTimeout(timer);
  }
  return result;
}

async function main() {
  const outIdx = process.argv.indexOf("--output");
  const outDir = outIdx >= 0 ? process.argv[outIdx + 1] : null;

  const db = yaml.load(fs.readFileSync(DB_PATH, "utf8"));
  const items = db.entries.map((e) => [e.id, e.name, e.official_url]);

  const results = [];
  let failed = 0;
  // 串行检测，避免并发触发反爬
  for (const [id, name, url] of items) {
    const r = await check(url);
    r.id = id;
    r.name = name;
    results.push(r);
    if (!r.ok) failed++;
    console.log(`${r.ok ? "OK  " : "FAIL"} ${id.padEnd(18)} ${url} -> ${r.status || r.error}`);
  }

  const report = {
    checked_at: new Date().toISOString(),
    summary: { total: items.length, ok: items.length - failed, failed },
    results,
  };
  if (outDir) {
    fs.mkdirSync(outDir, { recursive: true });
    const now = new Date();
    const pad = (n) => String(n).padStart(2, "0");
    const ts = `${now.getFullYear()}${pad(now.getMonth() + 1)}${pad(now.getDate())}-${pad(now.getHours())}${pad(now.getMinutes())}`;
    const p = path.join(outDir, `check-${ts}.json`);
    fs.writeFileSync(p, JSON.stringify(report, null, 2), "utf8");
    console.log(`report written: ${p}`);
  }
  process.exit(failed ? 1 : 0);
}

main();
