# Pixel LiveOps Admin — layout skeletons

Paste-ready, domain-neutral fragments for the deep-space neon-purple skin. Each
skeleton is labelled by archetype slot, not by a domain noun. Copy the shell from
`assets/template.html` first (it carries the `:root` tokens + sidebar + topbar +
content slot), then drop the region skeletons below into `<div class="content">`.
Replace every placeholder label with the real domain's equivalent.

Token recap (full block in `template.html`): canvas `#0c0a14`, sidebar/topbar
`#15101f`, card `#1e1730`, deep inset `#110e1c`, hairline border `#2c2440`; text
`#ece8f5 / #968fb0`; accent `var(--accent)` = `#a855f7`; cyan `var(--cyan)` =
`#22d3ee`; states `--green #4ade80 / --red #f87171 / --amber #fbbf24`.
Put `font-variant-numeric: tabular-nums` on every numeric cell.

---

## Page header (every screen)

```html
<div class="page-header">
  <div>
    <div class="page-title">{Screen title}</div>
    <div class="page-subtitle">{entity · scope · timestamp}</div>
  </div>
  <div class="header-actions">
    <button class="btn-ghost" type="button">{Secondary action}</button>
    <button class="btn-primary" type="button">+ {Primary action}</button>
  </div>
</div>
```

---

## KPI tile (repeat ×4 in a `.kpi-strip` grid)

```html
<div class="kpi-strip">  <!-- display:grid; grid-template-columns:repeat(4,1fr); gap:14px -->
  <div class="kpi-card">
    <div class="kpi-header">
      <div class="kpi-label">{UPPERCASE METRIC NAME}</div>
      <div class="kpi-icon"><!-- inline SVG glyph; add .cyan for second accent --></div>
    </div>
    <div class="kpi-value">{figure}</div>        <!-- font-variant-numeric:tabular-nums -->
    <div class="kpi-footer">
      <div class="kpi-delta up">{▲ delta text}</div>   <!-- .up / .down / .warn -->
      <!-- optional sparkline: 52×20 polyline in delta color -->
      <svg class="sparkline" width="52" height="20" viewBox="0 0 52 20" aria-hidden="true">
        <polyline points="{x,y ...}" fill="none" stroke="var(--accent)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
    </div>
  </div>
  <!-- 3 more tiles -->
</div>
```

---

## Two-column grid (trend chart + segments panel)

```html
<div class="main-grid">  <!-- display:grid; grid-template-columns:1fr 300px; gap:14px -->

  <!-- LEFT — trend chart card -->
  <div class="card">
    <div class="card-head">
      <div>
        <div class="card-title">{Metric} · {Period}</div>
        <div class="card-sub">{entity · scope}</div>
      </div>
      <a class="card-link" href="#">Full report →</a>
    </div>
    <div style="padding:16px">
      <svg width="100%" height="160" viewBox="0 0 600 160" preserveAspectRatio="none" aria-label="{Metric} chart">
        <defs>
          <linearGradient id="areaGrad" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="var(--accent)" stop-opacity=".35"/>
            <stop offset="100%" stop-color="var(--accent)" stop-opacity="0"/>
          </linearGradient>
        </defs>
        <!-- dotted gridlines at y=20,60,100,140 -->
        <line x1="0" y1="20" x2="600" y2="20" stroke="#2c2440" stroke-width="1" stroke-dasharray="4,4"/>
        <line x1="0" y1="60" x2="600" y2="60" stroke="#2c2440" stroke-width="1" stroke-dasharray="4,4"/>
        <line x1="0" y1="100" x2="600" y2="100" stroke="#2c2440" stroke-width="1" stroke-dasharray="4,4"/>
        <line x1="0" y1="140" x2="600" y2="140" stroke="#2c2440" stroke-width="1" stroke-dasharray="4,4"/>
        <!-- y labels -->
        <text x="0" y="18" font-size="9" fill="#968fb0" font-family="Inter,system-ui,sans-serif">{y4}</text>
        <text x="0" y="58" font-size="9" fill="#968fb0" font-family="Inter,system-ui,sans-serif">{y3}</text>
        <text x="0" y="98" font-size="9" fill="#968fb0" font-family="Inter,system-ui,sans-serif">{y2}</text>
        <text x="0" y="138" font-size="9" fill="#968fb0" font-family="Inter,system-ui,sans-serif">{y1}</text>
        <!-- area + line: replace points with actual data -->
        <polygon points="{data points} 580,140 20,140" fill="url(#areaGrad)"/>
        <polyline points="{data points}" fill="none" stroke="var(--accent)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        <!-- peak callout dot (cyan) -->
        <circle cx="{px}" cy="{py}" r="5" fill="var(--cyan)" stroke="#1e1730" stroke-width="2"/>
        <!-- x-axis date labels -->
        <text x="20" y="156" font-size="9" fill="#968fb0" text-anchor="middle" font-family="Inter,system-ui,sans-serif">{date1}</text>
        <text x="580" y="156" font-size="9" fill="#968fb0" text-anchor="middle" font-family="Inter,system-ui,sans-serif">{dateN}</text>
      </svg>
    </div>
  </div>

  <!-- RIGHT — segments / side panel -->
  <div class="card">
    <div class="card-head">
      <div>
        <div class="card-title">{Entity} Segments</div>
        <div class="card-sub">{scope · snapshot label}</div>
      </div>
      <a class="card-link" href="#">All →</a>
    </div>
    <!-- rows: one per segment/category -->
    <div style="padding:14px 16px;display:flex;flex-direction:column;gap:12px">
      <div style="display:flex;flex-direction:column;gap:4px">
        <div style="display:flex;justify-content:space-between;align-items:baseline">
          <span style="font-size:12px;font-weight:600;color:var(--text)">{Segment name}</span>
          <span style="font-size:11px;color:var(--text-muted);font-variant-numeric:tabular-nums">{count} · {pct}%</span>
        </div>
        <div style="height:5px;background:#110e1c;border-radius:4px;overflow:hidden">
          <div style="height:100%;width:{pct}%;border-radius:4px;background:linear-gradient(90deg,var(--accent) 0%,var(--accent-soft) 100%)"></div>
        </div>
      </div>
      <!-- more segment rows; use var(--cyan) gradient for "new/active" segment, #2c2440 for "inactive" -->
    </div>
    <div style="padding:10px 16px 14px;border-top:1px solid var(--border);text-align:center">
      <a class="card-link" href="#">View all {entities} →</a>
    </div>
  </div>
</div>
```

---

## Status-event table (full width)

```html
<div class="card">
  <div style="display:flex;align-items:center;justify-content:space-between;padding:14px 16px;border-bottom:1px solid var(--border)">
    <div>
      <div class="card-title">{Event/record type}</div>
      <div class="card-sub">{scope · filter label}</div>
    </div>
    <button class="btn-primary" type="button">+ {New record}</button>
  </div>
  <div class="table-wrap">
    <table>
      <thead>
        <tr><th>{Name}</th><th>{Type}</th><th>{Window/Date}</th><th>Status</th><th>Actions</th></tr>
      </thead>
      <tbody>
        <tr>
          <td><span style="font-weight:600">{Record name}</span></td>
          <td>
            <span style="display:inline-block;font-size:10px;font-weight:600;padding:2px 7px;border-radius:10px;background:rgba(168,85,247,.12);color:var(--accent-soft)">{type}</span>
          </td>
          <td style="color:var(--text-muted);font-variant-numeric:tabular-nums">{window}</td>
          <td><span class="pill live">{Active state}</span></td>  <!-- .live / .scheduled / .ended -->
          <td>
            <div style="display:flex;gap:6px">
              <div style="width:26px;height:26px;background:transparent;border:1px solid var(--border);border-radius:6px;display:flex;align-items:center;justify-content:center;cursor:pointer;color:var(--text-muted)" title="Edit" aria-label="Edit">
                <svg width="12" height="12" viewBox="0 0 12 12" fill="none" aria-hidden="true"><path d="M8 2 10 4 4 10H2V8L8 2Z" stroke="currentColor" stroke-width="1.3" stroke-linejoin="round"/></svg>
              </div>
              <div style="width:26px;height:26px;background:transparent;border:1px solid var(--border);border-radius:6px;display:flex;align-items:center;justify-content:center;cursor:pointer;color:var(--text-muted)" title="Toggle" aria-label="Toggle">
                <!-- pause SVG or play SVG based on state -->
                <svg width="12" height="12" viewBox="0 0 12 12" fill="none" aria-hidden="true"><rect x="3" y="2.5" width="2" height="7" rx="1" fill="currentColor"/><rect x="7" y="2.5" width="2" height="7" rx="1" fill="currentColor"/></svg>
              </div>
            </div>
          </td>
        </tr>
        <!-- more rows; pill variants: .live .scheduled .ended -->
      </tbody>
    </table>
  </div>
</div>
```

---

## Ranked items list (full width)

```html
<div class="card">
  <div class="card-head">
    <div>
      <div class="card-title">{Top items/records} by {metric} · {period}</div>
      <div class="card-sub">{scope}</div>
    </div>
    <a class="card-link" href="#">{Section} →</a>
  </div>
  <!-- one row per item; proportional bar width = item value / max value -->
  <div>
    <div style="display:flex;align-items:center;gap:10px;padding:10px 16px;border-bottom:1px solid var(--border)">
      <div style="width:18px;font-size:11px;font-weight:700;color:var(--text-muted);text-align:right;font-variant-numeric:tabular-nums">1</div>
      <div style="flex:1;min-width:0">
        <div style="font-size:12.5px;font-weight:600;color:var(--text)">{Item name}</div>
        <!-- optional tier/rarity chip -->
        <span style="display:inline-block;font-size:9px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;padding:1px 5px;border-radius:4px;background:rgba(251,191,36,.15);color:#fbbf24">{Tier}</span>
      </div>
      <div style="width:80px">
        <div style="font-size:10px;color:var(--text-muted);text-align:right;font-variant-numeric:tabular-nums">{secondary metric}</div>
        <div style="height:4px;background:#110e1c;border-radius:3px;margin-top:2px;overflow:hidden">
          <div style="height:100%;width:{pct}%;border-radius:3px;background:linear-gradient(90deg,var(--accent) 0%,var(--accent-soft) 100%)"></div>
        </div>
      </div>
      <div style="width:60px;font-size:12px;font-weight:600;color:var(--text);text-align:right;font-variant-numeric:tabular-nums">{primary metric}</div>
    </div>
    <!-- more rows -->
  </div>
</div>
```

---

## List toolbar (search + filter chips)

```html
<div style="display:flex;align-items:center;gap:10px;flex-wrap:wrap">
  <div style="position:relative;flex:1;max-width:280px">
    <svg style="position:absolute;left:10px;top:50%;transform:translateY(-50%);color:var(--text-muted);pointer-events:none" width="13" height="13" viewBox="0 0 14 14" fill="none" aria-hidden="true">
      <circle cx="6" cy="6" r="4" stroke="currentColor" stroke-width="1.4"/>
      <path d="M9.5 9.5 12 12" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/>
    </svg>
    <input type="text" placeholder="Filter {entities}…" aria-label="Filter"
      style="width:100%;background:#110e1c;border:1px solid var(--border);border-radius:8px;padding:7px 10px 7px 32px;font-size:12px;color:var(--text);outline:none;font-family:inherit">
  </div>
  <div style="display:flex;align-items:center;gap:6px;flex-wrap:wrap">
    <span style="font-size:11px;color:var(--text-muted);font-weight:500">{Facet}</span>
    <!-- chips: .active = accent bg/border/text; default = dark inset -->
    <span style="display:inline-flex;align-items:center;gap:4px;padding:4px 10px;border-radius:8px;font-size:11px;font-weight:600;background:rgba(168,85,247,.12);border:1px solid var(--accent);color:var(--accent-soft);cursor:pointer">
      All <span style="font-variant-numeric:tabular-nums">{n}</span>
    </span>
    <span style="display:inline-flex;align-items:center;gap:4px;padding:4px 10px;border-radius:8px;font-size:11px;font-weight:600;background:#110e1c;border:1px solid var(--border);color:var(--text-muted);cursor:pointer">
      {Value} <span style="font-variant-numeric:tabular-nums">{n}</span>
    </span>
  </div>
  <div style="margin-left:auto;font-size:12px;color:var(--text-muted);font-variant-numeric:tabular-nums">{n} {entities}</div>
</div>
```

---

## Record form — fields with inline validation

Rules live ON the field: a required mark (`*`), helper text below, and an inline
error message on an invalid field. The submit stays `disabled` until valid. Never
add a separate rules/validation-status summary panel.

```html
<form class="form-wrap" style="max-width:740px;margin:0 auto;display:flex;flex-direction:column;gap:16px" novalidate>
  <div class="card">
    <div class="card-section-title"><svg><!-- glyph --></svg>{Section}</div>
    <div class="card-body">
      <div class="field-grid">  <!-- 1fr 1fr; .field.full spans both -->

        <!-- valid field -->
        <div class="field">
          <label class="field-label" for="f1">{Label} <span class="req">*</span></label>
          <input id="f1" class="control" type="text" value="">
          <span class="helper">{what the value means / format hint}</span>
        </div>

        <!-- invalid field: add .invalid on .field, render .error-msg -->
        <div class="field invalid">
          <label class="field-label" for="f2">{Label} <span class="req">*</span></label>
          <input id="f2" class="control" type="text" aria-invalid="true">
          <span class="error-msg">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
            {Specific rule that failed}
          </span>
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

  <div style="display:flex;align-items:center;justify-content:space-between;gap:12px;padding-top:4px">
    <span style="font-size:12px;color:var(--text-muted)">Fields marked <span class="req">*</span> are required.</span>
    <div style="display:flex;gap:8px">
      <button type="button" class="btn-ghost">Cancel</button>
      <button type="submit" class="btn-primary" disabled>{Submit}</button>
    </div>
  </div>
</form>
```

---

## Record detail — breadcrumb + header + meta grid + related panels

```html
<div style="display:flex;flex-direction:column;gap:16px">
  <!-- breadcrumb -->
  <div style="display:flex;align-items:center;gap:7px;font-size:12px;color:var(--text-muted)">
    <a href="#" style="color:var(--text-muted);text-decoration:none">{Parent}</a>
    <svg width="12" height="12" viewBox="0 0 12 12" fill="none" aria-hidden="true"><path d="M4.5 3 7.5 6l-3 3" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
    <span>{ID}</span>
  </div>

  <!-- detail header -->
  <div style="display:flex;align-items:flex-start;justify-content:space-between;flex-wrap:wrap;gap:12px">
    <div>
      <div style="display:flex;align-items:center;gap:10px;margin-bottom:4px">
        <span style="font-family:'Courier New',monospace;font-size:13px;font-weight:700;color:var(--text-muted);font-variant-numeric:tabular-nums">{ID}</span>
        <span class="pill live">{State}</span>  <!-- .live / .scheduled / .ended -->
      </div>
      <div style="font-size:22px;font-weight:700;color:var(--text);line-height:1.2">{Record name}</div>
      <div style="font-size:13px;color:var(--text-muted);margin-top:4px">{type · entity · scope}</div>
    </div>
    <div style="display:flex;gap:8px;align-items:center">
      <button class="btn-ghost" type="button">{Secondary action}</button>
      <button class="btn-primary" type="button">Edit</button>
    </div>
  </div>

  <!-- meta grid (3-column label/value cells) -->
  <div class="card">
    <div style="display:grid;grid-template-columns:repeat(3,1fr)">
      <!-- cell: set border-right except last in row; border-bottom except last row -->
      <div style="padding:16px;border-right:1px solid var(--border);border-bottom:1px solid var(--border)">
        <div style="font-size:10px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--text-muted);margin-bottom:5px">{FIELD}</div>
        <div style="font-size:13.5px;font-weight:600;color:var(--text);font-variant-numeric:tabular-nums">{value}</div>
        <div style="font-size:11px;color:var(--text-muted);margin-top:2px">{sub}</div>
      </div>
      <!-- more cells -->
    </div>
  </div>

  <!-- related data: 2-col layout (metrics table + activity feed) -->
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;align-items:start">
    <div class="card"><!-- metrics table rows --></div>
    <div class="card"><!-- activity timeline --></div>
  </div>
</div>
```
