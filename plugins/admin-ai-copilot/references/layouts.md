# AI Copilot Admin — layout skeletons

Paste-ready, domain-neutral fragments for the deep-navy / indigo split-pane skin.
Copy the shell from `assets/template.html` first (it carries the `:root` tokens +
top bar + icon rail + canvas + copilot rail + status bar), then drop the region
skeletons below into the relevant slot. Replace every `{placeholder}` with the
real domain's equivalent.

Token recap (full block in `template.html`):
- canvas `#0f1419`, rail `#111922`, card `#1a2332`, card-hover `#1f2b3e`
- border `rgba(255,255,255,0.06)`, border-strong `rgba(255,255,255,0.1)`
- accent `--indigo: #6366f1`, `--indigo-dim: rgba(99,102,241,0.15)`
- secondary `--pink: #ec4899`; states `--green #22c55e`, `--yellow #f59e0b`, `--red #ef4444`
- text `--text-primary #f1f5f9 / --text-secondary #94a3b8 / --text-muted #64748b`

---

## Shell (every screen)

```html
<body> <!-- flex column, height 100% -->
  <header class="topbar"><!-- 56px: brand + breadcrumb + cmd-pill + actions --></header>
  <div class="body-layout"> <!-- flex row, flex:1, overflow hidden -->
    <nav class="nav-rail"><!-- 64px: icon nav items --></nav>
    <main class="canvas"><!-- or .main: flex:1, overflow-y auto, 24px padding --></main>
    <!-- optional right copilot rail: -->
    <aside class="copilot-rail"><!-- 380px: header + thread + composer --></aside>
  </div>
  <footer class="statusbar"><!-- 32px: agent state + cost + latency + model chip --></footer>
</body>
```

---

## Top bar — Cmd+K pill

The pill is centered flex-1, max-width 480px. Placeholder text is domain-specific.

```html
<div class="cmd-pill">
  <svg width="14" height="14" viewBox="0 0 16 16" fill="none">
    <circle cx="7" cy="7" r="5" stroke="currentColor" stroke-width="1.4"/>
    <path d="M11 11l3 3" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/>
  </svg>
  <span class="cmd-pill-text">{Ask {Agent name} or jump to a {primary entity} or {action}}</span>
  <span class="cmd-kbd">⌘K</span>
</div>
```

---

## KPI tile row (4 tiles)

```html
<div class="kpi-grid">  <!-- grid-template-columns: repeat(4,1fr); gap:12px -->
  <div class="kpi-tile success">  <!-- .success / .danger / .warn / (default indigo) -->
    <div class="kpi-label">{UPPERCASE METRIC}</div>
    <div class="kpi-value">{figure}</div>  <!-- font-variant-numeric:tabular-nums -->
    <div class="kpi-sub">
      <span class="kpi-delta up">▲{delta}</span>  <!-- .up / .down -->
      {context line}
    </div>
  </div>
  <!-- 3 more tiles -->
</div>
```

---

## Area chart card (full-width)

```html
<div class="card" style="padding:20px">
  <div class="card-header" style="padding:0 0 16px">
    <div>
      <div class="card-title">{Metric trend title}</div>
      <div class="card-meta">{scope · period · resolution}</div>
    </div>
    <div style="display:flex;gap:6px">
      <!-- period / aggregation chips -->
    </div>
  </div>
  <!-- Optional legend row -->
  <div style="display:flex;gap:16px;margin-bottom:12px">
    <div style="display:flex;align-items:center;gap:6px;font-size:11px;color:var(--text-secondary)">
      <div style="width:8px;height:8px;border-radius:50%;background:var(--indigo)"></div>
      {Primary series}
    </div>
  </div>
  <!-- Inline SVG chart: gridlines + area fill gradient + polyline + optional spike annotation -->
  <svg width="100%" height="120" viewBox="0 0 700 120" preserveAspectRatio="none" style="display:block">
    <defs>
      <linearGradient id="cg" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%" stop-color="#6366f1" stop-opacity="0.3"/>
        <stop offset="100%" stop-color="#6366f1" stop-opacity="0"/>
      </linearGradient>
    </defs>
    <!-- gridlines -->
    <line x1="0" y1="30" x2="700" y2="30" stroke="rgba(255,255,255,0.04)" stroke-width="1"/>
    <line x1="0" y1="60" x2="700" y2="60" stroke="rgba(255,255,255,0.04)" stroke-width="1"/>
    <line x1="0" y1="90" x2="700" y2="90" stroke="rgba(255,255,255,0.04)" stroke-width="1"/>
    <!-- axis labels (bottom) -->
    <text x="0"   y="115" fill="#475569" font-size="9">{t0}</text>
    <text x="170" y="115" fill="#475569" font-size="9">{t1}</text>
    <text x="345" y="115" fill="#475569" font-size="9">{t2}</text>
    <text x="515" y="115" fill="#475569" font-size="9">{t3}</text>
    <text x="670" y="115" fill="#475569" font-size="9">now</text>
    <!-- area fill -->
    <path d="M0,{y0} L{...} L700,{yN} L700,108 L0,108 Z" fill="url(#cg)"/>
    <!-- polyline -->
    <path d="M0,{y0} L{...} L700,{yN}" fill="none" stroke="var(--indigo)" stroke-width="2" stroke-linejoin="round"/>
    <!-- optional peak annotation -->
    <!-- <line x1="{xp}" y1="0" x2="{xp}" y2="108" stroke="var(--pink)" stroke-width="1" stroke-dasharray="3,3" opacity="0.5"/> -->
    <!-- <circle cx="{xp}" cy="{yp}" r="4" fill="var(--pink)"/> -->
    <!-- <text x="{xp+5}" y="{yp-4}" fill="var(--pink)" font-size="9" font-weight="600">{peak label}</text> -->
  </svg>
</div>
```

---

## Records table (dashboard or list screen)

```html
<div class="card">
  <div class="card-header">
    <div class="card-title">{Entity name} — {scope}</div>
    <div style="display:flex;align-items:center;gap:8px">
      <span style="font-size:11px;color:var(--text-muted)">{N} {entities} · updated {time}</span>
      <button class="btn-ghost">{Filter}</button>
    </div>
  </div>
  <table>
    <thead>
      <tr>
        <th>{ID}</th>
        <th>{Dim A}</th>
        <th>{Dim B}</th>
        <th>{Metric}</th>
        <th>{Date}</th>
        <th>Status</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="font-family:monospace;font-size:11px;color:var(--text-primary)">{id}</td>
        <td>{value A}</td>
        <td>{value B}</td>
        <td style="font-variant-numeric:tabular-nums">{metric}</td>
        <td>{date}</td>
        <td><span class="status-pill healthy">{State}</span></td>
        <!-- status-pill variants: .healthy / .degraded / .down -->
      </tr>
    </tbody>
  </table>
</div>
```

### List screen toolbar

```html
<div class="toolbar" style="display:flex;align-items:center;gap:12px;flex-wrap:wrap">
  <div class="search-pill" style="display:flex;align-items:center;gap:8px;background:var(--bg-card);border:1px solid var(--border);border-radius:24px;padding:7px 14px;flex:1;max-width:360px">
    <!-- magnifier icon SVG -->
    <input type="text" style="background:transparent;border:none;outline:none;color:var(--text-primary);font-size:12px;font-family:inherit;width:100%" placeholder="Filter by {fields}…">
  </div>
  <div style="display:flex;align-items:center;gap:8px">
    <span style="font-size:11px;font-weight:600;color:var(--text-muted);text-transform:uppercase;letter-spacing:0.06em">{Facet}</span>
    <span class="chip active">All <span class="chip-count">{n}</span></span>
    <span class="chip">{Value A} <span class="chip-count">{n}</span></span>
    <span class="chip">{Value B} <span class="chip-count">{n}</span></span>
  </div>
  <span style="margin-left:auto;font-size:12px;color:var(--text-muted)">Showing {a}–{b} of {n}</span>
</div>
```

Pagination footer:

```html
<div style="display:flex;align-items:center;justify-content:space-between;padding:12px 20px;border-top:1px solid var(--border);font-size:11px;color:var(--text-muted)">
  <span>Showing {a}–{b} of {n} {entities}</span>
  <div style="display:flex;gap:4px">
    <button class="page-btn">‹</button>
    <button class="page-btn active">1</button>
    <button class="page-btn">2</button>
    <button class="page-btn">3</button>
    <button class="page-btn">›</button>
  </div>
</div>
```

---

## Copilot rail — thread message patterns

### User message

```html
<div class="msg user">
  <div class="msg-avatar user-av">{XX}</div>
  <div class="msg-body">
    <div class="msg-sender">You</div>
    <div class="msg-bubble">{User question or command}</div>
  </div>
</div>
```

### Agent message (narrative + tool-call card + artifact + chips)

```html
<div class="msg">
  <div class="msg-avatar pilot">✦</div>
  <div class="msg-body">
    <div class="msg-sender">{Agent name}</div>
    <div class="msg-bubble">
      {Narrative answer — references domain entities + findings.}
      <div class="tool-card">
        <div class="tool-card-header">
          <span class="tool-name">{tool_function_name}</span>
          <span class="tool-status">ran in {N}ms · {N} rows</span>
        </div>
        <div class="tool-args">
          <span>{param}=</span>"{value}"
        </div>
        <div class="tool-result">{N} {entities} returned · {sort / filter summary}</div>
      </div>
    </div>
    <!-- optional inline chart artifact -->
    <div class="artifact-card">
      <div class="artifact-label">{Artifact title} — {scope}</div>
      <!-- inline SVG bar/line chart -->
    </div>
    <!-- suggestion chips -->
    <div class="chip-row">
      <div class="chip">{Action A}</div>
      <div class="chip">{Action B}</div>
      <div class="chip">{Action C}</div>
    </div>
  </div>
</div>
```

---

## Record form — fields with inline validation

Rules live ON the field: required mark (`*`), helper text below, inline error on
invalid fields. Submit stays `disabled` until the form is valid. Never add a
separate rules/validation-status summary panel.

```html
<form class="form-wrap" novalidate>
  <div class="card">
    <div class="card-section-title">
      <!-- section icon SVG -->
      {Section name}
    </div>
    <div class="card-body">
      <div class="field-grid">  <!-- grid-template-columns: 1fr 1fr; .field.full spans both -->

        <!-- Valid field -->
        <div class="field">
          <label class="field-label" for="f1">{Label} <span class="req">*</span></label>
          <input id="f1" class="control" type="text" value="{valid value}">
          <span class="helper">{format hint / constraint}</span>
        </div>

        <!-- Invalid field: .invalid on .field, render .error-msg -->
        <div class="field invalid">
          <label class="field-label" for="f2">{Label} <span class="req">*</span></label>
          <input id="f2" class="control" type="text" value="{bad value}" aria-invalid="true">
          <span class="error-msg">
            <!-- alert icon SVG -->
            {Specific rule that failed}
          </span>
        </div>

        <!-- Required select -->
        <div class="field">
          <label class="field-label" for="f3">{Label} <span class="req">*</span></label>
          <select id="f3" class="control">
            <option value="">Select…</option>
            <option>{Option A}</option>
          </select>
          <span class="helper">{constraint on the options}</span>
        </div>

        <!-- Optional textarea, full-width -->
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

## Record detail — header + meta grid + related panels

```html
<div> <!-- outer scroll container -->

  <!-- Breadcrumb -->
  <div class="bc">
    <a href="#">{Parent list}</a>
    <span style="opacity:0.3">›</span>
    <span>{Entity ID}</span>
  </div>

  <!-- Detail header -->
  <div class="detail-header" style="display:flex;align-items:flex-start;justify-content:space-between;gap:16px">
    <div>
      <div style="display:flex;align-items:center;gap:10px;margin-bottom:4px">
        <span style="font-size:22px;font-weight:700;letter-spacing:-0.02em;font-family:monospace">{Entity ID}</span>
        <span class="status-pill {state}">{State}</span>
      </div>
      <div style="font-size:13px;color:var(--text-secondary)">{code / name / parent context}</div>
    </div>
    <div style="display:flex;gap:8px">
      <button class="btn-ghost">{Secondary action}</button>
      <button class="btn-primary">Edit</button>
    </div>
  </div>

  <!-- Meta grid: 3-column, label/value pairs -->
  <div class="card">
    <div style="display:grid;grid-template-columns:repeat(3,1fr);padding:18px;gap:20px 16px">
      <div>
        <div style="font-size:10px;font-weight:600;text-transform:uppercase;letter-spacing:0.07em;color:var(--text-muted)">{FIELD A}</div>
        <div style="font-size:14px;font-weight:600;margin-top:3px;font-variant-numeric:tabular-nums">{value}</div>
        <div style="font-size:11px;color:var(--text-muted);margin-top:2px">{sub-note}</div>
      </div>
      <!-- more cells -->
    </div>
  </div>

  <!-- Two-column: related data + activity feed (7fr 5fr) -->
  <div style="display:grid;grid-template-columns:7fr 5fr;gap:16px;align-items:start">

    <!-- Related data panel (deploy history / operations / sub-records) -->
    <div class="card">
      <div class="card-header">
        <div class="card-title">{Related entity} history</div>
        <span style="font-size:11px;color:var(--text-muted)">Last {N}</span>
      </div>
      <table>
        <thead><tr><th>{Col}</th><!-- ... --><th>Result</th></tr></thead>
        <tbody>
          <tr>
            <td class="mono">{id}</td><!-- ... -->
            <td><span class="deploy-pill success">Success</span></td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Activity feed -->
    <div class="card">
      <div class="card-header">
        <div class="card-title">Recent Activity</div>
        <span style="font-size:11px;color:var(--text-muted)">Last 6h</span>
      </div>
      <div> <!-- activity-list -->
        <div style="display:flex;gap:10px;padding:10px 18px;border-bottom:1px solid var(--border)">
          <div style="width:8px;height:8px;border-radius:50%;background:var(--indigo);flex-shrink:0;margin-top:2px"></div>
          <div>
            <div style="font-size:12px;color:var(--text-secondary)"><strong style="color:var(--text-primary)">{Event}</strong> — {detail}</div>
            <div style="font-size:10px;color:var(--text-muted);margin-top:2px">{timestamp} · {elapsed}</div>
          </div>
        </div>
        <!-- more activity rows; dot colors: var(--indigo) info / var(--yellow) warn / var(--red) error / var(--green) ok -->
      </div>
    </div>

  </div>
</div>
```

---

## Status bar — agent state variants

```html
<!-- Idle -->
<div class="status-led" style="background:var(--green)"></div>
<span><strong style="color:var(--text-secondary)">{Agent}</strong> · idle</span>

<!-- Working -->
<div class="status-led" style="background:var(--yellow);animation:pulse-led 1s ease-in-out infinite"></div>
<span><strong style="color:var(--text-secondary)">{Agent}</strong> · Working: {brief description}…</span>

<!-- Error -->
<div class="status-led" style="background:var(--red)"></div>
<span><strong style="color:var(--text-secondary)">{Agent}</strong> · Error: {short message}</span>
```
