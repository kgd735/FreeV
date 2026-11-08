// 免费 VPN 数据库 — 运行时渲染。
// 页面加载时 fetch 同目录下的 free-vpn-db.yaml，用 js-yaml 解析后渲染。
// 数据库文件一变，刷新页面即自动更新，无需重新生成 HTML。
(function () {
  "use strict";

  var RES_LABEL = { true: "有家宽 IP", false: "机房 IP", partial: "部分家宽", unknown: "未知" };
  var RES_CLASS = { true: "res-yes", false: "res-no", partial: "res-part", unknown: "res-unknown" };

  var grid = document.getElementById("grid");
  var countEl = document.getElementById("count");
  var statusEl = document.getElementById("status");
  var qEl = document.getElementById("q");
  var sourceLine = document.getElementById("source-line");

  var entries = [];
  var filter = "all"; // all | res | unlimited | nosignup
  var statFilter = "all"; // all | active | res | uncertain

  function esc(s) {
    return String(s == null ? "" : s)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function isResidential(e) {
    return e.residential_ip.has === true || e.residential_ip.has === "partial";
  }

  function cardSearchText(e) {
    var ft = e.free_tier;
    return [
      e.name, e.id, ft.data_cap, ft.devices, ft.countries, ft.signup,
      e.residential_ip.note, e.ip_type, e.protocols.join(" "),
      e.logging, e.platforms.join(" "),
    ].join(" ").toLowerCase();
  }

  function cardHTML(e) {
    var ft = e.free_tier;
    var res = e.residential_ip;
    var badge = e.status === "active"
      ? '<span class="badge ok">已核实</span>'
      : '<span class="badge warn">未核实</span>';
    var changelog = e.change_log
      ? '<p class="changelog">变更：' + esc(e.change_log) + "</p>"
      : "";
    var sources = (e.sources && e.sources.length)
      ? '<p class="sources">来源：' + e.sources.map(function (u, i) {
          return '<a href="' + esc(u) + '" target="_blank" rel="noopener">[' + (i + 1) + "]</a>";
        }).join(" ") + "</p>"
      : "";
    return '<article class="card">'
      + '<header><h2><a href="' + esc(e.official_url) + '" target="_blank" rel="noopener">' + esc(e.name) + "</a></h2>" + badge + "</header>"
      + '<p class="res ' + RES_CLASS[String(res.has)] + '">' + esc(RES_LABEL[String(res.has)] || res.has) + " · " + esc(res.note) + "</p>"
      + "<dl>"
      + "<div><dt>免费额度</dt><dd>" + esc(ft.data_cap) + "</dd></div>"
      + "<div><dt>设备</dt><dd>" + esc(ft.devices) + "</dd></div>"
      + "<div><dt>国家/节点</dt><dd>" + esc(ft.countries) + "</dd></div>"
      + "<div><dt>注册</dt><dd>" + esc(ft.signup) + "</dd></div>"
      + "<div><dt>需信用卡</dt><dd>" + (ft.card_required ? "是" : "否") + "</dd></div>"
      + "<div><dt>IP 类型</dt><dd>" + esc(e.ip_type) + "</dd></div>"
      + "<div><dt>协议</dt><dd>" + esc(e.protocols.join(", ")) + "</dd></div>"
      + "<div><dt>日志/审计</dt><dd>" + esc(e.logging) + "</dd></div>"
      + "<div><dt>平台</dt><dd>" + esc(e.platforms.join(", ")) + "</dd></div>"
      + "<div><dt>最后核验</dt><dd>" + esc(e.last_verified) + "</dd></div>"
      + "</dl>"
      + changelog + sources
      + "</article>";
  }

  function renderStats(db) {
    var total = db.entries.length;
    var active = db.entries.filter(function (e) { return e.status === "active"; }).length;
    var res = db.entries.filter(isResidential).length;
    var uncertain = total - active;
    document.getElementById("stat-total").textContent = total;
    document.getElementById("stat-active").textContent = active;
    document.getElementById("stat-res").textContent = res;
    document.getElementById("stat-uncertain").textContent = uncertain;
    var resLabel = document.querySelector('[data-stat="res"] span');
    if (resLabel) resLabel.textContent = "家宽/住宅出口";
  }

  function renderTables(db) {
    var disc = db.discontinued || [];
    if (disc.length) {
      document.getElementById("discontinued-section").hidden = false;
      document.getElementById("discontinued-body").innerHTML = disc.map(function (d) {
        return "<tr><td>" + esc(d.name) + "</td><td>" + esc(d.change) + "</td><td>" + esc(d.date) + "</td>"
          + '<td><a href="' + esc(d.source) + '" target="_blank" rel="noopener">来源</a></td></tr>';
      }).join("");
    }
    var removed = db.removed || [];
    if (removed.length) {
      document.getElementById("removed-section").hidden = false;
      document.getElementById("removed-body").innerHTML = removed.map(function (r) {
        return "<tr><td>" + esc(r.name) + "</td><td>" + esc(r.reason) + "</td><td>" + esc(r.removed_date) + "</td></tr>";
      }).join("");
    }
  }

  function apply() {
    var needle = qEl.value.trim().toLowerCase();
    var n = 0;
    entries.forEach(function (item) {
      var e = item.entry;
      var show = !needle || item.search.includes(needle);
      if (filter === "res") show = show && isResidential(e);
      if (filter === "unlimited") show = show && String(e.free_tier.data_cap).toLowerCase().includes("unlimited");
      if (filter === "nosignup") {
        var s = String(e.free_tier.signup).toLowerCase();
        show = show && (s.includes("no") || s.includes("无需") || s.includes("免注册"));
      }
      if (statFilter === "active") show = show && e.status === "active";
      if (statFilter === "res") show = show && isResidential(e);
      if (statFilter === "uncertain") show = show && e.status !== "active";
      item.el.classList.toggle("hidden", !show);
      if (show) n++;
    });
    countEl.textContent = "共 " + n + " 条";
  }

  function setFilter(next, chipEl) {
    filter = next;
    document.querySelectorAll(".chip").forEach(function (x) { x.classList.remove("active"); });
    if (chipEl) chipEl.classList.add("active");
    apply();
  }

  function setStat(next, statEl) {
    statFilter = next;
    document.querySelectorAll(".stat").forEach(function (x) { x.classList.remove("active"); });
    if (statEl) statEl.classList.add("active");
    // 统计方块与筛选 chip 联动：家宽方块对应"仅家宽 IP"，其余回到"全部"
    if (next === "res") {
      setFilter("res", document.querySelector('.chip[data-filter="res"]'));
    } else {
      setFilter("all", document.querySelector('.chip[data-filter="all"]'));
    }
    apply();
  }

  document.querySelectorAll(".chip").forEach(function (c) {
    c.addEventListener("click", function () { setFilter(c.dataset.filter, c); });
  });
  document.querySelectorAll(".stat").forEach(function (s) {
    s.addEventListener("click", function () { setStat(s.dataset.stat, s); });
  });
  qEl.addEventListener("input", apply);

  fetch("./free-vpn-db.yaml", { cache: "no-store" })
    .then(function (resp) {
      if (!resp.ok) throw new Error("HTTP " + resp.status);
      return resp.text();
    })
    .then(function (text) {
      var db = jsyaml.load(text);
      if (!db || !Array.isArray(db.entries)) throw new Error("数据库格式不正确：缺少 entries");
      renderStats(db);
      renderTables(db);
      grid.innerHTML = db.entries.map(function (e) {
        return { entry: e, search: cardSearchText(e), html: cardHTML(e) };
      }).map(function (item) { return item.html; }).join("");
      entries = Array.prototype.map.call(grid.children, function (el, i) {
        return { el: el, entry: db.entries[i], search: cardSearchText(db.entries[i]) };
      });
      sourceLine.textContent = "数据来源：free-vpn-db.yaml（本仓库）。最后全面复核：" + (db.last_full_review || "—") + "。";
      statusEl.textContent = "数据库已加载（" + db.entries.length + " 条），刷新页面即同步最新内容。";
      apply();
    })
    .catch(function (err) {
      statusEl.classList.add("error");
      statusEl.textContent = "数据库加载失败：" + err.message
        + "。请通过 HTTP(S) 访问本页面（直接双击打开 file:// 无法读取数据库文件），或确认 free-vpn-db.yaml 与 index.html 在同一目录。";
      countEl.textContent = "";
    });
})();
