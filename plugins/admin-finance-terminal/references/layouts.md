# Terminal Admin — layout skeletons

Paste-ready, domain-neutral fragments for the black monospace terminal skin. Each
skeleton is labelled by archetype slot, not by a domain noun. Copy the shell from
`assets/template.html` first (it carries the `:root` tokens + status bar + ticker
strip + left rail + body slot + command-line footer), then drop the region
skeletons below into the appropriate panel. Replace every placeholder label with
the real domain's equivalent.

Token recap (full block in `template.html`): page `#0E0E0E`, panel `#1A1A1A`,
ticker `#111111`, borders `--grid: #2a2a2a`; text `#ffffff / #888888`; amber
`--amber: #FFB800`; green `--green: #00C851`. Monospace everywhere; sans only
for the F1 HELP hint string. All numbers right-aligned, `font-variant-numeric:
tabular-nums`. Zero border-radius on all elements.

---

## Status bar (every screen)

```html
<header class="statusbar">
  <span class="logo">{BRAND NAME}</span>
  <span class="sep">|</span>
  <span class="meta">{SESSION CONTEXT}</span>
  <span class="sep">|</span>
  <span class="chip live">LIVE</span>
  <span class="chip">{SID-XXXX-XXXX}</span>
  <span class="sep">|</span>
  <span class="latency">LAT {N}ms</span>
  <span class="sep">|</span>
  <span class="meta">USER: {USER.ID}</span>
  <div class="spacer"></div>
  <span class="hint">F1 HELP</span>
  <span class="sep">|</span>
  <span class="clock" id="clock">00:00:00</span>
</header>
```

---

## Ticker strip (every screen)

```html
<div class="ticker">
  <span class="ticker-label">{CATEGORY}</span>
  <div class="ticker-items">
    <div class="ticker-item">
      <span class="sym">{ENTITY-01}</span>
      <span class="price">{value}</span>
      <span class="delta up">+{delta}</span>  <!-- .up=green .dn=amber -->
    </div>
    <!-- repeat ticker-item for each live entity (6–8 recommended) -->
  </div>
</div>
```

---

## Left module rail

```html
<nav class="rail">
  <div class="rail-header">MODULES</div>
  <div class="rail-item">
    <span class="fkey">F1</span><span class="label">HELP</span><span class="dot"></span>
  </div>
  <div class="rail-item active">       <!-- .active = amber border + #1f1a00 bg -->
    <span class="fkey">F2</span><span class="label">{MODULE}</span><span class="dot"></span>
  </div>
  <div class="rail-item ok">           <!-- .ok = green dot -->
    <span class="fkey">F3</span><span class="label">{MODULE}</span><span class="dot"></span>
  </div>
  <!-- repeat F4–F8 for domain modules -->
  <div class="rail-footer">{v0.0.0 / PROD}</div>
</nav>
```

---

## Main data table (center top panel)

```html
<div class="panel">
  <div class="panel-header">
    <span class="panel-title">{ENTITY PLURAL}</span>
    <span class="panel-meta">AS OF {time}</span>
    <span class="panel-badge amber">{N} {QUALIFIER}</span>
  </div>
  <div class="tbl-wrap">
    <table>
      <thead>
        <tr>
          <th>{ID COL}</th>
          <th style="text-align:right">{COL B}</th>
          <th style="text-align:right">{COL C}</th>
          <th style="text-align:right">{NUMERIC COL}</th>
          <th style="text-align:right">STATUS</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td class="sym-cell">{ID}</td>
          <td style="text-align:right">{value}</td>
          <td style="text-align:right">{value}</td>
          <td style="text-align:right" class="pos">+{figure}</td>
          <!-- class="neg" for negative / amber — never red -->
          <td style="text-align:right">
            <span class="chip-status active">{STATE}</span>
            <!-- chip-status variants: .active (green) / .warn (amber) / .crit (#ff4444) -->
          </td>
        </tr>
        <!-- more rows; odd rows get rgba(255,255,255,0.018) automatically -->
      </tbody>
    </table>
  </div>
</div>
```

---

## Activity / event log (center bottom panel)

```html
<div class="panel" style="border-right:none;">
  <div class="panel-header">
    <span class="panel-title">EVENT LOG</span>
    <span class="panel-meta">{SCOPE}</span>
    <span class="panel-badge">{N} EVENTS</span>
  </div>
  <div class="tbl-wrap">
    <table>
      <thead>
        <tr>
          <th style="text-align:left">TIME</th>
          <th style="text-align:left">EVENT</th>
          <th style="text-align:left">ENTITY</th>
          <th style="text-align:left">{COL D}</th>
          <th style="text-align:left">DETAIL</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td class="neutral">HH:MM:SS</td>
          <td class="pos">{ACTION OK}</td>     <!-- .pos=green .neg=amber .neutral=dim -->
          <td>{entity}</td>
          <td>{value}</td>
          <td class="neutral">{note}</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
```

---

## Summary block (right top panel)

Big headline figure + sub-lines + SVG sparkline (inline polyline, no external lib).

```html
<div class="panel" style="border-right:none;">
  <div class="panel-header">
    <span class="panel-title">{KEY METRIC LABEL}</span>
    <span class="panel-meta">{PERIOD}</span>
    <span class="panel-badge amber">{STATE}</span>
  </div>
  <div class="summary-block">
    <div class="summary-period">{PERIOD / UNIT}</div>
    <div class="summary-value">{headline figure}</div>  <!-- .neg for amber -->
    <div class="summary-sub">
      <div><span>{SUB A} </span><strong class="pos">+{val}</strong></div>
      <div><span>{SUB B} </span><strong class="neg">-{val}</strong></div>
    </div>
    <div class="sparkline-wrap">
      <div class="sparkline-label">{METRIC} OVER TIME</div>
      <svg class="spark" viewBox="0 0 252 48" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg">
        <!-- baseline grid -->
        <line x1="0" y1="24" x2="252" y2="24" stroke="#2a2a2a" stroke-width="1"/>
        <!-- polyline: 24 data points; y=48 is bottom, y=0 is top -->
        <polyline
          points="0,40 11,38 22,35 33,30 44,26 55,28 66,22 77,18 88,20 99,15 110,12 121,14 132,10 143,8 154,11 165,7 176,9 187,6 198,8 209,5 220,7 231,9 242,6 252,4"
          fill="none" stroke="#00C851" stroke-width="1.5" stroke-linejoin="round"
        />
        <line x1="0" y1="44" x2="252" y2="44" stroke="#2a2a2a" stroke-width="1" stroke-dasharray="2,3"/>
      </svg>
    </div>
  </div>
</div>
```

---

## Gauge block (right bottom panel — constraint/limit bars)

```html
<div class="panel" style="border-right:none; border-bottom:none;">
  <div class="panel-header">
    <span class="panel-title">CONSTRAINTS</span>
    <span class="panel-meta">REAL-TIME</span>
    <span class="panel-badge">{N} WARN</span>
  </div>
  <div class="gauge-block">
    <div class="gauge-row">
      <div class="gauge-meta">
        <span class="gauge-name">{METRIC LABEL}</span>
        <span class="gauge-val">{value}</span>      <!-- .warn for amber -->
      </div>
      <div class="gauge-track">
        <div class="gauge-fill" style="width:{pct}%"></div>
        <!-- .warn=amber fill; .danger=#ff4444 fill -->
      </div>
    </div>
    <!-- repeat gauge-row for each constraint (4–6 gauges recommended) -->
  </div>
</div>
```

---

## List toolbar (search + filter chips)

```html
<div class="toolbar">
  <div class="toolbar-search">
    <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"
      stroke-linecap="round" stroke-linejoin="round">
      <circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/>
    </svg>
    <input type="text" placeholder="Search by {fields}...">
  </div>
  <div class="filter-group">
    <span class="filter-label">{FACET}</span>
    <span class="chip-filter active">ALL<span class="count"> {n}</span></span>
    <span class="chip-filter">{VALUE}<span class="count"> {n}</span></span>
    <!-- more chip-filter spans; .active = amber border + bg tint -->
  </div>
  <div class="toolbar-actions">
    <button class="btn-ghost">EXPORT</button>
    <button class="btn-primary">+ NEW {ENTITY}</button>
  </div>
</div>
```

---

## Record form — fields with inline validation

Rules live ON the field: required mark (`*`), helper text, and inline error on
invalid. Submit stays `disabled` until valid. Never add a rules/checklist/status
summary panel.

```html
<form class="form-wrap" novalidate>
  <div class="card">
    <div class="card-section-title">
      <span class="title-icon"><!-- inline SVG glyph --></span>
      {SECTION LABEL}
    </div>
    <div class="card-body">
      <div class="field-grid">

        <!-- valid required field -->
        <div class="field">
          <label class="field-label" for="f1">{LABEL} <span class="req">*</span></label>
          <input id="f1" class="control" type="text" value="">
          <span class="helper">{what the value drives or constraint hint}</span>
        </div>

        <!-- invalid field: .invalid on .field, render .error-msg -->
        <div class="field invalid">
          <label class="field-label" for="f2">{LABEL} <span class="req">*</span></label>
          <select id="f2" class="control" aria-invalid="true">
            <option value="">SELECT...</option>
          </select>
          <span class="error-msg">
            <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor"
              stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <circle cx="12" cy="12" r="10"/>
              <line x1="12" y1="8" x2="12" y2="12"/>
              <line x1="12" y1="16" x2="12.01" y2="16"/>
            </svg>
            {Specific rule that failed — e.g. "Must be a future time"}
          </span>
        </div>

      </div>
    </div>
  </div>

  <div class="form-footer">
    <span class="form-hint">Fields marked <span class="req">*</span> are required.</span>
    <div class="footer-actions">
      <button type="button" class="btn-ghost">CANCEL</button>
      <button type="submit" class="btn-primary" disabled>{SUBMIT ACTION}</button>
    </div>
  </div>
</form>
```

---

## Record detail — header band + meta grid + related panels

```html
<div class="detail-header">
  <div>
    <div class="detail-id-row">
      <span class="detail-id">{RECORD-ID}</span>
      <span class="chip-status active">{STATE}</span>
    </div>
    <div class="detail-sub">{TYPE · CONTEXT · OWNER}</div>
  </div>
  <div class="detail-actions">
    <button class="btn-ghost">{ACTION}</button>
    <button class="btn-primary">EDIT</button>
  </div>
</div>

<!-- meta grid: 3-col label/value cells -->
<div class="card">
  <div class="card-header">
    <span class="card-title">{ENTITY} DETAILS</span>
    <span class="card-badge">LAST PING {timestamp}</span>
  </div>
  <div class="meta-grid">  <!-- repeat(3,1fr); borders applied per-cell -->
    <div class="meta-cell">
      <div class="meta-label">{FIELD}</div>
      <div class="meta-value">{value}</div>
      <div class="meta-sub">{sub note}</div>
    </div>
    <!-- 5 more meta-cell divs for 6-cell (2-row × 3-col) grid -->
  </div>
</div>

<!-- two-column related panels: 7fr left / 5fr right -->
<div class="two-col">
  <div class="card"><!-- related data table: status-board row pattern or mini-table --></div>
  <div class="card"><!-- activity / event feed --></div>
</div>
```

---

## Command line footer (every screen)

```html
<div class="cmdline">
  <span class="cmd-prompt">CMD&gt;<span class="blink">_</span></span>
  <input class="cmd-input" type="text" placeholder="TYPE COMMAND OR USE HINT CHIPS..."
    spellcheck="false" autocomplete="off">
  <div class="cmd-hints">
    <span class="cmd-hint">{HINT A}</span>
    <span class="cmd-hint">{HINT B}</span>
    <span class="cmd-hint">{HINT C}</span>
  </div>
  <span class="cmd-sep">|</span>
  <span style="font-size:10px;color:var(--ink-dim);">TAB COMPLETE &nbsp; ESC CLEAR</span>
</div>
```
