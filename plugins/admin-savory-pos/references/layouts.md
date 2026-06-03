# Service Admin — layout skeletons

Paste-ready, domain-neutral fragments for the warm light-mode service admin skin.
Copy the shell from `assets/template.html` first (it carries the `:root` tokens +
sidebar + topbar + main slot), then drop the region skeletons below into
`<main class="content">`. Replace every `{placeholder}` with the real domain's
equivalent.

Token recap (full block in `template.html`): canvas `#faf8f5`, card `#ffffff`,
sidebar `#1c1917`, border `#ece6df`; text `#1e293b / #64748b`; accent
`var(--amber)` = `#f59e0b`; alert `var(--tomato)` = `#ef4444`; positive
`var(--green)` = `#22c55e`. Use `font-variant-numeric: tabular-nums` on every
numeric cell.

---

## Page header (every screen)

```html
<div class="page-header">
  <div class="page-header-left">
    <h2>{Page heading}</h2>
    <p>{Location · Date}</p>
  </div>
  <div class="header-actions">
    <button class="btn btn-ghost">{Secondary action}</button>
    <button class="btn btn-primary">+ {Primary action}</button>
  </div>
</div>
```

---

## KPI tile (repeat ×4 in a `.kpi-grid`)

```html
<div class="kpi-grid">  <!-- display:grid; grid-template-columns: repeat(4,1fr); gap:14px -->
  <div class="kpi-card">
    <div class="kpi-label">{METRIC NAME}</div>
    <div class="kpi-row">
      <div>
        <!-- optional currency prefix: -->
        <div style="display:flex;align-items:baseline;gap:3px">
          <span class="kpi-unit" style="font-size:16px">€</span>
          <span class="kpi-value">{figure}</span>
        </div>
        <!-- OR plain figure: -->
        <!-- <span class="kpi-value">{figure}</span> -->
      </div>
      <!-- 64×32 inline SVG sparkline (amber stroke, gradient fill) -->
      <svg width="64" height="32" viewBox="0 0 64 32" fill="none" aria-hidden="true">
        <defs>
          <linearGradient id="gX" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="#f59e0b" stop-opacity=".25"/>
            <stop offset="100%" stop-color="#f59e0b" stop-opacity="0"/>
          </linearGradient>
        </defs>
        <path d="M0 28 ... L64 4" stroke="var(--amber)" stroke-width="2" stroke-linecap="round" fill="none"/>
        <path d="M0 28 ... L64 4 L64 32 L0 32 Z" fill="url(#gX)"/>
      </svg>
      <!-- OR donut ring for a ratio metric (e.g. capacity): -->
      <!-- <svg width="40" height="40" viewBox="0 0 40 40" fill="none" aria-hidden="true">
             <circle cx="20" cy="20" r="15" stroke="var(--border)" stroke-width="5"/>
             <circle cx="20" cy="20" r="15" stroke="var(--amber)" stroke-width="5"
               stroke-dasharray="{arc} {gap}" stroke-dashoffset="23.6" stroke-linecap="round"/>
           </svg> -->
    </div>
    <div class="kpi-meta">
      <span class="delta up">▲ {delta}</span>   <!-- .up / .down -->
      <span class="kpi-sub">{context, e.g. vs yesterday}</span>
    </div>
  </div>
  <!-- 3 more tiles -->
</div>
```

---

## Live state board (3 columns)

```html
<div>
  <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:12px">
    <h3 style="font-size:15px;font-weight:700">
      <span class="live-dot"></span>{Board title}
    </h3>
    <a class="card-link" href="#">View all →</a>
  </div>
  <div class="state-board">  <!-- repeat(3,1fr); gap:14px -->

    <!-- Column 1 — first state (e.g. New) -->
    <div class="state-col">
      <div class="col-header">
        <div class="col-dot new"></div>   <!-- .new / .active / .done -->
        <div class="col-title">{State label}</div>
        <div class="col-count">{N}</div>
      </div>
      <!-- Record cards -->
      <div class="record-card">
        <div class="record-head">
          <span class="record-id">{#ID}</span>
          <span class="record-loc">{Location}</span>
          <span class="record-time">{elapsed}</span>
        </div>
        <div class="record-summary">{Item ×qty · Item ×qty}</div>
        <div class="record-footer">
          <span class="record-total">{€ total}</span>
          <button class="record-btn accept">{Primary action}</button>
        </div>
      </div>
      <!-- more cards -->
    </div>

    <!-- Column 2 — in-progress state (with elapsed-time bar) -->
    <div class="state-col">
      <div class="col-header">
        <div class="col-dot active"></div>
        <div class="col-title">{State label}</div>
        <div class="col-count">{N}</div>
      </div>
      <div class="record-card">
        <div class="record-head">
          <span class="record-id">{#ID}</span>
          <span class="record-loc">{Location}</span>
          <span class="record-time">{elapsed}</span>
        </div>
        <div class="elapsed-bar">
          <div class="elapsed-fill warn" style="width:{pct}%"></div>
          <!-- elapsed-fill variants: .ok / .warn / .late -->
        </div>
        <div class="record-summary">{Items}</div>
        <div class="record-footer">
          <span class="record-total">{€ total}</span>
          <span style="font-size:11px;color:var(--amber);font-weight:600">{N / target}</span>
        </div>
      </div>
    </div>

    <!-- Column 3 — completed state -->
    <div class="state-col">
      <div class="col-header">
        <div class="col-dot done"></div>
        <div class="col-title">{State label}</div>
        <div class="col-count">{N}</div>
      </div>
      <div class="record-card">
        <div class="record-head">
          <span class="record-id">{#ID}</span>
          <span class="record-loc">{Location}</span>
          <span class="record-time">done</span>
        </div>
        <div class="record-summary">{Items}</div>
        <div class="record-footer">
          <span class="record-total">{€ total}</span>
          <button class="record-btn done">{Final action}</button>
        </div>
      </div>
    </div>

  </div>
</div>
```

---

## Bottom 2-column grid (ranked list + trend chart)

```html
<div style="display:grid;grid-template-columns:55fr 45fr;gap:14px">

  <!-- LEFT: ranked items list -->
  <div class="card" style="padding:18px">
    <div class="card-header" style="border:none;padding:0;margin-bottom:14px">
      <span class="card-title" style="font-size:14px;font-weight:700">{Top items title}</span>
      <a class="card-link" href="#">{All items} →</a>
    </div>
    <!-- 6 rows: [rank badge] [name] [count] [value] [amber bar] -->
    <div class="ranked-row">
      <div class="rank-badge">1</div>
      <div class="ranked-name">{Item name}</div>
      <div class="ranked-count">{N} sold</div>
      <div class="ranked-value">{€ revenue}</div>
      <div class="ranked-bar-wrap"><div class="ranked-bar" style="width:100%"></div></div>
    </div>
    <div class="ranked-row">
      <div class="rank-badge">2</div>
      <div class="ranked-name">{Item name}</div>
      <div class="ranked-count">{N} sold</div>
      <div class="ranked-value">{€ revenue}</div>
      <div class="ranked-bar-wrap"><div class="ranked-bar" style="width:{pct}%"></div></div>
    </div>
    <!-- more rows; scale width to max value -->
  </div>

  <!-- RIGHT: hourly trend chart -->
  <div class="card" style="padding:18px">
    <div class="card-header" style="border:none;padding:0;margin-bottom:14px">
      <span class="card-title" style="font-size:14px;font-weight:700">{Metric (unit)}</span>
      <span style="font-size:11px;color:var(--text-secondary)">{Period}</span>
    </div>
    <div style="display:flex">
      <!-- Y-axis labels -->
      <div style="display:flex;flex-direction:column;justify-content:space-between;padding:4px 0;margin-right:6px;text-align:right">
        <span style="font-size:10px;color:var(--text-secondary)">{max}</span>
        <span style="font-size:10px;color:var(--text-secondary)">{mid}</span>
        <span style="font-size:10px;color:var(--text-secondary)">0</span>
      </div>
      <!-- Chart area -->
      <div style="flex:1">
        <svg width="100%" height="140" viewBox="0 0 280 140" preserveAspectRatio="none"
             xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
          <defs>
            <linearGradient id="gChart" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0%" stop-color="#f59e0b" stop-opacity=".3"/>
              <stop offset="100%" stop-color="#f59e0b" stop-opacity=".02"/>
            </linearGradient>
          </defs>
          <!-- Horizontal grid lines -->
          <line x1="0" y1="0"   x2="280" y2="0"   stroke="var(--border)" stroke-width="1"/>
          <line x1="0" y1="70"  x2="280" y2="70"  stroke="var(--border)" stroke-width="1"/>
          <line x1="0" y1="140" x2="280" y2="140" stroke="var(--border)" stroke-width="1"/>
          <!-- Area fill -->
          <path d="M0 {y0} ... L280 {yN} L280 140 L0 140 Z" fill="url(#gChart)"/>
          <!-- Polyline -->
          <polyline points="0,{y0} ... 280,{yN}"
            stroke="var(--amber)" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
          <!-- Data dots (optional — last dot open-circle) -->
          <circle cx="{x}" cy="{y}" r="3.5" fill="var(--amber)"/>
          <circle cx="280" cy="{yN}" r="4" fill="var(--card)" stroke="var(--amber)" stroke-width="2.5"/>
        </svg>
        <!-- X-axis labels -->
        <div style="display:flex;justify-content:space-between;padding:0 2px;margin-top:4px">
          <span style="font-size:10px;color:var(--text-secondary)">{t1}</span>
          <!-- repeat for each hour/label -->
          <span style="font-size:10px;color:var(--text-secondary)">{tN}</span>
        </div>
      </div>
    </div>
    <!-- Bottom strip: peak + running total -->
    <div style="display:flex;gap:18px;margin-top:12px;padding-top:12px;border-top:1px solid var(--border)">
      <div>
        <div style="font-size:10px;text-transform:uppercase;letter-spacing:.08em;color:var(--text-secondary)">Peak</div>
        <div style="font-size:14px;font-weight:700">{hour} · {€ value}</div>
      </div>
      <div>
        <div style="font-size:10px;text-transform:uppercase;letter-spacing:.08em;color:var(--text-secondary)">Running total</div>
        <div style="font-size:14px;font-weight:700;color:var(--amber)">{€ total}</div>
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
    <div class="card-title">
      <svg><!-- glyph --></svg>
      {Records title}
      <span class="card-count">{N results}</span>
    </div>
    <a class="card-link" href="#">View all →</a>
    <!-- OR for the list screen: action buttons -->
    <!-- <div style="display:flex;gap:8px">
           <button class="btn btn-ghost" style="font-size:12px;padding:6px 12px">Export CSV</button>
           <button class="btn btn-primary" style="font-size:12px;padding:6px 12px">+ New</button>
         </div> -->
  </div>
  <div class="table-wrap">
    <table>
      <thead>
        <tr>
          <th>{ID}</th>
          <th>{Location}</th>
          <th>{Items summary}</th>
          <th class="num">{Total}</th>
          <th>{Period}</th>
          <th>Status</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><a class="id-link" href="#">{#ID}</a></td>
          <td>{Location}</td>
          <td>{Item ×qty, Item ×qty}</td>
          <td class="num">{€ total}</td>
          <td>{Period}</td>
          <td><span class="pill pending">{State}</span></td>
          <!-- pill variants: .paid .pending .cancelled -->
        </tr>
        <!-- more rows -->
      </tbody>
    </table>
  </div>
  <!-- optional footer for the list screen -->
  <div class="table-footer">
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

### List screen toolbar (search + filter chips)

```html
<div class="toolbar">
  <div class="toolbar-search">
    <svg><!-- magnifier --></svg>
    <input type="text" placeholder="Filter by {fields}…">
  </div>
  <div class="filter-group">
    <span class="filter-label">{Facet}</span>
    <span class="chip active">All <span class="chip-count">{n}</span></span>
    <span class="chip">{State A} <span class="chip-count">{n}</span></span>
    <span class="chip">{State B} <span class="chip-count">{n}</span></span>
  </div>
</div>
```

---

## Record form — fields with inline validation

Rules live ON the field: required mark (`*`), helper text below, inline error on
invalid field. Submit stays `disabled` until the form is valid.
Never add a rules/validation-status summary panel.

```html
<form class="form-wrap" novalidate style="max-width:760px;display:flex;flex-direction:column;gap:16px">

  <div class="card">
    <div style="display:flex;align-items:center;gap:8px;padding:14px 18px;border-bottom:1px solid var(--border);font-size:13px;font-weight:700">
      <svg style="color:var(--amber)"><!-- section icon --></svg>
      {Section label}
    </div>
    <div style="padding:20px 18px">
      <div class="field-grid">

        <!-- valid field -->
        <div class="field">
          <label class="field-label" for="f1">{Label} <span class="req">*</span></label>
          <input id="f1" class="control" type="text" value="">
          <span class="helper">{format hint or constraint}</span>
        </div>

        <!-- invalid field -->
        <div class="field invalid">
          <label class="field-label" for="f2">{Label} <span class="req">*</span></label>
          <input id="f2" class="control" type="text" aria-invalid="true">
          <span class="error-msg">
            <svg width="13" height="13"><!-- alert icon --></svg>
            {Specific constraint that failed}
          </span>
        </div>

        <!-- required select -->
        <div class="field">
          <label class="field-label" for="f3">{Label} <span class="req">*</span></label>
          <select id="f3" class="control"><option value="">Select…</option></select>
          <span class="helper">{constraint on options}</span>
        </div>

        <!-- full-width textarea -->
        <div class="field full">
          <label class="field-label" for="f4">{Label}</label>
          <textarea id="f4" class="control" rows="3" style="resize:vertical;min-height:76px"></textarea>
          <span class="helper">{usage note}</span>
        </div>

      </div>
    </div>
  </div>

  <div style="display:flex;align-items:center;justify-content:space-between;padding-top:4px">
    <span class="form-hint">Fields marked <span class="req">*</span> are required.</span>
    <div style="display:flex;gap:10px">
      <button type="button" class="btn btn-ghost">Cancel</button>
      <button type="submit" class="btn btn-primary" disabled>{Submit}</button>
    </div>
  </div>

</form>
```

---

## Record detail — breadcrumb + header + meta grid + two-col panels

```html
<!-- Breadcrumb -->
<div style="font-size:13px;color:var(--text-secondary);display:flex;align-items:center;gap:6px">
  <a href="#" style="color:var(--amber);text-decoration:none;font-weight:500">{Parent}</a>
  <span>›</span>
  <span>{#ID}</span>
</div>

<!-- Detail header -->
<div style="display:flex;align-items:flex-start;justify-content:space-between;gap:16px;flex-wrap:wrap">
  <div>
    <div style="display:flex;align-items:center;gap:10px;margin-bottom:4px">
      <span style="font-size:22px;font-weight:800;font-variant-numeric:tabular-nums">{#ID}</span>
      <span class="pill paid">{Status}</span>   <!-- .paid / .pending / .cancelled -->
    </div>
    <div style="font-size:14px;color:var(--text-secondary)">{Location · Date}</div>
  </div>
  <div style="display:flex;gap:10px">
    <button class="btn btn-ghost">{Secondary action}</button>
    <button class="btn btn-primary">Edit</button>
  </div>
</div>

<!-- Meta grid: 3-column label/value pairs -->
<div class="card">
  <div style="display:grid;grid-template-columns:repeat(3,1fr)">
    <div style="padding:12px 14px;border-right:1px solid var(--border);border-bottom:1px solid var(--border)">
      <div style="font-size:10px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--text-secondary);margin-bottom:4px">{FIELD}</div>
      <div style="font-size:14px;font-weight:600;font-variant-numeric:tabular-nums">{value}</div>
      <div style="font-size:11px;color:var(--text-secondary);margin-top:1px">{sub}</div>
    </div>
    <!-- repeat; 3rd in a row omits border-right; last row omits border-bottom -->
  </div>
</div>

<!-- Two-column related panels -->
<div style="display:grid;grid-template-columns:7fr 5fr;gap:16px;align-items:start">

  <!-- LEFT: line items or related sub-table -->
  <div class="card">
    <div class="card-header">
      <div class="card-title"><svg><!-- icon --></svg>{Sub-table title}</div>
    </div>
    <div class="table-wrap">
      <table>
        <thead><tr><th>{Col}</th><th class="num">{Numeric}</th></tr></thead>
        <tbody>
          <tr><td>{row}</td><td class="num">{value}</td></tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- RIGHT: activity / event log -->
  <div class="card">
    <div class="card-header">
      <div class="card-title"><svg><!-- clock icon --></svg>Activity Log</div>
    </div>
    <!-- Activity rows -->
    <div style="padding:6px 0">
      <div style="display:flex;align-items:flex-start;gap:12px;padding:10px 18px;border-bottom:1px solid var(--border)">
        <div style="width:8px;height:8px;border-radius:50%;background:var(--green);margin-top:5px;flex-shrink:0"></div>
        <div style="flex:1">
          <div style="font-size:13px;color:var(--text-primary)">{Event description}</div>
          <div style="font-size:11px;color:var(--text-secondary);margin-top:2px;font-variant-numeric:tabular-nums">{time · actor}</div>
        </div>
      </div>
      <!-- more rows; dot color: var(--green) / var(--amber) / #94a3b8 -->
    </div>
  </div>

</div>
```
