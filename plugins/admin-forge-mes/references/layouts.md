# Forge Admin — layout skeletons

Paste-ready, domain-neutral fragments for the Forge dark/industrial skin. Each
skeleton is labelled by archetype slot, not by a domain noun. Copy the shell from
`assets/template.html` first (it carries the `:root` tokens + navbar + icon rail +
main slot), then drop the region skeletons below into `<main class="main">`.
Replace every placeholder label with the real domain's equivalent.

Token recap (full block in `template.html`): canvas `#0c0f14`, panel `#141922`,
inset `#1d2530`, hairline `#2a3340`; text `#e6ebf2 / #c5cdd7 / #8b96a5 / #64748b`;
accent `var(--accent)` = `#f97316`; state tokens `--state-*` with `*-dim` tints.
Put `font-variant-numeric: tabular-nums` on every numeric cell.

---

## Page header (every screen)

```html
<div class="page-header">
  <div>
    <div class="page-title">{Screen title}</div>
    <div class="page-subtitle">{scope · context · timestamp}</div>
  </div>
  <div class="header-actions">
    <button class="btn-ghost">{Secondary}</button>
    <button class="btn-primary">+ {Primary action}</button>
  </div>
</div>
```

---

## KPI tile (repeat ×4 in a `.kpi-row` grid)

```html
<div class="kpi-row">  <!-- display:grid; grid-template-columns: repeat(4,1fr); gap:14px -->
  <div class="kpi-tile">
    <div class="kpi-top">
      <div class="kpi-icon"><!-- inline SVG glyph, stroke=var(--accent) --></div>
      <span class="kpi-delta up">▲ {delta}</span>   <!-- .up / .down / .warn -->
    </div>
    <div class="kpi-value orange">{figure}</div>      <!-- .orange / .amber / .red, or default white -->
    <div>
      <div class="kpi-label">{UPPERCASE METRIC NAME}</div>
      <div class="kpi-sub">{target / context line}</div>
    </div>
  </div>
  <!-- 3 more tiles -->
</div>
```

---

## Two-column grid (status board + side panel)

```html
<div class="main-grid">  <!-- grid-template-columns: 7fr 5fr; gap:14px; align-items:start -->
  <div style="display:flex;flex-direction:column;gap:14px;">
    <!-- status-board card (below) -->
    <!-- optional: trend-chart card -->
  </div>
  <div class="card" style="display:flex;flex-direction:column;">
    <!-- alerts / side panel (below) -->
  </div>
</div>
```

### Status-board row

`[label + sub] [state pill] [current / target metric over a progress bar] [count]`

```html
<div class="card">
  <div class="card-header">
    <div class="card-title">
      <svg><!-- glyph --></svg>{Board title}
      <span class="card-count">{N items}</span>
    </div>
    <a href="#" class="view-all">View all →</a>
  </div>
  <div class="lines-board">
    <div class="line-row">  <!-- grid: 110px 90px 1fr 80px 28px -->
      <div><div class="line-name">{Entity}</div><div class="line-name-sub">{sub}</div></div>
      <span class="state-pill running"><span class="state-pill-dot"></span>{State}</span>
      <div class="line-progress-wrap">
        <div class="line-progress-nums"><span class="cur">{current}</span><span class="tgt">/ {target}</span></div>
        <div class="progress-bar"><div class="progress-bar-fill" style="width:{pct}%"></div></div>
      </div>
      <div></div>
      <div class="ops-icon"><svg><!-- people glyph --></svg>{count}</div>
    </div>
    <!-- more rows; state-pill variants: .running .idle .down -->
  </div>
</div>
```

### Side panel row (severity feed)

`[severity dot] [tag chip] [description] [elapsed]`

```html
<div class="alerts-list">
  <div class="alert-row">
    <div class="sev-dot critical"></div>   <!-- .critical / .warn / .info -->
    <div class="alert-body">
      <span class="alert-tag">{tag}</span>
      <div class="alert-desc">{one-line event}</div>
      <div class="alert-time">{elapsed}</div>
    </div>
  </div>
  <!-- more rows -->
</div>
```

---

## Records table (dashboard footer or list screen)

```html
<div class="card">
  <div class="card-header">
    <div class="card-title"><svg></svg>{Records title}</div>
    <div style="display:flex;gap:8px;align-items:center;">
      <button class="btn-ghost">{Export}</button>
      <button class="btn-primary">+ {New}</button>
    </div>
  </div>
  <div class="rec-table-wrap">
    <table class="rec-table">
      <thead>
        <tr><th>{ID}</th><th>{Code}</th><th>{Description}</th>
            <th style="text-align:right">{Numeric}</th><th>{Dim}</th><th>{Date}</th><th>Status</th></tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="rec-id">{ID}</span></td>
          <td><div class="code-cell"><span class="code-id">{CODE}</span><span class="code-name">{name}</span></div></td>
          <td class="desc-cell">{description}</td>
          <td style="text-align:right" class="qty-cell">{numeric}</td>
          <td class="line-cell">{dim}</td>
          <td><span class="due-date">{date}</span></td>  <!-- add .overdue for past dates -->
          <td><span class="rec-status inprogress"><span class="rec-status-dot"></span>{State}</span></td>
        </tr>
        <!-- status variants: .inprogress .queued .completed .onhold -->
      </tbody>
    </table>
  </div>
  <div class="rec-footer">
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

### List toolbar (search + filter chips)

```html
<div class="toolbar">
  <div class="toolbar-search">
    <svg><!-- magnifier --></svg>
    <input type="text" placeholder="Filter by {fields}…">
  </div>
  <div class="filter-group">
    <span class="filter-label">{Facet}</span>
    <span class="chip active">All <span class="chip-count">{n}</span></span>
    <span class="chip">{Value} <span class="chip-count">{n}</span></span>
  </div>
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
    <div class="card-section-title"><svg></svg>{Section}</div>
    <div class="card-body">
      <div class="field-grid">  <!-- 1fr 1fr; .field.full spans both -->

        <!-- valid field -->
        <div class="field">
          <label class="field-label" for="f1">{Label} <span class="req">*</span></label>
          <input id="f1" class="control" type="text" value="">
          <span class="helper">{what the value drives / format hint}</span>
        </div>

        <!-- invalid field: add .invalid on .field, render .error-msg -->
        <div class="field invalid">
          <label class="field-label" for="f2">{Label} <span class="req">*</span></label>
          <input id="f2" class="control" type="text" aria-invalid="true">
          <span class="error-msg"><svg><!-- alert --></svg>{Specific rule that failed}</span>
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

  <div class="form-footer">
    <span class="form-hint">Fields marked <span class="req">*</span> are required.</span>
    <div class="footer-actions">
      <button type="button" class="btn-ghost">Cancel</button>
      <button type="submit" class="btn-primary" disabled>{Submit}</button>
    </div>
  </div>
</form>
```

---

## Record detail — header + meta grid + related panels

```html
<div class="detail-wrap">
  <div class="breadcrumb"><a href="#">{Parent}</a> › <span>{ID}</span></div>

  <div class="detail-header">
    <div class="detail-title-block">
      <div class="detail-id-row">
        <span class="detail-id">{ID}</span>
        <span class="rec-status inprogress"><span class="rec-status-dot"></span>{State}</span>
      </div>
      <span class="detail-name">{code · name}</span>
    </div>
    <div class="detail-actions">
      <button class="btn-ghost">{Action}</button>
      <button class="btn-primary">Edit</button>
    </div>
  </div>

  <!-- meta grid: 3-col label/value cells -->
  <div class="card">
    <div class="meta-grid">  <!-- repeat(3,1fr) -->
      <div class="meta-cell">
        <div class="meta-label">{FIELD}</div>
        <div class="meta-value">{value}</div>
        <div class="meta-sub">{sub}</div>
      </div>
      <!-- more cells -->
    </div>
  </div>

  <!-- related data: a status-board / operations list + an activity feed -->
  <div class="two-col">  <!-- 7fr 5fr -->
    <div class="card"><!-- routing/operations rows --></div>
    <div class="card"><!-- activity timeline --></div>
  </div>
</div>
```
