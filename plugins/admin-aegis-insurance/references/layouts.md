# Aegis Admin — layout skeletons

Paste-ready, domain-neutral fragments for the institutional light-mode skin.
Each skeleton is labelled by archetype slot, not by a domain noun. Copy the shell
from `assets/template.html` first (it carries the `:root` tokens + sidebar +
topbar + main slot), then drop the region skeletons below into
`<div class="content">`. Replace every placeholder with the real domain's
equivalent.

Token recap (full block in `template.html`): page `#f6f8fb`; card `#ffffff`;
border `--clr-border: #e3e8f0`; sidebar `--clr-sidebar-bg: #0f2057`; primary
`--clr-navy-600: #2563eb`; teal `--clr-teal-500: #14b8a6`; status ramp
`--clr-green-*`, `--clr-amber-*`, `--clr-red-*`. Put
`font-variant-numeric: tabular-nums` on every numeric cell.

---

## Page header (every screen)

```html
<div style="display:flex;align-items:flex-start;justify-content:space-between;gap:16px">
  <div>
    <div style="font-size:20px;font-weight:700;color:#1e293b">{Screen title}</div>
    <div style="font-size:12px;color:#64748b;margin-top:3px">{scope · context}</div>
  </div>
  <div style="display:flex;gap:10px">
    <button class="btn-ghost">{Secondary action}</button>
    <button class="btn-primary">+ {Primary action}</button>
  </div>
</div>
```

---

## KPI card row (repeat ×4 in a 4-column grid)

```html
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:16px">

  <div class="card kpi-card" style="padding:18px 18px 14px">
    <!-- teal top bar via .kpi-card::before — already in shared CSS -->
    <div style="font-size:10.5px;font-weight:600;letter-spacing:.7px;text-transform:uppercase;color:#64748b;margin-bottom:8px">
      {METRIC LABEL}
    </div>
    <div style="display:flex;align-items:flex-end;justify-content:space-between;gap:8px">
      <div style="font-size:28px;font-weight:800;color:#1e293b;letter-spacing:-1px;line-height:1;font-variant-numeric:tabular-nums">
        {figure}
      </div>
      <!-- inline SVG sparkline (polyline or bar rects), stroke/fill = nav-600 or teal-500 or amber/red -->
      <svg width="64" height="32" viewBox="0 0 64 32" fill="none">
        <!-- polyline sparkline example -->
        <polyline points="0,26 16,20 32,22 48,14 64,10"
          stroke="var(--clr-navy-600)" stroke-width="1.8"
          stroke-linecap="round" stroke-linejoin="round" fill="none"/>
        <polyline points="0,26 16,20 32,22 48,14 64,10 64,32 0,32"
          fill="var(--clr-navy-600)" opacity="0.1"/>
      </svg>
    </div>
    <!-- delta chip: .kpi-delta.green / .amber / .red -->
    <div style="display:inline-flex;align-items:center;gap:3px;margin-top:8px;font-size:11.5px;font-weight:600;padding:2px 7px;border-radius:20px;background:var(--clr-green-100);color:var(--clr-green-700)">
      ▲ {delta text}
    </div>
  </div>

  <!-- 3 more tiles -->
</div>
```

---

## Horizontal pipeline board (4-stage)

```html
<div class="card" style="padding:20px">
  <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:14px">
    <span style="font-size:15px;font-weight:700;color:#1e293b">{Board title}</span>
    <a href="#" style="font-size:12.5px;color:var(--clr-navy-600);font-weight:500">Manage all →</a>
  </div>
  <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:12px">

    <!-- Stage column — repeat 4× with different color class -->
    <div>
      <!-- Stage header: .s1=red / .s2=amber / .s3=teal / .s4=green -->
      <div style="display:flex;align-items:center;justify-content:space-between;padding:8px 10px;border-radius:7px;margin-bottom:10px;font-size:12px;font-weight:700;text-transform:uppercase;background:var(--clr-red-100);color:var(--clr-red-500)">
        {Stage label}
        <span style="font-size:11px;font-weight:700;padding:1px 6px;border-radius:10px;background:rgba(0,0,0,0.08);color:inherit">{N}</span>
      </div>

      <!-- Pipeline card (2–3 per stage) -->
      <div style="background:var(--clr-surface);border-radius:7px;border:1px solid var(--clr-border);padding:10px 12px;margin-bottom:8px;border-left:3px solid var(--clr-red-500)">
        <div style="font-size:10.5px;font-weight:700;color:#64748b;margin-bottom:3px;font-family:monospace">{ID}</div>
        <div style="font-size:12.5px;font-weight:600;color:#1e293b;margin-bottom:2px">{Entity name}</div>
        <div style="display:flex;justify-content:space-between">
          <span style="font-size:11px;color:#64748b">{type · tier}</span>
          <span style="font-size:11.5px;font-weight:700;color:#1e293b;font-variant-numeric:tabular-nums">{amount}</span>
        </div>
        <div style="font-size:10px;color:#94a3b8;margin-top:4px">{elapsed}</div>
      </div>

    </div>
    <!-- stages 2–4 follow the same shape; adjust border-left color and header colors -->
  </div>
</div>
```

---

## Two-column lower grid (records table + side panel)

```html
<div style="display:grid;grid-template-columns:1fr 300px;gap:20px;align-items:start">

  <!-- Records table -->
  <div class="card" style="overflow:hidden">
    <div style="padding:16px 20px;border-bottom:1px solid var(--clr-border);display:flex;align-items:center;justify-content:space-between">
      <span style="font-size:15px;font-weight:700;color:#1e293b">{Table title}</span>
      <a href="#" style="font-size:12.5px;color:var(--clr-navy-600);font-weight:500">View all →</a>
    </div>
    <table style="width:100%;border-collapse:collapse">
      <thead>
        <tr>
          <th style="padding:10px 14px;text-align:left;font-size:10.5px;font-weight:700;letter-spacing:.6px;text-transform:uppercase;color:#64748b;background:var(--clr-surface);border-bottom:1px solid var(--clr-border)">{Col 1}</th>
          <!-- more <th> -->
          <th style="...">{Status}</th>
        </tr>
      </thead>
      <tbody>
        <tr style="transition:background .12s">
          <td style="padding:11px 14px;font-size:13px;color:#1e293b;border-bottom:1px solid #f1f5f9">
            <span style="font-family:'Menlo','Consolas',monospace;font-size:12px;color:var(--clr-navy-600);font-weight:600">{ID}</span>
          </td>
          <!-- more <td> -->
          <td style="padding:11px 14px;border-bottom:1px solid #f1f5f9">
            <!-- pill: inline style for the bg/color pair from the token map -->
            <span style="display:inline-flex;align-items:center;padding:2px 9px;border-radius:20px;font-size:11px;font-weight:700;background:var(--clr-green-100);color:var(--clr-green-700)">Active</span>
          </td>
        </tr>
        <!-- 6 more rows -->
      </tbody>
    </table>
  </div>

  <!-- Side detail panel -->
  <div class="card" style="overflow:hidden">
    <div style="padding:15px 18px;border-bottom:1px solid var(--clr-border);display:flex;align-items:center;justify-content:space-between">
      <span style="font-size:13.5px;font-weight:700;color:#1e293b">{Panel title}</span>
      <span style="background:var(--clr-amber-100);color:var(--clr-amber-700);font-size:11px;font-weight:700;padding:2px 7px;border-radius:10px">{N}</span>
    </div>
    <!-- Item list (4–6 items) -->
    <div style="padding:13px 18px;border-bottom:1px solid #f1f5f9">
      <div style="font-size:10.5px;font-weight:700;color:var(--clr-navy-600);font-family:monospace">{ID}</div>
      <div style="font-size:13px;font-weight:600;color:#1e293b;margin-bottom:2px">{Entity name}</div>
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px">
        <span style="font-size:11px;color:#64748b">{type}</span>
        <span style="font-size:11px;font-weight:600;color:var(--clr-amber-500)">{date}</span>
      </div>
      <div style="font-size:12px;font-weight:700;color:#1e293b;margin-bottom:8px;font-variant-numeric:tabular-nums">{value / yr}</div>
      <button style="display:inline-flex;align-items:center;gap:5px;padding:4px 10px;border-radius:6px;border:1px solid var(--clr-border);background:transparent;font-size:11.5px;font-weight:600;color:var(--clr-navy-600);cursor:pointer">{CTA}</button>
    </div>
    <!-- more items -->
  </div>

</div>
```

---

## Full-width inline SVG trend chart

```html
<div class="card" style="padding:20px">
  <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:16px">
    <div>
      <div style="font-size:15px;font-weight:700;color:#1e293b;margin-bottom:6px">{Chart title}</div>
      <div style="display:flex;align-items:center;gap:16px">
        <!-- legend dots: ::before circles in navy / teal -->
        <span style="display:inline-flex;align-items:center;gap:6px;font-size:12px;font-weight:500;color:#64748b">
          <span style="width:10px;height:10px;border-radius:50%;background:var(--clr-navy-600);display:inline-block"></span>
          {Series 1}
        </span>
        <span style="display:inline-flex;align-items:center;gap:6px;font-size:12px;font-weight:500;color:#64748b">
          <span style="width:10px;height:10px;border-radius:50%;background:var(--clr-teal-500);display:inline-block"></span>
          {Series 2}
        </span>
      </div>
    </div>
    <!-- period tabs -->
    <div style="display:flex;gap:2px">
      <button style="padding:4px 11px;border-radius:6px;font-size:12px;font-weight:600;background:var(--clr-navy-050);color:var(--clr-navy-600);border:none;cursor:pointer">6M</button>
      <button style="padding:4px 11px;border-radius:6px;font-size:12px;font-weight:600;background:transparent;color:#64748b;border:none;cursor:pointer">12M</button>
      <button style="padding:4px 11px;border-radius:6px;font-size:12px;font-weight:600;background:transparent;color:#64748b;border:none;cursor:pointer">24M</button>
    </div>
  </div>
  <svg viewBox="0 0 720 140" width="100%" height="140" fill="none" style="display:block">
    <!-- dashed grid lines at y=10,45,80,115 -->
    <line x1="56" y1="10"  x2="710" y2="10"  stroke="#e3e8f0" stroke-dasharray="4,4"/>
    <line x1="56" y1="45"  x2="710" y2="45"  stroke="#e3e8f0" stroke-dasharray="4,4"/>
    <line x1="56" y1="80"  x2="710" y2="80"  stroke="#e3e8f0" stroke-dasharray="4,4"/>
    <line x1="56" y1="115" x2="710" y2="115" stroke="#e3e8f0" stroke-dasharray="4,4"/>
    <!-- Y-axis labels -->
    <text x="50" y="14"  text-anchor="end" font-size="10" fill="#94a3b8" font-family="Inter,sans-serif">{max}</text>
    <text x="50" y="119" text-anchor="end" font-size="10" fill="#94a3b8" font-family="Inter,sans-serif">0</text>
    <!-- Series 1 (navy) area -->
    <polyline points="56,80 166,60 276,50 386,55 496,38 606,35 710,28"
      stroke="var(--clr-navy-600)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
    <polygon points="56,80 166,60 276,50 386,55 496,38 606,35 710,28 710,115 56,115"
      fill="var(--clr-navy-600)" opacity="0.08"/>
    <!-- Series 2 (teal) area -->
    <polyline points="56,95 166,82 276,78 386,85 496,68 606,62 710,55"
      stroke="var(--clr-teal-500)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
    <polygon points="56,95 166,82 276,78 386,85 496,68 606,62 710,55 710,115 56,115"
      fill="var(--clr-teal-500)" opacity="0.08"/>
    <!-- X-axis period labels -->
    <text x="56"  y="132" text-anchor="middle" font-size="10" fill="#94a3b8" font-family="Inter,sans-serif">{P1}</text>
    <text x="166" y="132" text-anchor="middle" font-size="10" fill="#94a3b8" font-family="Inter,sans-serif">{P2}</text>
    <text x="276" y="132" text-anchor="middle" font-size="10" fill="#94a3b8" font-family="Inter,sans-serif">{P3}</text>
    <text x="386" y="132" text-anchor="middle" font-size="10" fill="#94a3b8" font-family="Inter,sans-serif">{P4}</text>
    <text x="496" y="132" text-anchor="middle" font-size="10" fill="#94a3b8" font-family="Inter,sans-serif">{P5}</text>
    <text x="606" y="132" text-anchor="middle" font-size="10" fill="#94a3b8" font-family="Inter,sans-serif">{P6}</text>
  </svg>
</div>
```

---

## List toolbar (search + filter chips)

```html
<div style="display:flex;align-items:center;gap:12px;flex-wrap:wrap">
  <!-- Search -->
  <div style="display:flex;align-items:center;background:#fff;border:1px solid var(--clr-border);border-radius:8px;padding:0 12px;gap:8px;height:36px;min-width:280px;color:#64748b">
    <svg width="14" height="14" viewBox="0 0 14 14" fill="none"><circle cx="6" cy="6" r="4.5" stroke="#94a3b8" stroke-width="1.4"/><line x1="9.5" y1="9.5" x2="13" y2="13" stroke="#94a3b8" stroke-width="1.4" stroke-linecap="round"/></svg>
    <input type="text" placeholder="Filter by {fields}…" style="border:none;background:transparent;outline:none;font-size:13px;color:#1e293b;width:100%">
  </div>
  <!-- Filter chips (status facet) -->
  <div style="display:flex;align-items:center;gap:6px">
    <span style="font-size:12px;color:#64748b;font-weight:500">{Facet}</span>
    <!-- active chip -->
    <span style="display:inline-flex;align-items:center;gap:5px;padding:5px 10px;border-radius:20px;font-size:12px;font-weight:600;cursor:pointer;background:var(--clr-navy-050);border:1px solid var(--clr-navy-600);color:var(--clr-navy-600)">
      All <span style="font-size:10.5px;font-weight:700;background:var(--clr-navy-100);padding:1px 5px;border-radius:10px">{n}</span>
    </span>
    <!-- inactive chip -->
    <span style="display:inline-flex;align-items:center;gap:5px;padding:5px 10px;border-radius:20px;font-size:12px;font-weight:600;cursor:pointer;background:#fff;border:1px solid var(--clr-border);color:#64748b">
      {Value} <span style="font-size:10.5px;font-weight:700;background:rgba(0,0,0,0.07);padding:1px 5px;border-radius:10px">{n}</span>
    </span>
  </div>
</div>
```

---

## Record form — fields with inline validation

Rules live ON the field: required mark (`*`), helper text under the field, and
inline error on invalid fields. Submit stays `disabled` until valid. Never add
a separate rules/validation-status summary panel.

```html
<form novalidate>
  <div class="card" style="margin-bottom:20px">

    <!-- Section heading inside the card -->
    <div style="padding:20px 24px;border-bottom:1px solid var(--clr-border)">
      <div style="font-size:13px;font-weight:700;color:#1e293b;display:flex;align-items:center;gap:8px;margin-bottom:18px">
        <svg width="16" height="16" viewBox="0 0 16 16" fill="none" style="color:var(--clr-teal-500)"><!-- section glyph --></svg>
        {Section title}
      </div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:18px 24px">

        <!-- Valid required field -->
        <div class="field">
          <label class="field-label" for="f1">{Label} <span class="req">*</span></label>
          <input id="f1" class="control" type="text" value="{value}">
          <span class="helper">{what the value drives / format hint}</span>
        </div>

        <!-- Invalid field: add .invalid on .field -->
        <div class="field invalid">
          <label class="field-label" for="f2">{Label} <span class="req">*</span></label>
          <input id="f2" class="control" type="text" value="{bad value}" aria-invalid="true">
          <span class="error-msg">
            <svg width="12" height="12" viewBox="0 0 12 12" fill="none"><circle cx="6" cy="6" r="5.5" stroke="currentColor" stroke-width="1.3"/><line x1="6" y1="3.5" x2="6" y2="6.5" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/><circle cx="6" cy="8.5" r="0.6" fill="currentColor"/></svg>
            {Specific rule that failed}
          </span>
        </div>

        <!-- Required select -->
        <div class="field">
          <label class="field-label" for="f3">{Label} <span class="req">*</span></label>
          <select id="f3" class="control"><option value="">Select…</option></select>
          <span class="helper">{constraint on the options}</span>
        </div>

        <!-- Full-width textarea -->
        <div class="field" style="grid-column:1/-1">
          <label class="field-label" for="f4">{Label}</label>
          <textarea id="f4" class="control" style="height:auto;padding:10px 12px;resize:vertical" rows="3" placeholder="{hint}"></textarea>
          <span class="helper">{visibility note}</span>
        </div>

      </div>
    </div>

    <!-- Form footer -->
    <div style="display:flex;align-items:center;justify-content:space-between;padding:18px 24px;background:var(--clr-surface);border-top:1px solid var(--clr-border)">
      <span style="font-size:12px;color:#64748b">Fields marked <span class="req">*</span> are required.</span>
      <div style="display:flex;gap:10px">
        <button type="button" class="btn-ghost">Cancel</button>
        <button type="submit" class="btn-primary" disabled>{Submit}</button>
      </div>
    </div>

  </div>
</form>
```

---

## Record detail — header + meta grid + related panels

```html
<div style="display:flex;flex-direction:column;gap:20px">

  <!-- Breadcrumb -->
  <div style="font-size:12px;color:#64748b;display:flex;align-items:center;gap:5px">
    <a href="#" style="color:var(--clr-navy-600)">{Parent list}</a>
    <span style="color:#94a3b8;font-size:11px">›</span>
    <span>{ID}</span>
  </div>

  <!-- Detail header card -->
  <div class="card" style="padding:24px;display:flex;align-items:flex-start;justify-content:space-between;gap:20px">
    <div>
      <div style="display:flex;align-items:center;gap:10px;margin-bottom:4px">
        <span style="font-family:'Menlo','Consolas',monospace;font-size:13px;font-weight:700;color:var(--clr-navy-600)">{ID}</span>
        <!-- status pill -->
        <span style="display:inline-flex;align-items:center;padding:2px 9px;border-radius:20px;font-size:11px;font-weight:700;background:var(--clr-green-100);color:var(--clr-green-700)">Active</span>
      </div>
      <div style="font-size:22px;font-weight:700;color:#1e293b;letter-spacing:-.5px">{Entity name}</div>
      <div style="font-size:13px;color:#64748b;margin-top:4px">{type · line · agent · created}</div>
    </div>
    <div style="display:flex;gap:10px;flex-shrink:0">
      <button class="btn-ghost">{Secondary action}</button>
      <button class="btn-primary">Edit</button>
    </div>
  </div>

  <!-- Meta grid (3-col label/value) -->
  <div class="card">
    <div style="padding:16px 20px;border-bottom:1px solid var(--clr-border);font-size:13px;font-weight:700;color:#1e293b">Details</div>
    <div style="display:grid;grid-template-columns:repeat(3,1fr)">
      <!-- cell — add border-right/bottom manually or via nth-child -->
      <div style="padding:18px 20px;border-right:1px solid var(--clr-border);border-bottom:1px solid var(--clr-border)">
        <div style="font-size:10.5px;font-weight:600;letter-spacing:.6px;text-transform:uppercase;color:#64748b;margin-bottom:4px">{FIELD}</div>
        <div style="font-size:14px;font-weight:600;color:#1e293b">{value}</div>
        <div style="font-size:11px;color:#94a3b8;margin-top:2px">{sub}</div>
      </div>
      <!-- 5 more cells; last row: no border-bottom; every 3rd: no border-right -->
    </div>
  </div>

  <!-- Two-column: related records sub-table + activity feed -->
  <div style="display:grid;grid-template-columns:7fr 5fr;gap:20px;align-items:start">
    <div class="card"><!-- sub-table --></div>
    <div class="card"><!-- activity timeline --></div>
  </div>

</div>
```

---

## Table footer + pagination

```html
<div style="padding:12px 16px;border-top:1px solid var(--clr-border);display:flex;align-items:center;justify-content:space-between;background:var(--clr-surface)">
  <span style="font-size:12px;color:#64748b">Showing {a}–{b} of {n}</span>
  <div style="display:flex;gap:4px">
    <button style="width:30px;height:30px;border-radius:6px;border:1px solid var(--clr-border);background:#fff;font-size:12px;font-weight:600;color:#64748b;cursor:pointer">‹</button>
    <button style="width:30px;height:30px;border-radius:6px;border:1px solid var(--clr-navy-600);background:var(--clr-navy-600);font-size:12px;font-weight:600;color:#fff;cursor:pointer">1</button>
    <button style="width:30px;height:30px;border-radius:6px;border:1px solid var(--clr-border);background:#fff;font-size:12px;font-weight:600;color:#64748b;cursor:pointer">2</button>
    <button style="width:30px;height:30px;border-radius:6px;border:1px solid var(--clr-border);background:#fff;font-size:12px;font-weight:600;color:#64748b;cursor:pointer">›</button>
  </div>
</div>
```
