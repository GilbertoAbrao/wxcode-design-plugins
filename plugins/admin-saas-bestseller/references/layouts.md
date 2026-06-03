# SaaS Admin Bestseller — layout skeletons

Paste-ready, domain-neutral fragments for the polished light-mode SaaS admin
skin. Copy the shell from `assets/template.html` first (it carries the `:root`
tokens + sidebar + topbar + `.content` slot), then drop the region skeletons
below into `<main class="content">`. Replace every `{placeholder}` with the real
domain's equivalent.

Token recap (full block in `template.html`): surface `#f5f7fa`; card `#ffffff`;
border `#e8eaed`; accent `--accent` = `#5369f8`; text ramp `#111827 /
#6b7280 / #9ca3af`; green `#10b981` / red `#ef4444` / orange `#f59e0b`; card
shadow `0 1px 2px rgba(15,23,42,.04), 0 2px 8px rgba(15,23,42,.04)`.
Use `font-variant-numeric: tabular-nums` on every numeric cell.

---

## Page header (every screen)

```html
<div class="page-header" style="display:flex;align-items:center;justify-content:space-between;margin-bottom:20px;">
  <div>
    <div style="font-size:20px;font-weight:700;letter-spacing:-.3px;">{Screen title}</div>
    <div style="font-size:13px;color:var(--text-2);margin-top:2px;">{count · context · timestamp}</div>
  </div>
  <div style="display:flex;gap:8px;">
    <button class="btn btn-ghost">{Secondary action}</button>
    <button class="btn btn-primary">+ {Primary action}</button>
  </div>
</div>
```

---

## Greeting strip (dashboard only)

```html
<div style="display:flex;align-items:center;margin-bottom:24px;">
  <div>
    <h1 style="font-size:20px;font-weight:700;letter-spacing:-.3px;">Good morning, {Name}</h1>
    <p style="font-size:13px;color:var(--text-2);margin-top:2px;">{Date} — {context line}</p>
  </div>
  <div style="margin-left:auto;display:flex;gap:8px;">
    <button class="btn btn-ghost">Export</button>
    <button class="btn btn-primary">+ {New entity}</button>
  </div>
</div>
```

---

## 4 stat tiles (repeat ×4 in a repeat(4,1fr) grid)

```html
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-bottom:20px;">
  <div class="card" style="padding:20px;">
    <div style="display:flex;align-items:flex-start;justify-content:space-between;margin-bottom:12px;">
      <span style="font-size:10px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:var(--text-3);">{METRIC LABEL}</span>
      <div style="width:32px;height:32px;border-radius:8px;background:{tint};display:flex;align-items:center;justify-content:center;">
        <!-- inline SVG icon, stroke={accent color} -->
      </div>
    </div>
    <div style="font-size:26px;font-weight:800;letter-spacing:-.5px;margin-bottom:8px;font-variant-numeric:tabular-nums;">{figure}</div>
    <div style="display:flex;align-items:center;justify-content:space-between;">
      <span class="delta delta-up"><!-- or delta-down -->
        <!-- arrow SVG -->
        {±delta}
      </span>
      <!-- optional sparkline SVG 64×24 -->
    </div>
  </div>
  <!-- 3 more tiles -->
</div>
```

Delta classes:
```css
.delta { font-size:12px;font-weight:600;display:inline-flex;align-items:center;gap:3px;padding:2px 7px;border-radius:20px; }
.delta-up { color:var(--green);background:var(--green-light); }
.delta-down { color:var(--red);background:var(--red-light); }
```

---

## 8/4 mid-grid (chart card + activity feed)

```html
<div style="display:grid;grid-template-columns:1fr 340px;gap:16px;margin-bottom:20px;">

  <!-- Chart card (left) -->
  <div class="card">
    <div style="padding:20px 20px 0;display:flex;align-items:center;justify-content:space-between;">
      <div>
        <div style="font-size:15px;font-weight:700;">{Chart title}</div>
        <div style="font-size:12px;color:var(--text-3);margin-top:2px;">{subtitle}</div>
      </div>
      <div style="display:flex;gap:2px;">
        <button class="ptab">24H</button>
        <button class="ptab">7D</button>
        <button class="ptab active">30D</button>
        <button class="ptab">YTD</button>
      </div>
    </div>
    <!-- legend row -->
    <div style="display:flex;gap:16px;padding:12px 20px 0;">
      <div style="display:flex;align-items:center;gap:6px;font-size:12px;color:var(--text-2);">
        <div style="width:8px;height:8px;border-radius:50%;background:var(--accent);"></div>Current
      </div>
      <div style="display:flex;align-items:center;gap:6px;font-size:12px;color:var(--text-2);">
        <div style="width:8px;height:8px;border-radius:50%;background:#d1d5db;"></div>Previous
      </div>
    </div>
    <!-- area chart SVG -->
    <div style="padding:8px 20px 20px;">
      <svg width="100%" height="180" viewBox="0 0 560 180" preserveAspectRatio="none">
        <defs>
          <linearGradient id="cg" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="#5369f8" stop-opacity=".18"/>
            <stop offset="100%" stop-color="#5369f8" stop-opacity="0"/>
          </linearGradient>
        </defs>
        <!-- dotted grid lines at y=36,72,108,144 -->
        <line x1="0" y1="36" x2="560" y2="36" stroke="#e8eaed" stroke-width="1" stroke-dasharray="4 4"/>
        <line x1="0" y1="108" x2="560" y2="108" stroke="#e8eaed" stroke-width="1" stroke-dasharray="4 4"/>
        <!-- previous period: dashed grey polyline -->
        <path d="M0 140 ... L560 88" fill="none" stroke="#d1d5db" stroke-width="1.5" stroke-dasharray="5 3"/>
        <!-- current period: solid accent polyline + filled area -->
        <path d="M0 155 ... L560 40" fill="none" stroke="#5369f8" stroke-width="2"/>
        <path d="M0 155 ... L560 40 L560 180 L0 180Z" fill="url(#cg)"/>
        <!-- x-axis labels -->
        <text x="0" y="175" font-size="10" fill="#9ca3af" font-family="system-ui,sans-serif">{label}</text>
      </svg>
    </div>
  </div>

  <!-- Activity feed (right) -->
  <div class="card">
    <div style="padding:18px 20px 0;display:flex;align-items:center;justify-content:space-between;">
      <div style="font-size:15px;font-weight:700;">{Feed title}</div>
      <a href="#" class="view-all">View all</a>
    </div>
    <div style="padding-top:8px;">
      <div class="feed-item">
        <div class="fdot-wrap"><div class="fdot" style="background:var(--accent);"></div></div>
        <div class="feed-body">
          <div class="feed-action"><strong>{Actor}</strong> {action verb + object}</div>
          <div class="feed-time">{elapsed}</div>
        </div>
      </div>
      <!-- repeat feed-item rows; dot colors: accent / green / red / orange -->
    </div>
  </div>

</div>
```

Period-tab classes:
```css
.ptab { padding:5px 10px;border-radius:6px;font-size:12px;font-weight:500;cursor:pointer;border:none;background:transparent;color:var(--text-3);transition:background .15s,color .15s; }
.ptab.active { background:var(--accent-light);color:var(--accent);font-weight:600; }
```

Feed item classes:
```css
.feed-item { display:flex;align-items:flex-start;gap:12px;padding:12px 20px;border-bottom:1px solid var(--border); }
.feed-item:last-child { border-bottom:none; }
.fdot-wrap { flex-shrink:0;padding-top:2px; }
.fdot { width:8px;height:8px;border-radius:50%;margin-top:3px; }
.feed-body { flex:1;min-width:0; }
.feed-action { font-size:13px;color:var(--text-1);line-height:1.4; }
.feed-action strong { font-weight:600; }
.feed-time { font-size:11px;color:var(--text-3);margin-top:2px; }
```

---

## Records table card (dashboard footer or list screen)

```html
<div class="card">
  <div style="padding:20px 20px 16px;display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid var(--border);">
    <div style="font-size:15px;font-weight:700;">{Records title}</div>
    <a href="#" class="view-all">View all →</a>
  </div>
  <table>
    <thead>
      <tr>
        <th>{Entity}</th>
        <th>{Category}</th>
        <th style="text-align:right">{Numeric}</th>
        <th>{Date}</th>
        <th style="text-align:center">Status</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>
          <div style="display:flex;align-items:center;gap:10px;">
            <div class="avatar avatar-sm" style="background:{tint};color:{fg};">{IN}</div>
            <div>
              <div style="font-weight:600;font-size:13px;">{Name}</div>
              <div style="font-size:11px;color:var(--text-3);">{sub-label}</div>
            </div>
          </div>
        </td>
        <td><span class="cat-pill cat-c">{Category}</span></td>
        <td style="text-align:right" class="num-cell">{$value}</td>
        <td style="font-size:12px;color:var(--text-3);">{date}</td>
        <td style="text-align:center">
          <span class="status-pill st-active"><span class="st-dot"></span>{State}</span>
          <!-- variants: st-active / st-pending / st-inactive -->
        </td>
      </tr>
      <!-- more rows -->
    </tbody>
  </table>
  <div class="tbl-foot">
    <span class="tbl-count">Showing {a}–{b} of {n}</span>
    <div class="pagination">
      <button class="page-btn">‹</button>
      <button class="page-btn active">1</button>
      <button class="page-btn">2</button>
      <button class="page-btn">›</button>
    </div>
  </div>
</div>
```

---

## List toolbar (search + filter chips)

```html
<div style="display:flex;align-items:center;gap:12px;margin-bottom:16px;flex-wrap:wrap;">
  <div style="position:relative;flex:0 0 280px;">
    <!-- magnifier SVG absolute left:10px -->
    <input type="text" style="width:100%;height:36px;border:1px solid var(--border);border-radius:6px;padding:0 12px 0 34px;font-size:13px;background:var(--white);outline:none;" placeholder="Filter by {fields}…">
  </div>
  <div style="display:flex;align-items:center;gap:6px;">
    <span style="font-size:12px;font-weight:500;color:var(--text-3);">{Facet}</span>
    <span class="chip active">All <span class="chip-count">{n}</span></span>
    <span class="chip">{Value} <span class="chip-count">{n}</span></span>
    <!-- more chips -->
  </div>
  <div style="margin-left:auto;">
    <span style="font-size:13px;color:var(--text-3);">{n} results</span>
  </div>
</div>
```

Chip classes:
```css
.chip { display:inline-flex;align-items:center;gap:5px;padding:4px 10px;border-radius:20px;font-size:12px;font-weight:500;cursor:pointer;border:1px solid var(--border);background:var(--white);color:var(--text-2);transition:background .12s,border-color .12s,color .12s; }
.chip.active { background:var(--accent-light);border-color:var(--accent-light);color:var(--accent);font-weight:600; }
.chip-count { font-size:10px;font-weight:700;color:inherit;opacity:.7; }
```

---

## Record form — fields with inline validation

Rules live ON the field: a required mark (`*`), helper text under the field, and
an inline error on invalid fields. The submit stays `disabled` until the form is
valid. Never add a separate rules/validation-status panel.

```html
<form novalidate>
  <div class="card" style="margin-bottom:20px;">
    <div style="display:flex;align-items:center;gap:8px;padding:18px 20px 0;font-size:13px;font-weight:700;text-transform:uppercase;letter-spacing:.05em;">
      <!-- section icon SVG -->
      {Section Title}
    </div>
    <div style="padding:16px 20px 20px;">
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px 20px;">

        <!-- valid required field -->
        <div class="field">
          <label class="field-label" for="f1">{Label} <span class="req">*</span></label>
          <input id="f1" class="control" type="text" placeholder="{example}" value="">
          <span class="helper">{what the value drives / format hint}</span>
        </div>

        <!-- invalid field: add .invalid on .field -->
        <div class="field invalid">
          <label class="field-label" for="f2">{Label} <span class="req">*</span></label>
          <input id="f2" class="control" type="text" aria-invalid="true" value="{bad value}">
          <span class="error-msg">
            <!-- alert circle SVG width=12 -->
            {Specific rule that failed}
          </span>
        </div>

        <!-- required select -->
        <div class="field">
          <label class="field-label" for="f3">{Label} <span class="req">*</span></label>
          <select id="f3" class="control"><option value="">Select…</option></select>
          <span class="helper">{constraint on options}</span>
        </div>

      </div>
    </div>
  </div>

  <!-- form footer -->
  <div style="display:flex;align-items:center;justify-content:space-between;padding:16px 0 4px;">
    <span style="font-size:12px;color:var(--text-3);">Fields marked <span class="req">*</span> are required.</span>
    <div style="display:flex;gap:8px;">
      <button type="button" class="btn btn-ghost">Cancel</button>
      <button type="submit" class="btn btn-primary" disabled>{Submit action}</button>
    </div>
  </div>
</form>
```

---

## Record detail — header + meta grid + related panels

```html
<div>
  <!-- breadcrumb -->
  <nav style="display:flex;align-items:center;gap:6px;font-size:13px;color:var(--text-3);margin-bottom:16px;">
    <a href="#" style="color:var(--text-3);text-decoration:none;">{Parent list}</a>
    <span style="color:var(--border);">/</span>
    <span style="color:var(--text-1);font-weight:500;">{Entity name}</span>
  </nav>

  <!-- header strip -->
  <div style="display:flex;align-items:flex-start;justify-content:space-between;margin-bottom:20px;">
    <div style="display:flex;align-items:center;gap:14px;">
      <div class="avatar" style="width:44px;height:44px;font-size:16px;background:{tint};color:{fg};">{IN}</div>
      <div>
        <div style="font-size:22px;font-weight:800;letter-spacing:-.3px;">{Entity name}</div>
        <div style="display:flex;align-items:center;gap:8px;font-size:13px;color:var(--text-2);margin-top:4px;">
          <span class="cat-pill cat-c">{Category}</span>
          <span class="status-pill st-active"><span class="st-dot"></span>{State}</span>
          <span>{identifier / email}</span>
        </div>
      </div>
    </div>
    <div style="display:flex;gap:8px;">
      <button class="btn btn-ghost">{Secondary}</button>
      <button class="btn btn-primary">Edit</button>
    </div>
  </div>

  <!-- meta grid: 3-col label/value pairs -->
  <div class="card" style="margin-bottom:16px;">
    <div style="display:grid;grid-template-columns:repeat(3,1fr);">
      <div style="padding:16px 20px;border-right:1px solid var(--border);border-bottom:1px solid var(--border);">
        <div style="font-size:10px;font-weight:600;letter-spacing:.07em;text-transform:uppercase;color:var(--text-3);margin-bottom:4px;">{FIELD}</div>
        <div style="font-size:14px;font-weight:600;">{value}</div>
        <div style="font-size:11px;color:var(--text-3);margin-top:2px;">{hint}</div>
      </div>
      <!-- 5 more cells; last cell in each row has no border-right; last row has no border-bottom -->
    </div>
  </div>

  <!-- two related-data panels -->
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;">
    <div class="card">
      <!-- list/operations panel: card-head + rows -->
    </div>
    <div class="card">
      <!-- activity timeline panel: card-head + feed rows -->
    </div>
  </div>
</div>
```
