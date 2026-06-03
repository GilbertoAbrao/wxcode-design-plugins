# Estate Realty Admin — layout skeletons

Paste-ready, domain-neutral fragments for the refined light/teal skin. Each
skeleton is labelled by archetype slot, not by a domain noun. Copy the shell from
`assets/template.html` first (it carries the `:root` tokens + sidebar + topbar +
main slot), then drop the region skeletons below into `<div class="page-body">`.
Replace every placeholder label with the real domain's equivalent.

Token recap (full block in `template.html`): page bg `#f7f9f9`; surface `#ffffff`;
sidebar `#0f2623`; accent `var(--color-accent)` = `#0d9488`; accent-mid `#14b8a6`;
status tokens `--color-success / --color-warning / --color-danger`.
Put `font-variant-numeric: tabular-nums` on every numeric cell.

---

## Page header (every screen)

```html
<div class="page-header" style="display:flex;align-items:center;justify-content:space-between;">
  <div>
    <h1 style="font-size:20px;font-weight:700;letter-spacing:-0.02em;color:var(--color-text)">{Screen title}</h1>
    <p style="font-size:13px;color:var(--color-muted);margin-top:2px">{scope · context · date}</p>
  </div>
  <div>
    <button class="btn-ghost">{Secondary action}</button>
    <button class="btn-primary">+ {Primary action}</button>
  </div>
</div>
```

---

## KPI card (repeat ×4 in a `.kpi-row` equal-column grid)

```html
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:16px">  <!-- .kpi-row -->
  <div class="card" style="padding:18px 20px 14px;display:flex;flex-direction:column;gap:4px">
    <div style="font-size:10px;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:var(--color-muted)">{METRIC NAME}</div>
    <div style="font-size:28px;font-weight:800;letter-spacing:-0.03em;color:var(--color-text);line-height:1.1;font-variant-numeric:tabular-nums">{figure}</div>
    <div style="display:flex;align-items:center;justify-content:space-between;margin-top:8px">
      <!-- Delta chip: .up / .down / .flat -->
      <span style="display:inline-flex;align-items:center;gap:3px;font-size:11.5px;font-weight:600;padding:2px 7px;border-radius:20px;color:var(--color-success);background:var(--color-success-bg)">
        <svg width="10" height="10" viewBox="0 0 10 10" fill="none"><path d="M5 8V2M2 5l3-3 3 3" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/></svg>
        {+delta}
      </span>
      <!-- Inline sparkline: 5-point polyline; stroke color follows trend -->
      <svg width="56" height="22" viewBox="0 0 56 22" fill="none">
        <polyline points="2,{y1} 14,{y2} 26,{y3} 38,{y4} 50,{y5}" stroke="var(--color-accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round"/>
        <circle cx="50" cy="{y5}" r="2.5" fill="var(--color-accent)"/>
      </svg>
    </div>
  </div>
  <!-- 3 more cards -->
</div>
```

---

## Two-column grid (records table 60 / leaderboard 40)

```html
<div style="display:grid;grid-template-columns:60fr 40fr;gap:18px;align-items:start">
  <div class="card"><!-- records table (below) --></div>
  <div class="card"><!-- ranked leaderboard (below) --></div>
</div>
```

### Records table

`[thumbnail cell] [value] [type pill] [status pill] [member cell]`

```html
<div class="card">
  <div style="display:flex;align-items:center;justify-content:space-between;padding:16px 20px;border-bottom:1px solid var(--color-border)">
    <div>
      <div style="font-size:14px;font-weight:700;color:var(--color-text)">{Table title}</div>
      <div style="font-size:12px;color:var(--color-muted);margin-top:1px">{N} records · {context}</div>
    </div>
    <a style="font-size:12.5px;color:var(--color-accent);font-weight:600;text-decoration:none" href="#">View all →</a>
  </div>
  <table style="width:100%;border-collapse:collapse">
    <thead>
      <tr>
        <th style="font-size:10.5px;font-weight:700;letter-spacing:0.06em;text-transform:uppercase;color:var(--color-muted);padding:10px 16px;text-align:left;background:var(--color-bg);border-bottom:1px solid var(--color-border)">{Record}</th>
        <th ...>{Value}</th>
        <th ...>{Type}</th>
        <th ...>{Status}</th>
        <th ...>{Member}</th>
      </tr>
    </thead>
    <tbody>
      <tr style="border-bottom:1px solid var(--color-border)">
        <td style="padding:11px 16px;font-size:13px">
          <!-- Thumbnail cell -->
          <div style="display:flex;align-items:center;gap:10px">
            <div style="width:40px;height:32px;border-radius:5px;background:var(--color-accent-light);display:flex;align-items:center;justify-content:center;flex-shrink:0;color:var(--color-accent)">
              <!-- inline SVG icon for record type -->
            </div>
            <div>
              <div style="font-weight:600;font-size:12.5px;color:var(--color-text)">{Primary label}</div>
              <div style="font-size:10.5px;color:var(--color-muted)">{Reference / ID}</div>
            </div>
          </div>
        </td>
        <td style="padding:11px 16px;font-weight:700;font-variant-numeric:tabular-nums">{value}</td>
        <td style="padding:11px 16px"><span class="pill" style="background:var(--color-pill-blue-bg);color:var(--color-pill-blue)">{Type}</span></td>
        <td style="padding:11px 16px"><span class="pill" style="background:var(--color-success-bg);color:var(--color-success)">{State}</span></td>
        <td style="padding:11px 16px">
          <div style="display:flex;align-items:center;gap:7px">
            <div style="width:26px;height:26px;border-radius:50%;background:var(--color-accent-light);color:var(--color-accent);font-size:10px;font-weight:700;display:flex;align-items:center;justify-content:center">{II}</div>
            {Member name}
          </div>
        </td>
      </tr>
      <!-- more rows; zebra: even rows get background:var(--color-bg-subtle) -->
    </tbody>
  </table>
  <!-- Footer: count + pager -->
  <div style="padding:10px 16px;display:flex;align-items:center;justify-content:space-between;border-top:1px solid var(--color-border);font-size:12px;color:var(--color-muted)">
    <span>Showing {a}–{b} of {n}</span>
    <div style="display:flex;gap:4px">
      <button class="page-btn">‹</button>
      <button class="page-btn active">1</button>
      <button class="page-btn">2</button>
      <button class="page-btn">›</button>
    </div>
  </div>
</div>
```

### Ranked leaderboard

`[rank/medal] [avatar initials] [name / stats] [value + horizontal bar]`

```html
<div class="card">
  <div style="...card-header...">{Leaderboard title} / {dimension}</div>
  <!-- rows: repeat for each ranked member -->
  <div style="display:flex;align-items:center;gap:10px;padding:11px 20px;border-bottom:1px solid var(--color-border)">
    <!-- Rank: 🥇/🥈/🥉 for 1-3; plain number for 4+ -->
    <div style="width:22px;text-align:center;font-size:12px;font-weight:800;color:var(--color-muted)">{rank}</div>
    <div style="width:34px;height:34px;border-radius:50%;background:var(--color-accent-light);color:var(--color-accent);font-size:11px;font-weight:700;display:flex;align-items:center;justify-content:center;flex-shrink:0">{II}</div>
    <div style="flex:1;min-width:0">
      <div style="font-size:13px;font-weight:600;color:var(--color-text);white-space:nowrap;overflow:hidden;text-overflow:ellipsis">{Name}</div>
      <div style="font-size:11px;color:var(--color-muted)">{stats line}</div>
    </div>
    <div style="text-align:right;flex-shrink:0">
      <div style="font-size:13px;font-weight:700;color:var(--color-accent);font-variant-numeric:tabular-nums">{value}</div>
      <!-- Horizontal bar: width scaled to max -->
      <div style="width:64px;height:4px;background:var(--color-border);border-radius:2px;margin-top:4px">
        <div style="width:{pct}%;height:4px;background:var(--color-accent);border-radius:2px"></div>
      </div>
    </div>
  </div>
</div>
```

---

## Horizontal pipeline (5 stage-columns, full-width)

```html
<div class="card">
  <div style="...card-header...">{Pipeline title} / {count · context}</div>
  <div style="display:grid;grid-template-columns:repeat(5,1fr);padding:18px 20px 20px">
    <!-- Stage: repeat for each stage -->
    <div style="display:flex;flex-direction:column;position:relative">
      <!-- Vertical divider between stages -->
      <!-- + .pipeline-stage + .pipeline-stage::before { left:0; top:20px; width:1px; height:50px; background:var(--color-border) } -->
      <div style="padding:0 14px 10px;display:flex;align-items:center;justify-content:space-between">
        <div style="font-size:11px;font-weight:700;letter-spacing:0.05em;text-transform:uppercase;color:var(--color-muted)">{Stage name}</div>
        <span style="font-size:11px;font-weight:700;background:var(--color-accent-light);color:var(--color-accent);border-radius:20px;padding:1px 7px">{count}</span>
        <!-- Final stage badge: background:var(--color-success-bg); color:var(--color-success) -->
      </div>
      <!-- Item chips: 2–3 per stage -->
      <div style="display:flex;flex-direction:column;gap:6px;padding:0 14px">
        <div style="background:var(--color-bg);border:1px solid var(--color-border);border-radius:7px;padding:7px 10px;font-size:11.5px">
          <!-- highlight chip: border-color:var(--color-accent-mid); background:var(--color-accent-faint) -->
          <!-- done chip: border-color:var(--color-success-border); background:var(--color-success-faint) -->
          <div style="font-weight:600;color:var(--color-text);white-space:nowrap;overflow:hidden;text-overflow:ellipsis">{Primary}</div>
          <div style="font-size:10.5px;color:var(--color-muted);margin-top:1px">{sub / value}</div>
        </div>
      </div>
    </div>
    <!-- 4 more stage columns -->
  </div>
</div>
```

---

## List toolbar (search + filter chips)

```html
<div style="display:flex;align-items:center;gap:14px;flex-wrap:wrap">
  <!-- Search -->
  <div style="display:flex;align-items:center;gap:8px;background:var(--color-surface);border:1px solid var(--color-border);border-radius:8px;padding:7px 12px;flex:1;max-width:340px">
    <svg width="14" height="14" viewBox="0 0 14 14" fill="none"><circle cx="6" cy="6" r="4" stroke="var(--color-muted)" stroke-width="1.4"/><path d="M9.5 9.5L12 12" stroke="var(--color-muted)" stroke-width="1.4" stroke-linecap="round"/></svg>
    <input style="background:transparent;border:none;outline:none;font-family:inherit;font-size:13px;color:var(--color-text);width:100%" type="text" placeholder="Filter by {fields}…">
  </div>
  <!-- Filter chips -->
  <div style="display:flex;align-items:center;gap:6px;flex-wrap:wrap">
    <span style="font-size:12px;color:var(--color-muted);font-weight:500">{Facet}:</span>
    <!-- Active chip -->
    <span style="display:inline-flex;align-items:center;gap:5px;padding:5px 11px;border:1px solid var(--color-accent-mid);border-radius:20px;font-size:12px;font-weight:600;color:var(--color-accent);background:var(--color-accent-light)">
      All <span style="font-size:10px;font-weight:700;background:var(--color-accent);color:#fff;padding:1px 5px;border-radius:20px">{n}</span>
    </span>
    <!-- Inactive chip -->
    <span style="...border:1px solid var(--color-border);color:var(--color-muted)...">{Value}</span>
  </div>
</div>
```

---

## Record form — sections with inline validation

Rules live ON the field: required mark (`*`), helper text, and inline error on
invalid fields. The submit stays `disabled` until valid. Never add a separate
rules/validation-status summary panel.

```html
<form novalidate>
  <div class="card" style="margin-bottom:16px">
    <!-- Section -->
    <div style="padding:20px 24px">
      <div style="font-size:13px;font-weight:700;color:var(--color-text);margin-bottom:16px;display:flex;align-items:center;gap:8px">
        <!-- inline SVG section icon, stroke=var(--color-accent) -->
        {Section title}
      </div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px">

        <!-- Valid field -->
        <div style="display:flex;flex-direction:column;gap:4px">
          <label style="font-size:12.5px;font-weight:600;color:var(--color-text)" for="f1">
            {Label} <span style="color:var(--color-danger)">*</span>
          </label>
          <input id="f1" style="padding:8px 12px;border:1px solid var(--color-border);border-radius:8px;font-family:inherit;font-size:13px;color:var(--color-text);background:var(--color-surface);outline:none" type="text" value="">
          <span style="font-size:11.5px;color:var(--color-muted)">{Helper text — constraint or format hint}</span>
        </div>

        <!-- Invalid field: border-color:var(--color-danger); background:#fff8f8 on input -->
        <div style="display:flex;flex-direction:column;gap:4px">
          <label style="font-size:12.5px;font-weight:600;color:var(--color-text)" for="f2">
            {Label} <span style="color:var(--color-danger)">*</span>
          </label>
          <input id="f2" style="padding:8px 12px;border:1px solid var(--color-danger);border-radius:8px;font-family:inherit;font-size:13px;background:#fff8f8;outline:none" type="text" aria-invalid="true">
          <span style="font-size:11.5px;color:var(--color-danger);display:flex;align-items:center;gap:4px;font-weight:500">
            <!-- inline alert icon -->
            {Specific rule that failed}
          </span>
        </div>

        <!-- Required select -->
        <div style="display:flex;flex-direction:column;gap:4px">
          <label style="font-size:12.5px;font-weight:600;color:var(--color-text)" for="f3">
            {Label} <span style="color:var(--color-danger)">*</span>
          </label>
          <select id="f3" style="padding:8px 12px;border:1px solid var(--color-border);border-radius:8px;font-family:inherit;font-size:13px;color:var(--color-text);background:var(--color-surface);outline:none;width:100%">
            <option value="">Select…</option>
          </select>
          <span style="font-size:11.5px;color:var(--color-muted)">{Constraint on the options}</span>
        </div>

      </div>
    </div>

    <!-- Form footer -->
    <div style="display:flex;align-items:center;justify-content:space-between;padding:16px 24px;border-top:1px solid var(--color-border)">
      <span style="font-size:12px;color:var(--color-muted)">Fields marked <span style="color:var(--color-danger)">*</span> are required.</span>
      <div style="display:flex;align-items:center;gap:10px">
        <button type="button" class="btn-ghost">Cancel</button>
        <button type="submit" class="btn-primary" disabled>{Submit label}</button>
      </div>
    </div>
  </div>
</form>
```

---

## Record detail — header + meta grid + related panels

```html
<!-- Breadcrumb -->
<div style="display:flex;align-items:center;gap:6px;font-size:13px;color:var(--color-muted)">
  <a style="color:var(--color-accent);text-decoration:none" href="#">{Parent list}</a>
  <span>›</span>
  <span style="color:var(--color-text);font-weight:600">{ID}</span>
</div>

<!-- Detail header band -->
<div class="card" style="padding:22px 24px;display:flex;align-items:flex-start;justify-content:space-between;gap:16px">
  <div style="display:flex;flex-direction:column;gap:6px">
    <div style="display:flex;align-items:center;gap:10px">
      <span style="font-size:11px;font-weight:700;letter-spacing:0.06em;text-transform:uppercase;color:var(--color-muted);background:var(--color-bg);border:1px solid var(--color-border);padding:2px 8px;border-radius:6px">{ID}</span>
      <span class="pill" style="background:var(--color-success-bg);color:var(--color-success)">{State}</span>
    </div>
    <div style="font-size:22px;font-weight:800;letter-spacing:-0.02em;color:var(--color-text)">{Record name}</div>
    <div style="font-size:13px;color:var(--color-muted)">{type · dimension · date}</div>
  </div>
  <div style="display:flex;align-items:center;gap:8px;flex-shrink:0">
    <button class="btn-ghost">{Secondary action}</button>
    <button class="btn-primary">Edit</button>
  </div>
</div>

<!-- Meta grid: 3-col label/value cells -->
<div class="card">
  <div style="display:grid;grid-template-columns:repeat(3,1fr)">
    <!-- repeat for each field -->
    <div style="padding:18px 20px;border-right:1px solid var(--color-border)">
      <div style="font-size:10.5px;font-weight:700;letter-spacing:0.06em;text-transform:uppercase;color:var(--color-muted);margin-bottom:4px">{FIELD}</div>
      <div style="font-size:15px;font-weight:700;color:var(--color-text);font-variant-numeric:tabular-nums">{value}</div>
      <div style="font-size:11.5px;color:var(--color-muted);margin-top:2px">{sub}</div>
    </div>
    <!-- last cell: no border-right -->
  </div>
</div>

<!-- Related panels: 60/40 -->
<div style="display:grid;grid-template-columns:60fr 40fr;gap:16px;align-items:start">
  <div class="card"><!-- sub-table or status rows --></div>
  <div class="card"><!-- activity feed --></div>
</div>
```
