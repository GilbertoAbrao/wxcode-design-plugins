# Coral Admin — layout skeletons

Paste-ready, domain-neutral fragments for the Coral light-mode admin skin. Each
skeleton is labelled by archetype slot, not by a domain noun. Copy the shell from
`assets/template.html` first (it carries the `:root` tokens + sidebar + topbar +
main slot), then drop the region skeletons below into `<main class="page-content">`.
Replace every placeholder label with the real domain's equivalent.

Token recap (full block in `template.html`): page `#f8f9fb`, card/sidebar/topbar
`#ffffff`, border `#e6e9ef`; accent `--coral: #f43f5e`, `--coral-light: #fb7185`,
`--coral-muted: #fff1f2`; nav `--slate: #475569`, `--slate-light: #64748b`; status:
`--green: #16a34a`, `--amber: #d97706`, `--red: #dc2626` each with a `*-muted` tint.
Put `font-variant-numeric: tabular-nums` on every numeric cell.

---

## Page heading (every screen)

```html
<div class="page-heading">
  <div class="page-heading-left">
    <h1>{Screen title}</h1>
    <span class="period-badge">{context · period}</span>
  </div>
  <div class="page-heading-actions">
    <button class="btn-ghost">{Secondary action}</button>
    <button class="btn-primary">+ {Primary action}</button>
  </div>
</div>
```

---

## KPI card row (repeat ×4 in `.kpi-grid`)

```html
<div class="kpi-grid">  <!-- grid-template-columns: repeat(4,1fr); gap: 14px -->
  <div class="kpi-card">
    <div class="kpi-label">{UPPERCASE METRIC NAME}</div>
    <div style="display:flex;align-items:flex-end;justify-content:space-between;gap:8px">
      <div class="kpi-value">{figure}</div>
      <!-- inline sparkline SVG 80×32, stroke var(--coral-light) 1.5px -->
      <svg width="80" height="32" viewBox="0 0 80 32" fill="none" aria-hidden="true">
        <polyline points="0,24 20,18 40,14 60,10 80,6"
          stroke="var(--coral-light)" stroke-width="1.5"
          stroke-linecap="round" stroke-linejoin="round" fill="none"/>
      </svg>
    </div>
    <div style="display:flex;align-items:center;justify-content:space-between;gap:8px">
      <span class="delta up"><!-- or .down -->{delta}</span>
      <span style="font-size:11px;color:#9ca3af">{sub-text}</span>
    </div>
  </div>
  <!-- 3 more cards -->
</div>
```

---

## Mid row: trend chart card (left, ~60%)

```html
<div style="display:grid;grid-template-columns:3fr 2fr;gap:14px;margin-bottom:20px">
  <div class="card">
    <div class="card-header">
      <div>
        <div class="card-title">{Chart title}</div>
        <div class="card-subtitle">{subtitle}</div>
      </div>
      <div style="display:flex;gap:2px">
        <button class="chart-tab">{Dim A}</button>
        <button class="chart-tab active">{Dim B}</button>
        <button class="chart-tab">{Dim C}</button>
      </div>
    </div>
    <!-- SVG area chart: full-width, gradient fill coral-light α18%→transparent,
         2px coral stroke, 6 hairline gridlines #e6e9ef, x-axis + y-axis labels -->
    <svg viewBox="0 0 560 200" width="100%" height="200" aria-label="{description}">
      <defs>
        <linearGradient id="coral-grad" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stop-color="#fb7185" stop-opacity=".18"/>
          <stop offset="100%" stop-color="#fb7185" stop-opacity="0"/>
        </linearGradient>
      </defs>
      <!-- 6 horizontal grid lines at y=20,52,84,116,148,180 stroke="#e6e9ef" -->
      <!-- y-axis labels: text-anchor="end", x=34, font-size="10", fill="#9ca3af" -->
      <!-- x-axis labels: text-anchor="middle", y=198, font-size="10", fill="#9ca3af" -->
      <!-- area fill path + polyline points; endpoint circle r=4 fill=var(--coral) stroke=#fff sw=2 -->
    </svg>
  </div>

  <!-- breakdown bar chart card (right, ~40%) -->
  <div class="card">
    <div class="card-header">
      <div>
        <div class="card-title">{Breakdown title}</div>
        <div class="card-subtitle">{period}</div>
      </div>
    </div>
    <!-- Horizontal bars: for each category: -->
    <div style="display:flex;flex-direction:column;gap:14px;margin-top:4px">
      <div style="display:flex;flex-direction:column;gap:4px">
        <div style="display:flex;justify-content:space-between;font-size:12px">
          <span style="font-weight:500;color:var(--slate)">{Category}</span>
          <span style="font-weight:600;color:#111827;font-variant-numeric:tabular-nums">{value} · {pct}%</span>
        </div>
        <div style="height:8px;background:#f3f4f6;border-radius:4px;overflow:hidden">
          <div style="height:100%;width:{pct}%;border-radius:4px;background:var(--coral)"></div>
        </div>
      </div>
      <!-- repeat for Growth (coral-light), Starter (#f97316), Free (#94a3b8) -->
    </div>
    <!-- legend chips -->
  </div>
</div>
```

---

## Bottom row: records table card (left, ~60%)

```html
<div style="display:grid;grid-template-columns:3fr 2fr;gap:14px">
  <div style="background:var(--card);border:1px solid var(--border);border-radius:12px;box-shadow:0 1px 4px rgba(0,0,0,.05);overflow:hidden">
    <div style="display:flex;align-items:center;justify-content:space-between;padding:16px 20px;border-bottom:1px solid var(--border)">
      <div style="display:flex;align-items:center;gap:10px">
        <span style="font-size:15px;font-weight:600;color:#111827">{Table title}</span>
        <span style="font-size:11px;font-weight:700;background:var(--surface);border:1px solid var(--border);border-radius:10px;padding:1px 8px;color:#6b7280">{count}</span>
      </div>
      <a href="#" style="font-size:13px;font-weight:500;color:var(--coral)">View All →</a>
    </div>
    <table>
      <thead>
        <tr>
          <th>{ID}</th><th>{Entity}</th><th>{Tier}</th>
          <th>{Amount}</th><th>{Date}</th><th>Status</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td style="font-weight:600;color:#111827;font-family:monospace;font-size:12px">{ID}</td>
          <td><div style="display:flex;align-items:center;gap:8px">
            <div style="width:26px;height:26px;border-radius:50%;background:{color};display:flex;align-items:center;justify-content:center;font-size:10px;font-weight:700;color:#fff">{Initials}</div>
            {Name}
          </div></td>
          <td>{tier}</td>
          <td>{$amount}</td>
          <td>{date}</td>
          <td><span class="pill pill-paid"><!-- or pill-pending / pill-failed -->{State}</span></td>
        </tr>
        <!-- more rows -->
      </tbody>
    </table>
    <div style="display:flex;align-items:center;justify-content:space-between;padding:12px 20px;border-top:1px solid var(--border);background:var(--surface)">
      <span style="font-size:12px;color:#9ca3af">Showing {a}–{b} of {n}</span>
      <div class="pagination">
        <button class="page-btn">← Prev</button>
        <button class="page-btn active">1</button>
        <button class="page-btn">2</button>
        <button class="page-btn">Next →</button>
      </div>
    </div>
  </div>

  <!-- items-at-risk panel (right, ~40%) -->
  <div style="background:var(--card);border:1px solid var(--border);border-radius:12px;box-shadow:0 1px 4px rgba(0,0,0,.05);overflow:hidden;display:flex;flex-direction:column">
    <div style="padding:16px 20px;border-bottom:1px solid var(--border)">
      <div style="display:flex;align-items:center;justify-content:space-between">
        <span style="font-size:15px;font-weight:600;color:#111827">{Panel title}</span>
        <span style="font-size:11px;font-weight:700;background:var(--red-muted);color:var(--red);border-radius:10px;padding:2px 9px">{n} at risk</span>
      </div>
      <div style="font-size:12px;color:#9ca3af;margin-top:3px">{Subtitle describing the items}</div>
    </div>
    <div style="flex:1;overflow-y:auto;padding:8px 0">
      <!-- For each at-risk item: -->
      <div style="padding:12px 20px;border-bottom:1px solid var(--border);display:flex;flex-direction:column;gap:8px">
        <div style="display:flex;align-items:center;gap:9px">
          <div style="width:32px;height:32px;border-radius:50%;background:{color};display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;color:#fff">{Initials}</div>
          <div>
            <div style="font-size:13px;font-weight:600;color:#111827">{Name}</div>
            <div style="font-size:11px;color:#9ca3af">{tier · ref}</div>
          </div>
        </div>
        <div style="display:flex;align-items:center;justify-content:space-between;gap:8px">
          <div>
            <div style="font-size:13px;font-weight:600;color:#111827;font-variant-numeric:tabular-nums">{$amount}</div>
            <div style="font-size:11px;font-weight:600;color:var(--red)">{elapsed}</div>
          </div>
          <div style="display:flex;gap:8px;align-items:center">
            <button style="height:26px;padding:0 10px;border:1px solid var(--coral);border-radius:6px;font-size:11px;font-weight:600;color:var(--coral);background:#fff;font-family:inherit;cursor:pointer">{Primary action}</button>
            <button style="font-size:11px;font-weight:500;color:#9ca3af;background:none;border:none;cursor:pointer;font-family:inherit">{Secondary action}</button>
          </div>
        </div>
      </div>
      <!-- more items -->
    </div>
    <div style="padding:12px 20px;border-top:1px solid var(--border);background:var(--surface);font-size:11px;color:#9ca3af;text-align:center">
      {n} items at risk · <strong style="color:var(--red)">{exposure metric}</strong>
    </div>
  </div>
</div>
```

---

## List toolbar (search + filter chips)

```html
<div style="display:flex;align-items:center;gap:12px;margin-bottom:16px;flex-wrap:wrap">
  <!-- search pill -->
  <div style="position:relative;flex:0 0 280px">
    <svg width="14" height="14" viewBox="0 0 14 14" fill="none" style="position:absolute;left:10px;top:50%;transform:translateY(-50%);color:#9ca3af;pointer-events:none">
      <circle cx="6" cy="6" r="4.5" stroke="currentColor" stroke-width="1.5"/>
      <path d="M9.5 9.5L12 12" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
    </svg>
    <input type="search" placeholder="Filter by {fields}…" style="width:100%;height:34px;border:1px solid var(--border);border-radius:8px;padding:0 10px 0 34px;font-size:13px;color:#374151;background:#fff;outline:none;font-family:inherit">
  </div>
  <!-- status chips -->
  <span style="font-size:12px;font-weight:500;color:#9ca3af;margin-right:2px">{Facet}</span>
  <span style="display:inline-flex;align-items:center;gap:4px;height:30px;padding:0 10px;border:1px solid var(--coral);border-radius:20px;font-size:12px;font-weight:500;color:var(--coral);background:var(--coral-muted);cursor:pointer">All <span style="font-size:10px;font-weight:700;background:var(--coral);color:#fff;border-radius:9px;padding:1px 5px">{n}</span></span>
  <span style="display:inline-flex;align-items:center;gap:4px;height:30px;padding:0 10px;border:1px solid var(--border);border-radius:20px;font-size:12px;font-weight:500;color:var(--slate);background:#fff;cursor:pointer">{Value} <span style="font-size:10px;font-weight:700;background:var(--surface);border-radius:9px;padding:1px 5px;color:#6b7280">{n}</span></span>
</div>
```

---

## Record form — sections with inline validation

Rules live ON the field: a required mark (`*` coral), helper text under the field,
inline error on invalid fields. Submit stays `disabled` until the form is valid.
Never add a separate rules/validation-status panel.

```html
<form style="max-width:760px;display:flex;flex-direction:column;gap:16px" novalidate>

  <!-- Form card -->
  <div style="background:var(--card);border:1px solid var(--border);border-radius:12px;box-shadow:0 1px 4px rgba(0,0,0,.05);overflow:hidden">
    <div style="display:flex;align-items:center;gap:7px;font-size:11px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;color:#9ca3af;padding:14px 20px;border-bottom:1px solid var(--border);background:var(--surface)">
      <svg width="13" height="13" viewBox="0 0 13 13" fill="none" style="color:var(--coral)"><!-- section glyph --></svg>
      {Section title}
    </div>
    <div style="padding:20px;display:flex;flex-direction:column;gap:16px">
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px">

        <!-- valid field -->
        <div class="field">
          <label class="field-label" for="f1">{Label} <span class="req">*</span></label>
          <select id="f1" class="control" aria-required="true">
            <option value="">Select…</option>
          </select>
          <span class="helper">{What the value drives / constraint}</span>
        </div>

        <!-- invalid field: add .invalid, show .error-msg -->
        <div class="field invalid">
          <label class="field-label" for="f2">{Label} <span class="req">*</span></label>
          <input id="f2" class="control" type="number" aria-invalid="true" aria-describedby="f2-err" aria-required="true">
          <span class="error-msg" id="f2-err">
            <svg width="12" height="12" viewBox="0 0 12 12" fill="none" aria-hidden="true">
              <circle cx="6" cy="6" r="5.25" stroke="currentColor" stroke-width="1.5"/>
              <path d="M6 4v2.5M6 8h.01" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
            </svg>
            {Specific rule that failed}
          </span>
        </div>

        <!-- date field -->
        <div class="field">
          <label class="field-label" for="f3">{Label} <span class="req">*</span></label>
          <input id="f3" class="control" type="date" aria-required="true">
          <span class="helper">Must be today or a future date</span>
        </div>

        <!-- textarea spanning both columns -->
        <div class="field" style="grid-column:1/-1">
          <label class="field-label" for="f4">{Label}</label>
          <textarea id="f4" class="control" style="height:auto;padding:10px 12px;resize:vertical;min-height:80px" placeholder="{placeholder}"></textarea>
        </div>

      </div>
    </div>
  </div>

  <!-- Form footer -->
  <div style="display:flex;align-items:center;justify-content:space-between;gap:12px;background:var(--card);border:1px solid var(--border);border-radius:12px;padding:16px 20px;box-shadow:0 1px 4px rgba(0,0,0,.05)">
    <span style="font-size:12px;color:#9ca3af">Fields marked <span class="req">*</span> are required.</span>
    <div style="display:flex;gap:10px">
      <button type="button" class="btn-ghost">Cancel</button>
      <button type="submit" class="btn-primary" disabled>{Submit label}</button>
    </div>
  </div>

</form>
```

---

## Record detail — header + meta grid + related panels

```html
<div class="breadcrumb">
  <a href="#">{Parent}</a>
  <span class="breadcrumb-sep">›</span>
  <a href="#">{List}</a>
  <span class="breadcrumb-sep">›</span>
  <span>{ID}</span>
</div>

<!-- Header band -->
<div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:20px;gap:16px;flex-wrap:wrap">
  <div style="display:flex;flex-direction:column;gap:5px">
    <div style="display:flex;align-items:center;gap:10px">
      <span style="font-size:20px;font-weight:700;color:#111827;font-family:monospace">{ID}</span>
      <span class="pill pill-paid"><!-- pill-pending / pill-failed -->{State}</span>
    </div>
    <span style="font-size:14px;color:#6b7280">{entity name · tier · dimension}</span>
  </div>
  <div style="display:flex;gap:10px;align-items:center">
    <button class="btn-ghost">{Secondary action}</button>
    <button class="btn-primary">Edit</button>
  </div>
</div>

<!-- Meta grid (3 columns) -->
<div style="background:var(--card);border:1px solid var(--border);border-radius:12px;box-shadow:0 1px 4px rgba(0,0,0,.05);margin-bottom:16px">
  <div style="display:flex;align-items:center;justify-content:space-between;padding:16px 20px;border-bottom:1px solid var(--border)">
    <span style="font-size:15px;font-weight:600;color:#111827">Details</span>
    <span style="font-size:13px;font-weight:500;color:var(--coral);cursor:pointer">Edit</span>
  </div>
  <div style="display:grid;grid-template-columns:repeat(3,1fr)">
    <!-- For each field: -->
    <div style="padding:18px 20px;border-right:1px solid var(--border);border-bottom:1px solid var(--border)">
      <div style="font-size:10px;font-weight:600;text-transform:uppercase;letter-spacing:.06em;color:#9ca3af;margin-bottom:5px">{FIELD LABEL}</div>
      <div style="font-size:14px;font-weight:600;color:#111827;font-variant-numeric:tabular-nums">{value}</div>
      <div style="font-size:11px;color:#9ca3af;margin-top:2px">{sub}</div>
    </div>
    <!-- Remove border-right from every 3rd cell; remove border-bottom from last row -->
  </div>
</div>

<!-- Related data (2 cols: 3fr 2fr) -->
<div style="display:grid;grid-template-columns:3fr 2fr;gap:16px">
  <!-- Main sub-panel: mini-table or item rows -->
  <div style="background:var(--card);border:1px solid var(--border);border-radius:12px;box-shadow:0 1px 4px rgba(0,0,0,.05);overflow:hidden">
    <!-- card-header + table -->
  </div>
  <!-- Activity / feed panel -->
  <div style="background:var(--card);border:1px solid var(--border);border-radius:12px;box-shadow:0 1px 4px rgba(0,0,0,.05);overflow:hidden">
    <div style="display:flex;align-items:center;justify-content:space-between;padding:16px 20px;border-bottom:1px solid var(--border)">
      <span style="font-size:15px;font-weight:600;color:#111827">Activity</span>
    </div>
    <!-- For each activity row: -->
    <div style="display:flex;gap:12px;padding:14px 20px;border-bottom:1px solid var(--border)">
      <span style="width:8px;height:8px;border-radius:50%;background:var(--coral);flex-shrink:0;margin-top:4px"></span>
      <div>
        <div style="font-size:13px;font-weight:500;color:#111827">{Event title}</div>
        <div style="font-size:11px;color:#9ca3af;margin-top:2px"><strong style="color:#374151">{Actor}</strong> · {timestamp}</div>
      </div>
    </div>
  </div>
</div>
```
