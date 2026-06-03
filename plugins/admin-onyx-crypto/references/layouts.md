# Onyx Admin — layout skeletons

Paste-ready, domain-neutral fragments for the Onyx deep-obsidian / emerald-neon
skin. Copy the shell from `assets/template.html` first (it carries the `:root`
tokens + left rail + topbar + main slot), then drop the region skeletons below
into `<main class="page">`. Replace every placeholder label with the real
domain's equivalent.

Token recap (full block in `template.html`): canvas `#0a0a0f`, surface
`#14141c`, elevated `#1c1c28`, hover `#222232`, hairline `#262633`; text
`#e8e8f0 / #8a8aa0 / #55556a`; accent `var(--accent)` = `#10b981` (emerald),
`var(--accent2)` = `#8b5cf6` (violet); gain `#10b981`, loss `#f43f5e`.
Put `font-variant-numeric: tabular-nums` on every numeric cell.

---

## Page header (every screen)

```html
<div class="page-header">
  <div>
    <h1 class="page-title">{Screen Title}</h1>
    <div class="page-sub">{scope · context · timestamp}</div>
  </div>
  <div class="page-actions">
    <button class="btn btn-ghost">{Secondary}</button>
    <button class="btn btn-primary">+ {Primary action}</button>
  </div>
</div>
```

---

## KPI card row (×4 in a `.kpi-grid`)

Neon-glow on hover (`border-color: --accent` + `box-shadow: 0 0 16px --accent-glow`).

```html
<div class="kpi-grid">  <!-- display:grid; grid-template-columns:repeat(4,1fr); gap:16px -->
  <div class="kpi-card">
    <div class="kpi-label">{UPPERCASE METRIC NAME}</div>
    <div class="kpi-row">
      <div class="kpi-value">{figure}</div>   <!-- optionally color:var(--gain) or var(--loss) -->
      <svg class="kpi-sparkline" width="72" height="32" viewBox="0 0 72 32" fill="none" aria-hidden="true">
        <!-- polyline: stroke=var(--accent) or var(--accent2) or var(--loss) -->
        <polyline points="2,24 18,18 34,14 50,10 70,6" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round"/>
      </svg>
    </div>
    <div class="kpi-footer">
      <span class="delta-chip gain"><!-- SVG up arrow -->{+delta}</span>  <!-- .gain / .loss -->
      <span class="kpi-sub">{context sub-line}</span>
    </div>
  </div>
  <!-- 3 more cards -->
</div>
```

---

## Main grid — area chart + ranked rows

```html
<div style="display:grid;grid-template-columns:1fr 340px;gap:16px">

  <!-- Left: area chart card -->
  <div class="card">
    <div class="card-header">
      <div>
        <div class="card-title">{Chart Title}</div>
        <div class="card-sub">{sub-line}</div>
      </div>
      <!-- Timeframe tabs -->
      <div class="timeframe-tabs" role="tablist" aria-label="Chart timeframe">
        <button class="tf-tab" role="tab" aria-selected="false">1H</button>
        <button class="tf-tab active" role="tab" aria-selected="true">24H</button>
        <button class="tf-tab" role="tab" aria-selected="false">7D</button>
        <button class="tf-tab" role="tab" aria-selected="false">30D</button>
        <button class="tf-tab" role="tab" aria-selected="false">ALL</button>
      </div>
    </div>
    <div class="chart-wrap">
      <!-- Callout line above chart -->
      <div class="chart-callout">
        <span class="chart-callout-val">{big value}</span>
        <span class="chart-callout-delta">{↑ delta}</span>
        <span class="chart-callout-period">{period}</span>
      </div>
      <!-- Inline SVG area chart with emerald stroke + translucent fill -->
      <svg width="100%" viewBox="0 0 680 180" preserveAspectRatio="none" aria-label="{chart description}" role="img">
        <defs>
          <linearGradient id="areaGrad" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="var(--accent)" stop-opacity=".30"/>
            <stop offset="85%" stop-color="var(--accent)" stop-opacity="0"/>
          </linearGradient>
        </defs>
        <!-- Faint grid lines at y=30,70,110,150 -->
        <line x1="0" y1="30" x2="680" y2="30" stroke="var(--border)" stroke-width=".8"/>
        <line x1="0" y1="70" x2="680" y2="70" stroke="var(--border)" stroke-width=".8"/>
        <line x1="0" y1="110" x2="680" y2="110" stroke="var(--border)" stroke-width=".8"/>
        <line x1="0" y1="150" x2="680" y2="150" stroke="var(--border)" stroke-width=".8"/>
        <!-- Y-axis labels (font-size 9, fill var(--text-dim)) -->
        <!-- X-axis labels (font-size 9, fill var(--text-dim)) -->
        <!-- Area fill -->
        <path d="M30,{y0} C...{curve} L680,160 L30,160 Z" fill="url(#areaGrad)"/>
        <!-- Stroke -->
        <path d="M30,{y0} C...{curve}" fill="none" stroke="var(--accent)" stroke-width="2"/>
        <!-- Live endpoint dot -->
        <circle cx="650" cy="{yn}" r="5" fill="var(--accent)" stroke="var(--bg-elevated)" stroke-width="2.5"/>
      </svg>
    </div>
  </div>

  <!-- Right: ranked rows side panel -->
  <div class="card">
    <div class="card-header">
      <div>
        <div class="card-title">{Panel Title}</div>
        <div class="card-sub">{sub-line}</div>
      </div>
    </div>
    <div role="list" aria-label="{Panel description}">
      <!-- Repeat ranked-item rows -->
      <div style="display:flex;align-items:center;gap:10px;padding:10px 20px;border-bottom:1px solid var(--border);transition:background .12s;" role="listitem">
        <!-- Badge: 34×34, border-radius 8px, letter-mark, color by accent/loss -->
        <div style="width:34px;height:34px;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:11px;font-weight:700;font-family:monospace;background:rgba(16,185,129,.14);color:var(--accent)">{TKR}</div>
        <div style="flex:1;min-width:0">
          <div style="font-size:13px;font-weight:700">{Label}</div>
          <div style="font-size:11px;color:var(--text-muted)">{Sub}</div>
        </div>
        <div style="text-align:right">
          <div style="font-size:13px;font-weight:600;font-variant-numeric:tabular-nums">{value}</div>
          <div style="font-size:11.5px;font-weight:700;font-variant-numeric:tabular-nums;color:var(--gain)">{+delta}</div>  <!-- var(--loss) for negative -->
        </div>
      </div>
    </div>
  </div>

</div>
```

---

## Records table (full-width card)

```html
<div class="card">
  <div class="card-header">
    <div>
      <div class="card-title">{Records Title}</div>
      <div class="card-sub">{N items · context}</div>
    </div>
    <a href="#" style="font-size:13px;font-weight:600;color:var(--accent);text-decoration:none">View All →</a>
  </div>
  <div style="overflow-x:auto">
    <table>
      <thead>
        <tr>
          <th>{Asset}</th>
          <th>{Price}</th>
          <th>{Delta %}</th>
          <th>{Quantity}</th>
          <th>{Value}</th>
          <th>Action</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <!-- Asset cell: badge icon + two-line name -->
          <td>
            <div style="display:flex;align-items:center;gap:10px">
              <div style="width:32px;height:32px;border-radius:50%;background:rgba(16,185,129,.16);color:var(--accent);display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:800;flex-shrink:0">{L}</div>
              <div>
                <div style="font-size:13.5px;font-weight:700">{TICKER}</div>
                <div style="font-size:11.5px;color:var(--text-muted)">{Name}</div>
              </div>
            </div>
          </td>
          <td>{$price}</td>
          <td style="font-weight:700;font-size:13px;color:var(--gain)">{+pct}</td>  <!-- var(--loss) for negative -->
          <td>{qty}</td>
          <td>{$value}</td>
          <td>
            <button style="background:var(--bg-surface);border:1px solid var(--border);border-radius:6px;padding:5px 12px;font-size:12px;font-weight:600;color:var(--text-muted);cursor:pointer;font-family:var(--font)">{Action}</button>
          </td>
        </tr>
        <!-- more rows -->
      </tbody>
    </table>
  </div>
  <!-- Optional pager -->
  <div class="table-footer">
    <span>Showing {a}–{b} of {n}</span>
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

## List screen toolbar (search + filter chips)

```html
<div style="display:flex;align-items:center;gap:12px;flex-wrap:wrap">
  <!-- Search pill -->
  <div style="display:flex;align-items:center;gap:8px;background:var(--bg-elevated);border:1px solid var(--border);border-radius:8px;padding:8px 14px;flex:1;max-width:360px">
    <svg width="14" height="14" viewBox="0 0 14 14" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><circle cx="6" cy="6" r="4"/><line x1="9.5" y1="9.5" x2="13" y2="13"/></svg>
    <input type="text" placeholder="Filter by {fields}…" style="background:none;border:none;outline:none;color:var(--text-primary);font-family:var(--font);font-size:13px;width:100%">
  </div>
  <!-- Filter chips -->
  <div style="display:flex;align-items:center;gap:6px;flex-wrap:wrap">
    <span style="font-size:11px;font-weight:600;text-transform:uppercase;letter-spacing:.06em;color:var(--text-dim)">{Facet}</span>
    <!-- active chip -->
    <span style="display:inline-flex;align-items:center;gap:5px;padding:5px 12px;border-radius:20px;font-size:12px;font-weight:600;cursor:pointer;background:var(--accent-bg);border:1px solid var(--accent);color:var(--accent)">
      All <span style="font-size:10px;padding:1px 5px;border-radius:10px;background:rgba(255,255,255,.06)">{n}</span>
    </span>
    <!-- inactive chips -->
    <span style="display:inline-flex;align-items:center;gap:5px;padding:5px 12px;border-radius:20px;font-size:12px;font-weight:600;cursor:pointer;background:var(--bg-elevated);border:1px solid var(--border);color:var(--text-muted)">
      {Value} <span style="font-size:10px;padding:1px 5px;border-radius:10px;background:rgba(255,255,255,.06)">{n}</span>
    </span>
  </div>
</div>
```

---

## Record form — fields with inline validation

Rules live ON the field: required mark (`*`), helper text below, inline error on
invalid field. Submit stays `disabled` until the form is valid. Never add a
separate rules/validation-status panel.

```html
<form style="max-width:760px;display:flex;flex-direction:column;gap:16px" novalidate>
  <div class="card" style="background:var(--bg-surface)">
    <div style="font-size:11px;font-weight:600;letter-spacing:.5px;text-transform:uppercase;color:var(--text-muted);padding:14px 18px;border-bottom:1px solid var(--border);display:flex;align-items:center;gap:7px">
      <!-- inline SVG icon, color:var(--accent) --> {Section title}
    </div>
    <div style="padding:18px;display:flex;flex-direction:column;gap:16px">
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px">

        <!-- Valid field -->
        <div class="field">
          <label class="field-label" for="f1">{Label} <span class="req">*</span></label>
          <input id="f1" class="control" type="text" value="">
          <span class="helper">{format hint / constraint}</span>
        </div>

        <!-- Invalid field: .invalid on .field, show .error-msg -->
        <div class="field invalid">
          <label class="field-label" for="f2">{Label} <span class="req">*</span></label>
          <input id="f2" class="control" type="text" aria-invalid="true" aria-describedby="f2-err">
          <span class="error-msg" id="f2-err" role="alert">
            <svg width="11" height="11" viewBox="0 0 11 11" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="5.5" cy="5.5" r="4.5"/><line x1="5.5" y1="3.5" x2="5.5" y2="6"/><circle cx="5.5" cy="7.5" r=".6" fill="currentColor" stroke="none"/></svg>
            {Specific validation message}
          </span>
        </div>

        <!-- Required select -->
        <div class="field">
          <label class="field-label" for="f3">{Label} <span class="req">*</span></label>
          <select id="f3" class="control"><option value="">Select…</option></select>
          <span class="helper">{option constraint}</span>
        </div>

      </div>
    </div>
  </div>

  <div style="display:flex;align-items:center;justify-content:space-between;gap:12px;padding:16px 0 0">
    <span style="font-size:12px;color:var(--text-dim)">Fields marked <span class="req">*</span> are required.</span>
    <div style="display:flex;gap:10px">
      <button type="button" class="btn btn-ghost">Cancel</button>
      <button type="submit" class="btn btn-primary" disabled aria-disabled="true">{Submit}</button>
    </div>
  </div>
</form>
```

---

## Record detail — header + meta grid + related panels

```html
<div style="display:flex;flex-direction:column;gap:20px">

  <!-- Breadcrumb -->
  <div style="display:flex;align-items:center;gap:7px;font-size:12px;color:var(--text-dim)">
    <a href="#" style="color:var(--text-muted);text-decoration:none">{Parent}</a>
    <svg width="10" height="10" viewBox="0 0 10 10" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M3.5 2l3 3-3 3"/></svg>
    <span>{ID / Name}</span>
  </div>

  <!-- Detail header band -->
  <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px">
    <div style="display:flex;align-items:center;gap:12px;flex-wrap:wrap">
      <!-- Asset icon: 48×48 circle, letter-mark -->
      <div style="width:48px;height:48px;border-radius:50%;background:rgba(16,185,129,.16);color:var(--accent);display:flex;align-items:center;justify-content:center;font-size:18px;font-weight:800">{L}</div>
      <div>
        <div style="display:flex;align-items:center;gap:10px;flex-wrap:wrap">
          <span style="font-size:22px;font-weight:800;letter-spacing:-.5px">{Ticker / ID}</span>
          <!-- Status pill: .active / .pending / .closed -->
          <span class="status-pill active"><span class="pill-dot"></span>{State}</span>
        </div>
        <div style="font-size:13px;color:var(--text-muted);margin-top:2px">{type · context · account}</div>
      </div>
    </div>
    <div style="display:flex;gap:10px">
      <button class="btn btn-ghost">{Action}</button>
      <button class="btn btn-primary">Edit</button>
    </div>
  </div>

  <!-- Meta grid: 3-column label/value cells -->
  <div class="card">
    <div style="display:grid;grid-template-columns:repeat(3,1fr)">
      <!-- Cells: nth-child(3n) has no right border; nth-last-child(-n+3) has no bottom border -->
      <div style="padding:16px 20px;border-right:1px solid var(--border);border-bottom:1px solid var(--border)">
        <div style="font-size:10.5px;font-weight:600;letter-spacing:.07em;text-transform:uppercase;color:var(--text-dim);margin-bottom:6px">{FIELD}</div>
        <div style="font-size:15px;font-weight:700;font-variant-numeric:tabular-nums">{value}</div>
        <div style="font-size:11.5px;color:var(--text-muted);margin-top:3px">{sub}</div>
      </div>
      <!-- more cells... -->
    </div>
  </div>

  <!-- Two-col related panels -->
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;align-items:start">
    <div class="card"><!-- price history mini-chart + data table --></div>
    <div class="card"><!-- activity feed rows --></div>
  </div>

</div>
```
