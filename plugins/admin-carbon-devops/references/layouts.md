# Carbon Admin — layout skeletons

Paste-ready, domain-neutral fragments for the Carbon dark/terminal skin. Each
skeleton is labelled by archetype slot, not by a domain noun. Copy the shell
from `assets/template.html` first (it carries `:root` tokens + navbar + icon
rail + main slot), then drop the region skeletons below into `<main class="main">`.
Replace every `{placeholder}` with the real domain's equivalent.

Token recap (full block in `template.html`): canvas `#0b0d10`, panel `#14171c`,
inset `#1c2128`, hairline `#262c34`; text `#e6edf3 / #8b949e / #6e7681`;
accent green `var(--accent)` = `#22c55e`; blue secondary `var(--blue)` = `#3b82f6`;
state tokens `--state-pass/fail/run/skip` with `*-dim` tints.
Monospace face: `ui-monospace,"SF Mono",Menlo,"Cascadia Code",monospace` on IDs,
hashes, codes, branch names. `font-variant-numeric: tabular-nums` on every
numeric cell.

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

## KPI tile row (4 tiles in .kpi-grid)

```html
<div class="kpi-grid">  <!-- display:grid; grid-template-columns:repeat(4,1fr); gap:12px -->
  <div class="kpi-tile">
    <div class="kpi-label">{UPPERCASE METRIC NAME}</div>
    <div class="kpi-value">{figure}</div>  <!-- add .green / .amber / .red to recolor -->
    <span class="kpi-delta up">▲ {delta context}</span>  <!-- .up or .down -->
    <!-- optional inline SVG sparkline in top-right corner: -->
    <svg class="kpi-sparkline" width="56" height="24" viewBox="0 0 56 24">
      <polyline points="..." fill="none" stroke="var(--accent)" stroke-width="1.5" opacity=".8"/>
    </svg>
  </div>
  <!-- 3 more tiles -->
</div>
```

---

## Pipeline / status board (full-width card)

Rows of `[name chip] [code chip] [author] [branch] [timestamp] [stage chips] [duration]`

```html
<div class="card">
  <div class="card-header">
    <div class="card-title">
      <svg><!-- glyph --></svg>{Board title}
      <span class="card-count">{N active}</span>
    </div>
    <a href="#" class="view-all">View all →</a>
  </div>
  <div class="pipeline-list">
    <div class="pipeline-row">  <!-- see template.html for full grid CSS -->
      <span class="pname mono">{entity-name/workflow}</span>
      <span class="sha-chip">{#ID code}</span>
      <span style="color:#8b949e">{actor}</span>
      <span class="branch-chip mono">{ref/branch}</span>
      <span class="ts">{elapsed}</span>
      <div class="stages">
        <span class="stage-chip pass">{Step 1}</span>
        <span class="stage-chip pass">{Step 2}</span>
        <span class="stage-chip run"><span class="run-dot"></span>{Step 3}</span>
        <!-- .pass / .fail / .run / .skip -->
      </div>
      <span class="dur mono">{duration}</span>
    </div>
    <!-- more rows -->
  </div>
</div>
```

Stage chip classes: `.pass` (green outline), `.fail` (red outline),
`.run` (amber outline + `.run-dot` pulse), `.skip` (muted).

---

## Two-column grid (chart left 2/3 + side panel right 1/3)

```html
<div style="display:grid;grid-template-columns:2fr 1fr;gap:14px;align-items:start;">

  <!-- Chart card -->
  <div class="card">
    <div class="card-header">
      <div class="card-title"><svg></svg>{Chart title}</div>
      <span style="font-size:11px;color:#8b949e">{period}</span>
    </div>
    <div style="padding:16px">
      <svg width="100%" height="140" viewBox="0 0 420 140" preserveAspectRatio="none">
        <!-- horizontal gridlines -->
        <line x1="0" y1="20"  x2="420" y2="20"  stroke="#262c34" stroke-width="1"/>
        <line x1="0" y1="60"  x2="420" y2="60"  stroke="#262c34" stroke-width="1"/>
        <line x1="0" y1="100" x2="420" y2="100" stroke="#262c34" stroke-width="1"/>
        <!-- bars: positive (green), negative/fail (red) -->
        <rect x="..." y="..." width="18" height="..." rx="3" fill="var(--state-pass)" opacity=".75"/>
        <rect x="..." y="..." width="18" height="..." rx="3" fill="var(--state-fail)" opacity=".75"/>
        <!-- x-axis labels -->
        <text x="..." y="130" fill="#8b949e" font-size="10" font-family="-apple-system,sans-serif" text-anchor="middle">{label}</text>
      </svg>
      <!-- legend -->
      <div style="display:flex;gap:14px;margin-top:6px;font-size:11px;color:#8b949e;">
        <span style="display:flex;align-items:center;gap:5px;"><span style="width:10px;height:10px;background:var(--state-pass);border-radius:2px;opacity:.75"></span>{Pass label}</span>
        <span style="display:flex;align-items:center;gap:5px;"><span style="width:10px;height:10px;background:var(--state-fail);border-radius:2px;opacity:.75"></span>{Fail label}</span>
      </div>
    </div>
  </div>

  <!-- Severity feed / side panel -->
  <div class="card">
    <div class="card-header">
      <div class="card-title"><svg></svg>{Panel title}</div>
      <span class="card-count">{N}</span>
    </div>
    <div class="sev-list">  <!-- flex column -->
      <div class="sev-row">  <!-- flex, gap:10px -->
        <div class="sev-dot p1"></div>  <!-- .p1 / .p2 / .p3 -->
        <div class="sev-body">
          <span class="sev-tag mono">{TAG}</span>
          <div class="sev-desc">{one-line event description}</div>
          <div class="sev-time">{elapsed}</div>
        </div>
      </div>
      <!-- more rows -->
    </div>
  </div>

</div>
```

---

## Records table (dashboard footer or list screen)

```html
<div class="card">
  <div class="card-header">
    <div class="card-title"><svg></svg>{Table title}</div>
    <div class="filter-tabs">
      <span class="ftab active">All</span>
      <span class="ftab">{State A}</span>
      <span class="ftab">{State B}</span>
    </div>
  </div>
  <div class="rec-table-wrap">
    <table class="rec-table">
      <thead>
        <tr>
          <th>{ID}</th><th>{Code/Branch}</th><th>{Hash/Ref}</th>
          <th>{Actor}</th><th>Status</th><th>Duration</th><th></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="id-cell">#{id}</span></td>
          <td><span class="code-cell">{code}</span></td>
          <td><span class="sha-cell">{hash}</span></td>
          <td style="color:#8b949e">{actor}</td>
          <td><span class="status-pill pass"><span class="sdot"></span>Passed</span></td>
          <td class="num-cell" style="color:#8b949e">{d}m {s}s</td>
          <td><a href="#" style="color:var(--blue);font-size:11px;text-decoration:none">View</a></td>
        </tr>
        <!-- status-pill variants: .pass .fail .run .skip -->
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
<div class="toolbar">  <!-- display:flex; gap:12px; flex-wrap:wrap -->
  <div class="toolbar-search">
    <svg><!-- magnifier --></svg>
    <input type="text" placeholder="Search by {fields}…">
  </div>
  <div class="filter-group">
    <span class="filter-label">{Facet}</span>
    <span class="chip active">All <span class="chip-count">{n}</span></span>
    <span class="chip">{Value A} <span class="chip-count">{n}</span></span>
    <span class="chip">{Value B} <span class="chip-count">{n}</span></span>
  </div>
</div>
```

---

## Record form — fields with inline validation

Rules live ON the field: required mark (`*`), helper text beneath the field, and
an inline error message on an invalid field. The submit stays `disabled` until
the form is valid. Never add a separate rules / validation-status summary panel.

```html
<form class="form-wrap" novalidate>  <!-- max-width:720px; flex-column; gap:16px -->

  <div class="card">
    <div class="card-section-title"><svg></svg>{Section}</div>
    <div class="card-body">
      <div class="field-grid">  <!-- 1fr 1fr; .field.full spans both -->

        <!-- Valid field -->
        <div class="field">
          <label class="field-label" for="f1">{Label} <span class="req">*</span></label>
          <input id="f1" class="control" type="text" value="{value}">
          <span class="helper">{Format hint or constraint}</span>
        </div>

        <!-- Invalid field: add .invalid on .field -->
        <div class="field invalid">
          <label class="field-label" for="f2">{Label} <span class="req">*</span></label>
          <input id="f2" class="control" type="text" aria-invalid="true" value="">
          <span class="error-msg">
            <svg width="12" height="12" fill="none" viewBox="0 0 12 12"><circle cx="6" cy="6" r="5" stroke="currentColor" stroke-width="1.3"/><path d="M6 4v3M6 8.5v.5" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"/></svg>
            {Specific rule that failed — e.g. "Value must be greater than 0"}
          </span>
        </div>

        <!-- Required select -->
        <div class="field">
          <label class="field-label" for="f3">{Label} <span class="req">*</span></label>
          <select id="f3" class="control"><option value="">Select…</option></select>
          <span class="helper">{Constraint on the options}</span>
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

## Record detail — header + meta grid + related panels

```html
<div>
  <div class="breadcrumb"><a href="#">{Parent list}</a> › <span>{ID}</span></div>

  <div class="detail-header">
    <div class="detail-title-block">
      <div class="detail-id-row">
        <span class="detail-id mono">#{ID}</span>
        <span class="status-pill pass"><span class="sdot"></span>{State}</span>
      </div>
      <span style="font-size:13px;color:#8b949e">{entity · ref · code}</span>
    </div>
    <div class="detail-actions">
      <button class="btn-ghost">{Action}</button>
      <button class="btn-primary">Edit</button>
    </div>
  </div>

  <!-- Meta grid: 3 columns of label/value pairs -->
  <div class="card">
    <div class="meta-grid">  <!-- display:grid; grid-template-columns:repeat(3,1fr); padding:16px; gap:14px -->
      <div class="meta-cell">
        <div class="meta-label">{FIELD}</div>
        <div class="meta-value">{value}</div>
        <div class="meta-sub">{sub-context}</div>
      </div>
      <!-- more cells -->
    </div>
  </div>

  <!-- Two-col related data: stage steps / mini-table left + activity / log feed right -->
  <div style="display:grid;grid-template-columns:7fr 5fr;gap:14px;">
    <div class="card"><!-- steps table --></div>
    <div class="card"><!-- activity / log feed --></div>
  </div>
</div>
```
