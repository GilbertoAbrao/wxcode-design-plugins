# Midnight Ops — layout skeletons

Paste-ready, domain-neutral fragments for the Midnight Ops navy/teal skin. Each
skeleton is labelled by archetype slot, not by a domain noun. Copy the shell from
`assets/template.html` first (it carries the `:root` tokens + navbar + left rail +
main slot), then drop the region skeletons below into `<main class="main">`.
Replace every placeholder label with the real domain's equivalent.

Token recap (full block in `template.html`): canvas `#0b1120`, panel `#111827`,
inset `#1e293b`, hairline `#1f2937`; text `#e2e8f0 / #94a3b8 / #64748b`;
accent teal `#14b8a6` / cyan `#22d3ee`; state tokens `--green`, `--amber`, `--red`,
`--blue`, each with `-light`, `-bg`, `-glow`, `-border` variants. Put
`font-variant-numeric: tabular-nums` on every numeric cell.

---

## Page header (every screen)

```html
<div class="page-header">
  <div>
    <div class="page-title">{Screen title}</div>
    <div class="page-sub">{Context · environment · timestamp}</div>
  </div>
  <div class="header-actions">
    <!-- optional live dot -->
    <div class="live-dot" aria-hidden="true"></div>
    <span style="font-size:11px;color:var(--text-muted)">Live</span>
    <button class="btn-outline">{Secondary}</button>
    <button class="btn-accent">{+ Primary action}</button>
  </div>
</div>
```

---

## Metric tile row (×4, equal grid)

```html
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:12px;">
  <div class="metric-tile">
    <div class="tile-header">
      <span class="tile-label">{METRIC NAME}</span>
      <div class="tile-icon"><!-- 13×13 inline SVG; color:var(--accent-teal) --></div>
    </div>
    <!-- figure recolors: default var(--text-primary); alert: var(--red); success: var(--accent-cyan) -->
    <div class="tile-value" style="font-size:26px;font-weight:700;letter-spacing:-.02em;font-variant-numeric:tabular-nums">{value} <span style="font-size:13px;font-weight:400;color:var(--text-muted)">{unit}</span></div>
    <div class="tile-footer">
      <!-- .delta-up → var(--green);  .delta-down → var(--red) -->
      <div class="tile-delta delta-up">▲ {delta}%</div>
      <!-- 72×24 inline SVG sparkline (path + gradient fill, no axes) -->
      <svg class="sparkline" width="72" height="24" viewBox="0 0 72 24">
        <defs><linearGradient id="sg-{n}" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="var(--accent-teal)" stop-opacity=".3"/><stop offset="100%" stop-color="var(--accent-teal)" stop-opacity="0"/></linearGradient></defs>
        <path d="M0 20 ...path data... L72 24 L0 24Z" fill="url(#sg-{n})"/>
        <path d="M0 20 ...path data..." fill="none" stroke="var(--accent-teal)" stroke-width="1.5" stroke-linecap="round"/>
      </svg>
      <span style="font-size:10px;color:var(--text-dim)">{period}</span>
    </div>
  </div>
  <!-- 3 more tiles -->
</div>
```

Add these CSS classes to `<style>`:

```css
.metric-tile { background:var(--surface-1); border:1px solid var(--border); border-radius:var(--radius-md); padding:14px 16px 12px; display:flex; flex-direction:column; gap:8px; box-shadow:var(--shadow-card); transition:border-color .15s; }
.metric-tile:hover { border-color:var(--border-hi); }
.tile-header { display:flex; align-items:center; justify-content:space-between; }
.tile-label { font-size:11px; font-weight:500; color:var(--text-muted); text-transform:uppercase; letter-spacing:.05em; }
.tile-icon { width:26px; height:26px; border-radius:var(--radius-sm); background:var(--surface-2); border:1px solid var(--border); display:flex; align-items:center; justify-content:center; color:var(--accent-teal); }
.tile-footer { display:flex; align-items:center; justify-content:space-between; }
.tile-delta { display:flex; align-items:center; gap:3px; font-size:11px; font-weight:600; }
.delta-up { color:var(--green); }
.delta-down { color:var(--red); }
```

---

## Two-column content row (chart + status-list)

```html
<div style="display:grid;grid-template-columns:1fr 280px;gap:16px;">

  <!-- LEFT: time-series chart panel -->
  <div class="chart-panel">
    <div class="panel-header">
      <div>
        <div class="panel-title">{Metric} Trend — Last {window}</div>
        <div class="panel-sub">{bucket size} · {scope}</div>
      </div>
      <!-- legend chips: colored dot + label -->
    </div>
    <!-- chart-container: chart-yaxis absolute left + chart-svg-wrap margin-left:40px + chart-xaxis -->
  </div>

  <!-- RIGHT: status-list panel -->
  <div class="health-panel">
    <div class="panel-header">
      <div class="panel-title">{Entity} Status</div>
      <div class="panel-sub">{N} entities · {context}</div>
    </div>
    <!-- health-list: rows of [glow-dot] [name] [badge] -->
  </div>

</div>
```

### Status-list row

```html
<div class="health-row">
  <div class="status-dot dot-healthy"></div>   <!-- .dot-healthy / .dot-degraded / .dot-down -->
  <div class="health-name">{entity-name}</div>
  <span class="health-badge badge-healthy">OK</span>   <!-- .badge-healthy / .badge-degraded / .badge-down -->
</div>
```

```css
.health-panel { background:var(--surface-1); border:1px solid var(--border); border-radius:var(--radius-md); padding:14px 16px; box-shadow:var(--shadow-card); }
.health-list { display:flex; flex-direction:column; gap:1px; margin-top:12px; }
.health-row { display:flex; align-items:center; gap:10px; padding:7px 6px; border-radius:var(--radius-sm); transition:background .1s; }
.health-row:hover { background:var(--surface-2); }
.status-dot { width:8px; height:8px; border-radius:50%; flex-shrink:0; }
.dot-healthy  { background:var(--green); box-shadow:0 0 5px var(--green-glow); }
.dot-degraded { background:var(--amber); box-shadow:0 0 5px var(--amber-glow); }
.dot-down     { background:var(--red);   box-shadow:0 0 5px var(--red-glow); }
.health-name  { font-size:12px; font-weight:500; flex:1; }
.health-badge { font-size:10px; font-weight:600; padding:1px 6px; border-radius:20px; flex-shrink:0; }
.badge-healthy  { background:var(--green-bg); color:var(--green-light); }
.badge-degraded { background:var(--amber-bg); color:var(--amber-light); }
.badge-down     { background:var(--red-bg);   color:var(--red-light); }
```

---

## Full-width records table

```html
<div class="table-panel">
  <div class="panel-header">
    <div class="panel-title">{Records} — {scope}</div>
    <div class="panel-sub">{N} open · sorted by severity</div>
  </div>
  <table class="records-table">
    <thead>
      <tr>
        <th>Severity</th><th>ID</th><th>Title</th>
        <th>{Dimension}</th><th>Duration</th><th>Assignee</th><th>Status</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><span class="sev-pill sev-p1">P1</span></td>
        <td><span class="rec-id">#REC-{n}</span></td>
        <td style="max-width:260px;overflow:hidden;text-overflow:ellipsis">{title}</td>
        <td>{dimension}</td>
        <td style="color:var(--text-muted);font-size:11px">{duration}</td>
        <td>
          <div style="display:flex;align-items:center;gap:6px;">
            <div style="width:20px;height:20px;border-radius:50%;font-size:9px;font-weight:700;display:flex;align-items:center;justify-content:center;color:#0b1120;background:linear-gradient(135deg,var(--accent-teal),var(--accent-cyan))">{XX}</div>
            {Name}
          </div>
        </td>
        <td><span class="state-pill state-active">Investigating</span></td>
        <!-- state variants: .state-active .state-monitoring .state-resolved .state-queued -->
      </tr>
    </tbody>
  </table>
</div>
```

```css
.table-panel { background:var(--surface-1); border:1px solid var(--border); border-radius:var(--radius-md); box-shadow:var(--shadow-card); overflow:hidden; }
.records-table { width:100%; border-collapse:collapse; }
.records-table th { font-size:10px; font-weight:600; color:var(--text-dim); text-transform:uppercase; letter-spacing:.06em; padding:8px 18px; text-align:left; border-bottom:1px solid var(--border); white-space:nowrap; }
.records-table td { padding:10px 18px; font-size:12px; border-bottom:1px solid var(--border); vertical-align:middle; white-space:nowrap; font-variant-numeric:tabular-nums; }
.records-table tr:last-child td { border-bottom:none; }
.records-table tbody tr:hover td { background:var(--surface-2); }
.sev-pill { display:inline-flex; align-items:center; padding:2px 8px; border-radius:20px; font-size:10px; font-weight:700; letter-spacing:.04em; }
.sev-p1 { background:var(--red-bg);   color:var(--red-light);   border:1px solid var(--red-border); }
.sev-p2 { background:var(--amber-bg); color:var(--amber-light); border:1px solid var(--amber-border); }
.sev-p3 { background:var(--blue-bg);  color:var(--blue-light);  border:1px solid var(--blue-border); }
.state-pill { display:inline-block; padding:2px 8px; border-radius:20px; font-size:10px; font-weight:600; }
.state-active     { background:var(--red-bg);    color:var(--red-light); }
.state-monitoring { background:var(--amber-bg);  color:var(--amber-light); }
.state-resolved   { background:var(--green-bg);  color:var(--green-light); }
.state-queued     { background:var(--surface-2); color:var(--text-muted); border:1px solid var(--border); }
.rec-id { font-family:"SF Mono","Fira Code",monospace; font-size:11px; color:var(--text-muted); }
```

### List toolbar (search + filter chips)

```html
<div class="toolbar" style="display:flex;align-items:center;gap:12px;flex-wrap:wrap;">
  <div style="position:relative;flex:1;max-width:360px;">
    <!-- magnifier SVG -->
    <input type="text" placeholder="Filter by {fields}…" style="width:100%;height:32px;background:var(--surface-1);border:1px solid var(--border);border-radius:var(--radius-sm);color:var(--text-primary);font-family:var(--font);font-size:12px;padding:0 10px 0 30px;outline:none;">
  </div>
  <div style="display:flex;align-items:center;gap:6px;">
    <span style="font-size:11px;color:var(--text-dim)">{Facet}:</span>
    <button class="chip active" aria-pressed="true">All <span class="chip-count">{n}</span></button>
    <button class="chip" aria-pressed="false">{Value} <span class="chip-count">{n}</span></button>
  </div>
</div>
```

```css
.chip { height:24px; padding:0 10px; border-radius:20px; font-size:11px; font-weight:500; cursor:pointer; border:1px solid var(--border); background:transparent; color:var(--text-muted); display:inline-flex; align-items:center; gap:4px; transition:border-color .12s,color .12s,background .12s; }
.chip:hover { border-color:var(--border-hi); color:var(--text-primary); }
.chip.active { background:var(--accent-glow); border-color:var(--accent-teal); color:var(--accent-teal); }
.chip-count { font-size:10px; opacity:.7; }
```

### Table footer (result count + pagination)

```html
<div style="display:flex;align-items:center;justify-content:space-between;padding:10px 18px;border-top:1px solid var(--border);">
  <span style="font-size:11px;color:var(--text-muted)">Showing {a}–{b} of {n}</span>
  <div style="display:flex;gap:4px;">
    <button class="page-btn" aria-label="Previous">‹</button>
    <button class="page-btn active" aria-current="page">1</button>
    <button class="page-btn">2</button>
    <button class="page-btn">3</button>
    <button class="page-btn" aria-label="Next">›</button>
  </div>
</div>
```

```css
.page-btn { width:28px; height:28px; border-radius:var(--radius-sm); border:1px solid var(--border); background:transparent; color:var(--text-muted); font-family:var(--font); font-size:11px; cursor:pointer; display:flex; align-items:center; justify-content:center; transition:background .12s,color .12s,border-color .12s; }
.page-btn:hover { background:var(--surface-2); color:var(--text-primary); }
.page-btn.active { background:var(--accent-teal); border-color:var(--accent-teal); color:#0b1120; font-weight:600; }
```

---

## Record form — fields with inline validation

Rules live ON the field: a required mark (`*`), helper text under the field, and
an inline error message on an invalid field. The submit stays `disabled` until
the form is valid. Never add a separate rules/validation-status summary panel.

```html
<form novalidate>
  <div class="form-section">
    <div class="section-header">
      <div class="section-title"><!-- SVG icon -->{Section}</div>
    </div>
    <div class="section-body">
      <div class="field-grid">

        <!-- valid field -->
        <div class="field">
          <label class="field-label" for="f1">{Label} <span class="req">*</span></label>
          <input id="f1" class="control" type="text" placeholder="{hint}">
          <span class="helper">{what the value drives / format hint}</span>
        </div>

        <!-- invalid field: add .invalid on .field, render .error-msg -->
        <div class="field invalid">
          <label class="field-label" for="f2">{Label} <span class="req">*</span></label>
          <select id="f2" class="control" aria-invalid="true">
            <option value="">Select…</option>
          </select>
          <span class="error-msg">
            <!-- small alert SVG -->
            {Specific rule that failed}
          </span>
        </div>

        <!-- full-width textarea -->
        <div class="field full">
          <label class="field-label" for="f3">{Label} <span class="req">*</span></label>
          <textarea id="f3" class="control" style="height:80px;resize:vertical;padding:8px 10px"></textarea>
          <span class="helper">{constraint / format hint}</span>
        </div>

      </div>
    </div>
  </div>

  <div class="form-footer">
    <span class="form-hint">Fields marked <span class="req">*</span> are required</span>
    <div class="footer-actions">
      <button type="button" class="btn-ghost">Cancel</button>
      <button type="submit" class="btn-submit" disabled>{Submit}</button>
    </div>
  </div>
</form>
```

```css
.form-section { background:var(--surface-1); border:1px solid var(--border); border-radius:var(--radius-md); box-shadow:var(--shadow-card); }
.section-header { padding:14px 18px 12px; border-bottom:1px solid var(--border); }
.section-title { font-size:12px; font-weight:600; display:flex; align-items:center; gap:7px; }
.section-title svg { color:var(--accent-teal); }
.section-body { padding:18px; }
.field-grid { display:grid; grid-template-columns:1fr 1fr; gap:14px 20px; }
.field { display:flex; flex-direction:column; gap:5px; }
.field.full { grid-column:1/-1; }
.field-label { font-size:11px; font-weight:500; color:var(--text-muted); }
.req { color:var(--accent-teal); margin-left:2px; }
.control { height:34px; background:var(--surface-2); border:1px solid var(--border); border-radius:var(--radius-sm); color:var(--text-primary); font-family:var(--font); font-size:12px; padding:0 10px; outline:none; transition:border-color .15s; width:100%; }
.control:focus { border-color:var(--accent-teal); }
.control::placeholder { color:var(--text-dim); }
.helper { font-size:11px; color:var(--text-dim); line-height:1.4; }
.field.invalid .control { border-color:var(--red); }
.error-msg { font-size:11px; color:var(--red-light); display:flex; align-items:center; gap:4px; }
.form-footer { display:flex; align-items:center; justify-content:space-between; padding:14px 0 0; }
.form-hint { font-size:11px; color:var(--text-muted); }
.footer-actions { display:flex; gap:8px; }
.btn-ghost { height:32px; padding:0 16px; border:1px solid var(--border-hi); border-radius:var(--radius-sm); background:transparent; color:var(--text-muted); font-family:var(--font); font-size:12px; font-weight:500; cursor:pointer; transition:border-color .12s,color .12s; }
.btn-submit { height:32px; padding:0 18px; border:none; border-radius:var(--radius-sm); background:var(--accent-teal); color:#0b1120; font-family:var(--font); font-size:12px; font-weight:600; cursor:pointer; box-shadow:var(--shadow-glow); transition:background .12s; }
.btn-submit:disabled { background:var(--surface-2); color:var(--text-dim); box-shadow:none; cursor:not-allowed; }
```

---

## Record detail — header + meta grid + related panels

```html
<nav class="breadcrumb" style="font-size:11px;color:var(--text-muted);display:flex;align-items:center;gap:6px;">
  <a href="#" style="color:var(--accent-teal)">{Parent list}</a>
  <span>›</span><span>{ID}</span>
</nav>

<!-- detail header -->
<div style="display:flex;align-items:flex-start;justify-content:space-between;gap:16px;">
  <div>
    <div style="display:flex;align-items:center;gap:10px;">
      <span class="rec-id">{#ID}</span>
      <span class="sev-pill sev-p1">P1</span>
      <span class="state-pill state-active">Investigating</span>
    </div>
    <div style="font-size:15px;font-weight:600;margin-top:4px">{Title}</div>
  </div>
  <div style="display:flex;gap:8px;flex-shrink:0;">
    <button class="btn-ghost">{Action}</button>
    <button class="btn-accent">Edit</button>
  </div>
</div>

<!-- meta card: 3-col label/value grid -->
<div class="card">
  <div style="display:grid;grid-template-columns:repeat(3,1fr);">
    <div style="padding:14px 18px;border-right:1px solid var(--border);border-bottom:1px solid var(--border);">
      <div style="font-size:10px;font-weight:500;color:var(--text-dim);text-transform:uppercase;letter-spacing:.05em;margin-bottom:4px">{FIELD}</div>
      <div style="font-size:13px;font-weight:500;font-variant-numeric:tabular-nums">{value}</div>
      <div style="font-size:11px;color:var(--text-muted);margin-top:2px">{sub}</div>
    </div>
    <!-- repeat ×6; last row cells: border-bottom:none; col 3n: border-right:none -->
  </div>
</div>

<!-- two-col: related sub-panel + activity feed -->
<div style="display:grid;grid-template-columns:1fr 280px;gap:16px;">
  <div class="card"><!-- status-list or mini-table --></div>
  <div class="card"><!-- activity timeline --></div>
</div>
```
