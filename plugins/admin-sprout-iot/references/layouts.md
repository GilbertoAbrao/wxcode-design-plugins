# Sprout Admin — layout skeletons

Paste-ready, domain-neutral fragments for the Sprout dark/technical-fresh skin.
Each skeleton is labelled by archetype slot, not by a domain noun. Copy the
shell from `assets/template.html` first (it carries the `:root` tokens + left
rail + topbar + main slot), then drop the region skeletons below into
`<main class="content">`. Replace every `{placeholder}` with the real domain's
equivalent.

Token recap (full block in `template.html`): canvas `#0c1118`, panel `#131b26`,
inset `#1a2533`, hairline `#223040`; text `#dfe7ef / #b0bdca / #8597a8`;
accent `var(--c-lime)` = `#84cc16` (healthy/online), `var(--c-cyan)` = `#22d3ee`
(data/telemetry); severity `var(--c-amber)` = `#f59e0b`, `var(--c-red)` = `#ef4444`.
Put `font-variant-numeric: tabular-nums` on every numeric cell.

---

## Page header (every screen)

```html
<div class="page-hdr">
  <div>
    <div class="page-title">{Screen title}</div>
    <div class="page-sub">{context · scope · last updated}</div>
  </div>
  <div style="display:flex;gap:8px">
    <button class="btn-ghost">{Secondary action}</button>
    <button class="btn-primary">+ {Primary action}</button>
  </div>
</div>
```

---

## KPI card row (repeat ×4 in a `.kpi-grid`)

```html
<div class="kpi-grid"> <!-- display:grid; grid-template-columns:repeat(4,1fr); gap:14px -->
  <div class="kpi-card"> <!-- bg:--c-bg-surface; border; border-radius:10px; padding:16px 18px -->
    <div class="kpi-label">{UPPERCASE METRIC LABEL}
      <!-- icon SVG in --c-muted, float right via space-between flex -->
    </div>
    <div class="kpi-row"> <!-- space-between flex -->
      <div class="kpi-value lime">{figure}</div>  <!-- .lime / .red / .cyan / .amber -->
      <svg><!-- tiny 8-pt sparkline: polyline + area-fill polygon in accent color --></svg>
    </div>
    <div class="kpi-delta up">{↑ delta label}</div>  <!-- .up / .down / .warn -->
  </div>
  <!-- 3 more cards -->
</div>
```

---

## Two-column panel row (multi-channel + severity feed)

```html
<div class="panel-row"> <!-- display:grid; grid-template-columns:1fr 380px; gap:14px -->

  <!-- LEFT: multi-channel panel -->
  <div class="channel-card"> <!-- surface card -->
    <div class="channel-hdr"> <!-- space-between flex -->
      <h3>{Panel title — last N min}</h3>
      <div class="channel-legend"> <!-- legend chips -->
        <span class="legend-chip"><span class="legend-dot cyan"></span>{Channel A}</span>
        <span class="legend-chip"><span class="legend-dot lime"></span>{Channel B}</span>
        <span class="legend-chip"><span class="legend-dot amber"></span>{Channel C}</span>
      </div>
    </div>
    <div class="channels"> <!-- flex-direction:column; gap:14px -->
      <div class="channel-row"> <!-- flex; align-items:center; gap:12px -->
        <div class="ch-label">{CHANNEL LABEL}</div>  <!-- 86px fixed width -->
        <svg class="ch-spark" height="36" viewBox="0 0 320 36" preserveAspectRatio="none" fill="none">
          <!-- polyline + area-fill polygon; stroke in accent color; opacity ~.08 fill -->
          <line x1="0" y1="36" x2="320" y2="36" stroke="var(--c-border)" stroke-width="1"/>
        </svg>
        <div class="ch-val cyan">{value + unit}</div>  <!-- .cyan / .lime / .amber -->
      </div>
      <!-- more channel rows -->
    </div>
    <div class="ch-timeaxis"> <!-- small muted tick labels; padded to align with sparkline -->
      <span>−30m</span><span>−20m</span><span>−10m</span><span>now</span>
    </div>
  </div>

  <!-- RIGHT: severity feed -->
  <div class="severity-card"> <!-- surface card -->
    <div class="card-hdr">
      <h3>{Feed title}</h3>
      <a href="#">View all →</a>
    </div>
    <div class="sev-row"> <!-- flex; align-items:flex-start; gap:10px; border-bottom -->
      <span class="sev-pill crit">CRIT</span>  <!-- .crit / .warn / .info -->
      <div class="sev-body">
        <div class="sev-name">{entity name}</div>
        <div class="sev-msg">{one-line event description}</div>
      </div>
      <div class="sev-age">{elapsed}</div>
    </div>
    <!-- more sev-rows -->
  </div>

</div>
```

---

## Records table (dashboard footer or list screen)

```html
<div class="rec-card"> <!-- surface card; padding:18px 0 0 -->
  <div class="rec-card-hdr"> <!-- space-between flex; padding:0 20px 14px -->
    <h3>{Records title}</h3>
    <div style="display:flex;align-items:center;gap:14px">
      <div class="filter-pills">
        <button class="filter-pill active">All ({n})</button>
        <button class="filter-pill">{Value}</button>
        <button class="filter-pill">{Value}</button>
      </div>
      <a href="#" style="font-size:12px;color:var(--c-cyan)">{Action} →</a>
    </div>
  </div>
  <table class="rec-table">
    <thead>
      <tr>
        <th>{Entity}</th><th>{Category}</th><th>{Version}</th>
        <th>{Signal}</th><th>{Timestamp}</th><th>Status</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>
          <div class="name-cell">
            <div class="dev-icon {alt|act}"><!-- category SVG icon --></div>
            <div>
              <div class="dev-name">{Record name}</div>
              <div class="dev-uid">{uid:xx:xx:xx:xx}</div>
            </div>
          </div>
        </td>
        <td style="color:var(--c-muted)">{Category}</td>
        <td><span class="ver-badge {stale?}">{vX.Y.Z}</span></td>
        <td>
          <div class="sig-bars">
            <div class="sig-bar on s4" style="height:4px"></div>
            <div class="sig-bar on s4" style="height:7px"></div>
            <div class="sig-bar on s4" style="height:10px"></div>
            <div class="sig-bar on s4" style="height:14px"></div>
            <!-- bars with .on.s1/.s2/.s3/.s4 for signal level; no .on for off -->
          </div>
        </td>
        <td class="ts-cell">{timestamp}</td>
        <td><span class="status-pill ok">{State}</span></td>
        <!-- status-pill variants: .ok / .err / .warn / .info -->
      </tr>
    </tbody>
  </table>
  <div class="rec-footer">
    <span>Showing {a}–{b} of {n}</span>
    <div class="pager">
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
<div class="toolbar"> <!-- flex; align-items:center; gap:12px; margin-bottom:14px -->
  <div class="toolbar-search"> <!-- surface border pill -->
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

Rules live ON the field: a required mark (`*`), helper text under the field,
and an inline error message on an invalid field. The submit stays `disabled`
until the form is valid. Never add a separate rules/validation-status panel.

```html
<form class="form-wrap" novalidate> <!-- max-width:760px -->

  <div class="card" style="margin-bottom:16px">
    <div class="card-section-title"> <!-- bordered bottom; uppercase micro-label -->
      <svg><!-- section icon --></svg>
      {Section name}
    </div>
    <div class="card-body" style="padding:18px">

      <div class="field-grid"> <!-- display:grid; grid-template-columns:1fr 1fr; gap:16px -->

        <!-- valid required field -->
        <div class="field">
          <label class="field-label" for="f1">{Label} <span class="req">*</span></label>
          <input id="f1" class="control" type="text" value="">
          <span class="helper">{format hint / what this drives}</span>
        </div>

        <!-- invalid field: add .invalid on .field, show .error-msg -->
        <div class="field invalid">
          <label class="field-label" for="f2">{Label} <span class="req">*</span></label>
          <input id="f2" class="control" type="text" aria-invalid="true">
          <span class="error-msg">
            <svg width="12" height="12" viewBox="0 0 12 12" fill="none">
              <path d="M6 1L11 10H1L6 1Z" stroke="currentColor" stroke-width="1.3" stroke-linejoin="round"/>
              <path d="M6 5V7" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"/>
              <circle cx="6" cy="8.5" r=".5" fill="currentColor"/>
            </svg>
            {Specific rule that failed}
          </span>
        </div>

        <!-- required select -->
        <div class="field">
          <label class="field-label" for="f3">{Label} <span class="req">*</span></label>
          <select id="f3" class="control">
            <option value="">Select…</option>
            <option>{Option}</option>
          </select>
          <span class="helper">{constraint on the options}</span>
        </div>

        <!-- full-width field: add .full -->
        <div class="field full">
          <label class="field-label" for="f4">{Label}</label>
          <textarea id="f4" class="control" rows="3" placeholder="{hint}…"></textarea>
        </div>

      </div><!-- /field-grid -->
    </div><!-- /card-body -->
  </div><!-- /card -->

  <div class="form-footer"> <!-- space-between flex -->
    <span class="form-hint">Fields marked <span class="req">*</span> are required.</span>
    <div class="footer-actions">
      <button type="button" class="btn-ghost">Cancel</button>
      <button type="submit" class="btn-primary" disabled>{Submit label}</button>
    </div>
  </div>

</form>
```

---

## Record detail — header + meta grid + related panels

```html
<div class="detail-wrap">
  <div class="breadcrumb"><a href="#">{Parent list}</a> › <span>{Record ID}</span></div>

  <div class="detail-header"> <!-- space-between flex -->
    <div>
      <div class="detail-id-row">
        <span class="detail-id">{uid:xx:xx:xx:xx}</span>
        <span class="status-pill warn">{State}</span>
      </div>
      <div class="detail-name">{Record name}</div>
      <div class="detail-sub">{Category · Group · Gateway}</div>
    </div>
    <div class="detail-actions">
      <button class="btn-ghost">{Secondary}</button>
      <button class="btn-primary">Edit</button>
    </div>
  </div>

  <!-- meta grid: 3-col label/value cells -->
  <div class="card" style="margin-bottom:16px">
    <div class="meta-grid"> <!-- display:grid; grid-template-columns:repeat(3,1fr) -->
      <div class="meta-cell"> <!-- border-right + border-bottom pattern -->
        <div class="meta-label">{FIELD}</div>
        <div class="meta-value">{value}</div>
        <div class="meta-sub">{sub}</div>
      </div>
      <!-- 5 more cells = 2 rows of 3 -->
    </div>
  </div>

  <!-- two-col: multi-channel sub-panel + activity feed -->
  <div class="two-col"> <!-- display:grid; grid-template-columns:7fr 5fr; gap:14px -->
    <div class="card">
      <!-- recent readings: channel-row pattern (label / sparkline / value) -->
    </div>
    <div class="card">
      <!-- event log / activity feed:
           each row: colored dot + event text + timestamp -->
    </div>
  </div>
</div>
```
