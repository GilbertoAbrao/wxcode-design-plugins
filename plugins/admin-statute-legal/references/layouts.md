# Statute Admin — layout skeletons

Paste-ready, domain-neutral fragments for the Statute warm-white / burgundy-gold
professional skin. Each skeleton is labelled by archetype slot, not by a domain
noun. Copy the shell from `assets/template.html` first (it carries the `:root`
tokens + sidebar + topbar + `.page-body` slot), then drop the region skeletons
below into `<div class="page-body">`. Replace every placeholder label with the
real domain's equivalent.

Token recap (full block in `template.html`):
- Canvas `#faf8f6`; raised card `#ffffff`; border `#e8e2dc`; inner row `#f4f0ec`.
- Sidebar `#1e1714` / hover `#2d2420` / active `#3a2820`.
- Text: headings `#1e293b` / body `#334155` / muted `#64748b`.
- Accent (burgundy): `var(--clr-accent)` = `#9f1239`; hi `#be123c`; subtle `#fdf2f4`; muted `#fce7eb`.
- Gold: `var(--clr-gold)` = `#b45309`; hi `#d97706`.
- Status tokens: `--status-active-*`, `--status-pending-*`, `--status-closed-*`, `--status-urgent-*`.
- Mono IDs: `ui-monospace, "Cascadia Code", "Fira Code", monospace`.
- Put `font-variant-numeric: tabular-nums` on every numeric cell.

---

## Page header strip (every screen)

```html
<div class="page-strip" style="display:flex;align-items:center;gap:12px;margin-bottom:22px;flex-wrap:wrap">
  <div style="font-size:13px;color:#64748b">{date · context}</div>
  <span class="summary-chip" style="display:inline-flex;align-items:center;gap:5px;background:var(--delta-up-bg);color:var(--delta-up-fg);font-size:12px;font-weight:600;padding:3px 10px;border-radius:20px">
    <svg width="12" height="12" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
    {Key metric summary}
  </span>
  <div style="display:flex;gap:8px;margin-left:auto">
    <button class="btn-ghost">Export CSV</button>
    <button class="btn-primary">+ {Primary action}</button>
  </div>
</div>
```

---

## KPI tile (repeat ×4 in a 4-column grid)

```html
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-bottom:22px">

  <!-- Burgundy accent tile -->
  <div class="kpi-card" style="background:#fff;border:1px solid #e8e2dc;border-radius:10px;padding:18px 18px 16px;box-shadow:0 2px 8px rgba(0,0,0,0.05);position:relative;overflow:hidden">
    <div style="position:absolute;top:0;left:0;width:100%;height:3px;background:var(--clr-accent);border-radius:10px 10px 0 0"></div>
    <div style="position:absolute;top:16px;right:16px;opacity:0.15">
      <!-- inline SVG glyph, stroke=var(--clr-accent) -->
    </div>
    <div style="font-size:11px;font-weight:500;color:#64748b;letter-spacing:0.06em;text-transform:uppercase;margin-bottom:8px">{METRIC LABEL}</div>
    <div style="font-size:30px;font-weight:700;color:#1e293b;line-height:1;margin-bottom:10px;font-variant-numeric:tabular-nums">{figure}</div>
    <div style="font-size:12px;color:#64748b;display:flex;align-items:center;gap:6px">
      <span style="display:inline-flex;align-items:center;gap:3px;font-size:11px;font-weight:600;padding:2px 7px;border-radius:10px;background:var(--delta-up-bg);color:var(--delta-up-fg)">
        ▲ {delta}
      </span>
      {vs context}
    </div>
  </div>

  <!-- Gold accent tile (add class="gold" or change the ::before color) -->
  <div class="kpi-card" style="background:#fff;border:1px solid #e8e2dc;border-radius:10px;padding:18px 18px 16px;box-shadow:0 2px 8px rgba(0,0,0,0.05);position:relative;overflow:hidden">
    <div style="position:absolute;top:0;left:0;width:100%;height:3px;background:var(--clr-gold);border-radius:10px 10px 0 0"></div>
    <div style="font-size:11px;font-weight:500;color:#64748b;letter-spacing:0.06em;text-transform:uppercase;margin-bottom:8px">{METRIC LABEL}</div>
    <div style="font-size:30px;font-weight:700;color:#1e293b;line-height:1;margin-bottom:10px;font-variant-numeric:tabular-nums">{figure}</div>
    <div style="font-size:13px;color:#64748b">{target / context}</div>
    <!-- progress bar (optional) -->
    <div style="height:5px;background:#e8e2dc;border-radius:3px;margin-top:8px;overflow:hidden">
      <div style="height:100%;border-radius:3px;background:var(--clr-gold);width:{pct}%"></div>
    </div>
  </div>

  <!-- 2 more tiles -->
</div>
```

---

## Two-column grid (records table + right panel)

```html
<div style="display:grid;grid-template-columns:1fr 320px;gap:16px;margin-bottom:16px">

  <!-- LEFT: records table card -->
  <div class="card">
    <div class="card-header" style="display:flex;align-items:center;justify-content:space-between;padding:16px 20px;border-bottom:1px solid #e8e2dc">
      <div style="font-size:14px;font-weight:600;color:#1e293b">{Table title}</div>
      <a href="#" style="font-size:12px;color:var(--clr-accent);text-decoration:none;font-weight:500">View all →</a>
    </div>
    <table style="width:100%;border-collapse:collapse">
      <thead>
        <tr>
          <th style="font-size:11px;font-weight:500;color:#64748b;letter-spacing:0.05em;text-transform:uppercase;padding:10px 16px;text-align:left;background:#faf8f6;border-bottom:1px solid #e8e2dc">{ID}</th>
          <th style="...">{Entity / Name}</th>
          <th style="...">{Category}</th>
          <th style="...">{Assigned}</th>
          <th style="...">Status</th>
          <th style="..."></th>
        </tr>
      </thead>
      <tbody>
        <tr style="border-bottom:1px solid #f4f0ec">
          <td style="padding:11px 16px;font-size:13px;color:#334155;vertical-align:middle">
            <span style="font-family:ui-monospace,monospace;font-size:12px;color:var(--clr-accent);font-weight:600">{ID}</span>
          </td>
          <td style="..."><span style="font-weight:500;color:#1e293b">{Name}</span></td>
          <td style="...">{category}</td>
          <td style="...">
            <div style="display:flex;align-items:center;gap:7px">
              <div style="width:22px;height:22px;border-radius:50%;background:{color};display:flex;align-items:center;justify-content:center;font-size:10px;font-weight:700;color:#fff">{XX}</div>
              {Name}
            </div>
          </td>
          <td style="..."><span class="pill pill-active"><span class="pill-dot"></span>{State}</span></td>
          <td style="..."><a href="#" style="font-size:12px;color:var(--clr-accent);font-weight:500">Open</a></td>
        </tr>
        <!-- more rows; pill variants: .pill-active .pill-pending .pill-closed .pill-urgent -->
      </tbody>
    </table>
  </div>

  <!-- RIGHT: stacked panels -->
  <div style="display:flex;flex-direction:column;gap:16px">

    <!-- Deadline / events feed card -->
    <div class="card">
      <div class="card-header" style="display:flex;align-items:center;justify-content:space-between;padding:16px 20px;border-bottom:1px solid #e8e2dc">
        <div style="font-size:14px;font-weight:600;color:#1e293b">{Feed title}</div>
        <a href="#" style="font-size:12px;color:var(--clr-accent);font-weight:500">{link}</a>
      </div>
      <div>
        <!-- Feed row: urgency dot → mono ref → description → date -->
        <div style="display:flex;align-items:flex-start;gap:10px;padding:10px 16px;border-bottom:1px solid #f4f0ec">
          <div style="width:8px;height:8px;border-radius:50%;flex-shrink:0;margin-top:4px;background:var(--dot-urgent)"></div>  <!-- .dot-urgent / .dot-warn / .dot-ok -->
          <div>
            <div style="font-size:11px;font-weight:600;color:var(--clr-accent);font-family:ui-monospace,monospace">{REF-ID}</div>
            <div style="font-size:12px;color:#334155;font-weight:500;margin-top:1px">{description}</div>
            <div style="font-size:11px;color:#64748b;margin-top:1px">{date}</div>
          </div>
        </div>
        <!-- more rows -->
      </div>
    </div>

    <!-- Distribution bar chart card -->
    <div class="card">
      <div class="card-header" style="display:flex;align-items:center;justify-content:space-between;padding:16px 20px;border-bottom:1px solid #e8e2dc">
        <div style="font-size:14px;font-weight:600;color:#1e293b">{Chart title}</div>
      </div>
      <div style="padding:16px 20px">
        <!-- Bar row: label → track → count inside bar -->
        <div style="display:flex;align-items:center;gap:8px;margin-bottom:10px">
          <div style="width:80px;font-size:11px;color:#64748b;text-align:right;flex-shrink:0">{Label}</div>
          <div style="flex:1;height:18px;background:#f4f0ec;border-radius:4px;overflow:hidden">
            <div style="height:100%;border-radius:4px;background:var(--clr-accent);width:{pct}%;display:flex;align-items:center;justify-content:flex-end;padding-right:7px">
              <span style="font-size:11px;font-weight:700;color:#fff">{count}</span>
            </div>
          </div>
        </div>
        <!-- alternate rows with background:var(--clr-gold) for the gold variant -->
      </div>
    </div>

  </div>
</div>
```

---

## Full-width documents / items list

```html
<div class="card">
  <div class="card-header" style="display:flex;align-items:center;justify-content:space-between;padding:16px 20px;border-bottom:1px solid #e8e2dc">
    <div style="font-size:14px;font-weight:600;color:#1e293b">{List title}</div>
    <a href="#" style="font-size:12px;color:var(--clr-accent);font-weight:500">{link} →</a>
  </div>
  <div>
    <!-- Item row: icon chip → title + meta → date + ghost action -->
    <div style="display:flex;align-items:center;gap:12px;padding:11px 20px;border-bottom:1px solid #f4f0ec;transition:background 0.12s">
      <div style="width:32px;height:32px;background:var(--clr-accent-subtle);border-radius:8px;display:flex;align-items:center;justify-content:center;flex-shrink:0;color:var(--clr-accent)">
        <!-- inline SVG doc icon -->
      </div>
      <div>
        <div style="font-size:13px;font-weight:500;color:#1e293b;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;max-width:260px">{Title}</div>
        <div style="font-size:11px;color:#64748b;margin-top:1px">
          Ref <a href="#" style="color:var(--clr-accent);text-decoration:none;font-weight:500">{ID}</a> &nbsp;·&nbsp; {Author}
        </div>
      </div>
      <div style="margin-left:auto;display:flex;align-items:center;gap:16px;flex-shrink:0">
        <div style="font-size:12px;color:#64748b;white-space:nowrap">{date}</div>
        <a href="#" style="font-size:12px;font-weight:500;color:var(--clr-accent);text-decoration:none;padding:4px 10px;border:1px solid var(--clr-accent-muted);border-radius:6px">View</a>
      </div>
    </div>
    <!-- more rows -->
  </div>
</div>
```

---

## List toolbar (search + filter chips)

```html
<div style="display:flex;align-items:center;gap:12px;margin-bottom:18px;flex-wrap:wrap">
  <div style="display:flex;align-items:center;gap:8px;background:#fff;border:1px solid #e8e2dc;border-radius:8px;padding:8px 14px;flex:1;max-width:360px">
    <!-- magnifier SVG -->
    <input type="text" placeholder="Filter by {fields}…" style="background:transparent;border:none;outline:none;color:#334155;font-size:13px;width:100%;font-family:inherit">
  </div>
  <div style="display:flex;align-items:center;gap:8px;flex-wrap:wrap">
    <span style="font-size:12px;color:#64748b;font-weight:500">{Facet}:</span>
    <!-- active chip -->
    <span style="display:inline-flex;align-items:center;gap:5px;padding:5px 12px;border-radius:20px;font-size:12px;font-weight:600;color:var(--clr-accent);background:var(--clr-accent-subtle);border:1px solid var(--clr-accent-muted);cursor:pointer">
      All <span style="font-size:11px;font-weight:600;background:var(--clr-accent);color:#fff;padding:0 5px;border-radius:8px">{n}</span>
    </span>
    <!-- inactive chip -->
    <span style="display:inline-flex;align-items:center;gap:5px;padding:5px 12px;border-radius:20px;font-size:12px;font-weight:500;color:#64748b;background:#fff;border:1px solid #e8e2dc;cursor:pointer">
      {Value} <span style="font-size:11px;font-weight:600;background:var(--clr-accent-muted);color:var(--clr-accent);padding:0 5px;border-radius:8px">{n}</span>
    </span>
  </div>
  <div style="font-size:13px;color:#64748b;margin-left:auto">{n} records</div>
</div>
```

---

## Record form — fields with inline validation

Rules live ON the field: required mark (`*`), helper text, inline error on invalid.
The submit stays `disabled` until the form is valid. Never render a separate
rules/validation-status summary panel.

```html
<form style="display:flex;flex-direction:column;gap:18px;max-width:860px" novalidate>

  <div class="card">
    <div style="display:flex;align-items:center;gap:8px;padding:14px 20px;border-bottom:1px solid #e8e2dc;font-size:13px;font-weight:600;color:#1e293b">
      <!-- section icon SVG, color:var(--clr-accent) -->
      {Section title}
    </div>
    <div style="padding:20px">
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px">

        <!-- valid field -->
        <div style="display:flex;flex-direction:column;gap:5px">
          <label style="font-size:13px;font-weight:500;color:#1e293b" for="f1">
            {Label} <span style="color:var(--clr-accent);margin-left:2px">*</span>
          </label>
          <input id="f1" style="width:100%;border:1px solid #e8e2dc;border-radius:7px;background:#fff;padding:8px 12px;font-size:13px;color:#334155;font-family:inherit;outline:none" type="text" value="">
          <span style="font-size:11px;color:#64748b">{format hint / constraint}</span>
        </div>

        <!-- invalid field — add border-color:var(--clr-accent-hi) + box-shadow on input -->
        <div style="display:flex;flex-direction:column;gap:5px">
          <label style="font-size:13px;font-weight:500;color:#1e293b" for="f2">
            {Label} <span style="color:var(--clr-accent);margin-left:2px">*</span>
          </label>
          <input id="f2" style="width:100%;border:1px solid var(--clr-accent-hi);border-radius:7px;background:#fff;padding:8px 12px;font-size:13px;color:#334155;font-family:inherit;outline:none;box-shadow:0 0 0 3px var(--clr-accent-muted)" type="text" aria-invalid="true">
          <span style="display:flex;align-items:center;gap:4px;font-size:11px;font-weight:500;color:var(--clr-accent-hi)">
            <!-- alert icon -->
            {Specific rule that failed}
          </span>
        </div>

        <!-- required select -->
        <div style="display:flex;flex-direction:column;gap:5px">
          <label style="font-size:13px;font-weight:500;color:#1e293b" for="f3">
            {Label} <span style="color:var(--clr-accent);margin-left:2px">*</span>
          </label>
          <select id="f3" style="width:100%;border:1px solid #e8e2dc;border-radius:7px;background:#fff;padding:8px 12px;font-size:13px;color:#334155;font-family:inherit;outline:none;cursor:pointer">
            <option value="">Select…</option>
            <option>{Option A}</option>
          </select>
          <span style="font-size:11px;color:#64748b">{constraint on the options}</span>
        </div>

      </div>
    </div>
  </div>

  <!-- more sections -->

  <div style="display:flex;align-items:center;justify-content:space-between;padding:16px 0 0">
    <span style="font-size:12px;color:#64748b">Fields marked <span style="color:var(--clr-accent);font-weight:600">*</span> are required.</span>
    <div style="display:flex;gap:10px">
      <button type="button" class="btn-ghost">Cancel</button>
      <button type="submit" class="btn-primary" disabled>{Submit}</button>
    </div>
  </div>

</form>
```

---

## Record detail — header band + meta grid + two-column sub-panels

```html
<div style="display:flex;flex-direction:column;gap:18px">

  <!-- breadcrumb (topbar slot) -->
  <div style="font-size:13px;color:#64748b">
    <a href="#" style="color:var(--clr-accent);text-decoration:none;font-weight:500">{Parent}</a> &rsaquo;
    <a href="#" style="color:var(--clr-accent);text-decoration:none;font-weight:500">{List}</a> &rsaquo;
    {ID}
  </div>

  <!-- header band: ID + status + title + actions -->
  <div class="card" style="padding:20px 24px;display:flex;align-items:center;justify-content:space-between">
    <div>
      <div style="display:flex;align-items:center;gap:12px">
        <span style="font-family:ui-monospace,monospace;font-size:15px;font-weight:700;color:var(--clr-accent)">{ID}</span>
        <span class="pill pill-active"><span class="pill-dot"></span>{State}</span>
      </div>
      <div style="font-size:18px;font-weight:700;color:#1e293b;margin-top:6px">{Title}</div>
      <div style="font-size:13px;color:#64748b;margin-top:2px">{category · date · due}</div>
    </div>
    <div style="display:flex;gap:8px">
      <button class="btn-ghost">{Secondary}</button>
      <button class="btn-primary">Edit</button>
    </div>
  </div>

  <!-- meta grid: 3-col label/value -->
  <div class="card">
    <div style="display:grid;grid-template-columns:repeat(3,1fr)">
      <div style="padding:16px 20px;border-right:1px solid #e8e2dc;border-bottom:1px solid #e8e2dc">
        <div style="font-size:10px;font-weight:500;color:#64748b;letter-spacing:0.07em;text-transform:uppercase;margin-bottom:5px">{FIELD}</div>
        <div style="font-size:14px;font-weight:600;color:#1e293b;font-variant-numeric:tabular-nums">{value}</div>
        <div style="font-size:11px;color:#64748b;margin-top:2px">{sub}</div>
      </div>
      <!-- more cells; last in row has no border-right; last row has no border-bottom -->
    </div>
  </div>

  <!-- two-column: related sub-table (7fr) + activity feed (5fr) -->
  <div style="display:grid;grid-template-columns:7fr 5fr;gap:18px">
    <div class="card"><!-- sub-table or operations rows --></div>
    <div class="card"><!-- activity / history feed --></div>
  </div>

</div>
```

---

## Pager (table footer)

```html
<div style="display:flex;align-items:center;justify-content:space-between;padding:12px 20px;border-top:1px solid #e8e2dc;font-size:13px;color:#64748b">
  <span>Showing {a}–{b} of {n}</span>
  <div style="display:flex;gap:4px">
    <button style="width:32px;height:32px;border-radius:7px;border:1px solid #e8e2dc;background:#fff;font-size:13px;color:#64748b;cursor:pointer">‹</button>
    <button style="width:32px;height:32px;border-radius:7px;border:1px solid var(--clr-accent);background:var(--clr-accent);font-size:13px;color:#fff;font-weight:600;cursor:pointer">1</button>
    <button style="width:32px;height:32px;border-radius:7px;border:1px solid #e8e2dc;background:#fff;font-size:13px;color:#64748b;cursor:pointer">2</button>
    <button style="...">›</button>
  </div>
</div>
```
