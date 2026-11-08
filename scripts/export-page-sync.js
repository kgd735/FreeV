#!/usr/bin/env node
/** 把 free-vpn-db.yaml 导出为页面同步快照，供 artifact.edit 的 research_dir 使用。
 * 用法: node scripts/export-page-sync.js
 * 输出: ~/workspace/research_notes/free-vpn-tier-database-20261104-0324/notes/db-sync.md
 */
const fs = require("node:fs");
const path = require("node:path");
const yaml = require("js-yaml");

const DB_PATH = path.join(__dirname, "..", "free-vpn-db.yaml");
const OUT_PATH = "/home/hatch/workspace/research_notes/free-vpn-tier-database-20261104-0324/notes/db-sync.md";

const RES_LABEL = { true: "是", false: "否", partial: "部分", unknown: "未知" };

function main() {
  const db = yaml.load(fs.readFileSync(DB_PATH, "utf8"));

  const lines = [
    "# 免费 VPN 数据库 — 页面同步快照（自动生成，请勿手改）",
    "",
    `- last_full_review: ${db.last_full_review || ""}`,
    `- entries: ${db.entries.length} 条`,
    `- removed: ${(db.removed || []).length} 条`,
    `- discontinued: ${(db.discontinued || []).length} 条`,
    "",
    "## 全部条目",
    "",
    "| 名称 | 状态 | 免费额度 | 设备 | 国家 | 家宽IP | 日志 | 官网 |",
    "|---|---|---|---|---|---|---|---|",
  ];
  for (const e of db.entries) {
    const ft = e.free_tier;
    const res = e.residential_ip;
    lines.push(
      `| ${e.name} | ${e.status} | ${ft.data_cap} | ${ft.devices} | ${ft.countries} | ` +
        `${RES_LABEL[String(res.has)] ?? String(res.has)} | ${String(e.logging).slice(0, 60)} | ${e.official_url} |`
    );
  }
  lines.push("", "## 每条详情", "");
  for (const e of db.entries) {
    const ft = e.free_tier;
    const res = e.residential_ip;
    lines.push(
      `### ${e.name} (${e.id})`,
      `- 官网: ${e.official_url}`,
      `- 状态: ${e.status}（last_verified: ${e.last_verified}）`,
      `- 免费额度: ${ft.data_cap}；设备: ${ft.devices}；国家: ${ft.countries}；注册: ${ft.signup}；需信用卡: ${ft.card_required}`,
      `- 家宽IP: ${res.has} — ${res.note}`,
      `- IP类型: ${e.ip_type}`,
      `- 协议: ${e.protocols.join(", ")}`,
      `- 日志: ${e.logging}`,
      `- 平台: ${e.platforms.join(", ")}`
    );
    if (e.change_log) lines.push(`- 变更记录: ${e.change_log}`);
    if (e.sources) lines.push(`- 来源: ${e.sources.join(", ")}`);
    lines.push("");
  }
  if ((db.removed || []).length) {
    lines.push("## 已移除（removed 墓碑）", "");
    for (const r of db.removed) {
      lines.push(`- ${r.name}：${r.reason}（移除于 ${r.removed_date}，证据：${r.evidence || ""}）`);
    }
    lines.push("");
  }
  if ((db.discontinued || []).length) {
    lines.push("## 已停服（discontinued）", "");
    for (const r of db.discontinued) {
      lines.push(`- ${r.name}：${r.change}（${r.date}）`);
    }
    lines.push("");
  }

  fs.mkdirSync(path.dirname(OUT_PATH), { recursive: true });
  fs.writeFileSync(OUT_PATH, lines.join("\n"), "utf8");
  console.log(`wrote ${OUT_PATH} (${db.entries.length} entries)`);
}

main();
