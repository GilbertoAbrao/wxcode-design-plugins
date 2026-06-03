# Vault Admin — layout skeletons

Paste-ready, domain-neutral fragments for the Vault deep-navy / amber-gold
admin skin. Each skeleton is labelled by archetype slot, not by a domain
noun. Copy the shell from `assets/template.html` first (it carries the
`:root` token block + rail nav + topbar + main slot), then drop the region
skeletons below into `<main class="content">`.
Replace every `{placeholder}` with the real domain's equivalent.

Token recap (full block in `template.html`):
canvas `#0a0f1e`, panel `#121a2e`, raised `#1b2640`, border `#243049`;
text `#e5e9f0 / #c5cdd7 / #8b97ad / #4e5e7a`;
accent `var(--accent)` = `#f59e0b`; signal `--green #34d399`, `--red #f87171`.
Put `font-variant-numeric: tabular-nums` on every numeric cell.

---

## Page header (every screen)

```html
<div class="page-header" style="display:flex;align-items:flex-end;justify-content:space-between;">
  <div>
    <h1 style="font-size:20px;font-weight:700;letter-spacing:-.02em;color:var(--text-primary)">{Screen title}</h1>
    <p style="font-size:13px;color:var(--text-muted);margin-top:2px">{scope · period · context}</p>
  </div>
  <div style="display:flex;gap:10px;align-items:center">
    <button class="btn-ghost">{Secondary action}</button>
    <button class="btn-primary">+ {Primary action}</button>
  </div>
</div>
```

---

## KPI card row (×4 equal-width tiles)

```html
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:16px">

  <div style="background:var(--bg-panel);border:1px solid var(--border);border-radius:10px;padding:18px 20px 16px;position:relative;overflow:hidden">
    <!-- 3px amber accent strip top-left -->
    <div style="position:absolute;top:0;left:0;width:3px;height:40px;background:var(--accent);border-radius:0 0 3px 0"></div>

    <div style="font-size:10px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--text-muted);margin-bottom:8px">{METRIC LABEL}</div>
    <div style="font-size:26px;font-weight:700;letter-spacing:-.03em;font-variant-numeric:tabular-nums;line-height:1;margin-bottom:10px">{figure}</div>

    <!-- Footer: delta chip | sparkline SVG | sub text -->
    <div style="display:flex;align-items:center;justify-content:space-between">
      <!-- Delta chip: use green for up, red for down -->
      <span style="font-size:12px;font-weight:600;font-variant-numeric:tabular-nums;color:var(--green);display:flex;align-items:center;gap:3px">
        <svg width="10" height="10" viewBox="0 0 10 10" fill="none"><path d="M5 8V2M2 5l3-3 3 3" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
        {delta}
      </span>
      <!-- 5-point sparkline — adjust points to data; stroke color matches signal -->
      <svg width="60" height="24" viewBox="0 0 60 24" fill="none" aria-hidden="true">
        <defs>
          <linearGradient id="spk-{n}" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="var(--green)" stop-opacity="0.25"/>
            <stop offset="100%" stop-color="var(--green)" stop-opacity="0"/>
          </linearGradient>
        </defs>
        <path d="M0,18 L15,14 L30,10 L45,7 L60,4" stroke="var(--green)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
        <path d="M0,18 L15,14 L30,10 L45,7 L60,4 L60,24 L0,24Z" fill="url(#spk-{n})"/>
      </svg>
      <span style="font-size:11px;color:var(--text-faint)">{sub text}</span>
    </div>
  </div>

  <!-- Repeat × 3 more tiles; adjust signal colors per metric -->
</div>
```

---

## Two-column grid (area chart + donut)

```html
<div style="display:grid;grid-template-columns:7fr 5fr;gap:16px">

  <!-- LEFT: time-series area chart card -->
  <div class="card" style="padding:20px">
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:16px">
      <div>
        <div style="font-size:14px;font-weight:700;color:var(--text-primary)">{Chart title}</div>
        <div style="font-size:12px;color:var(--text-muted);margin-top:1px">{sub / date range}</div>
      </div>
      <!-- Period tabs -->
      <div style="display:flex;gap:2px;background:var(--bg-raised);border:1px solid var(--border);border-radius:7px;padding:2px">
        <span style="font-size:11px;font-weight:600;padding:3px 10px;border-radius:5px;cursor:pointer;color:var(--text-muted)">1M</span>
        <span style="font-size:11px;font-weight:600;padding:3px 10px;border-radius:5px;cursor:pointer;background:var(--bg-panel);color:var(--accent-hi)">3M</span>
        <span style="font-size:11px;font-weight:600;padding:3px 10px;border-radius:5px;cursor:pointer;color:var(--text-muted)">6M</span>
        <span style="font-size:11px;font-weight:600;padding:3px 10px;border-radius:5px;cursor:pointer;color:var(--text-muted)">YTD</span>
      </div>
    </div>
    <!-- Legend row -->
    <div style="display:flex;gap:16px;margin-bottom:12px">
      <div style="display:flex;align-items:center;gap:6px;font-size:12px;color:var(--text-muted)">
        <div style="width:8px;height:8px;border-radius:50%;background:var(--green)"></div> {Series A}
      </div>
      <div style="display:flex;align-items:center;gap:6px;font-size:12px;color:var(--text-muted)">
        <div style="width:8px;height:8px;border-radius:50%;background:var(--red)"></div> {Series B}
      </div>
    </div>
    <!-- Inline SVG area chart (560×200 viewBox) — replace data points -->
    <svg viewBox="0 0 560 200" width="100%" height="200" xmlns="http://www.w3.org/2000/svg" aria-label="{Chart description}">
      <defs>
        <linearGradient id="grad-a" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stop-color="var(--green)" stop-opacity="0.22"/>
          <stop offset="100%" stop-color="var(--green)" stop-opacity="0"/>
        </linearGradient>
        <linearGradient id="grad-b" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stop-color="var(--red)" stop-opacity="0.18"/>
          <stop offset="100%" stop-color="var(--red)" stop-opacity="0"/>
        </linearGradient>
      </defs>
      <!-- Horizontal grid lines -->
      <line x1="0" y1="160" x2="560" y2="160" stroke="var(--border)" stroke-width="1"/>
      <line x1="0" y1="120" x2="560" y2="120" stroke="var(--border)" stroke-width="1" stroke-dasharray="4 4"/>
      <line x1="0" y1="80"  x2="560" y2="80"  stroke="var(--border)" stroke-width="1" stroke-dasharray="4 4"/>
      <line x1="0" y1="40"  x2="560" y2="40"  stroke="var(--border)" stroke-width="1" stroke-dasharray="4 4"/>
      <!-- Y-axis labels -->
      <text x="0" y="165" font-size="10" fill="var(--text-faint)" font-family="Inter,system-ui,sans-serif">{y0}</text>
      <text x="0" y="125" font-size="10" fill="var(--text-faint)" font-family="Inter,system-ui,sans-serif">{y1}</text>
      <text x="0" y="85"  font-size="10" fill="var(--text-faint)" font-family="Inter,system-ui,sans-serif">{y2}</text>
      <text x="0" y="45"  font-size="10" fill="var(--text-faint)" font-family="Inter,system-ui,sans-serif">{y3}</text>
      <g transform="translate(30,0)">
        <!-- X-axis period labels -->
        <text x="0"   y="185" font-size="10" fill="var(--text-faint)" font-family="Inter,system-ui,sans-serif" text-anchor="middle">{t1}</text>
        <text x="106" y="185" font-size="10" fill="var(--text-faint)" font-family="Inter,system-ui,sans-serif" text-anchor="middle">{t2}</text>
        <text x="212" y="185" font-size="10" fill="var(--text-faint)" font-family="Inter,system-ui,sans-serif" text-anchor="middle">{t3}</text>
        <text x="318" y="185" font-size="10" fill="var(--text-faint)" font-family="Inter,system-ui,sans-serif" text-anchor="middle">{t4}</text>
        <text x="424" y="185" font-size="10" fill="var(--text-faint)" font-family="Inter,system-ui,sans-serif" text-anchor="middle">{t5}</text>
        <text x="530" y="185" font-size="10" fill="var(--text-faint)" font-family="Inter,system-ui,sans-serif" text-anchor="middle">{t6}</text>
        <!-- Series A area + line (replace path data with real coordinates) -->
        <path d="M0,72 C53,80 106,56 212,56 C318,56 424,48 530,36 L530,160 L0,160Z" fill="url(#grad-a)"/>
        <path d="M0,72 C53,80 106,56 212,56 C318,56 424,48 530,36" stroke="var(--green)" stroke-width="2" fill="none" stroke-linecap="round"/>
        <!-- Series B area + line -->
        <path d="M0,104 C53,96 106,100 212,100 C318,96 424,88 530,80 L530,160 L0,160Z" fill="url(#grad-b)"/>
        <path d="M0,104 C53,96 106,100 212,100 C318,96 424,88 530,80" stroke="var(--red)" stroke-width="2" fill="none" stroke-linecap="round"/>
      </g>
    </svg>
  </div>

  <!-- RIGHT: allocation donut card -->
  <!--
    Donut: cx=90, cy=90, r=70, stroke-width=22
    Circumference = 2π×70 ≈ 439.82
    For each slice: stroke-dasharray = (pct/100)*439.82  (gap to fill remainder)
    Rotate each slice: stroke-dashoffset = -(cumulative-pct/100)*439.82
    Rotate the whole donut: transform="rotate(-90 90 90)"
  -->
  <div class="card" style="padding:20px">
    <div style="font-size:14px;font-weight:700;color:var(--text-primary);margin-bottom:16px">{Donut title}</div>
    <div style="display:flex;flex-direction:column;align-items:center;gap:16px">
      <!-- Donut SVG -->
      <div style="position:relative;width:180px;height:180px">
        <svg viewBox="0 0 180 180" width="180" height="180" xmlns="http://www.w3.org/2000/svg" aria-label="{Donut description}">
          <circle cx="90" cy="90" r="70" fill="none" stroke="var(--border)" stroke-width="22"/>
          <!-- Slice 1 — adjust dasharray and dashoffset per data -->
          <circle cx="90" cy="90" r="70" fill="none" stroke="var(--slice-1)" stroke-width="22"
            stroke-dasharray="198 242" stroke-dashoffset="0"
            transform="rotate(-90 90 90)"/>
          <!-- Slice 2 -->
          <circle cx="90" cy="90" r="70" fill="none" stroke="var(--slice-2)" stroke-width="22"
            stroke-dasharray="96 344" stroke-dashoffset="-202"
            transform="rotate(-90 90 90)"/>
          <!-- Slice 3 -->
          <circle cx="90" cy="90" r="70" fill="none" stroke="var(--slice-3)" stroke-width="22"
            stroke-dasharray="64 376" stroke-dashoffset="-300"
            transform="rotate(-90 90 90)"/>
          <!-- Slice 4 -->
          <circle cx="90" cy="90" r="70" fill="none" stroke="var(--slice-4)" stroke-width="22"
            stroke-dasharray="48 392" stroke-dashoffset="-366"
            transform="rotate(-90 90 90)"/>
          <!-- Slice 5 -->
          <circle cx="90" cy="90" r="70" fill="none" stroke="var(--slice-5)" stroke-width="22"
            stroke-dasharray="30 410" stroke-dashoffset="-415"
            transform="rotate(-90 90 90)"/>
        </svg>
        <!-- Centered total label -->
        <div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);text-align:center;pointer-events:none">
          <span style="font-size:18px;font-weight:700;font-variant-numeric:tabular-nums;letter-spacing:-.02em;color:var(--text-primary);display:block">{total}</span>
          <span style="font-size:10px;color:var(--text-muted);text-transform:uppercase;letter-spacing:.06em;display:block;margin-top:1px">Total</span>
        </div>
      </div>
      <!-- Legend rows -->
      <div style="width:100%">
        <div style="display:flex;align-items:center;gap:8px;padding:5px 0;border-bottom:1px solid var(--border);font-size:12px">
          <div style="width:8px;height:8px;border-radius:50%;background:var(--slice-1);flex-shrink:0"></div>
          <span style="flex:1;color:var(--text-muted)">{Category 1}</span>
          <span style="font-variant-numeric:tabular-nums;font-weight:600;color:var(--text-primary)">{amount}</span>
          <span style="width:34px;text-align:right;font-size:11px;font-variant-numeric:tabular-nums;color:var(--text-faint)">{pct}%</span>
        </div>
        <!-- Repeat for each category; last row omits border-bottom -->
      </div>
    </div>
  </div>

</div><!-- /two-column grid -->
```

---

## Records table card (dashboard footer or list screen)

```html
<div class="card" style="overflow:hidden">
  <div style="display:flex;align-items:center;justify-content:space-between;padding:16px 16px 12px">
    <div>
      <div style="font-size:14px;font-weight:700;color:var(--text-primary)">{Records title}</div>
      <div style="font-size:12px;color:var(--text-muted);margin-top:1px">{N most recent entries}</div>
    </div>
    <a href="#" style="font-size:12px;color:var(--accent);font-weight:600;text-decoration:none">View all →</a>
  </div>
  <table style="width:100%;border-collapse:collapse">
    <thead>
      <tr>
        <th style="font-size:10.5px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--text-faint);padding:0 16px 10px;text-align:left;border-bottom:1px solid var(--border)">{Date}</th>
        <th style="…">{Entity}</th>
        <th style="…">{Type}</th>
        <th style="…;text-align:right">{Amount}</th>
        <th style="…;text-align:right">Status</th>
      </tr>
    </thead>
    <tbody>
      <tr style="border-bottom:1px solid var(--border);transition:background .1s">
        <td style="padding:11px 16px;font-size:12px;color:var(--text-muted);font-variant-numeric:tabular-nums;white-space:nowrap">{date}</td>
        <td style="padding:11px 16px;font-size:13px;font-weight:500">{entity}</td>
        <td style="padding:11px 16px;font-size:11.5px;color:var(--text-muted)">{type}</td>
        <!-- amount: .positive = color:var(--green), .negative = color:var(--red) -->
        <td style="padding:11px 16px;font-size:13px;font-weight:600;text-align:right;font-variant-numeric:tabular-nums;color:var(--green)">+{amount}</td>
        <td style="padding:11px 16px;text-align:right">
          <span class="status-pill status-settled">Settled</span>
          <!-- variants: .status-pending, .status-rejected -->
        </td>
      </tr>
      <!-- more rows -->
    </tbody>
  </table>
  <!-- Pagination -->
  <div style="display:flex;align-items:center;justify-content:space-between;padding:14px 16px;font-size:12px;color:var(--text-muted);border-top:1px solid var(--border)">
    <span>Showing {a}–{b} of {n}</span>
    <div style="display:flex;gap:4px">
      <button style="width:28px;height:28px;border-radius:6px;border:1px solid var(--border);background:transparent;color:var(--text-muted);font-size:12px;font-weight:600;cursor:pointer;display:flex;align-items:center;justify-content:center;font-family:inherit">‹</button>
      <button style="width:28px;height:28px;border-radius:6px;border:1px solid var(--accent);background:var(--accent);color:#0a0f1e;font-size:12px;font-weight:600;cursor:pointer;display:flex;align-items:center;justify-content:center;font-family:inherit">1</button>
      <button style="…same as first…">2</button>
      <button style="…same as first…">›</button>
    </div>
  </div>
</div>
```

---

## List toolbar (search + filter chips)

```html
<div style="display:flex;align-items:center;gap:12px;flex-wrap:wrap">
  <!-- Search pill -->
  <div style="display:flex;align-items:center;gap:8px;background:var(--bg-panel);border:1px solid var(--border);border-radius:8px;padding:7px 14px;flex:0 0 280px">
    <svg width="14" height="14" viewBox="0 0 14 14" fill="none"><circle cx="6" cy="6" r="4.5" stroke="var(--text-muted)" stroke-width="1.4"/><path d="M10 10l3 3" stroke="var(--text-muted)" stroke-width="1.4" stroke-linecap="round"/></svg>
    <input type="text" placeholder="Filter by {fields}…" style="background:transparent;border:none;outline:none;color:var(--text-primary);font-size:13px;width:100%;font-family:inherit" aria-label="Search">
  </div>
  <!-- Filter chips -->
  <div style="display:flex;align-items:center;gap:6px;flex-wrap:wrap">
    <span style="font-size:11px;text-transform:uppercase;letter-spacing:.06em;color:var(--text-faint);font-weight:600">{Facet}</span>
    <!-- active chip -->
    <span style="display:flex;align-items:center;gap:5px;padding:4px 10px;border:1px solid rgba(245,158,11,.3);border-radius:20px;font-size:12px;font-weight:600;background:var(--pill-amber-bg);color:var(--accent-hi);cursor:pointer">
      All <span style="background:rgba(245,158,11,.2);border-radius:10px;padding:0 5px;font-size:10px">{n}</span>
    </span>
    <!-- inactive chip -->
    <span style="display:flex;align-items:center;gap:5px;padding:4px 10px;border:1px solid var(--border);border-radius:20px;font-size:12px;font-weight:600;color:var(--text-muted);cursor:pointer">
      {Value} <span style="background:var(--bg-raised);border-radius:10px;padding:0 5px;font-size:10px">{n}</span>
    </span>
  </div>
</div>
```

---

## Record form — fields with inline validation

Rules live ON the field: a required mark (`*`), helper text, and an inline
error on an invalid field. Submit stays `disabled` until valid. Never add a
rules/validation-status summary panel.

```html
<form novalidate style="max-width:780px;margin:0 auto;display:flex;flex-direction:column;gap:20px">

  <div class="card">
    <div style="font-size:11px;font-weight:600;letter-spacing:.5px;text-transform:uppercase;color:var(--text-muted);padding:14px 18px;border-bottom:1px solid var(--border);display:flex;align-items:center;gap:7px">
      <svg><!-- section glyph --></svg> {Section title}
    </div>
    <div style="padding:20px 18px;display:flex;flex-direction:column;gap:18px">
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px">

        <!-- Valid field -->
        <div style="display:flex;flex-direction:column;gap:6px">
          <label style="font-size:12.5px;font-weight:600;color:var(--text-secondary);display:flex;align-items:center;gap:4px" for="f1">
            {Label} <span style="color:var(--accent);font-weight:700" aria-label="required">*</span>
          </label>
          <input id="f1" style="background:var(--bg-shell);border:1px solid var(--border);border-radius:8px;padding:9px 12px;color:var(--text-primary);font-size:13.5px;font-family:inherit;outline:none;width:100%;font-variant-numeric:tabular-nums" type="text" value="{value}" aria-required="true">
          <span style="font-size:11.5px;color:var(--text-faint)">{helper text / format hint}</span>
        </div>

        <!-- Invalid field -->
        <div style="display:flex;flex-direction:column;gap:6px">
          <label style="font-size:12.5px;font-weight:600;color:var(--text-secondary);display:flex;align-items:center;gap:4px" for="f2">
            {Label} <span style="color:var(--accent);font-weight:700" aria-label="required">*</span>
          </label>
          <input id="f2" style="background:var(--bg-shell);border:1px solid var(--red);border-radius:8px;padding:9px 12px;color:var(--text-primary);font-size:13.5px;font-family:inherit;outline:none;width:100%;font-variant-numeric:tabular-nums" type="text" aria-invalid="true" aria-required="true" aria-describedby="f2-err">
          <span id="f2-err" role="alert" style="font-size:11.5px;color:var(--red);display:flex;align-items:center;gap:5px">
            <svg width="12" height="12" viewBox="0 0 12 12" fill="none" aria-hidden="true"><circle cx="6" cy="6" r="5" stroke="currentColor" stroke-width="1.4"/><path d="M6 4v2.5M6 8v.5" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/></svg>
            {Specific rule that failed}
          </span>
        </div>

      </div>
    </div>
  </div>

  <!-- Form footer -->
  <div style="display:flex;align-items:center;justify-content:space-between;background:var(--bg-panel);border:1px solid var(--border);border-radius:10px;padding:16px 18px;flex-wrap:wrap;gap:12px">
    <span style="font-size:12px;color:var(--text-muted)">Fields marked <span style="color:var(--accent);font-weight:700">*</span> are required.</span>
    <div style="display:flex;gap:10px">
      <button type="button" class="btn-ghost">Cancel</button>
      <button type="submit" class="btn-primary" disabled aria-disabled="true">{Submit label}</button>
    </div>
  </div>

</form>
```

---

## Record detail — breadcrumb + header + meta grid + related panels

```html
<!-- Breadcrumb -->
<nav style="display:flex;align-items:center;gap:7px;font-size:12px;color:var(--text-faint)" aria-label="Breadcrumb">
  <a href="#" style="color:var(--text-muted);text-decoration:none">{Parent screen}</a>
  <svg width="10" height="10" viewBox="0 0 10 10" fill="none" aria-hidden="true"><path d="M3 2l4 3-4 3" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
  <span>{Record ID}</span>
</nav>

<!-- Header band: ID + status pill + actions -->
<div style="display:flex;align-items:flex-start;justify-content:space-between;flex-wrap:wrap;gap:12px">
  <div>
    <div style="display:flex;align-items:center;gap:10px;margin-bottom:4px">
      <span style="font-family:'Courier New',monospace;font-size:16px;font-weight:700">{Record ID}</span>
      <span class="status-pill status-settled">{State}</span>
      <!-- variants: .status-pending, .status-rejected -->
    </div>
    <div style="font-size:15px;font-weight:500;color:var(--text-secondary)">{Entity · Type}</div>
  </div>
  <div style="display:flex;gap:10px">
    <button class="btn-ghost">{Secondary action}</button>
    <button class="btn-primary">Edit</button>
  </div>
</div>

<!-- Meta grid: 3 columns of label/value pairs -->
<div class="card">
  <div style="display:grid;grid-template-columns:repeat(3,1fr)">
    <div style="padding:16px 18px;border-right:1px solid var(--border);border-bottom:1px solid var(--border)">
      <div style="font-size:10px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--text-faint);margin-bottom:5px">{FIELD}</div>
      <div style="font-size:14px;font-weight:600;font-variant-numeric:tabular-nums">{value}</div>
      <div style="font-size:11px;color:var(--text-muted);margin-top:2px">{sub}</div>
    </div>
    <!-- repeat for each cell; nth-child(3n) removes right border; nth-last-child(-n+3) removes bottom border -->
  </div>
</div>

<!-- Two-column sub-panels: related data + activity feed -->
<div style="display:grid;grid-template-columns:7fr 5fr;gap:16px;align-items:start">
  <div class="card"><!-- mini-table of related records --></div>
  <div class="card"><!-- activity feed: dot + event + meta timestamp --></div>
</div>
```
