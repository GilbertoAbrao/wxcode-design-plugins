# Slate Admin — layout skeletons

Paste-ready, domain-neutral fragments for the Slate light-mode skin. Each skeleton
is labelled by archetype slot, not by a domain noun. Copy the shell from
`assets/template.html` first (it carries the `:root` tokens + sidebar + topbar +
main/content slot), then drop the region skeletons below into `<div class="content">`.
Replace every {placeholder} with the real domain's equivalent.

Token recap (full block in `template.html`): page `#f9fafb`, card `#ffffff`, hover
`#f3f4f6`, border `#e5e7eb`; text `#111827 / #6b7280 / #9ca3af`; accent emerald
`var(--accent)` = `#10b981`; accent amber `#f59e0b`; card shadow
`0 1px 3px rgba(0,0,0,.07)`. Put `font-variant-numeric: tabular-nums` on every
numeric cell.

---

## KPI card row (repeat ×4 in a `.kpi-row` grid)

```html
<div class="kpi-row">  <!-- display:grid; grid-template-columns:repeat(4,1fr); gap:16px -->
  <div class="kpi-card">
    <div class="kpi-top">
      <span class="kpi-label">{METRIC NAME}</span>
      <!-- Inline SVG sparkline 56×28 px; emerald for positive, danger red for downward -->
      <svg class="kpi-sparkline" width="56" height="28" viewBox="0 0 56 28" fill="none">
        <polyline points="0,22 8,18 16,20 24,14 32,16 40,10 48,8 56,4"
          stroke="var(--accent)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        <polyline points="0,22 8,18 16,20 24,14 32,16 40,10 48,8 56,4 56,28 0,28"
          fill="var(--accent)" fill-opacity=".10"/>
      </svg>
    </div>
    <div class="kpi-value">{figure}</div>     <!-- font-variant-numeric:tabular-nums; 26px/800 -->
    <div class="kpi-bottom">
      <span class="delta up">↑ {pct}%</span>  <!-- .up / .down / .warn -->
      <span class="kpi-sub">{vs prior period}</span>
    </div>
  </div>
  <!-- 3 more cards -->
</div>
```

---

## Two-column grid: metric bar chart + ranked items panel

```html
<div class="lower-grid">  <!-- display:grid; grid-template-columns:1fr 320px; gap:16px -->

  <!-- Left: metric bar chart -->
  <div class="chart-card">
    <div class="card-header">
      <div>
        <div class="card-title">{Chart title}</div>
        <div class="card-meta">{period · unit}</div>
      </div>
      <!-- optional legend -->
    </div>
    <div class="chart-area">
      <div class="chart-y-labels">  <!-- abs-positioned; width:44px; flex-col space-between -->
        <span>{max}</span><span>{mid}</span><span>{low}</span><span>0</span>
      </div>
      <div class="chart-wrap">   <!-- margin-left:52px -->
        <svg width="100%" height="180" viewBox="0 0 620 180" preserveAspectRatio="xMidYMid meet">
          <!-- Gridlines at y=10, 60, 110, 158 -->
          <!-- Prior-period bars: fill var(--accent-light) -->
          <!-- Current-period bars: fill #cbd5e1 (muted slate) -->
          <!-- Active/current bar: fill var(--accent) + tooltip bubble -->
          <!-- Future bars: fill #e2e8f0 -->
          <!-- X-axis labels: font-size=10, fill=#9ca3af; active label fill=var(--accent) weight=700 -->
        </svg>
      </div>
    </div>
  </div>

  <!-- Right: ranked items panel -->
  <div class="ranked-card">
    <div class="card-header">
      <div class="card-title">{Panel title}</div>
      <a class="view-all" href="#">View all →</a>
    </div>
    <div class="ranked-row">   <!-- display:flex; align-items:center; gap:12px; padding:10px 0; border-bottom -->
      <svg class="ranked-thumb" viewBox="0 0 38 38" fill="none" width="38" height="38">
        <!-- Color-block shape: rect bg + accent shape -->
        <rect width="38" height="38" rx="6" fill="var(--accent-light)"/>
        <rect x="10" y="10" width="18" height="18" rx="4" fill="var(--accent)"/>
      </svg>
      <div class="ranked-info">
        <div class="ranked-name">{Item name}</div>
        <div class="ranked-sub">{sub-label}</div>
      </div>
      <div class="bar-wrap">  <!-- flex:1; max-width:80px -->
        <div class="bar-bg"><div class="bar-fill" style="width:{pct}%"></div></div>
      </div>
      <div class="ranked-metric">{metric figure}</div>
    </div>
    <!-- 4 more rows, vary thumb shape/color -->
  </div>

</div>
```

---

## Full-width records table

```html
<div class="records-card">
  <div class="records-header">
    <div class="card-title">{Records title}</div>
    <a class="view-all" href="#">View all {entities} →</a>
  </div>
  <table>
    <thead>
      <tr>
        <th>{ID}</th><th>{Primary entity}</th><th>{Dimension}</th>
        <th>{Date}</th><th style="text-align:right">{Metric}</th><th>Status</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><span class="rec-id">{#ID}</span></td>
        <td>
          <div class="rec-entity">
            <div class="rec-avatar" style="background:var(--accent-light);color:var(--accent-dark)">{AB}</div>
            <div>{Name}</div>
          </div>
        </td>
        <td style="color:var(--text-secondary)">{dimension value}</td>
        <td style="color:var(--text-secondary)">{date}</td>
        <td class="rec-metric" style="text-align:right">{figure}</td>
        <td><span class="badge active">{State}</span></td>
        <!-- badge variants: .active .pending .inactive .danger -->
      </tr>
    </tbody>
  </table>
</div>
```

---

## List screen toolbar (search + filter chips)

```html
<div class="toolbar">  <!-- display:flex; align-items:center; gap:12px; flex-wrap:wrap -->
  <div class="toolbar-search">
    <svg><!-- magnifier --></svg>
    <input type="text" placeholder="Filter by {fields}…" readonly/>
  </div>
  <div class="filter-group">
    <span class="filter-label">{Facet}</span>
    <span class="chip active">All <span class="chip-count">{n}</span></span>
    <span class="chip">{Value A} <span class="chip-count">{n}</span></span>
    <span class="chip">{Value B} <span class="chip-count">{n}</span></span>
  </div>
  <span class="result-count">{n} records</span>
</div>
```

---

## Record form — sectioned cards with inline validation

Rules live ON the field: a required mark (`*`), helper text under the field, and an
inline error on an invalid field. The submit stays `disabled` until the form is valid.
Never add a separate rules/validation-status summary panel.

```html
<form class="form-wrap" novalidate>

  <div class="form-card">
    <div class="form-card-title"><svg><!-- section icon --></svg>{Section label}</div>
    <div class="form-card-body">
      <div class="field-grid">  <!-- 1fr 1fr; .field.full spans both -->

        <!-- valid field -->
        <div class="field">
          <label class="field-label" for="f1">{Label} <span class="req">*</span></label>
          <input id="f1" class="control" type="text" value=""/>
          <span class="helper">{format hint or constraint}</span>
        </div>

        <!-- invalid field: add .invalid on .field, render .error-msg -->
        <div class="field invalid">
          <label class="field-label" for="f2">{Label} <span class="req">*</span></label>
          <input id="f2" class="control" type="text" aria-invalid="true"/>
          <span class="error-msg"><svg><!-- alert icon --></svg>{Specific rule that failed}</span>
        </div>

        <!-- required select -->
        <div class="field">
          <label class="field-label" for="f3">{Label} <span class="req">*</span></label>
          <select id="f3" class="control"><option value="">Select…</option></select>
          <span class="helper">{constraint on the options}</span>
        </div>

        <!-- optional textarea, full-width -->
        <div class="field full">
          <label class="field-label" for="f4">{Label}</label>
          <textarea id="f4" class="control" placeholder="{hint}"></textarea>
          <span class="helper">{visibility note}</span>
        </div>

      </div>
    </div>
  </div>

  <div class="form-footer">
    <span class="form-hint">Fields marked <span class="req">*</span> are required.</span>
    <div class="footer-actions">
      <button type="button" class="btn-ghost">Cancel</button>
      <button type="submit" class="btn-primary" disabled>{Submit label}</button>
    </div>
  </div>

</form>
```

---

## Record detail — header band + meta grid + related panels

```html
<div class="detail-wrap">

  <!-- Header band: card with ID + status badge + action buttons -->
  <div class="detail-header">
    <div class="detail-id-block">
      <div class="detail-id-row">
        <span class="detail-id">{#ID}</span>
        <span class="badge active">{State}</span>
      </div>
      <div class="detail-name">{Record name / title}</div>
      <div class="detail-sub">{dimension · context}</div>
    </div>
    <div class="detail-actions">
      <button class="btn-ghost">{Secondary action}</button>
      <button class="btn-primary">Edit</button>
    </div>
  </div>

  <!-- Meta grid: card with 3-column label/value cells -->
  <div class="meta-card">
    <div class="card-title">{Section title}</div>
    <div class="meta-grid">  <!-- repeat(3,1fr); gap:16px 24px -->
      <div class="meta-cell">
        <div class="meta-label">{FIELD}</div>
        <div class="meta-value">{value}</div>
        <div class="meta-sub">{sub-line}</div>
      </div>
      <!-- more cells -->
    </div>
  </div>

  <!-- Two-column lower section: related data + activity feed -->
  <div class="lower-grid">
    <div class="sub-card">
      <!-- sub-card-header + table of related rows -->
    </div>
    <div class="sub-card">
      <!-- activity-list: dot + body (desc + time) per event -->
    </div>
  </div>

</div>
```

---

## Pager footer

```html
<div class="list-footer">
  <span>Showing {a}–{b} of {n}</span>
  <div class="pagination">
    <button class="page-btn">‹</button>
    <button class="page-btn active">1</button>
    <button class="page-btn">2</button>
    <button class="page-btn">3</button>
    <button class="page-btn">›</button>
  </div>
</div>
```
