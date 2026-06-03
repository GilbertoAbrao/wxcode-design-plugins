# Meadow Admin — layout skeletons

Paste-ready, domain-neutral fragments for the Meadow light/natural skin. Each
skeleton is labelled by archetype slot, not by a domain noun. Copy the shell
from `assets/template.html` first (it carries the `:root` tokens + sidebar +
topbar + main slot), then drop the region skeletons below into
`<div class="content">`. Replace every placeholder label with the real
domain's equivalent.

Token recap (full block in `template.html`): page bg `#f7faf5`; card/panel
`#ffffff`; hairline `#e6ece1`; accent `var(--accent)` = `#16a34a`; earth
accent `var(--earth)` = `#a16207`; state tokens `--state-*` with `*-bg`
tints. Put `font-variant-numeric: tabular-nums` on every numeric cell.

---

## Page header (every screen)

```html
<div class="page-header">
  <div>
    <div class="page-title-text">{Screen title}</div>
    <div class="page-sub">{scope · context · date}</div>
  </div>
  <div class="header-actions">
    <button class="btn-ghost">{Secondary}</button>
    <button class="btn-primary">+ {Primary action}</button>
  </div>
</div>
```

---

## KPI card row (repeat ×4 in a `.kpi-grid`)

```html
<div class="kpi-grid">  <!-- grid-template-columns: repeat(4,1fr); gap:14px -->
  <div class="kpi-card">
    <div class="kpi-icon-wrap"><!-- inline SVG 18×18 glyph, color=var(--accent) --></div>
    <!-- use .kpi-icon-earth for earth-accent secondary card -->
    <div class="kpi-label">{UPPERCASE METRIC NAME}</div>
    <div class="kpi-value">{figure}<span style="font-size:14px;font-weight:500;color:#64748b;"> {unit}</span></div>
    <!-- pick one delta variant: -->
    <div class="delta-up">▲ {delta}</div>
    <!-- <div class="delta-down">▼ {delta}</div> -->
    <!-- <div class="delta-neutral">— {label}</div> -->
  </div>
  <!-- 3 more cards -->
</div>
```

---

## Two-column layout (status board / left + side panel / right)

```html
<div class="main-grid">  <!-- grid-template-columns: 1fr 300px; gap:16px -->
  <div class="left-col">
    <!-- stack of cards: status board, chart, readings table -->
  </div>
  <div class="right-panel">
    <!-- context card + task card -->
  </div>
</div>
```

### Status board card (dense table with state pills)

```html
<div class="card">
  <div class="card-header">
    <div class="card-title">{Board title}</div>
    <a href="#" class="card-link">View all →</a>
  </div>
  <table class="data-table">
    <thead>
      <tr>
        <th>{Primary label}</th>
        <th>{Category}</th>
        <th>{Stage}</th>
        <th>{Health}</th>
        <th class="num">{Metric}</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><span class="row-name">{Entity name}</span></td>
        <td>
          <span class="sub-badge">
            <span class="sub-dot" style="background:{dot-color};"></span>{Type}
          </span>
        </td>
        <td><span class="muted-text">{Stage label}</span></td>
        <td>
          <span class="pill pill-healthy">Healthy</span>
          <!-- variants: pill-moderate  pill-attention -->
        </td>
        <td class="num-cell">{value} {unit}</td>
      </tr>
      <!-- more rows -->
    </tbody>
  </table>
</div>
```

### Inline SVG trend chart card

```html
<div class="card">
  <div class="card-header">
    <div class="card-title">{Chart title} ({unit})</div>
    <span style="font-size:12px;color:#94a3b8;">{scope}</span>
  </div>
  <div class="chart-wrap" style="padding:16px 18px 18px;">
    <div class="chart-legend" style="display:flex;gap:16px;margin-bottom:12px;">
      <div style="display:flex;align-items:center;gap:6px;font-size:12px;color:#64748b;">
        <div style="width:10px;height:3px;border-radius:2px;background:var(--chart-primary);"></div>{Series 1}
      </div>
      <div style="display:flex;align-items:center;gap:6px;font-size:12px;color:#64748b;">
        <div style="width:10px;height:2px;background:repeating-linear-gradient(90deg,var(--chart-secondary) 0 5px,transparent 5px 9px);"></div>{Series 2}
      </div>
    </div>
    <!-- SVG area chart: adjust viewBox width to fit x-axis points -->
    <svg style="width:100%;height:140px;display:block;overflow:visible;" viewBox="0 0 560 140" preserveAspectRatio="none">
      <!-- grid lines -->
      <line x1="40" y1="10" x2="40" y2="115" stroke="#e6ece1" stroke-width="1"/>
      <line x1="40" y1="115" x2="548" y2="115" stroke="#e6ece1" stroke-width="1"/>
      <line x1="40" y1="77" x2="548" y2="77" stroke="#f0f4ee" stroke-width="1" stroke-dasharray="3 4"/>
      <line x1="40" y1="46" x2="548" y2="46" stroke="#f0f4ee" stroke-width="1" stroke-dasharray="3 4"/>
      <!-- y-axis labels (replace values) -->
      <text x="35" y="118" fill="#94a3b8" font-size="9" text-anchor="end" font-family="system-ui,sans-serif">0</text>
      <text x="35" y="80" fill="#94a3b8" font-size="9" text-anchor="end" font-family="system-ui,sans-serif">{mid}</text>
      <text x="35" y="18" fill="#94a3b8" font-size="9" text-anchor="end" font-family="system-ui,sans-serif">{max}</text>
      <!-- area fill (primary series) -->
      <path d="M{x1},{y1} L{x2},{y2} … L{xN},{yN} L{xN},115 L{x1},115 Z" fill="var(--chart-primary-fill)"/>
      <!-- primary line -->
      <polyline points="{x1},{y1} {x2},{y2} …" fill="none" stroke="var(--chart-primary)" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
      <!-- secondary line (dashed) -->
      <polyline points="{x1},{y1} {x2},{y2} …" fill="none" stroke="var(--chart-secondary)" stroke-width="1.8" stroke-dasharray="5 4" stroke-linecap="round" stroke-linejoin="round"/>
      <!-- data dots (primary series) -->
      <circle cx="{x1}" cy="{y1}" r="3" fill="var(--chart-primary)"/>
      <!-- x-axis labels (period labels) -->
      <text x="{x1}" y="128" fill="#94a3b8" font-size="9" text-anchor="middle" font-family="system-ui,sans-serif">{P1}</text>
    </svg>
  </div>
</div>
```

### Telemetry / readings table

```html
<div class="card">
  <div class="card-header">
    <div class="card-title">{Readings title}</div>
    <a href="#" class="card-link">{action →}</a>
  </div>
  <table class="data-table">
    <thead>
      <tr>
        <th>ID</th><th>Location</th><th>Metric</th><th>Reading</th><th>Status</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><span class="mono-id">{ID}</span></td>
        <td>{location}</td>
        <td>{metric type}</td>
        <td><span style="font-size:13px;font-weight:600;color:#1e293b;font-variant-numeric:tabular-nums;">{value}</span></td>
        <td>
          <span class="pill pill-online">Online</span>
          <!-- variants: pill-warning  pill-offline -->
        </td>
      </tr>
    </tbody>
  </table>
</div>
```

---

## Records list screen (toolbar + table + pager)

```html
<!-- toolbar -->
<div style="display:flex;align-items:center;gap:12px;flex-wrap:wrap;">
  <div style="display:flex;align-items:center;gap:8px;background:#fff;border:1px solid #e6ece1;border-radius:7px;padding:7px 12px;color:#94a3b8;min-width:260px;">
    <svg width="15" height="15" fill="none" viewBox="0 0 15 15"><circle cx="6.5" cy="6.5" r="4" stroke="currentColor" stroke-width="1.4"/><path d="M10 10l2.5 2.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
    <input type="text" style="border:none;background:transparent;font-size:13px;color:#1e293b;outline:none;width:100%;" placeholder="Filter by {fields}…">
  </div>
  <div style="display:flex;align-items:center;gap:6px;">
    <span style="font-size:11.5px;font-weight:600;color:#64748b;">{Facet}</span>
    <span style="font-size:12px;font-weight:600;border-radius:99px;padding:4px 10px;cursor:pointer;border:1px solid var(--accent-border);background:var(--accent-muted);color:var(--accent);">All <span style="font-size:10.5px;font-weight:700;opacity:.8;">{n}</span></span>
    <span style="font-size:12px;font-weight:600;border-radius:99px;padding:4px 10px;cursor:pointer;border:1px solid #e6ece1;background:#fff;color:#64748b;">{Value}</span>
  </div>
  <span style="margin-left:auto;font-size:12px;color:#94a3b8;">Showing {a}–{b} of {n}</span>
</div>

<!-- table -->
<div class="card">
  <table class="data-table">
    <thead>
      <tr>
        <th>{ID}</th><th>{Name}</th><th>{Type}</th><th>{Stage}</th>
        <th>{Health}</th><th class="num">{Metric}</th><th></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><span class="mono-id">{ID}</span></td>
        <td><span class="row-name">{Name}</span></td>
        <td>{type}</td>
        <td><span class="muted-text">{stage}</span></td>
        <td><span class="pill pill-healthy">Healthy</span></td>
        <td class="num-cell">{value} {unit}</td>
        <td>
          <div style="display:flex;gap:6px;justify-content:flex-end;">
            <button style="border:1px solid #e6ece1;background:#fff;color:#64748b;font-size:11.5px;font-weight:600;border-radius:6px;padding:4px 9px;cursor:pointer;">View</button>
            <button style="border:1px solid #e6ece1;background:#fff;color:#64748b;font-size:11.5px;font-weight:600;border-radius:6px;padding:4px 9px;cursor:pointer;">Edit</button>
          </div>
        </td>
      </tr>
    </tbody>
  </table>
  <div class="rec-footer">
    <span class="footer-count">Showing {a}–{b} of {n} records</span>
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

## Record form — fields with inline validation

Rules live ON the field: required mark (`*`), helper text, inline error on
invalid field. Submit disabled until form is valid. Never add a separate
rules/validation-status panel.

```html
<form novalidate style="display:flex;flex-direction:column;gap:16px;">
  <!-- section card -->
  <div class="card">
    <div style="display:flex;align-items:center;padding:16px 20px 14px;border-bottom:1px solid #e6ece1;">
      <div style="font-size:13.5px;font-weight:700;color:#1e293b;display:flex;align-items:center;gap:7px;">
        <svg width="15" height="15" fill="none" viewBox="0 0 15 15" style="color:var(--accent);"><rect x="2" y="2" width="11" height="11" rx="2.5" stroke="currentColor" stroke-width="1.4"/></svg>
        {Section label}
      </div>
    </div>
    <div style="padding:20px;">
      <div class="field-grid">

        <!-- valid required field -->
        <div class="field">
          <label class="field-label" for="f1">{Label} <span class="req">*</span></label>
          <input id="f1" class="control" type="text" value="" placeholder="{hint}">
          <span class="helper">{what the value drives / format hint}</span>
        </div>

        <!-- invalid field: add .invalid on .field, render .error-msg -->
        <div class="field invalid">
          <label class="field-label" for="f2">{Label} <span class="req">*</span></label>
          <input id="f2" class="control" type="text" aria-invalid="true">
          <span class="error-msg">
            <svg width="13" height="13" fill="none" viewBox="0 0 13 13"><circle cx="6.5" cy="6.5" r="5.5" stroke="currentColor" stroke-width="1.3"/><path d="M6.5 4v3.5" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/><circle cx="6.5" cy="9.5" r=".7" fill="currentColor"/></svg>
            {Specific rule that failed}
          </span>
        </div>

        <!-- required select -->
        <div class="field">
          <label class="field-label" for="f3">{Label} <span class="req">*</span></label>
          <select id="f3" class="control"><option value="">Select…</option></select>
          <span class="helper">{constraint on the options}</span>
        </div>

      </div>
    </div>
  </div>

  <!-- form footer -->
  <div style="display:flex;align-items:center;justify-content:space-between;padding:16px 20px;background:#fff;border:1px solid #e6ece1;border-radius:12px;box-shadow:0 1px 4px rgba(0,0,0,.04);">
    <span style="font-size:12px;color:#94a3b8;">Fields marked <span class="req">*</span> are required.</span>
    <div style="display:flex;gap:8px;">
      <button type="button" class="btn-ghost">Cancel</button>
      <button type="submit" class="btn-primary" disabled>{Submit label}</button>
    </div>
  </div>
</form>
```

---

## Record detail — breadcrumb + header + meta grid + related panels

```html
<div class="breadcrumb">
  <a href="#">{Parent list}</a>
  <svg width="12" height="12" fill="none" viewBox="0 0 12 12"><path d="M4 3l4 3-4 3" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/></svg>
  <span>{ID}</span>
</div>

<!-- header band -->
<div style="display:flex;align-items:flex-start;justify-content:space-between;gap:16px;">
  <div>
    <div style="display:flex;align-items:center;gap:10px;">
      <span style="font-size:12.5px;font-weight:700;color:#94a3b8;letter-spacing:.04em;font-family:'Courier New',monospace;">{ID}</span>
      <span class="pill pill-healthy">{State}</span>
    </div>
    <div style="font-size:22px;font-weight:800;color:#1e293b;letter-spacing:-0.02em;">{Name}</div>
    <div style="font-size:13px;color:#64748b;margin-top:2px;">{type · stage · scope}</div>
  </div>
  <div style="display:flex;gap:8px;flex-shrink:0;">
    <button class="btn-ghost">{Action}</button>
    <button class="btn-primary">Edit</button>
  </div>
</div>

<!-- meta grid -->
<div class="card">
  <div class="meta-grid">  <!-- repeat(3,1fr) -->
    <div class="meta-cell">
      <div class="meta-label">{FIELD}</div>
      <div class="meta-value">{value}</div>
      <div class="meta-sub">{sub-label}</div>
    </div>
    <!-- more cells (up to 9 for a 3×3 grid) -->
  </div>
</div>

<!-- related data: 1fr / 300px -->
<div class="two-col">
  <div class="card">
    <!-- readings sub-table (use .data-table skeleton above) -->
  </div>
  <div class="card">
    <!-- activity timeline -->
    <div class="card-header"><div class="card-title">Recent Activity</div><a class="card-link" href="#">Full log →</a></div>
    <div style="padding:8px 0;">
      <div style="display:flex;align-items:flex-start;gap:10px;padding:10px 18px;border-bottom:1px solid #f0f4ee;">
        <div style="width:8px;height:8px;border-radius:99px;background:var(--accent);flex-shrink:0;margin-top:5px;"></div>
        <div>
          <div style="font-size:13px;color:#334155;line-height:1.4;">{event text}</div>
          <div style="font-size:11px;color:#94a3b8;margin-top:2px;">{timestamp}</div>
          <div style="font-size:11px;font-weight:600;color:#64748b;">{actor}</div>
        </div>
      </div>
      <!-- more activity rows; use background:#a16207 for earth-dot, #94a3b8 for muted-dot, #dc2626 for alert-dot -->
    </div>
  </div>
</div>
```

---

## Side panel — context + task card

```html
<div class="right-panel">
  <!-- context card: hero strip + sub-strip -->
  <div class="card">
    <div class="card-header"><div class="card-title">{Context title}</div><span style="font-size:11px;color:#94a3b8;">{scope}</span></div>
    <div style="display:flex;align-items:center;gap:14px;padding:18px 18px 14px;border-bottom:1px solid #e6ece1;">
      <svg style="color:var(--earth);" width="48" height="48" fill="none" viewBox="0 0 48 48"><!-- domain icon --></svg>
      <div>
        <div style="font-size:32px;font-weight:800;color:#1e293b;letter-spacing:-0.04em;font-variant-numeric:tabular-nums;">{big figure}</div>
        <div style="font-size:13px;color:#64748b;margin-top:2px;">{label}</div>
        <div style="font-size:11px;color:#94a3b8;margin-top:1px;">{sub-label}</div>
      </div>
    </div>
    <!-- 5-item sub-strip -->
    <div style="display:flex;justify-content:space-between;padding:12px 18px;">
      <!-- repeat 5 times -->
      <div style="text-align:center;">
        <div style="font-size:10.5px;font-weight:700;color:#94a3b8;text-transform:uppercase;margin-bottom:4px;">{label}</div>
        <div style="color:var(--earth);margin-bottom:4px;"><!-- SVG icon 20×20 --></div>
        <div style="font-size:12px;font-weight:700;color:#1e293b;font-variant-numeric:tabular-nums;">{hi}</div>
        <div style="font-size:11px;color:#94a3b8;font-variant-numeric:tabular-nums;">{lo}</div>
      </div>
    </div>
  </div>

  <!-- task card -->
  <div class="card">
    <div class="card-header"><div class="card-title">{Tasks title}</div><a class="card-link" href="#">All →</a></div>
    <div style="padding:8px 0;">
      <!-- task row -->
      <div style="display:flex;align-items:flex-start;gap:10px;padding:9px 18px;cursor:pointer;">
        <svg style="color:#cbd5e1;flex-shrink:0;margin-top:1px;" width="16" height="16" fill="none" viewBox="0 0 16 16"><circle cx="8" cy="8" r="6.5" stroke="currentColor" stroke-width="1.4"/></svg>
        <div style="width:7px;height:7px;border-radius:99px;flex-shrink:0;margin-top:5px;background:var(--state-attention);"></div>
        <!-- priority: --state-attention (high) / --state-moderate (med) / --accent (low) -->
        <span style="font-size:13px;color:#334155;line-height:1.4;flex:1;">{task label}</span>
        <span style="font-size:10px;font-weight:700;color:var(--accent);background:var(--accent-muted);border-radius:5px;padding:2px 6px;white-space:nowrap;flex-shrink:0;">{assignee}</span>
      </div>
    </div>
    <div style="display:flex;align-items:center;gap:7px;padding:10px 18px;font-size:13px;font-weight:600;color:var(--accent);cursor:pointer;border-top:1px solid #e6ece1;margin-top:2px;">
      <svg width="14" height="14" fill="none" viewBox="0 0 14 14"><path d="M7 2v10M2 7h10" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
      Add task
    </div>
  </div>
</div>
```
