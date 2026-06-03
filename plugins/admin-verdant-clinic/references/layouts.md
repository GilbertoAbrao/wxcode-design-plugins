# Verdant Admin — layout skeletons

Paste-ready, domain-neutral fragments for the Verdant calm light-mode skin. Each
skeleton is labelled by archetype slot, not by a domain noun. Copy the shell from
`assets/template.html` first (it carries the `:root` tokens + sidebar + topbar +
main slot), then drop the region skeletons below into `<main class="page-body">`.
Replace every `{placeholder}` with the real domain's equivalent.

Token recap (full block in `template.html`): page bg `#f7faf9`; card / sidebar bg
`#ffffff`; border `#e3ece9`; text ramp `#1e293b / #475569 / #94a3b8`; accent
`var(--accent-emerald)` = `#10b981` → hover teal `#0d9488`; status tokens
`--status-stable-* / --status-pending-* / --status-urgent-* / --status-info-*`.
Use `font-variant-numeric: tabular-nums` on every numeric cell.

---

## Page header (every screen)

```html
<div class="page-header">
  <div>
    <h1 class="page-title">{Screen title}</h1>
    <p class="page-subtitle">{Scope · context · date}</p>
  </div>
  <div class="page-actions">
    <button class="btn-ghost">{Secondary action}</button>
    <button class="btn-primary">+ {Primary action}</button>
  </div>
</div>
```

---

## KPI card row (×4 in a `.kpi-row` grid)

```html
<section aria-label="{Metrics section}" class="kpi-row">
  <!-- repeat for each KPI -->
  <div class="kpi-card">
    <div class="kpi-header">
      <span class="kpi-label">{METRIC NAME}</span>
      <span class="kpi-icon emerald" aria-hidden="true"><!-- inline SVG --></span>
      <!-- tone variants: .emerald / .teal / .amber / .rose -->
    </div>
    <div class="kpi-value">{figure}<span style="font-size:16px;font-weight:500;color:#94a3b8"> {unit}</span></div>
    <div class="kpi-footer">
      <!-- sparkline: polyline SVG for trend, rect SVG for bar-sparkline, or a fill bar -->
      <svg width="72" height="24" viewBox="0 0 72 24" fill="none" aria-hidden="true">
        <polyline points="0,20 12,15 24,17 36,10 48,12 60,7 72,4"
          stroke="var(--spark-emerald)" stroke-width="2"
          stroke-linecap="round" stroke-linejoin="round" fill="none"/>
      </svg>
      <span class="delta-chip up">↑ {pct}%</span>
      <!-- .up / .down / .flat -->
    </div>
  </div>
</section>
```

---

## 2-column main grid (schedule board + chart panel)

```html
<div class="mid-grid">  <!-- grid-template-columns: 1fr 340px; gap: 16px -->

  <!-- Left: schedule / board table -->
  <div class="card">
    <div class="card-header">
      <div>
        <div class="card-title">{Board title}</div>
        <div class="card-subtitle">{count · context}</div>
      </div>
      <a href="#" class="view-all">View all</a>
    </div>
    <table class="schedule-table">
      <thead>
        <tr>
          <th>{Time / ID}</th><th>{Entity}</th><th>{Type}</th><th>{Slot}</th><th>Status</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td class="slot-time">{HH:MM}</td>
          <td>
            <div class="entity-cell">
              <div class="entity-dot dot-em">{XX}</div>
              <div>
                <div class="entity-name">{Name}</div>
                <div class="entity-sub">{sub-ID or secondary label}</div>
              </div>
            </div>
          </td>
          <td>{type label}</td>
          <td><span class="slot-badge">{slot}</span></td>
          <td><span class="status-pill pill-pending">{State}</span></td>
          <!-- pill variants: .pill-stable .pill-pending .pill-urgent .pill-info -->
        </tr>
        <!-- 7 more rows -->
      </tbody>
    </table>
  </div>

  <!-- Right: mini-chart panel -->
  <div class="card">
    <div class="card-header">
      <div>
        <div class="card-title">{Chart title}</div>
        <div class="card-subtitle">Last {N} days · {M} series</div>
      </div>
    </div>
    <div class="chart-card-body" style="padding:16px 20px;">
      <div class="chart-legend" style="display:flex;gap:14px;flex-wrap:wrap;margin-bottom:14px;" aria-hidden="true">
        <span class="legend-item"><span class="legend-dot ld-1"></span>{Series A}</span>
        <span class="legend-item"><span class="legend-dot ld-2"></span>{Series B}</span>
        <span class="legend-item"><span class="legend-dot ld-3"></span>{Series C}</span>
        <span class="legend-item"><span class="legend-dot ld-4"></span>{Series D}</span>
      </div>
      <!-- 7-day × 4-series grouped bar chart — adjust rects for real data -->
      <svg viewBox="0 0 300 130" width="100%" height="130" aria-label="{chart description}">
        <!-- grid lines -->
        <line x1="0" y1="0"   x2="300" y2="0"   stroke="#e3ece9" stroke-width="1"/>
        <line x1="0" y1="32"  x2="300" y2="32"  stroke="#e3ece9" stroke-width="1"/>
        <line x1="0" y1="64"  x2="300" y2="64"  stroke="#e3ece9" stroke-width="1"/>
        <line x1="0" y1="96"  x2="300" y2="96"  stroke="#e3ece9" stroke-width="1"/>
        <line x1="0" y1="128" x2="300" y2="128" stroke="#e3ece9" stroke-width="1"/>
        <!-- Day 1: x offset 4; 4 bars at x+0, x+10, x+20, x+30; width 9 each -->
        <rect x="4"  y="{y}" width="9" height="{h}" rx="2" fill="var(--chart-bar-1)"/>
        <rect x="14" y="{y}" width="9" height="{h}" rx="2" fill="var(--chart-bar-2)"/>
        <rect x="24" y="{y}" width="9" height="{h}" rx="2" fill="var(--chart-bar-3)"/>
        <rect x="34" y="{y}" width="9" height="{h}" rx="2" fill="var(--chart-bar-4)"/>
        <!-- Repeat for days 2–7; next group starts at x+42 -->
      </svg>
      <div style="display:flex;justify-content:space-between;padding:0 4px;margin-top:6px;font-size:10px;color:#94a3b8;" aria-hidden="true">
        <span>{d1}</span><span>{d2}</span><span>{d3}</span>
        <span>{d4}</span><span>{d5}</span><span>{d6}</span><span>{d7}</span>
      </div>
    </div>
  </div>

</div>
```

---

## Records table (dashboard footer or list screen)

```html
<div class="card">
  <div class="card-header">
    <div>
      <div class="card-title">{Records title}</div>
      <div class="card-subtitle">{scope · timestamp}</div>
    </div>
    <a href="#" class="view-all">View all</a>
  </div>
  <table class="records-table">
    <thead>
      <tr>
        <th>{Entity / Name}</th><th>{Metric}</th><th>{Category}</th><th>{Timestamp}</th><th>Status</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>
          <div class="rec-name-cell" style="display:flex;align-items:center;gap:10px;">
            <div class="entity-dot dot-em">{XX}</div>
            <div>
              <div class="rec-name" style="font-weight:600;color:#1e293b;">{Name}</div>
              <div class="rec-sub" style="font-size:11px;color:#94a3b8;">{ID / sub-label}</div>
            </div>
          </div>
        </td>
        <td style="font-variant-numeric:tabular-nums;">{metric}</td>
        <td><span class="cat-tag">{Category}</span></td>
        <td>{timestamp}</td>
        <td><span class="status-pill pill-pending">{State}</span></td>
      </tr>
      <!-- 7 more rows -->
    </tbody>
  </table>
</div>
```

---

## List toolbar (search + filter chips)

```html
<div class="toolbar" role="search" aria-label="Filter {records}">
  <div class="toolbar-search">
    <!-- magnifier SVG -->
    <input type="search" placeholder="Filter by {fields}…" aria-label="Filter {records}" />
  </div>
  <div class="filter-group">
    <span class="filter-label">{Facet}</span>
    <span class="chip active">All <span class="chip-count">{n}</span></span>
    <span class="chip">{Value A} <span class="chip-count">{n}</span></span>
    <span class="chip">{Value B} <span class="chip-count">{n}</span></span>
  </div>
  <span class="result-count">Showing {a}–{b} of {n}</span>
</div>
```

---

## Record form — fields with inline validation

Rules live ON the field: a required mark (`*`), helper text under the field, and
an inline error message on an invalid field. The submit stays `disabled` until the
form is valid. Never add a separate rules/validation-status summary panel.

```html
<form class="form-wrap" novalidate>

  <div class="card">
    <div class="card-section-title"><!-- SVG icon -->{Section label}</div>
    <div class="card-body" style="padding:20px;">
      <div class="field-grid" style="display:grid;grid-template-columns:1fr 1fr;gap:18px 20px;">

        <!-- Valid field -->
        <div class="field valid">
          <label class="field-label" for="f1">{Label} <span class="req">*</span></label>
          <input id="f1" class="control" type="text" value="{value}" aria-required="true" />
          <span class="valid-msg"><!-- check SVG -->{Confirmation text}</span>
        </div>

        <!-- Invalid field -->
        <div class="field invalid">
          <label class="field-label" for="f2">{Label} <span class="req">*</span></label>
          <input id="f2" class="control" type="text" value="" aria-required="true"
                 aria-invalid="true" aria-describedby="f2-err" />
          <span id="f2-err" class="error-msg" role="alert">
            <!-- alert SVG -->{Specific rule that failed}
          </span>
        </div>

        <!-- Required select -->
        <div class="field">
          <label class="field-label" for="f3">{Label} <span class="req">*</span></label>
          <select id="f3" class="control" aria-required="true">
            <option value="">Select…</option>
            <option>{Option A}</option>
          </select>
          <span class="helper">{Constraint hint}</span>
        </div>

        <!-- Date with future constraint -->
        <div class="field">
          <label class="field-label" for="f4">{Date label} <span class="req">*</span></label>
          <input id="f4" class="control" type="date" aria-required="true" />
          <span class="helper">Must be today or a future date</span>
        </div>

        <!-- Full-width textarea -->
        <div class="field full" style="grid-column:1/-1;">
          <label class="field-label" for="f5">{Notes}</label>
          <textarea id="f5" class="control" style="min-height:80px;resize:vertical;" placeholder="{hint}"></textarea>
        </div>

      </div>
    </div>
  </div>

  <div class="form-footer">
    <span class="form-hint">Fields marked <span class="req">*</span> are required.</span>
    <div class="footer-actions">
      <button type="button" class="btn-ghost">Cancel</button>
      <button type="submit" class="btn-primary" disabled aria-disabled="true">{Submit action}</button>
    </div>
  </div>

</form>
```

---

## Record detail — header + meta grid + related panels

```html
<div style="display:flex;flex-direction:column;gap:20px;">

  <!-- Breadcrumb trail -->
  <nav aria-label="Breadcrumb" style="display:flex;align-items:center;gap:6px;font-size:13px;color:#94a3b8;">
    <a href="#">{Parent list}</a>
    <span style="color:#cbd5e1;">/</span>
    <strong style="color:#1e293b;">{Record ID}</strong>
  </nav>

  <!-- Header band -->
  <div class="detail-header" style="background:#fff;border:1px solid #e3ece9;border-radius:12px;box-shadow:0 1px 4px rgba(0,0,0,.05);padding:20px 24px;display:flex;align-items:center;justify-content:space-between;gap:16px;">
    <div style="display:flex;align-items:center;gap:14px;">
      <div class="entity-dot dot-em" style="width:40px;height:40px;font-size:14px;">{XX}</div>
      <div>
        <div style="display:flex;align-items:center;gap:10px;flex-wrap:wrap;">
          <span style="font-family:'Courier New',monospace;font-size:12px;color:#64748b;background:#f1f5f3;padding:3px 7px;border-radius:4px;">{ID}</span>
          <span class="status-pill pill-stable">{State}</span>
        </div>
        <div style="font-size:22px;font-weight:800;color:#0f172a;letter-spacing:-.4px;margin-top:4px;">{Primary name}</div>
        <div style="font-size:13px;color:#94a3b8;">{Category · group · sub-label}</div>
      </div>
    </div>
    <div style="display:flex;gap:10px;align-items:center;flex-shrink:0;">
      <button class="btn-ghost">{Action}</button>
      <button class="btn-primary">Edit</button>
    </div>
  </div>

  <!-- Meta grid: 3-col label/value cells -->
  <div class="card">
    <div style="display:grid;grid-template-columns:repeat(3,1fr);">
      <!-- Each cell -->
      <div style="padding:16px 20px;border-right:1px solid #e3ece9;border-bottom:1px solid #e3ece9;">
        <div style="font-size:10.5px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:#94a3b8;margin-bottom:4px;">{FIELD}</div>
        <div style="font-size:14px;font-weight:600;color:#1e293b;">{value}</div>
        <div style="font-size:11px;color:#94a3b8;margin-top:2px;">{sub}</div>
      </div>
      <!-- Repeat ×(3n cells); last column: no border-right; last row: no border-bottom -->
    </div>
  </div>

  <!-- Lower two-col: related data + activity -->
  <div style="display:grid;grid-template-columns:7fr 5fr;gap:16px;align-items:start;">
    <div class="card"><!-- related records / sessions table (same pattern as records-table) --></div>
    <div class="card"><!-- activity timeline feed --></div>
  </div>

</div>
```

---

## Pagination footer

```html
<div style="display:flex;align-items:center;justify-content:space-between;padding:12px 16px;border-top:1px solid #e3ece9;font-size:12px;color:#94a3b8;">
  <span>Showing {a}–{b} of {n}</span>
  <div style="display:flex;gap:4px;" aria-label="Pagination">
    <button class="page-btn" aria-label="Previous">‹</button>
    <button class="page-btn active" aria-current="page">1</button>
    <button class="page-btn">2</button>
    <button class="page-btn">›</button>
  </div>
</div>
```
