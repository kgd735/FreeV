#!/usr/bin/env python3
"""从 free-vpn-db.yaml 生成可独立部署的静态页面。

用法: python3 page/generate.py
输出: page/index.html（自包含单文件，无外部依赖；由脚本自动生成，请勿手改）

数据唯一来源是 ../free-vpn-db.yaml：改数据 → 重新运行本脚本 → 提交并推送。
"""
import html
import json
import os

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(HERE, "..", "free-vpn-db.yaml")
OUT_PATH = os.path.join(HERE, "index.html")

RES_LABEL = {True: "有家宽 IP", False: "机房 IP", "partial": "部分家宽", "unknown": "未知"}
RES_CLASS = {True: "res-yes", False: "res-no", "partial": "res-part", "unknown": "res-unknown"}


def esc(s):
    return html.escape(str(s), quote=True)


def main():
    with open(DB_PATH, encoding="utf-8") as f:
        db = yaml.safe_load(f)

    entries = db["entries"]
    total = len(entries)
    active = sum(1 for e in entries if e["status"] == "active")
    uncertain = sum(1 for e in entries if e["status"] != "active")
    res_true = sum(1 for e in entries if e["residential_ip"]["has"] is True)
    res_part = sum(1 for e in entries if e["residential_ip"]["has"] == "partial")
    res_count = res_true + res_part
    last_review = db.get("last_full_review", "")

    cards = []
    for e in entries:
        ft = e["free_tier"]
        res = e["residential_ip"]
        res_key = res["has"]
        badge = (
            '<span class="badge ok">已核实</span>'
            if e["status"] == "active"
            else '<span class="badge warn">未核实</span>'
        )
        changelog = (
            f"<p class=\"changelog\">变更：{esc(e['change_log'])}</p>" if e.get("change_log") else ""
        )
        sources = (
            "<p class=\"sources\">来源："
            + " ".join(
                f"<a href=\"{esc(u)}\" target=\"_blank\" rel=\"noopener\">[{i + 1}]</a>"
                for i, u in enumerate(e.get("sources") or [])
            )
            + "</p>"
            if e.get("sources")
            else ""
        )
        search_text = " ".join(
            [
                e["name"],
                e["id"],
                ft["data_cap"],
                ft["devices"],
                ft["countries"],
                ft["signup"],
                res["note"],
                e["ip_type"],
                " ".join(e["protocols"]),
                e["logging"],
                " ".join(e["platforms"]),
            ]
        ).lower()
        cards.append(
            f"""<article class="card" data-search="{esc(search_text)}"
          data-res="{esc(res_key)}" data-status="{esc(e['status'])}"
          data-free="{esc('unlimited' in ft['data_cap'].lower())}"
          data-signup="{esc('no' in ft['signup'].lower() or '无需' in ft['signup'] or '免注册' in ft['signup'])}">
        <header><h2><a href="{esc(e['official_url'])}" target="_blank" rel="noopener">{esc(e['name'])}</a></h2>{badge}</header>
        <p class="res {RES_CLASS[res_key]}">{esc(RES_LABEL[res_key])} · {esc(res['note'])}</p>
        <dl>
          <div><dt>免费额度</dt><dd>{esc(ft['data_cap'])}</dd></div>
          <div><dt>设备</dt><dd>{esc(ft['devices'])}</dd></div>
          <div><dt>国家/节点</dt><dd>{esc(ft['countries'])}</dd></div>
          <div><dt>注册</dt><dd>{esc(ft['signup'])}</dd></div>
          <div><dt>需信用卡</dt><dd>{'否' if not ft['card_required'] else '是'}</dd></div>
          <div><dt>IP 类型</dt><dd>{esc(e['ip_type'])}</dd></div>
          <div><dt>协议</dt><dd>{esc(', '.join(e['protocols']))}</dd></div>
          <div><dt>日志/审计</dt><dd>{esc(e['logging'])}</dd></div>
          <div><dt>平台</dt><dd>{esc(', '.join(e['platforms']))}</dd></div>
          <div><dt>最后核验</dt><dd>{esc(e['last_verified'])}</dd></div>
        </dl>
        {changelog}
        {sources}
      </article>"""
        )

    disc_rows = []
    for d in db.get("discontinued") or []:
        disc_rows.append(
            f"<tr><td>{esc(d['name'])}</td><td>{esc(d['change'])}</td>"
            f"<td>{esc(d['date'])}</td>"
            f"<td><a href=\"{esc(d['source'])}\" target=\"_blank\" rel=\"noopener\">来源</a></td></tr>"
        )

    removed_rows = []
    for r in db.get("removed") or []:
        removed_rows.append(
            f"<tr><td>{esc(r['name'])}</td><td>{esc(r['reason'])}</td>"
            f"<td>{esc(r['removed_date'])}</td></tr>"
        )

    page = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>免费 VPN 数据库</title>
<style>
  :root {{ --bg:#0f1115; --card:#171a21; --line:#262b36; --text:#e8eaf0; --muted:#9aa3b2;
          --accent:#6ea8fe; --green:#3fb97f; --amber:#e0a63c; --red:#e06c5a; }}
  * {{ box-sizing:border-box; }}
  body {{ margin:0; background:var(--bg); color:var(--text);
         font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Microsoft YaHei",sans-serif; }}
  header.hero {{ padding:36px 20px 8px; max-width:1080px; margin:0 auto; }}
  header.hero h1 {{ margin:0 0 8px; font-size:28px; }}
  header.hero p {{ color:var(--muted); margin:4px 0; }}
  .stats {{ display:flex; flex-wrap:wrap; gap:12px; max-width:1080px; margin:18px auto; padding:0 20px; }}
  .stat {{ flex:1 1 140px; background:var(--card); border:1px solid var(--line);
          border-radius:12px; padding:14px 16px; }}
  .stat b {{ display:block; font-size:26px; }}
  .stat span {{ color:var(--muted); font-size:13px; }}
  .toolbar {{ position:sticky; top:0; z-index:10; background:rgba(15,17,21,.96);
             border-bottom:1px solid var(--line); padding:12px 20px;
             display:flex; flex-wrap:wrap; gap:8px; align-items:center; }}
  .toolbar input[type=search] {{ flex:1 1 220px; padding:9px 12px; border-radius:8px;
             border:1px solid var(--line); background:var(--card); color:var(--text); font-size:15px; }}
  .chip {{ padding:8px 14px; border-radius:999px; border:1px solid var(--line);
          background:var(--card); color:var(--text); cursor:pointer; font-size:14px; }}
  .chip.active {{ background:var(--accent); border-color:var(--accent); color:#0b1220; }}
  main {{ max-width:1080px; margin:0 auto; padding:20px; }}
  #count {{ color:var(--muted); margin:0 0 14px; }}
  .grid {{ display:grid; grid-template-columns:repeat(auto-fill,minmax(320px,1fr)); gap:14px; }}
  .card {{ background:var(--card); border:1px solid var(--line); border-radius:12px; padding:16px; }}
  .card header {{ display:flex; justify-content:space-between; align-items:flex-start; gap:8px; }}
  .card h2 {{ margin:0; font-size:18px; }}
  .card h2 a {{ color:var(--text); text-decoration:none; }}
  .card h2 a:hover {{ color:var(--accent); }}
  .badge {{ font-size:12px; padding:3px 8px; border-radius:999px; white-space:nowrap; }}
  .badge.ok {{ background:rgba(63,185,127,.18); color:var(--green); }}
  .badge.warn {{ background:rgba(224,166,60,.18); color:var(--amber); }}
  .res {{ font-size:14px; margin:10px 0; }}
  .res-yes {{ color:var(--green); }} .res-part {{ color:var(--amber); }}
  .res-no {{ color:var(--muted); }} .res-unknown {{ color:var(--red); }}
  .card dl {{ margin:0; font-size:14px; }}
  .card dl div {{ display:flex; gap:8px; padding:5px 0; border-top:1px solid var(--line); }}
  .card dt {{ flex:0 0 76px; color:var(--muted); }}
  .card dd {{ margin:0; }}
  .changelog, .sources {{ font-size:13px; color:var(--muted); }}
  .sources a {{ color:var(--accent); }}
  section.dead {{ margin-top:36px; }}
  section.dead h2 {{ font-size:20px; }}
  table {{ width:100%; border-collapse:collapse; font-size:14px; }}
  th, td {{ text-align:left; padding:8px; border-bottom:1px solid var(--line); }}
  th {{ color:var(--muted); }}
  footer {{ max-width:1080px; margin:0 auto; padding:24px 20px 40px; color:var(--muted); font-size:13px; }}
  footer a {{ color:var(--accent); }}
  .hidden {{ display:none !important; }}
</style>
</head>
<body>
<header class="hero">
  <h1>免费 VPN 数据库</h1>
  <p>有免费档的 VPN 信息库，含免费额度、设备数、注册要求、日志审计与家宽 IP 情况。数据每周复核、每日检索新增。</p>
  <p>免费 ≠ 无代价：P2P 类会把你的设备当作别人的出口；部分服务记录连接日志。先看日志与代价，再决定用哪家。</p>
</header>
<div class="stats">
  <div class="stat"><b>{total}</b><span>免费档条目</span></div>
  <div class="stat"><b>{active}</b><span>已核实有效</span></div>
  <div class="stat"><b>{res_count}</b><span>家宽/住宅出口（真住宅 {res_true} + 部分 {res_part}）</span></div>
  <div class="stat"><b>{uncertain}</b><span>未核实</span></div>
</div>
<div class="toolbar">
  <input type="search" id="q" placeholder="搜索名称、协议、平台…">
  <button class="chip active" data-filter="all">全部</button>
  <button class="chip" data-filter="res">仅家宽 IP</button>
  <button class="chip" data-filter="unlimited">不限流量</button>
  <button class="chip" data-filter="nosignup">免注册</button>
</div>
<main>
  <p id="count">共 {total} 条</p>
  <div class="grid" id="grid">
{''.join(cards)}
  </div>
  <section class="dead">
    <h2>已下线 / 取消免费档</h2>
    <table><thead><tr><th>名称</th><th>变化</th><th>日期</th><th></th></tr></thead>
    <tbody>{''.join(disc_rows)}</tbody></table>
  </section>
  {('<section class="dead"><h2>已移除（墓碑）</h2><table><thead><tr><th>名称</th><th>原因</th><th>移除日期</th></tr></thead><tbody>' + ''.join(removed_rows) + '</tbody></table></section>') if removed_rows else ''}
</main>
<footer>
  <p>数据来源：free-vpn-db.yaml（本仓库）。最后全面复核：{esc(last_review)}。</p>
  <p>核实方式：官网可达性检测 + 评测交叉核对；确认无效 = 官网长期不可达且 90 天内无免费档可信证据，删除后记入墓碑。</p>
</footer>
<script>
  const q = document.getElementById('q');
  const cards = [...document.querySelectorAll('.card')];
  const count = document.getElementById('count');
  let filter = 'all';
  document.querySelectorAll('.chip').forEach(c => c.addEventListener('click', () => {{
    document.querySelectorAll('.chip').forEach(x => x.classList.remove('active'));
    c.classList.add('active');
    filter = c.dataset.filter;
    apply();
  }}));
  q.addEventListener('input', apply);
  function apply() {{
    const needle = q.value.trim().toLowerCase();
    let n = 0;
    cards.forEach(card => {{
      let show = !needle || card.dataset.search.includes(needle);
      if (filter === 'res') show = show && (card.dataset.res === 'True' || card.dataset.res === 'partial');
      if (filter === 'unlimited') show = show && card.dataset.free === 'True';
      if (filter === 'nosignup') show = show && card.dataset.signup === 'True';
      card.classList.toggle('hidden', !show);
      if (show) n++;
    }});
    count.textContent = '共 ' + n + ' 条';
  }}
</script>
</body>
</html>
"""

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(page)
    print(f"wrote {OUT_PATH} ({total} entries, {active} active, {res_count} residential)")


if __name__ == "__main__":
    main()
