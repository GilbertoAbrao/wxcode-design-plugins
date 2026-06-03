# Kinetic Admin — layout skeletons

Paste-ready, domain-neutral fragments for the Kinetic dark-green / lime skin.
Each skeleton is labelled by archetype slot, not by a domain noun. Copy the
shell from `assets/template.html` first (it carries the `:root` tokens + topbar
+ icon rail + main slot), then drop the region skeletons below into
`<main class="main">`. Replace every `{placeholder}` label with the real
domain's equivalent.

Token recap (full block in `template.html`):
- Canvas `#0f1410`, panel `#19211a`, inset `#232e25`, hairline `#2c3a2f`
- Text `#e6efe6 / #c5d5c5 / #93a392 / #5a6e5a`
- Accent `var(--accent)` = `#84cc16` (lime)
- State tokens `--state-active / --state-frozen / --state-overdue / --state-pending`
  each with `*-bg` tint at ~13% alpha

Put `font-variant-numeric: tabular-nums` on every numeric cell.

---

## Page header (every screen)

```html
<div class="page-header">
  <div>
    <div class="page-title">{Screen title}</div>
    <div class="page-subtitle">{scope · context · timestamp}</div>
  </div>
  <div class="page-actions">
    <button class="btn-ghost">{Secondary}</button>
    <button class="btn-primary">+ {Primary action}</button>
  </div>
</div>
```

---

## KPI tile (repeat ×4 in a `.kpi-row` grid)

```html
<div class="kpi-row">  <!-- display:grid; grid-template-columns:repeat(4,1fr); gap:16px -->
  <div class="kpi-tile">
    <div class="kpi-icon"><!-- inline SVG glyph, color via var(--accent) --></div>
    <div class="kpi-label">{UPPERCASE METRIC NAME}</div>
    <div class="kpi-value">{figure}</div>       <!-- recolor: style="color:var(--accent)" or --state-overdue -->
    <div><span class="kpi-delta up">▲ {delta}</span></div>  <!-- .up or .down -->
    <!-- optional: <div class="kpi-meta">{sub-line}</div> -->
  </div>
  <!-- 3 more tiles -->
</div>
```

---

## Two-column row (schedule/slot board + chart)

```html
<div style="display:grid;grid-template-columns:7fr 5fr;gap:16px">
  <!-- LEFT: slot / schedule board -->
  <div class="card">
    <div class="card-header">
      <span class="card-title">{Board title}</span>
      <a class="card-link" href="#">View all →</a>
    </div>
    <!-- schedule rows (below) -->
  </div>
  <!-- RIGHT: area chart card -->
  <div class="card">
    <div class="card-header">
      <span class="card-title">{Chart title}</span>
      <span style="font-size:11px;color:#93a392">{sub-label}</span>
    </div>
    <!-- chart legend + SVG area chart (below) -->
  </div>
</div>
```

### Schedule / slot row

`[time] [item name] [facilitator] [capacity bar + fraction]`

```html
<div style="display:grid;grid-template-columns:44px 1fr 120px 140px;align-items:center;gap:10px;padding:11px 18px;border-bottom:1px solid #232e25;transition:background .1s">
  <div style="font-size:12px;font-weight:700;color:var(--accent);font-variant-numeric:tabular-nums">{HH:MM}</div>
  <div style="font-size:12px;font-weight:600;color:#e6efe6">{Item name}</div>
  <div style="font-size:11px;color:#93a392">{Facilitator}</div>
  <div style="display:flex;flex-direction:column;gap:4px">
    <div style="display:flex;align-items:center;justify-content:space-between">
      <span style="font-size:10px;color:#93a392;font-variant-numeric:tabular-nums">{n} / {max}</span>
      <!-- if full: <span class="cap-full-pill">Full</span> -->
    </div>
    <div class="cap-bar-wrap">
      <div class="cap-bar-fill" style="width:{pct}%"></div>
    </div>
  </div>
</div>
```

### Area chart (inline SVG, two series)

```html
<div style="padding:0 18px 16px">
  <!-- Legend -->
  <div style="display:flex;gap:14px;padding:0 0 10px">
    <div style="display:flex;align-items:center;gap:5px;font-size:11px;color:#93a392">
      <div style="width:16px;height:3px;border-radius:2px;background:var(--accent)"></div>{This period}
    </div>
    <div style="display:flex;align-items:center;gap:5px;font-size:11px;color:#93a392">
      <div style="width:16px;height:3px;border-radius:2px;background:#93a392;opacity:.6"></div>{Last period}
    </div>
  </div>
  <svg width="100%" viewBox="0 0 360 148" aria-label="{Chart description}" role="img" style="display:block;overflow:visible">
    <defs>
      <linearGradient id="areaGrad" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%" stop-color="var(--accent)" stop-opacity="0.32"/>
        <stop offset="100%" stop-color="var(--accent)" stop-opacity="0.02"/>
      </linearGradient>
    </defs>
    <!-- dotted grid lines at y=20,60,100 -->
    <line x1="0" y1="20"  x2="360" y2="20"  stroke="#2c3a2f" stroke-width="1" stroke-dasharray="3,4"/>
    <line x1="0" y1="60"  x2="360" y2="60"  stroke="#2c3a2f" stroke-width="1" stroke-dasharray="3,4"/>
    <line x1="0" y1="100" x2="360" y2="100" stroke="#2c3a2f" stroke-width="1" stroke-dasharray="3,4"/>
    <!-- area fill (this period) — replace points with real data -->
    <polygon points="0,{y0} {x1},{y1} … 360,{yN} 360,120 0,120" fill="url(#areaGrad)"/>
    <!-- line stroke (this period) -->
    <polyline points="0,{y0} {x1},{y1} … 360,{yN}" fill="none" stroke="var(--accent)" stroke-width="1.5" stroke-linejoin="round"/>
    <!-- last period dashed line -->
    <polyline points="0,{y0} {x1},{y1} … 360,{yN}" fill="none" stroke="#93a392" stroke-width="1" stroke-dasharray="4,4" opacity=".7"/>
    <!-- x-axis labels at bottom -->
    <text x="0"   y="138" fill="#5a6e5a" font-size="9" text-anchor="middle">{L1}</text>
    <!-- more labels … -->
  </svg>
</div>
```

---

## Records table (dashboard footer or list screen)

```html
<div class="card">
  <div class="card-header">
    <span class="card-title">{Records title}</span>
    <div style="display:flex;gap:8px;align-items:center">
      <button class="btn-ghost">{Export}</button>
      <button class="btn-primary">+ {New}</button>
    </div>
  </div>
  <table class="tbl" aria-label="{table description}">
    <thead>
      <tr>
        <th>{Primary entity}</th>
        <th>{Tier / type}</th>
        <th>Status</th>
        <th>{Timestamp}</th>
        <th style="text-align:right">{Numeric}</th>
        <th></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><!-- avatar cell: .member-cell .member-avatar .member-name --></td>
        <td><span style="font-size:11px;color:#93a392">{tier}</span></td>
        <td><span class="status-pill active"><span class="status-dot"></span>{State}</span></td>
        <td><span style="font-size:11px;color:#93a392;font-variant-numeric:tabular-nums">{time}</span></td>
        <td style="text-align:right;font-variant-numeric:tabular-nums;font-size:12px">{n}</td>
        <td><span style="color:#93a392;cursor:pointer;font-size:14px;letter-spacing:1px">⋯</span></td>
      </tr>
      <!-- status variants: .active .frozen .overdue .pending -->
    </tbody>
  </table>
  <div style="display:flex;align-items:center;justify-content:space-between;padding:12px 18px;border-top:1px solid #2c3a2f">
    <span style="font-size:12px;color:#93a392">Showing {a}–{b} of {n}</span>
    <div style="display:flex;align-items:center;gap:4px">
      <!-- page buttons: .page-btn and .page-btn.active -->
    </div>
  </div>
</div>
```

### List toolbar (search + filter chips)

```html
<div style="display:flex;align-items:center;gap:12px;flex-wrap:wrap">
  <div style="position:relative;flex:0 0 260px">
    <!-- search icon + input (see template.html) -->
    <input class="control" type="text" placeholder="Filter by {fields}…" style="height:34px;background:#19211a;padding-left:32px">
  </div>
  <div style="display:flex;align-items:center;gap:8px">
    <span style="font-size:11px;color:#93a392;text-transform:uppercase;letter-spacing:.06em">{Facet}</span>
    <span class="chip active">All <span class="chip-count">{n}</span></span>
    <span class="chip">{Value} <span class="chip-count">{n}</span></span>
    <!-- chip classes: .chip and .chip.active -->
  </div>
</div>
```

---

## Record form — fields with inline validation

Rules live ON the field: a required mark (`*`), helper text under the field, and
an inline error message on invalid fields. The submit stays `disabled` until the
form is valid. Never add a separate rules/validation-status summary panel.

```html
<form novalidate>
  <div class="card" style="margin-bottom:16px">
    <div style="display:flex;align-items:center;gap:8px;padding:14px 18px;border-bottom:1px solid #2c3a2f">
      <!-- optional section icon (SVG, color:var(--accent)) -->
      <span style="font-size:13px;font-weight:600;color:#e6efe6">{Section name}</span>
    </div>
    <div style="padding:18px 18px 8px">
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:14px 20px">

        <!-- valid field -->
        <div class="field">
          <label class="field-label" for="f1">{Label} <span class="req">*</span></label>
          <input id="f1" class="control" type="text" placeholder="{hint}" value="">
          <span class="helper">{what the value drives / format hint}</span>
        </div>

        <!-- invalid field — add .invalid on .field -->
        <div class="field invalid">
          <label class="field-label" for="f2">{Label} <span class="req">*</span></label>
          <input id="f2" class="control" type="text" aria-invalid="true">
          <span class="error-msg">
            <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
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

  <div style="display:flex;align-items:center;justify-content:space-between;padding-top:16px">
    <span style="font-size:11px;color:#93a392">Fields marked <span class="req">*</span> are required.</span>
    <div style="display:flex;align-items:center;gap:8px">
      <button type="button" class="btn-ghost">Cancel</button>
      <button type="submit" class="btn-primary" disabled>{Submit}</button>
    </div>
  </div>
</form>
```

---

## Record detail — header + meta grid + related panels

```html
<div style="display:flex;align-items:center;gap:16px">
  <!-- avatar circle (lime bg, dark initials) -->
  <div style="width:52px;height:52px;border-radius:50%;background:var(--accent);display:flex;align-items:center;justify-content:center;font-size:18px;font-weight:800;color:#0f1410;flex-shrink:0">{XX}</div>
  <div style="flex:1">
    <div style="display:flex;align-items:center;gap:10px">
      <span style="font-size:19px;font-weight:700;color:#e6efe6;letter-spacing:-0.02em">{Name / ID}</span>
      <span class="status-pill active"><span class="status-dot"></span>{State}</span>
    </div>
    <div style="font-size:12px;color:#93a392;margin-top:3px">{sub-line — key attributes}</div>
  </div>
  <div style="display:flex;align-items:center;gap:8px">
    <button class="btn-ghost">{Action}</button>
    <button class="btn-primary">Edit</button>
  </div>
</div>

<!-- meta grid: 4 cells -->
<div class="card">
  <div style="display:grid;grid-template-columns:repeat(4,1fr)">
    <div style="padding:16px 18px;border-right:1px solid #2c3a2f">
      <div style="font-size:10px;font-weight:600;text-transform:uppercase;letter-spacing:.07em;color:#93a392;margin-bottom:5px">{FIELD}</div>
      <div style="font-size:14px;font-weight:700;color:#e6efe6;font-variant-numeric:tabular-nums">{value}</div>
      <div style="font-size:11px;color:#93a392;margin-top:2px">{sub}</div>
    </div>
    <!-- 3 more cells — last one: no border-right -->
  </div>
</div>

<!-- lower two-column: 7fr / 5fr -->
<div style="display:grid;grid-template-columns:7fr 5fr;gap:16px;align-items:start">
  <div class="card"><!-- slot-board rows or related sub-table --></div>
  <div class="card"><!-- activity / event feed --></div>
</div>
```

---

## Personnel card row (3 equal columns)

```html
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px">
  <div style="background:#232e25;border:1px solid #2c3a2f;border-radius:10px;padding:18px;display:flex;flex-direction:column;gap:12px">
    <div style="display:flex;align-items:center;gap:12px">
      <!-- avatar: 40px circle, lime bg, dark text -->
      <div style="width:40px;height:40px;border-radius:50%;background:var(--accent);display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:800;color:#0f1410;flex-shrink:0">{XX}</div>
      <div>
        <div style="font-size:13px;font-weight:700;color:#e6efe6">{Name}</div>
        <div style="font-size:11px;color:#93a392;margin-top:1px">{Specialty / role}</div>
      </div>
    </div>
    <div style="display:flex;align-items:center;justify-content:space-between;font-size:11px">
      <span style="color:#93a392">{n} sessions this week</span>
      <!-- star rating: lime stars, .3 opacity for empty -->
      <span style="display:inline-flex;gap:1px;color:var(--accent)">★★★★★</span>
    </div>
  </div>
  <!-- 2 more cards -->
</div>
```
