#!/usr/bin/env node
/** 构建：校验 free-vpn-db.yaml，并把页面运行时需要的文件准备好。
 * - 复制 free-vpn-db.yaml -> page/free-vpn-db.yaml（页面用 fetch 加载它）
 * - 确保 page/vendor/js-yaml.min.js 存在（浏览器端 YAML 解析器）
 * 用法: node scripts/build.js
 */
const fs = require("node:fs");
const path = require("node:path");
const yaml = require("js-yaml");

const ROOT = path.resolve(__dirname, "..");
const DB_PATH = path.join(ROOT, "free-vpn-db.yaml");
const PAGE_YAML = path.join(ROOT, "page", "free-vpn-db.yaml");
const VENDOR_SRC = path.join(ROOT, "node_modules", "js-yaml", "dist", "js-yaml.min.js");
const VENDOR_DST = path.join(ROOT, "page", "vendor", "js-yaml.min.js");

function main() {
  const text = fs.readFileSync(DB_PATH, "utf8");
  const db = yaml.load(text);

  // 基础 schema 校验
  if (!db || !Array.isArray(db.entries)) {
    throw new Error("free-vpn-db.yaml: entries 必须是数组");
  }
  const required = ["id", "name", "official_url", "status", "free_tier", "residential_ip"];
  for (const e of db.entries) {
    for (const k of required) {
      if (e[k] === undefined) throw new Error(`条目 ${e.id || "?"} 缺少字段 ${k}`);
    }
    if (typeof e.residential_ip.has !== "boolean" && !["partial", "unknown"].includes(e.residential_ip.has)) {
      throw new Error(`条目 ${e.id} residential_ip.has 取值非法: ${e.residential_ip.has}`);
    }
  }

  fs.mkdirSync(path.dirname(PAGE_YAML), { recursive: true });
  fs.copyFileSync(DB_PATH, PAGE_YAML);

  fs.mkdirSync(path.dirname(VENDOR_DST), { recursive: true });
  if (!fs.existsSync(VENDOR_DST)) {
    fs.copyFileSync(VENDOR_SRC, VENDOR_DST);
  }

  const active = db.entries.filter((e) => e.status === "active").length;
  const res = db.entries.filter((e) => e.residential_ip.has === true || e.residential_ip.has === "partial").length;
  console.log(`build ok: ${db.entries.length} entries (${active} active, ${res} residential), page/free-vpn-db.yaml 已同步`);
}

main();
