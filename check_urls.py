#!/usr/bin/env python3
"""检测 free-vpn-db.yaml 中所有官网 URL 的可达性。

用法: python3 check_urls.py [--output DIR]
输出 JSON 报告到 stdout，并可选写入 DIR/check-YYYYMMDD-HHMMSS.json
退出码：0=全部可达，1=有失败项
"""
import json
import sys
import urllib.request
from datetime import datetime, timezone

import yaml

DB_PATH = "/home/hatch/workspace/vpn-db/free-vpn-db.yaml"

HEADERS = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"}


def check(url: str, timeout: int = 20) -> dict:
    result = {"url": url, "ok": False, "status": None, "error": None}
    try:
        req = urllib.request.Request(url, headers=HEADERS, method="GET")
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            result["status"] = resp.status
            result["ok"] = 200 <= resp.status < 400
    except Exception as e:  # noqa: BLE001 - report any failure plainly
        result["error"] = f"{type(e).__name__}: {e}"
    return result


def main() -> int:
    out_dir = None
    if "--output" in sys.argv:
        out_dir = sys.argv[sys.argv.index("--output") + 1]

    with open(DB_PATH, encoding="utf-8") as f:
        db = yaml.safe_load(f)

    items = [(e["id"], e["name"], e["official_url"]) for e in db["entries"]]
    report = {"checked_at": datetime.now(timezone.utc).isoformat(), "results": []}
    failed = 0
    for vid, name, url in items:
        r = check(url)
        r["id"] = vid
        r["name"] = name
        report["results"].append(r)
        if not r["ok"]:
            failed += 1
        print(f"{'OK ' if r['ok'] else 'FAIL'} {vid:18s} {url} -> {r['status'] or r['error']}")

    report["summary"] = {
        "total": len(items),
        "ok": len(items) - failed,
        "failed": failed,
    }
    if out_dir:
        import os

        os.makedirs(out_dir, exist_ok=True)
        ts = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
        path = os.path.join(out_dir, f"check-{ts}.json")
        with open(path, "w", encoding="utf-8") as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        print(f"report written: {path}")

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
