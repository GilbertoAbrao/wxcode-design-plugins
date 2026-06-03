# Harbor Admin — layout skeletons

Paste-ready, domain-neutral fragments for the Harbor light-mode skin.
Copy the shell from `assets/template.html` first (it carries the
`:root` tokens + sidebar + topbar + `<main class="main">`), then drop
the region skeletons below into `<main class="main">`. Replace every
`{placeholder}` with the real domain's equivalent.

Token recap (full block in `template.html`): canvas `#f6f8fb`, panel
`#ffffff`, sidebar bg `#0f2460`; text `#1e293b / #64748b / #94a3b8`;
primary `var(--c-navy)` = `#1e3a8a`, `var(--c-blue)` = `#2563eb`,
`var(--c-teal)` = `#0d9488`; semantic vars `--c-green / --c-red /
--c-amber / --c-violet / --c-rose` each with a `-light` tint.
Put `font-variant-numeric: tabular-nums` (or class `.tabnum`) on every
numeric cell.

---

## Page header (every screen)

```html
<div class="page-header">
  <div class="page-header-left">
    <h1>{Screen heading}</h1>
    <p>{Scope · context · timestamp}</p>
  </div>
  <div class="page-header-actions">
    <button class="btn btn-ghost">{Secondary action}</button>
    <button class="btn btn-primary">+ {Primary action}</button>
  </div>
</div>
```

---

## Hero strip (stylized card + KPI tiles)

```html
<div style="display:grid;grid-template-columns:1.45fr 1fr 1fr 1fr;gap:16px">

  <!-- Stylized card SVG (gradient panel) -->
  <div style="border-radius:var(--r-card);overflow:hidden;box-shadow:var(--c-shadow-md)">
    <div style="width:100%;aspect-ratio:1.586;position:relative;background:linear-gradient(135deg,var(--c-navy) 0%,#1d4ed8 55%,var(--c-teal) 100%);border-radius:var(--r-card);padding:22px 24px;display:flex;flex-direction:column;justify-content:space-between;color:#fff;overflow:hidden">
      <!-- Abstract SVG background geometry here -->
      <!-- Top row: chip SVG + wordmark -->
      <div style="display:flex;align-items:center;justify-content:space-between">
        <!-- Replace with abstract chip SVG -->
        <div style="width:36px;height:28px;border-radius:4px;background:rgba(255,255,255,.15);border:1px solid rgba(255,255,255,.3)"></div>
        <span style="font-size:1.1rem;font-weight:800;letter-spacing:.04em">{Brand}<span style="opacity:.7">{Sub}</span></span>
      </div>
      <!-- Masked entity identifier -->
      <div style="font-size:1rem;font-weight:600;letter-spacing:.18em;font-variant-numeric:tabular-nums">····  ····  ····  {last4}</div>
      <!-- Bottom: holder / sub-label / network mark -->
      <div style="display:flex;align-items:flex-end;justify-content:space-between">
        <div><div style="font-size:.62rem;letter-spacing:.1em;text-transform:uppercase;opacity:.65">{Holder label}</div><div style="font-size:.85rem;font-weight:600">{Holder value}</div></div>
        <div><div style="font-size:.62rem;letter-spacing:.1em;text-transform:uppercase;opacity:.65">{Sub-label}</div><div style="font-size:.85rem;font-weight:600;font-variant-numeric:tabular-nums">{sub-value}</div></div>
        <!-- Abstract dual-circle network mark (fictional) -->
        <svg width="44" height="28" viewBox="0 0 44 28" fill="none" aria-hidden="true"><circle cx="16" cy="14" r="12" fill="rgba(255,255,255,.25)"/><circle cx="28" cy="14" r="12" fill="rgba(56,189,248,.35)"/><text x="22" y="19" font-size="6" font-weight="800" fill="rgba(255,255,255,.8)" text-anchor="middle" font-family="system-ui,sans-serif">{mark}</text></svg>
      </div>
    </div>
  </div>

  <!-- KPI tile (repeat ×3) -->
  <div class="card" style="padding:18px 20px;display:flex;flex-direction:column;gap:10px">
    <div style="display:flex;align-items:center;justify-content:space-between">
      <span style="font-size:.65rem;font-weight:700;letter-spacing:.09em;text-transform:uppercase;color:var(--c-text-muted)">{METRIC NAME}</span>
      <!-- icon chip: kpi-icon-blue / kpi-icon-green / kpi-icon-red -->
      <div style="width:32px;height:32px;border-radius:8px;display:flex;align-items:center;justify-content:center;background:var(--c-blue-light);color:var(--c-blue)">
        <!-- inline SVG glyph -->
      </div>
    </div>
    <div class="tabnum" style="font-size:1.45rem;font-weight:700;color:var(--c-text-primary)">{figure}</div>
    <div style="display:flex;align-items:center;gap:6px">
      <!-- delta chip: green-light/green for up, red-light/red for down -->
      <span style="display:inline-flex;align-items:center;gap:3px;font-size:.75rem;font-weight:600;padding:2px 7px;border-radius:99px;background:var(--c-green-light);color:var(--c-green)">▲ {delta}</span>
      <span style="font-size:.75rem;color:var(--c-text-muted)">{period}</span>
    </div>
  </div>
  <!-- repeat 2 more KPI tiles -->

</div>
```

---

## 2-column content grid (left: chart + table | right: action panel + list)

```html
<div style="display:grid;grid-template-columns:2fr 1fr;gap:16px;align-items:start">

  <!-- Left column -->
  <div style="display:flex;flex-direction:column;gap:16px">
    <!-- Donut chart card (below) -->
    <!-- Records table card (below) -->
  </div>

  <!-- Right column -->
  <div style="display:flex;flex-direction:column;gap:16px">
    <!-- Quick-action panel (below) -->
    <!-- Scheduled items list (below) -->
  </div>

</div>
```

### Donut chart card

`[title + period-selector] [SVG donut] [legend: dot / label / amount / mini-bar / pct]`

```html
<div class="card">
  <div class="card-header">
    <span class="card-title">{Breakdown title}</span>
    <div style="display:flex;gap:4px">
      <button style="font-size:.75rem;font-weight:600;padding:4px 10px;border-radius:6px;border:none;background:var(--c-blue-light);color:var(--c-blue);cursor:pointer">This Period</button>
      <button style="font-size:.75rem;font-weight:600;padding:4px 10px;border-radius:6px;border:none;background:transparent;color:var(--c-text-muted);cursor:pointer">Prior</button>
    </div>
  </div>
  <div style="padding:16px 20px">
    <div style="display:flex;align-items:center;gap:24px">
      <!-- SVG donut: r=46, circ≈289, center=65. Each segment: stroke-dasharray="<arc> <rest>", stroke-dashoffset="-<cumulative>" -->
      <svg width="130" height="130" viewBox="0 0 130 130" aria-label="{Chart description}" role="img">
        <defs><style>.seg{fill:none;stroke-width:18;stroke-linecap:butt}</style></defs>
        <circle class="seg" cx="65" cy="65" r="46" stroke="var(--c-blue)"       stroke-dasharray="{arc1} {rest1}"  stroke-dashoffset="0"       transform="rotate(-90 65 65)"/>
        <circle class="seg" cx="65" cy="65" r="46" stroke="var(--c-teal)"       stroke-dasharray="{arc2} {rest2}"  stroke-dashoffset="-{cum2}" transform="rotate(-90 65 65)"/>
        <circle class="seg" cx="65" cy="65" r="46" stroke="var(--c-amber)"      stroke-dasharray="{arc3} {rest3}"  stroke-dashoffset="-{cum3}" transform="rotate(-90 65 65)"/>
        <!-- more segments; use --c-violet, --c-rose, --c-text-faint -->
        <text x="65" y="61" text-anchor="middle" font-size="11" font-weight="700" fill="var(--c-text-muted)" font-family="system-ui,sans-serif">{center-label}</text>
        <text x="65" y="76" text-anchor="middle" font-size="13" font-weight="800" fill="var(--c-navy)"       font-family="system-ui,sans-serif" font-variant-numeric="tabular-nums">{center-value}</text>
      </svg>
      <!-- Legend -->
      <div style="display:flex;flex-direction:column;gap:8px;flex:1">
        <!-- Repeat per segment -->
        <div style="display:flex;align-items:center;gap:8px">
          <div style="width:10px;height:10px;border-radius:50%;background:var(--c-blue);flex-shrink:0"></div>
          <span style="font-size:.8rem;flex:1;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">{Category}</span>
          <span class="tabnum" style="font-size:.8rem;font-weight:600;white-space:nowrap">{amount}</span>
          <div style="flex:1;max-width:60px;height:4px;background:var(--c-border);border-radius:99px;overflow:hidden"><div style="height:100%;border-radius:99px;width:{pct}%;background:var(--c-blue)"></div></div>
          <span style="font-size:.72rem;color:var(--c-text-muted);min-width:32px;text-align:right">{pct}%</span>
        </div>
      </div>
    </div>
  </div>
</div>
```

### Records table card (dashboard footer)

```html
<div class="card">
  <div class="card-header" style="padding-bottom:12px">
    <span class="card-title">{Records title}</span>
    <a href="#" class="card-action">View all</a>
  </div>
  <table class="rec-table">
    <thead>
      <tr><th>{Date}</th><th>{Primary entity}</th><th>{Category}</th><th class="num">{Amount}</th><th>Status</th></tr>
    </thead>
    <tbody>
      <tr>
        <td style="color:var(--c-text-muted);white-space:nowrap">{date}</td>
        <td>
          <div style="display:flex;align-items:center;gap:10px">
            <div style="width:32px;height:32px;border-radius:8px;background:var(--c-teal-light);color:var(--c-teal);display:flex;align-items:center;justify-content:center;flex-shrink:0;font-size:.85rem">{icon}</div>
            <div><div style="font-weight:600">{Entity name}</div><div style="font-size:.72rem;color:var(--c-text-muted)">{sub-label}</div></div>
          </div>
        </td>
        <td><span class="chip chip-teal">{Category}</span></td>
        <td class="tabnum amt-debit" style="text-align:right">−${amount}</td>
        <td><span class="s-pill s-completed"><span class="s-dot"></span>Completed</span></td>
      </tr>
      <!-- status variants: s-completed / s-pending / s-failed -->
    </tbody>
  </table>
</div>
```

---

## Records list (list screen)

```html
<!-- Toolbar above the table card -->
<div style="display:flex;align-items:center;gap:12px;flex-wrap:wrap;margin-bottom:16px">
  <div style="position:relative;flex:1;max-width:320px">
    <!-- magnifier icon at left:11px -->
    <input type="text" placeholder="Filter by {fields}…"
      style="width:100%;height:36px;border:1px solid var(--c-border);border-radius:8px;padding:0 12px 0 36px;font-size:.84rem;background:var(--c-surface);outline:none">
  </div>
  <div style="display:flex;align-items:center;gap:6px;flex-wrap:wrap">
    <span style="font-size:.72rem;font-weight:600;color:var(--c-text-muted)">{Facet}</span>
    <span style="display:inline-flex;align-items:center;gap:4px;padding:4px 10px;border-radius:99px;font-size:.75rem;font-weight:600;cursor:pointer;border:1px solid var(--c-blue);background:var(--c-blue-light);color:var(--c-blue)">All <span style="background:rgba(37,99,235,.15);color:var(--c-blue);padding:1px 5px;border-radius:99px;font-size:.68rem">{n}</span></span>
    <span style="display:inline-flex;align-items:center;gap:4px;padding:4px 10px;border-radius:99px;font-size:.75rem;font-weight:600;cursor:pointer;border:1px solid var(--c-border);background:var(--c-surface);color:var(--c-text-muted)">{Value}</span>
  </div>
</div>

<div class="card">
  <!-- rec-table with ID column prepended -->
  <table class="rec-table">
    <thead>
      <tr><th>ID</th><th>{Date}</th><th>{Entity}</th><th>{Category}</th><th class="num">{Amount}</th><th>Status</th></tr>
    </thead>
    <tbody>
      <tr>
        <td><span class="rec-id">{ID}</span></td>
        <td style="color:var(--c-text-muted);white-space:nowrap">{date}</td>
        <td><!-- entity cell --></td>
        <td><!-- chip --></td>
        <td class="tabnum amt-debit" style="text-align:right">−${amount}</td>
        <td><!-- status pill --></td>
      </tr>
    </tbody>
  </table>
  <div class="rec-footer">
    <span class="rec-count">Showing {a}–{b} of {n}</span>
    <div class="pagination">
      <button class="page-btn">‹</button>
      <button class="page-btn active">1</button>
      <button class="page-btn">2</button>
      <button class="page-btn">›</button>
    </div>
  </div>
</div>
```

---

## Record form — inline validation (NO separate rules panel)

Rules live ON the field: required mark (`*`), helper text below, inline
error on the invalid field. Submit stays `disabled` until valid. Never
add a rules/checklist/validation-status panel.

```html
<form novalidate>

  <div class="card" style="margin-bottom:16px">
    <div style="display:flex;align-items:center;gap:8px;padding:16px 20px;border-bottom:1px solid var(--c-border);font-size:.82rem;font-weight:700;color:var(--c-text-muted);text-transform:uppercase;letter-spacing:.05em">
      <!-- section icon -->
      {Section title}
    </div>
    <div style="padding:20px">
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px 20px">

        <!-- Valid field -->
        <div class="field">
          <label class="field-label" for="f1">{Label} <span class="req">*</span></label>
          <input id="f1" class="control" type="text" value="{value}">
          <span class="helper">{format hint / constraint}</span>
        </div>

        <!-- Invalid field — add .invalid on .field, show .error-msg -->
        <div class="field invalid">
          <label class="field-label" for="f2">{Label} <span class="req">*</span></label>
          <input id="f2" class="control" type="text" aria-invalid="true" aria-describedby="err-f2">
          <span class="error-msg" id="err-f2">
            <svg width="12" height="12" viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><circle cx="6" cy="6" r="5"/><path d="M6 4v2.5M6 8.3v.2" stroke-linecap="round"/></svg>
            {Specific rule that failed}
          </span>
        </div>

        <!-- Required select -->
        <div class="field">
          <label class="field-label" for="f3">{Label} <span class="req">*</span></label>
          <select id="f3" class="control"><option value="">Select…</option></select>
          <span class="helper">{constraint on options}</span>
        </div>

        <!-- Amount with prefix -->
        <div class="field">
          <label class="field-label" for="f4">{Amount label} <span class="req">*</span></label>
          <div style="position:relative">
            <span style="position:absolute;left:12px;top:50%;transform:translateY(-50%);font-size:.9rem;font-weight:600;color:var(--c-text-muted);pointer-events:none">$</span>
            <input id="f4" class="control tabnum" type="number" style="padding-left:26px" min="0.01" step="0.01" placeholder="0.00">
          </div>
          <span class="helper">Must be greater than $0.00.</span>
        </div>

      </div>
    </div>
  </div>

  <div class="card">
    <div style="display:flex;align-items:center;justify-content:space-between;padding:16px 20px;background:var(--c-canvas);border-top:1px solid var(--c-border)">
      <span style="font-size:.78rem;color:var(--c-text-muted)">Fields marked <span class="req">*</span> are required.</span>
      <div style="display:flex;gap:8px">
        <button type="button" class="btn btn-ghost">Cancel</button>
        <button type="submit" class="btn btn-primary" disabled>{Submit action}</button>
      </div>
    </div>
  </div>

</form>
```

---

## Record detail — breadcrumb + header + meta grid + related panels

```html
<div style="font-size:.8rem;color:var(--c-text-muted)"><a href="#" style="color:var(--c-blue);text-decoration:none">{Parent}</a> › {ID}</div>

<div style="display:flex;align-items:flex-start;justify-content:space-between;gap:16px;margin-top:16px">
  <div>
    <div style="display:flex;align-items:center;gap:10px;margin-bottom:4px">
      <span style="font-family:'Courier New',monospace;font-size:1rem;font-weight:700;font-variant-numeric:tabular-nums">{ID}</span>
      <span class="s-pill s-completed"><span class="s-dot"></span>{State}</span>
    </div>
    <div style="font-size:.9rem;color:var(--c-text-muted)">{Entity name · sub-label · date}</div>
  </div>
  <div style="display:flex;gap:8px;flex-shrink:0">
    <button class="btn btn-ghost">{Secondary action}</button>
    <button class="btn btn-primary">Edit</button>
  </div>
</div>

<!-- Meta grid: 3 columns of label/value pairs -->
<div class="card" style="margin-top:16px">
  <div style="display:grid;grid-template-columns:repeat(3,1fr);padding:20px;gap:20px">
    <div>
      <div style="font-size:.65rem;font-weight:700;text-transform:uppercase;letter-spacing:.07em;color:var(--c-text-muted)">{FIELD A}</div>
      <div class="tabnum" style="font-size:.9rem;font-weight:600;margin-top:2px">{value}</div>
      <div style="font-size:.75rem;color:var(--c-text-muted)">{sub}</div>
    </div>
    <!-- repeat cells -->
  </div>
</div>

<!-- 7fr / 5fr related panels -->
<div style="display:grid;grid-template-columns:7fr 5fr;gap:16px;align-items:start;margin-top:16px">
  <div class="card"><!-- mini-table of related records --></div>
  <div class="card"><!-- activity timeline --></div>
</div>
```

---

## Quick-action panel (right-column card)

```html
<div class="card">
  <div class="card-header" style="padding-bottom:14px">
    <span class="card-title">{Action panel title}</span>
    <a href="#" class="card-action">{View all link}</a>
  </div>
  <!-- Payee / recipient avatar row -->
  <div style="padding:0 20px 12px;display:flex;gap:10px;overflow-x:auto;scrollbar-width:none">
    <div style="display:flex;flex-direction:column;align-items:center;gap:5px;cursor:pointer;min-width:52px">
      <div style="width:44px;height:44px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:.85rem;font-weight:700;color:#fff;background:linear-gradient(135deg,var(--c-blue),var(--c-teal));border:2px solid var(--c-teal);box-shadow:0 0 0 3px var(--c-teal-light)">{XX}</div>
      <span style="font-size:.7rem;color:var(--c-text-muted);white-space:nowrap">{Name}</span>
    </div>
    <!-- more recipients -->
  </div>
  <!-- Amount input with prefix -->
  <div style="padding:0 20px 16px;display:flex;flex-direction:column;gap:10px">
    <div>
      <label style="font-size:.72rem;font-weight:600;color:var(--c-text-muted);display:block;margin-bottom:3px">Amount</label>
      <div style="position:relative">
        <span style="position:absolute;left:12px;top:50%;transform:translateY(-50%);font-size:.9rem;font-weight:600;color:var(--c-text-muted);pointer-events:none">$</span>
        <input class="tabnum" type="text" placeholder="0.00"
          style="width:100%;height:38px;border:1px solid var(--c-border);border-radius:8px;padding:0 12px 0 28px;font-size:.9rem;font-weight:600;background:var(--c-canvas);outline:none">
      </div>
    </div>
    <div>
      <label style="font-size:.72rem;font-weight:600;color:var(--c-text-muted);display:block;margin-bottom:3px">Note (optional)</label>
      <input type="text" placeholder="e.g. {note placeholder}"
        style="width:100%;height:38px;border:1px solid var(--c-border);border-radius:8px;padding:0 12px;font-size:.85rem;background:var(--c-canvas);outline:none">
    </div>
    <button class="btn btn-teal" style="height:40px;border-radius:8px;border:none;background:var(--c-teal);color:#fff;font-size:.85rem;font-weight:700;cursor:pointer;display:flex;align-items:center;justify-content:center;gap:8px">
      <svg width="15" height="15" viewBox="0 0 15 15" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M2 7.5h11M8.5 3l4.5 4.5L8.5 12" stroke-linecap="round" stroke-linejoin="round"/></svg>
      {CTA label}
    </button>
  </div>
</div>
```

---

## Scheduled items list (right-column card)

```html
<div class="card">
  <div class="card-header" style="padding-bottom:4px">
    <span class="card-title">{Upcoming items title}</span>
    <a href="#" class="card-action">See all</a>
  </div>
  <div style="padding:0 20px 16px;display:flex;flex-direction:column">
    <div style="display:flex;align-items:center;gap:10px;padding:10px 0;border-bottom:1px solid var(--c-border)">
      <div style="width:34px;height:34px;border-radius:8px;background:var(--c-blue-light);color:var(--c-blue);display:flex;align-items:center;justify-content:center;font-size:.9rem;flex-shrink:0">{icon}</div>
      <div style="flex:1;min-width:0">
        <div style="font-size:.82rem;font-weight:600">{Item name}</div>
        <div style="font-size:.72rem;color:var(--c-text-muted)">{Due date}</div>
      </div>
      <div class="tabnum" style="font-size:.82rem;font-weight:700;white-space:nowrap">{amount}</div>
    </div>
    <!-- more items; last item: border-bottom:none -->
  </div>
</div>
```
