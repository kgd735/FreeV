#!/usr/bin/env python3
"""把 free-vpn-db.yaml 导出为页面同步快照，供 artifact.edit 的 research_dir 使用。

用法: python3 export_page_sync.py
输出: ~/workspace/research_notes/free-vpn-tier-database-20261104-0324/notes/db-sync.md
"""
import os

import yaml

DB_PATH = "/home/hatch/workspace/vpn-db/free-vpn-db.yaml"
OUT_PATH = "/home/hatch/workspace/research_notes/free-vpn-tier-database-20261104-0324/notes/db-sync.md"


def main() -> None:
    with open(DB_PATH, encoding="utf-8") as f:
        db = yaml.safe_load(f)

    lines = [
        "# 免费 VPN 数据库 — 页面同步快照（自动生成，请勿手改）",
        "",
        f"- last_full_review: {db.get('last_full_review')}",
        f"- entries: {len(db['entries'])} 条",
        f"- removed: {len(db.get('removed') or [])} 条",
        f"- discontinued: {len(db.get('discontinued') or [])} 条",
        "",
        "## 全部条目",
        "",
        "| 名称 | 状态 | 免费额度 | 设备 | 国家 | 家宽IP | 日志 | 官网 |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for e in db["entries"]:
        ft = e["free_tier"]
        res = e["residential_ip"]
        res_label = {"True": "是", "False": "否", "partial": "部分", "unknown": "未知"}.get(
            str(res["has"]), str(res["has"])
        )
        lines.append(
            f"| {e['name']} | {e['status']} | {ft['data_cap']} | {ft['devices']} | "
            f"{ft['countries']} | {res_label} | {e['logging'][:60]} | {e['official_url']} |"
        )
    lines += ["", "## 每条详情", ""]
    for e in db["entries"]:
        ft = e["free_tier"]
        res = e["residential_ip"]
        lines += [
            f"### {e['name']} ({e['id']})",
            f"- 官网: {e['official_url']}",
            f"- 状态: {e['status']}（last_verified: {e['last_verified']}）",
            f"- 免费额度: {ft['data_cap']}；设备: {ft['devices']}；国家: {ft['countries']}；"
            f"注册: {ft['signup']}；需信用卡: {ft['card_required']}",
            f"- 家宽IP: {res['has']} — {res['note']}",
            f"- IP类型: {e['ip_type']}",
            f"- 协议: {', '.join(e['protocols'])}",
            f"- 日志: {e['logging']}",
            f"- 平台: {', '.join(e['platforms'])}",
        ]
        if e.get("change_log"):
            lines.append(f"- 变更记录: {e['change_log']}")
        if e.get("sources"):
            lines.append(f"- 来源: {', '.join(e['sources'])}")
        lines.append("")
    if db.get("removed"):
        lines += ["## 已移除（removed 墓碑）", ""]
        for r in db["removed"]:
            lines.append(f"- {r['name']}：{r['reason']}（移除于 {r['removed_date']}，证据：{r.get('evidence', '')}）")
        lines.append("")
    if db.get("discontinued"):
        lines += ["## 已停服（discontinued）", ""]
        for r in db["discontinued"]:
            lines.append(f"- {r['name']}：{r['change']}（{r['date']}）")
        lines.append("")

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"wrote {OUT_PATH} ({len(db['entries'])} entries)")


if __name__ == "__main__":
    main()
