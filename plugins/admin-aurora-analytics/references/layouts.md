# Aurora Admin — layout skeletons

Paste-ready, domain-neutral fragments for the Aurora light/indigo skin. Each
skeleton is labelled by archetype slot, not by a domain noun. Copy the shell from
`assets/template.html` first (it carries the `:root` tokens + sidebar + topbar +
main slot), then drop the region skeletons below into `<main class="main">`.
Replace every placeholder label with the real domain's equivalent.

Token recap (full block in `template.html`): canvas `#f8fafc`, panel `#ffffff`,
border `#e2e8f0`, soft `#f1f5f9`; text `#0f172a / #475569 / #94a3b8`;
accent `var(--c-indigo)` = `#6366f1`, violet `#7c3aed`; status tokens
`--c-green`, `--c-amber`, `--c-red`, `--c-sky` with `-lt` tints.
Put `font-variant-numeric: tabular-nums` on every numeric cell.

---

## Page header (every screen)

```html
<div style="display:flex;align-items:flex-end;justify-content:space-between;margin-bottom:4px">
  <div>
    <div style="font-size:22px;font-weight:700;letter-spacing:-.4px;color:var(--c-text)">{Screen title}</div>
    <div style="font-size:13px;color:var(--c-muted);margin-top:2px">{scope · context · date range}</div>
  </div>
  <div style="display:flex;gap:8px">
    <button class="btn-ghost">{Secondary}</button>
    <button class="btn-primary">+ {Primary action}</button>
  </div>
</div>
```

---

## KPI tile (repeat ×4 in a grid)

```html
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:16px">
  <div class="card" style="padding:20px">
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:10px">
      <span style="font-size:12px;font-weight:600;text-transform:uppercase;letter-spacing:.5px;color:var(--c-faint)">{METRIC LABEL}</span>
      <div style="width:32px;height:32px;border-radius:8px;background:var(--c-indigo-lt);display:flex;align-items:center;justify-content:center">
        <!-- inline SVG icon, stroke=var(--c-indigo) -->
      </div>
    </div>
    <div style="font-size:28px;font-weight:800;letter-spacing:-1px;line-height:1;font-variant-numeric:tabular-nums">{figure}</div>
    <div style="display:flex;align-items:center;justify-content:space-between;margin-top:10px">
      <span class="delta up">▲ {delta}</span>   <!-- .up / .down -->
      <!-- inline SVG sparkline 72×28, 7-point path + gradient fill -->
    </div>
  </div>
  <!-- 3 more tiles -->
</div>
```

Delta chip:

```html
<span style="display:inline-flex;align-items:center;gap:3px;font-size:11.5px;font-weight:600;border-radius:100px;padding:2px 7px;background:var(--c-green-lt);color:var(--c-green)">
  <svg width="10" height="10" viewBox="0 0 10 10" fill="currentColor"><path d="M5 2l4 5H1z"/></svg>
  {delta}
</span>
<!-- Down: background:var(--c-red-lt);color:var(--c-red) — path d="M5 8L1 3h8z" -->
```

---

## Two-column layout (primary content + right rail)

```html
<div style="display:grid;grid-template-columns:1fr 296px;gap:20px;align-items:start">
  <div style="display:flex;flex-direction:column;gap:20px;min-width:0">
    <!-- area chart card + records table -->
  </div>
  <div style="display:flex;flex-direction:column;gap:16px">
    <!-- donut rail card + insights card + activity card -->
  </div>
</div>
```

---

## Area chart card

```html
<div class="card" style="padding:24px">
  <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:20px">
    <div>
      <div style="font-size:15px;font-weight:700;color:var(--c-text)">{Chart title}</div>
      <div style="font-size:12px;color:var(--c-faint);margin-top:1px">{period · scope}</div>
    </div>
    <div style="display:flex;gap:16px">
      <!-- legend items: colored dot + label -->
      <div style="display:flex;align-items:center;gap:6px;font-size:12px;color:var(--c-muted)">
        <div style="width:8px;height:8px;border-radius:50%;background:var(--c-indigo)"></div>
        {Series A}
      </div>
      <div style="display:flex;align-items:center;gap:6px;font-size:12px;color:var(--c-muted)">
        <div style="width:8px;height:8px;border-radius:50%;background:var(--c-violet)"></div>
        {Series B}
      </div>
    </div>
  </div>
  <div style="position:relative;width:100%;height:220px">
    <svg viewBox="0 0 760 220" preserveAspectRatio="none" style="width:100%;height:100%;overflow:visible">
      <defs>
        <linearGradient id="ag1" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stop-color="var(--c-indigo)" stop-opacity=".18"/>
          <stop offset="100%" stop-color="var(--c-indigo)" stop-opacity="0"/>
        </linearGradient>
      </defs>
      <!-- Y-axis guide lines at y=20,60,100,140,180 stroke="#e2e8f0" -->
      <!-- Y labels: font-size=9 fill=var(--c-faint) -->
      <!-- Series path + closed area fill url(#ag1) -->
      <!-- Data-point circles: r=3.5 fill=#fff stroke=var(--c-indigo) stroke-width=2 -->
      <!-- X labels: font-size=9 fill=var(--c-faint) text-anchor=middle -->
    </svg>
  </div>
</div>
```

---

## Records table (dashboard footer or list screen)

```html
<div class="card" style="overflow:hidden">
  <div style="display:flex;align-items:center;justify-content:space-between;padding:20px 24px 16px">
    <div>
      <div style="font-size:15px;font-weight:700;color:var(--c-text)">{Table title}</div>
      <div style="font-size:12px;color:var(--c-faint);margin-top:1px">{scope · period}</div>
    </div>
    <button class="btn-ghost" style="font-size:12px;padding:5px 10px">
      View all <svg width="11" height="11" viewBox="0 0 11 11" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"><path d="M2 5.5h7M6 2.5l3 3-3 3"/></svg>
    </button>
  </div>
  <div style="overflow-x:auto">
    <table style="width:100%;border-collapse:collapse;font-size:13px">
      <thead>
        <tr>
          <th style="text-align:left;font-size:11px;font-weight:600;text-transform:uppercase;letter-spacing:.5px;color:var(--c-faint);padding:12px 16px 10px 24px;border-bottom:1px solid var(--c-border)">{Entity}</th>
          <th style="text-align:left;font-size:11px;font-weight:600;text-transform:uppercase;letter-spacing:.5px;color:var(--c-faint);padding:12px 16px 10px;border-bottom:1px solid var(--c-border)">{Source}</th>
          <th style="text-align:left;font-size:11px;font-weight:600;text-transform:uppercase;letter-spacing:.5px;color:var(--c-faint);padding:12px 16px 10px;border-bottom:1px solid var(--c-border)">{Dim A}</th>
          <th style="text-align:left;font-size:11px;font-weight:600;text-transform:uppercase;letter-spacing:.5px;color:var(--c-faint);padding:12px 16px 10px;border-bottom:1px solid var(--c-border)">{Numeric}</th>
          <th style="text-align:left;font-size:11px;font-weight:600;text-transform:uppercase;letter-spacing:.5px;color:var(--c-faint);padding:12px 16px 10px;border-bottom:1px solid var(--c-border)">{Count}</th>
          <th style="text-align:left;font-size:11px;font-weight:600;text-transform:uppercase;letter-spacing:.5px;color:var(--c-faint);padding:12px 24px 10px 16px;border-bottom:1px solid var(--c-border)">{Status}</th>
        </tr>
      </thead>
      <tbody>
        <tr style="border-bottom:1px solid var(--c-border-soft)">
          <td style="padding:13px 16px 13px 24px;vertical-align:middle">
            <!-- entity cell: avatar chip + name + sub -->
            <div style="display:flex;align-items:center;gap:10px">
              <div style="width:28px;height:28px;border-radius:50%;background:linear-gradient(135deg,var(--c-indigo),var(--c-violet));display:flex;align-items:center;justify-content:center;color:#fff;font-size:11px;font-weight:700;flex-shrink:0">{XX}</div>
              <div>
                <div style="font-weight:600">{Entity name}</div>
                <div style="font-size:12px;color:var(--c-faint)">{sub / email}</div>
              </div>
            </div>
          </td>
          <td style="padding:13px 16px;vertical-align:middle">
            <!-- source pill: choose background/color from token pairs -->
            <span style="display:inline-flex;align-items:center;font-size:11px;font-weight:600;border-radius:100px;padding:2px 8px;background:var(--c-blue-lt);color:var(--c-blue)">{Source}</span>
          </td>
          <td style="padding:13px 16px;color:var(--c-text);vertical-align:middle">{Dim A}</td>
          <td style="padding:13px 16px;color:var(--c-text);vertical-align:middle;font-variant-numeric:tabular-nums">{numeric}</td>
          <td style="padding:13px 16px;color:var(--c-text);vertical-align:middle;font-variant-numeric:tabular-nums">{count}</td>
          <td style="padding:13px 24px 13px 16px;vertical-align:middle">
            <!-- status: .status-active / .status-pending / .status-inactive -->
            <span class="status-pill status-active"><span class="status-pill-dot"></span>{State}</span>
          </td>
        </tr>
        <!-- more rows -->
      </tbody>
    </table>
  </div>
  <!-- Optional footer with pager -->
  <div style="display:flex;align-items:center;justify-content:space-between;padding:14px 24px;border-top:1px solid var(--c-border-soft)">
    <span style="font-size:12px;color:var(--c-faint)">Showing {a}–{b} of {n}</span>
    <div style="display:flex;gap:4px">
      <!-- page-btn: 30px sq, border, radius 6px; active: bg indigo -->
      <button style="width:30px;height:30px;border-radius:6px;border:1px solid var(--c-border);background:var(--c-surface);font-size:12px;color:var(--c-muted);cursor:pointer">‹</button>
      <button style="width:30px;height:30px;border-radius:6px;border:1px solid var(--c-indigo);background:var(--c-indigo);font-size:12px;color:#fff;cursor:pointer">1</button>
      <button style="width:30px;height:30px;border-radius:6px;border:1px solid var(--c-border);background:var(--c-surface);font-size:12px;color:var(--c-muted);cursor:pointer">2</button>
      <button style="width:30px;height:30px;border-radius:6px;border:1px solid var(--c-border);background:var(--c-surface);font-size:12px;color:var(--c-muted);cursor:pointer">›</button>
    </div>
  </div>
</div>
```

### List toolbar (search + filter chips)

```html
<div style="display:flex;align-items:center;gap:12px;flex-wrap:wrap">
  <div style="display:flex;align-items:center;gap:8px;background:var(--c-surface);border:1px solid var(--c-border);border-radius:8px;padding:8px 14px;width:280px;box-shadow:var(--shadow-sm)">
    <!-- magnifier SVG -->
    <input type="text" placeholder="Filter by {fields}…" style="border:none;background:transparent;font-family:var(--font);font-size:13px;color:var(--c-text);outline:none;width:100%">
  </div>
  <div style="display:flex;align-items:center;gap:6px">
    <span style="font-size:12px;font-weight:500;color:var(--c-faint)">{Facet}</span>
    <!-- active chip -->
    <span style="display:inline-flex;align-items:center;gap:5px;padding:5px 12px;border-radius:100px;font-size:12px;font-weight:600;background:var(--c-indigo-lt);border:1px solid var(--c-indigo);color:var(--c-indigo);cursor:pointer">
      All <span style="font-size:11px;font-weight:700;background:var(--c-indigo);border-radius:100px;padding:0 5px;color:#fff">{n}</span>
    </span>
    <!-- inactive chips: bg surface, border border, color muted -->
    <span style="display:inline-flex;align-items:center;gap:5px;padding:5px 12px;border-radius:100px;font-size:12px;font-weight:500;background:var(--c-surface);border:1px solid var(--c-border);color:var(--c-muted);cursor:pointer">
      {Value} <span style="font-size:11px;font-weight:700;background:var(--c-border);border-radius:100px;padding:0 5px;color:var(--c-muted)">{n}</span>
    </span>
  </div>
</div>
```

---

## Right rail — donut card

```html
<div class="card" style="padding:20px">
  <div style="font-size:14px;font-weight:700;color:var(--c-text);margin-bottom:16px">{Rail title}</div>
  <div style="position:relative;width:120px;height:120px;margin:0 auto 16px">
    <svg viewBox="0 0 100 100" style="width:100%;height:100%">
      <!-- segments: cx=50 cy=50 r=38 fill=none stroke-width=14; use stroke-dasharray + stroke-dashoffset -->
      <!-- circumference ≈ 238.8; each segment: dasharray = (pct * 238.8 / 100) rest -->
      <!-- rotate-90 on each circle; offset accumulates -->
      <circle cx="50" cy="50" r="38" fill="none" stroke="var(--c-indigo)" stroke-width="14"
        stroke-dasharray="{pct_a * 2.388} {(100 - pct_a) * 2.388}" stroke-dashoffset="0" transform="rotate(-90 50 50)"/>
      <!-- more segments… -->
    </svg>
    <div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);text-align:center">
      <div style="font-size:20px;font-weight:800;color:var(--c-text);line-height:1;font-variant-numeric:tabular-nums">{total}</div>
      <div style="font-size:10px;color:var(--c-faint);margin-top:2px">{unit}</div>
    </div>
  </div>
  <div style="display:flex;flex-direction:column;gap:10px">
    <!-- channel row -->
    <div>
      <div style="display:flex;align-items:center;gap:10px">
        <div style="width:8px;height:8px;border-radius:50%;background:var(--c-indigo);flex-shrink:0"></div>
        <div style="font-size:13px;color:var(--c-text);flex:1">{Category}</div>
        <div style="font-size:12px;font-weight:600;color:var(--c-muted);font-variant-numeric:tabular-nums">{pct}%</div>
      </div>
      <div style="height:4px;background:var(--c-border);border-radius:2px;margin-top:4px;overflow:hidden">
        <div style="height:100%;background:var(--c-indigo);border-radius:2px;width:{pct}%"></div>
      </div>
    </div>
    <!-- more rows -->
  </div>
</div>
```

---

## Right rail — insights card

```html
<div class="card" style="padding:20px">
  <div style="font-size:14px;font-weight:700;color:var(--c-text);margin-bottom:16px">{Insights title}</div>
  <!-- insight item -->
  <div style="display:flex;gap:10px;padding:10px 0;border-bottom:1px solid var(--c-border-soft);font-size:13px;line-height:1.5;color:var(--c-muted)">
    <div style="width:28px;height:28px;border-radius:8px;display:flex;align-items:center;justify-content:center;flex-shrink:0;margin-top:1px;background:var(--c-indigo-lt)">
      <!-- icon SVG stroke=var(--c-indigo) -->
    </div>
    <div><strong style="color:var(--c-text)">{observation headline}</strong> {supporting detail sentence}.</div>
  </div>
  <!-- last item: border-bottom:none;padding-bottom:0 -->
</div>
```

---

## Right rail — activity feed card

```html
<div class="card" style="padding:20px">
  <div style="font-size:14px;font-weight:700;color:var(--c-text);margin-bottom:16px">{Activity title}</div>
  <!-- activity item -->
  <div style="display:flex;gap:10px;padding:9px 0;border-bottom:1px solid var(--c-border-soft)">
    <div style="display:flex;flex-direction:column;align-items:center;padding-top:5px">
      <div style="width:8px;height:8px;border-radius:50%;background:var(--c-indigo);flex-shrink:0"></div>
    </div>
    <div style="flex:1">
      <div style="font-size:13px;color:var(--c-text);font-weight:500">{event title}</div>
      <div style="font-size:11px;color:var(--c-faint);margin-top:2px">{actor} · {elapsed}</div>
    </div>
  </div>
  <!-- last item: border-bottom:none -->
</div>
```

---

## Record form — fields with inline validation

Rules live ON the field: a required mark (`*`), helper text under the field, and
an inline error message on an invalid field. The submit stays `disabled` until
the form is valid. Never add a separate rules/validation-status summary panel.

```html
<form novalidate>
  <div class="card" style="padding:24px;margin-bottom:16px">
    <div style="display:flex;align-items:center;gap:8px;font-size:14px;font-weight:700;color:var(--c-text);margin-bottom:20px;padding-bottom:14px;border-bottom:1px solid var(--c-border-soft)">
      <!-- section icon SVG -->
      {Section title}
    </div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:18px 20px">

      <!-- valid field -->
      <div style="display:flex;flex-direction:column;gap:5px">
        <label style="font-size:13px;font-weight:600;color:var(--c-text)" for="f1">
          {Label} <span style="color:var(--c-red)">*</span>
        </label>
        <input id="f1" type="text" value=""
          style="width:100%;padding:9px 12px;background:var(--c-surface);border:1.5px solid var(--c-border);border-radius:8px;font-family:var(--font);font-size:13.5px;color:var(--c-text);outline:none">
        <span style="font-size:11.5px;color:var(--c-faint)">{what the value drives / format hint}</span>
      </div>

      <!-- invalid field: border-color red, error-msg shown -->
      <div style="display:flex;flex-direction:column;gap:5px">
        <label style="font-size:13px;font-weight:600;color:var(--c-text)" for="f2">
          {Label} <span style="color:var(--c-red)">*</span>
        </label>
        <input id="f2" type="text" aria-invalid="true"
          style="width:100%;padding:9px 12px;background:var(--c-surface);border:1.5px solid var(--c-red);border-radius:8px;font-family:var(--font);font-size:13.5px;color:var(--c-text);outline:none">
        <span style="display:flex;align-items:center;gap:5px;font-size:11.5px;color:var(--c-red);font-weight:500">
          <!-- alert circle SVG -->
          {Specific rule that failed}
        </span>
      </div>

      <!-- required select -->
      <div style="display:flex;flex-direction:column;gap:5px">
        <label style="font-size:13px;font-weight:600;color:var(--c-text)" for="f3">
          {Label} <span style="color:var(--c-red)">*</span>
        </label>
        <select id="f3"
          style="width:100%;padding:9px 12px;background:var(--c-surface);border:1.5px solid var(--c-border);border-radius:8px;font-family:var(--font);font-size:13.5px;color:var(--c-text);outline:none;cursor:pointer">
          <option value="">Select…</option>
        </select>
        <span style="font-size:11.5px;color:var(--c-faint)">{constraint on the options}</span>
      </div>

      <!-- full-width textarea -->
      <div style="display:flex;flex-direction:column;gap:5px;grid-column:1/-1">
        <label style="font-size:13px;font-weight:600;color:var(--c-text)" for="f4">{Label}</label>
        <textarea id="f4"
          style="width:100%;padding:9px 12px;background:var(--c-surface);border:1.5px solid var(--c-border);border-radius:8px;font-family:var(--font);font-size:13.5px;color:var(--c-text);outline:none;resize:vertical;min-height:80px"
          placeholder="{hint}"></textarea>
        <span style="font-size:11.5px;color:var(--c-faint)">{helper text}</span>
      </div>

    </div>
  </div>

  <div style="display:flex;align-items:center;justify-content:space-between;background:var(--c-surface);border:1px solid var(--c-border);border-radius:12px;padding:16px 24px;box-shadow:var(--shadow-sm)">
    <span style="font-size:12px;color:var(--c-faint)">Fields marked <span style="color:var(--c-red)">*</span> are required.</span>
    <div style="display:flex;gap:10px">
      <button type="button" class="btn-ghost">Cancel</button>
      <button type="submit" class="btn-primary" disabled>{Submit action}</button>
    </div>
  </div>
</form>
```

---

## Record detail — header + meta grid + related panels

```html
<div style="display:flex;flex-direction:column;gap:20px">

  <!-- Breadcrumb -->
  <div style="font-size:12px;color:var(--c-faint)">
    <a href="#" style="color:var(--c-muted);text-decoration:none">{Parent}</a> ›
    <span style="color:var(--c-text);font-weight:500">{Record ID}</span>
  </div>

  <!-- Header band -->
  <div style="display:flex;align-items:flex-start;justify-content:space-between;gap:16px">
    <div>
      <div style="display:flex;align-items:center;gap:10px;margin-bottom:6px">
        <span style="font-size:12px;font-weight:700;font-family:'Courier New',monospace;background:var(--c-border-soft);border:1px solid var(--c-border);border-radius:6px;padding:2px 8px;color:var(--c-muted)">{ID}</span>
        <span class="status-pill status-active"><span class="status-pill-dot"></span>{State}</span>
      </div>
      <div style="font-size:24px;font-weight:800;letter-spacing:-.5px;color:var(--c-text)">{Primary title}</div>
      <div style="font-size:13px;color:var(--c-muted);margin-top:2px">{sub-line · context}</div>
    </div>
    <div style="display:flex;gap:8px;flex-shrink:0">
      <button class="btn-ghost">{Secondary action}</button>
      <button class="btn-primary">{Primary action}</button>
    </div>
  </div>

  <!-- Meta grid card -->
  <div class="card" style="padding:24px">
    <div style="font-size:14px;font-weight:700;color:var(--c-text);margin-bottom:18px;padding-bottom:12px;border-bottom:1px solid var(--c-border-soft)">{Details title}</div>
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:20px">
      <div>
        <div style="font-size:11px;font-weight:600;text-transform:uppercase;letter-spacing:.5px;color:var(--c-faint)">{FIELD}</div>
        <div style="font-size:14px;font-weight:600;color:var(--c-text);margin-top:3px;font-variant-numeric:tabular-nums">{value}</div>
        <div style="font-size:11.5px;color:var(--c-faint);margin-top:2px">{sub}</div>
      </div>
      <!-- more cells -->
    </div>
  </div>

  <!-- Two-col: related sub-table + activity feed -->
  <div style="display:grid;grid-template-columns:7fr 5fr;gap:20px;align-items:start">
    <div class="card" style="overflow:hidden">
      <!-- sub-table header + table rows + footer -->
    </div>
    <div class="card" style="padding:20px">
      <!-- activity items -->
    </div>
  </div>

</div>
```
