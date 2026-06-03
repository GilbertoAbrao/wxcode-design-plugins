# Meridian Admin — layout skeletons

Paste-ready, domain-neutral fragments for the Meridian warm-light-mode / indigo-accent skin.
Each skeleton is labelled by archetype slot, not by a domain noun. Copy the shell from
`assets/template.html` first (it carries the `:root` tokens + sidebar + topbar + main slot),
then drop the region skeletons below into `<div class="content">`.
Replace every `{placeholder}` with the real domain's equivalent.

Token recap (full block in `template.html`): canvas `#f8f8fb`, sidebar/card `#ffffff`,
border `#e8e8ef`, row divider `#f1f1f5`; text `#1e1e2d / #6b7280 / #9ca3af`;
accent `var(--color-accent)` = `#4f46e5`; state tokens `--color-success/warn/danger/probation`
with matching `-bg` tints. Category bar palette: `--color-cat-a…f`.

---

## KPI tile row (repeat ×4 in a `.kpi-row` grid)

```html
<div class="kpi-row">  <!-- display:grid; grid-template-columns:repeat(4,1fr); gap:16px -->
  <div class="kpi-card">
    <div class="kpi-label">{UPPERCASE METRIC LABEL}</div>
    <div class="kpi-number">{figure}</div>
    <div class="kpi-footer">
      <span class="kpi-delta up">↑ {delta}</span>   <!-- .up / .down / .warn -->
      <svg class="kpi-sparkline" width="60" height="32" viewBox="0 0 60 32" fill="none">
        <!-- inline polyline + polygon area fill; stroke color matches delta state -->
      </svg>
    </div>
  </div>
  <!-- 3 more tiles -->
</div>
```

---

## Two-column mid-grid (area-chart card + breakdown card)

```html
<div style="display:grid;grid-template-columns:1fr 300px;gap:16px;margin-bottom:20px;align-items:start">

  <!-- Area-chart card -->
  <div class="chart-card">  <!-- .chart-card = white card, 12px radius, shadow -->
    <div class="card-header">
      <div>
        <div class="card-title">{Chart title}</div>
        <div class="card-subtitle">{scope · period}</div>
      </div>
      <div style="display:flex;flex-direction:column;align-items:flex-end;gap:8px">
        <!-- Period tab group -->
        <div class="chart-tabs">
          <span class="chart-tab">6M</span>
          <span class="chart-tab active">12M</span>
          <span class="chart-tab">All</span>
        </div>
        <div class="chart-legend">
          <div class="legend-item"><span class="legend-dot" style="background:var(--color-accent)"></span>{Series label}</div>
        </div>
      </div>
    </div>
    <!-- Full-width inline SVG: grid lines + gradient area + polyline + axis labels -->
    <svg width="100%" viewBox="0 0 640 180" preserveAspectRatio="none" fill="none">
      <!-- horizontal grid lines at y=30,70,110,150 -->
      <!-- defs: linearGradient id="areaGrad" from accent@.18 to accent@0 -->
      <!-- polygon fill="url(#areaGrad)" : area under the line -->
      <!-- polyline stroke="var(--color-accent)" : the data line -->
      <!-- circle at latest point: r=4 fill accent + r=7 fill accent@.15 -->
      <!-- text x-axis labels at bottom (y=168) -->
      <!-- text y-axis labels at left -->
    </svg>
  </div>

  <!-- Horizontal-bar breakdown card -->
  <div class="dept-card">  <!-- .dept-card = white card, 12px radius, shadow, padding:20px -->
    <div class="card-header" style="margin-bottom:20px">
      <div>
        <div class="card-title">{Breakdown title}</div>
        <div class="card-subtitle">{N} total</div>
      </div>
    </div>
    <!-- One .dept-row per category -->
    <div class="dept-row">
      <div class="dept-swatch" style="background:var(--color-cat-a)"></div>
      <div class="dept-name">{Category A}</div>
      <div class="dept-bar-track"><div class="dept-bar-fill" style="width:100%;background:var(--color-cat-a)"></div></div>
      <div class="dept-count">{N}</div>
      <div class="dept-pct">{pct}%</div>
    </div>
    <!-- More rows; bar widths are percentages relative to the max category -->
  </div>

</div>
```

---

## Bottom row (records table + 320px side panel)

```html
<div style="display:grid;grid-template-columns:1fr 300px;gap:16px;align-items:start">

  <!-- Records table card -->
  <div class="table-card">
    <div class="table-header">
      <div style="display:flex;align-items:center;gap:10px">
        <div class="table-title">{Records title}</div>
        <div class="table-count">{N}</div>
        <div class="filter-pills">
          <span class="filter-pill active">All</span>
          <span class="filter-pill">{State A}</span>
          <span class="filter-pill">{State B}</span>
        </div>
      </div>
      <button class="btn-primary">
        <svg width="12" height="12" viewBox="0 0 12 12" fill="none"><path d="M6 2v8M2 6h8" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
        {Add action}
      </button>
    </div>
    <table>
      <thead>
        <tr>
          <th>{Name / Identifier}</th>
          <th>{Role / Type}</th>
          <th>{Category}</th>
          <th>Status</th>
          <th>{Date}</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>
            <div class="rec-cell">
              <div class="rec-avatar" style="background:{color}">{II}</div>
              <div>
                <div class="rec-name">{Full name}</div>
                <div class="rec-sub">{sub-line}</div>
              </div>
            </div>
          </td>
          <td>{role}</td>
          <td>{category}</td>
          <td><span class="status-pill s-active">{State}</span></td>   <!-- s-active/s-warn/s-info/s-danger -->
          <td>{date}</td>
        </tr>
        <!-- More rows -->
      </tbody>
    </table>
    <div class="table-footer">
      <span>Showing {a}–{b} of {N}</span>
      <div class="pagination">
        <button class="page-btn">‹</button>
        <button class="page-btn active">1</button>
        <button class="page-btn">2</button>
        <button class="page-btn">›</button>
      </div>
    </div>
  </div>

  <!-- Side panel: queued-approvals list -->
  <div class="side-panel">
    <div class="panel-card">
      <div class="panel-title">{Panel title}</div>
      <div class="panel-sub">{date / context sub-line}</div>

      <!-- approval-item: avatar + info + action buttons + day count -->
      <div class="approval-item">
        <div class="appr-avatar" style="background:{color}">{II}</div>
        <div class="appr-info">
          <div class="appr-name">{Name}</div>
          <div class="appr-type">{Request type}</div>
          <div class="appr-actions">
            <button class="appr-btn appr-btn-ok">Approve</button>
            <button class="appr-btn appr-btn-no">Decline</button>
          </div>
        </div>
        <div class="appr-days">{N} days</div>
      </div>
      <!-- More approval-items -->
    </div>

    <div class="panel-card">
      <div class="pending-header">
        <div class="pending-label">{Secondary section title}</div>
        <span class="pending-count">{N}</span>
      </div>
      <div class="pending-item">
        <div class="pending-dot"></div>
        <div class="pending-body">
          <div class="pending-name">{Name}</div>
          <div class="pending-detail">{detail line}</div>
          <div class="pending-when">{submitted when}</div>
        </div>
      </div>
      <!-- More pending-items -->
      <a class="view-all" href="#">View all {N} →</a>
    </div>
  </div>

</div>
```

---

## Records list — search + filter toolbar (full-page variant)

```html
<div class="list-toolbar">  <!-- flex; gap:12px; margin-bottom:16px -->
  <!-- Search -->
  <div class="toolbar-search">  <!-- position:relative; flex:1; max-width:320px -->
    <svg class="toolbar-search-icon"><!-- magnifier --></svg>
    <input type="text" placeholder="Search by {fields}…">
  </div>
  <!-- Status filter chips -->
  <div class="filter-group">
    <span class="filter-label">{Facet}</span>
    <span class="chip active">All <span class="chip-count">{N}</span></span>
    <span class="chip">{Value} <span class="chip-count">{n}</span></span>
  </div>
  <!-- Category filter chips -->
  <div class="filter-group">
    <span class="filter-label">{Facet 2}</span>
    <span class="chip active">All</span>
    <span class="chip">{Cat A}</span>
    <span class="chip">{Cat B}</span>
  </div>
  <button class="btn-primary">+ {Add}</button>
</div>
```

---

## Record form — fields with inline validation

Rules live ON the field: required mark (`*`), helper text, inline error on invalid.
Submit is disabled until valid. Never add a separate rules/validation-status panel.

```html
<form class="form-container" novalidate>

  <div class="form-card">
    <div class="card-section-header">
      <!-- icon + section title -->
      <span class="card-section-title">{Section title}</span>
    </div>
    <div class="card-body">
      <div class="field-grid">  <!-- display:grid; grid-template-columns:1fr 1fr; gap:16px -->

        <!-- Valid field -->
        <div class="field valid">
          <label class="field-label" for="f1">{Label} <span class="req">*</span></label>
          <input id="f1" class="control" type="text" value="{value}">
          <span class="helper">{what it drives / format hint}</span>
        </div>

        <!-- Invalid field -->
        <div class="field invalid">
          <label class="field-label" for="f2">{Label} <span class="req">*</span></label>
          <input id="f2" class="control" type="text" aria-invalid="true" aria-describedby="f2-err">
          <span class="error-msg" id="f2-err">
            <svg width="12" height="12" viewBox="0 0 12 12" fill="none"><circle cx="6" cy="6" r="5" stroke="currentColor" stroke-width="1.3"/><path d="M6 4v3M6 8.5v.5" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"/></svg>
            {Specific rule that failed}
          </span>
        </div>

        <!-- Required select -->
        <div class="field">
          <label class="field-label" for="f3">{Label} <span class="req">*</span></label>
          <select id="f3" class="control"><option value="">Select…</option></select>
          <span class="helper">{constraint on the options}</span>
        </div>

        <!-- Full-width textarea -->
        <div class="field full">
          <label class="field-label" for="f4">{Label}</label>
          <textarea id="f4" class="control" placeholder="{hint}"></textarea>
        </div>

      </div>
    </div>
  </div>

  <div class="form-footer">
    <span class="form-hint">Fields marked <span class="req">*</span> are required.</span>
    <div class="footer-actions">
      <button type="button" class="btn-ghost">Cancel</button>
      <button type="submit" class="btn-primary" disabled>{Submit action}</button>
    </div>
  </div>

</form>
```

---

## Record detail — breadcrumb + header + meta grid + related panels

```html
<div class="detail-wrap">  <!-- max-width:900px -->

  <div class="breadcrumb">
    <a href="#">{Parent list}</a>
    <span class="breadcrumb-sep">›</span>
    <span>{Record identifier}</span>
  </div>

  <!-- Header band -->
  <div class="detail-header">
    <div class="detail-avatar">{II}</div>
    <div class="detail-title-block">
      <div class="detail-name">{Record name}</div>
      <div class="detail-meta">
        <span>{Role/type}</span>
        <span style="color:#d1d5db">·</span>
        <span>{Category}</span>
        <span style="color:#d1d5db">·</span>
        <span class="status-pill s-active">{State}</span>
      </div>
    </div>
    <div class="detail-actions">
      <button class="btn-ghost">Edit</button>
      <button class="btn-primary">{Primary action}</button>
    </div>
  </div>

  <!-- Meta grid: 3-col label/value -->
  <div class="card">
    <div class="meta-grid">  <!-- display:grid; grid-template-columns:repeat(3,1fr) -->
      <div class="meta-cell">
        <div class="meta-label">{FIELD}</div>
        <div class="meta-value">{value}</div>
        <div class="meta-sub">{sub-line}</div>
      </div>
      <!-- More cells (border-right on cols 1,2; border-bottom on all but last row) -->
    </div>
  </div>

  <!-- Two-col related panels -->
  <div class="two-col">  <!-- display:grid; grid-template-columns:1fr 1fr; gap:16px -->
    <div class="card"><!-- mini breakdown or sub-panel rows --></div>
    <div class="card"><!-- activity log or secondary sub-panel --></div>
  </div>

</div>
```
