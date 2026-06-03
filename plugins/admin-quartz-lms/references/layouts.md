# Quartz Admin — layout skeletons

Paste-ready, domain-neutral fragments for the Quartz light-mode / purple-accent
skin. Each skeleton is labelled by archetype slot, not by a domain noun. Copy the
shell from `assets/template.html` first (it carries the `:root` tokens + sidebar
+ topbar + main slot), then drop the region skeletons below into
`<main class="page-body">`. Replace every `{placeholder}` with the real domain's
equivalent.

Token recap (full block in `template.html`): canvas `#faf9fc`, card `#ffffff`,
border `#ebe7f1`; text `#1e293b / #475569 / #94a3b8`; accent `var(--accent)` =
`#9333ea`; status tokens `--state-active/draft/arch-*`; category color ramp
`--clr-cat-*` with `*-bg` tints. Put `font-variant-numeric: tabular-nums` on all
numeric cells.

---

## Greeting strip (dashboard)

```html
<div style="display:flex;align-items:flex-end;justify-content:space-between;margin-bottom:22px;gap:12px;flex-wrap:wrap;">
  <div>
    <h1 style="font-size:20px;font-weight:700;letter-spacing:-.3px">{Welcome heading}</h1>
    <p style="font-size:13px;color:var(--text-400);margin-top:2px">{date · context sub-line}</p>
  </div>
  <div style="display:flex;gap:10px;">
    <button class="btn-ghost">{Secondary action}</button>
    <button class="btn-primary">+ {Primary action}</button>
  </div>
</div>
```

---

## KPI tile row (repeat ×4 in a grid)

```html
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-bottom:22px;">
  <div class="card" style="padding:18px 18px 14px;display:flex;flex-direction:column;gap:10px;">
    <div style="display:flex;align-items:flex-start;justify-content:space-between;">
      <div style="font-size:10.5px;text-transform:uppercase;letter-spacing:.7px;font-weight:700;color:var(--text-400)">{METRIC NAME}</div>
      <div style="width:32px;height:32px;border-radius:8px;background:var(--accent-dim);color:var(--accent);display:flex;align-items:center;justify-content:center;">
        <!-- icon SVG here -->
      </div>
    </div>
    <div style="font-size:26px;font-weight:800;letter-spacing:-.5px;line-height:1;font-variant-numeric:tabular-nums">{Big figure}</div>
    <div style="display:flex;align-items:center;justify-content:space-between;gap:8px;">
      <!-- Delta chip: .up = green, .dn = red -->
      <span class="kpi-delta up">▲ {delta}</span>
      <!-- Inline SVG sparkline or donut (22×22 for donut) -->
    </div>
  </div>
  <!-- 3 more tiles; swap icon chip color class: c-purple / c-teal / c-green / c-blue -->
</div>
```

---

## Two-column grid (chart + side panel)

```html
<div style="display:grid;grid-template-columns:1fr 320px;gap:18px;margin-bottom:22px;">
  <div class="card"><!-- Dual-line area chart (see below) --></div>
  <div class="card"><!-- Upcoming-items panel (see below) --></div>
</div>
```

### Dual-line area chart card

```html
<div class="card">
  <div class="card-header">
    <div>
      <div class="card-title">{Primary line} vs {Secondary line}</div>
      <div class="card-subtitle">{scope description}</div>
    </div>
    <div style="display:flex;gap:4px;background:var(--surface);border:1px solid var(--border);border-radius:8px;padding:3px;">
      <button style="padding:5px 12px;border-radius:6px;border:none;background:none;font-size:12px;font-weight:500;color:var(--text-400);font-family:inherit;cursor:pointer;">{Period A}</button>
      <button style="padding:5px 12px;border-radius:6px;border:none;background:var(--card);font-size:12px;font-weight:600;color:var(--accent-deep);font-family:inherit;cursor:pointer;box-shadow:0 1px 3px rgba(0,0,0,.08);">{Period B} (active)</button>
      <button style="padding:5px 12px;border-radius:6px;border:none;background:none;font-size:12px;font-weight:500;color:var(--text-400);font-family:inherit;cursor:pointer;">{Period C}</button>
    </div>
  </div>
  <div class="card-body">
    <!-- Legend -->
    <div style="display:flex;gap:18px;margin-bottom:12px;">
      <div style="display:flex;align-items:center;gap:6px;font-size:12px;color:var(--text-600);">
        <span style="width:8px;height:8px;border-radius:50%;background:var(--accent-light);display:inline-block;"></span>{Primary label}
      </div>
      <div style="display:flex;align-items:center;gap:6px;font-size:12px;color:var(--text-600);">
        <span style="width:8px;height:8px;border-radius:50%;background:var(--clr-teal-600);display:inline-block;"></span>{Secondary label}
      </div>
    </div>
    <!-- SVG chart — dual area+line, dashed gridlines, labeled axes -->
    <svg viewBox="0 0 600 180" xmlns="http://www.w3.org/2000/svg" style="width:100%;display:block;" aria-label="{description}" role="img">
      <defs>
        <linearGradient id="g-a" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stop-color="var(--accent-light)" stop-opacity=".22"/>
          <stop offset="100%" stop-color="var(--accent-light)" stop-opacity="0"/>
        </linearGradient>
        <linearGradient id="g-b" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stop-color="var(--clr-teal-600)" stop-opacity=".18"/>
          <stop offset="100%" stop-color="var(--clr-teal-600)" stop-opacity="0"/>
        </linearGradient>
      </defs>
      <!-- Gridlines: horizontal dashed at 20/55/90/125, solid baseline at 160 -->
      <line x1="50" y1="160" x2="590" y2="160" stroke="var(--border)" stroke-width="1"/>
      <!-- Y-axis labels (text-anchor="end") and X-axis labels (text-anchor="middle") -->
      <!-- Area fill A then line A (stroke var(--accent-light)) -->
      <!-- Area fill B then line B (stroke var(--clr-teal-600)) -->
      <!-- End-point dots for both lines -->
    </svg>
  </div>
</div>
```

### Upcoming-items panel

`[category dot] [title + parent + tag pill] [due date + urgency]`

```html
<div class="card">
  <div class="card-header">
    <div>
      <div class="card-title">{Panel title}</div>
      <div class="card-subtitle">{scope, e.g. "Next 7 days"}</div>
    </div>
    <a href="#" class="view-all">View all</a>
  </div>
  <!-- Rows — no wrapper div needed, items stack directly -->
  <div style="display:flex;align-items:flex-start;gap:12px;padding:13px 20px;border-bottom:1px solid var(--border);">
    <span style="width:8px;height:8px;border-radius:50%;background:var(--clr-cat-tech);margin-top:5px;flex-shrink:0;" aria-hidden="true"></span>
    <div style="flex:1;min-width:0;">
      <div style="font-size:13px;font-weight:600;color:var(--text-900);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">{Item title}</div>
      <div style="font-size:11.5px;color:var(--text-400);margin-top:1px;">{Parent entity}</div>
      <span class="cat-tag tech">{Category}</span>
    </div>
    <div style="text-align:right;flex-shrink:0;">
      <div style="font-size:11.5px;color:var(--text-600);font-weight:500;">{Due date}</div>
      <!-- urgency: "Tomorrow" red, "2 days" amber, "4+ days" muted -->
      <div style="font-size:10.5px;color:#dc2626;font-weight:600;margin-top:2px;">{Urgency}</div>
    </div>
  </div>
  <!-- More rows; last row omits border-bottom -->
</div>
```

---

## Records table (dashboard footer or list screen)

```html
<div class="card">
  <div class="card-header">
    <div>
      <div class="card-title">{Records title}</div>
      <div class="card-subtitle">{count · scope}</div>
    </div>
    <a href="#" class="view-all">View all →</a>
  </div>
  <div style="overflow-x:auto;">
    <table style="width:100%;border-collapse:collapse;">
      <thead>
        <tr>
          <th style="text-align:left;font-size:10.5px;text-transform:uppercase;letter-spacing:.6px;font-weight:700;color:var(--text-400);padding:10px 16px;border-bottom:1px solid var(--border);">{Column}</th>
          <!-- More <th> cells -->
          <th style="...">Status</th>
        </tr>
      </thead>
      <tbody>
        <tr style="transition:background .1s;cursor:default;">
          <td style="padding:13px 16px;font-size:13px;color:var(--text-600);border-bottom:1px solid var(--border);vertical-align:middle;">
            <span style="font-weight:600;color:var(--text-900);display:block;margin-bottom:2px;">{Primary label}</span>
            <span class="cat-tag tech">{Category}</span>
          </td>
          <!-- More <td> cells; use font-variant-numeric:tabular-nums for numbers -->
          <td style="...">
            <div style="display:flex;align-items:center;gap:8px;">
              <div style="width:80px;height:5px;background:var(--border);border-radius:20px;overflow:hidden;flex-shrink:0;">
                <div style="height:100%;background:var(--accent-light);border-radius:20px;width:{pct}%;"></div>
              </div>
              <span style="font-size:12px;font-weight:600;color:var(--text-600);font-variant-numeric:tabular-nums;">{pct}%</span>
            </div>
          </td>
          <td><span class="status-pill active"><span class="status-dot"></span>{State}</span></td>
        </tr>
        <!-- status-pill variants: .active .draft .archived -->
      </tbody>
    </table>
  </div>
</div>
```

### List toolbar (search + filter chips + count)

```html
<div style="display:flex;align-items:center;gap:12px;margin-bottom:16px;flex-wrap:wrap;">
  <!-- Search input -->
  <div style="position:relative;flex:1;max-width:320px;">
    <svg style="position:absolute;left:12px;top:50%;transform:translateY(-50%);color:var(--text-400);" width="14" height="14" viewBox="0 0 14 14" fill="none"><circle cx="6" cy="6" r="4.5" stroke="currentColor" stroke-width="1.4"/><path d="M9.5 9.5l3 3" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/></svg>
    <input type="search" placeholder="Filter by {fields}…" style="width:100%;padding:9px 14px 9px 36px;border:1px solid var(--border);border-radius:8px;font-size:13px;font-family:inherit;color:var(--text-900);background:var(--card);outline:none;">
  </div>
  <!-- Filter chips group -->
  <div style="display:flex;align-items:center;gap:6px;">
    <span style="font-size:12px;color:var(--text-400);font-weight:500;">{Facet}</span>
    <!-- Active chip -->
    <span style="display:inline-flex;align-items:center;gap:5px;padding:5px 12px;border:1px solid var(--accent-mid);border-radius:20px;font-size:12px;font-weight:600;color:var(--accent-deep);background:var(--accent-dim);cursor:pointer;">All <span style="font-size:10px;background:var(--accent-deep);color:#fff;border-radius:10px;padding:0 5px;font-weight:700;">{n}</span></span>
    <!-- Other chips -->
    <span style="display:inline-flex;align-items:center;gap:5px;padding:5px 12px;border:1px solid var(--border);border-radius:20px;font-size:12px;font-weight:500;color:var(--text-600);background:var(--card);cursor:pointer;">{Value} <span style="font-size:10px;background:var(--accent);color:#fff;border-radius:10px;padding:0 5px;font-weight:700;">{n}</span></span>
  </div>
  <span style="margin-left:auto;font-size:12px;color:var(--text-400);">{n} results</span>
</div>
```

### Pagination footer

```html
<div style="display:flex;align-items:center;justify-content:space-between;padding:12px 16px;border-top:1px solid var(--border);">
  <span style="font-size:12.5px;color:var(--text-400);">Showing {a}–{b} of {n}</span>
  <div style="display:flex;gap:4px;">
    <button style="width:30px;height:30px;border:1px solid var(--border);border-radius:6px;background:var(--card);color:var(--text-600);font-size:12.5px;cursor:pointer;">‹</button>
    <button style="width:30px;height:30px;border:1px solid var(--accent);border-radius:6px;background:var(--accent);color:#fff;font-size:12.5px;cursor:pointer;">1</button>
    <button style="width:30px;height:30px;border:1px solid var(--border);border-radius:6px;background:var(--card);color:var(--text-600);font-size:12.5px;cursor:pointer;">2</button>
    <button style="width:30px;height:30px;border:1px solid var(--border);border-radius:6px;background:var(--card);color:var(--text-600);font-size:12.5px;cursor:pointer;">›</button>
  </div>
</div>
```

---

## Record form — fields with inline validation

Rules live ON the field: required mark (`*`), helper text under the field, and
inline error message on an invalid field. Submit stays `disabled` until valid.
Never add a separate rules/validation-status summary panel.

```html
<form novalidate>
  <div class="card">
    <div style="display:flex;align-items:center;gap:8px;padding:14px 20px;border-bottom:1px solid var(--border);">
      <svg style="width:20px;height:20px;color:var(--accent);" viewBox="0 0 20 20" fill="none"><!-- section icon --></svg>
      <span style="font-size:13px;font-weight:700;color:var(--text-900);">{Section title}</span>
    </div>
    <div style="padding:20px;">
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px 20px;">

        <!-- Valid field -->
        <div style="display:flex;flex-direction:column;gap:5px;">
          <label style="font-size:12.5px;font-weight:600;color:var(--text-900);" for="f1">
            {Label} <span style="color:var(--accent);font-weight:700;">*</span>
          </label>
          <input id="f1" style="padding:9px 12px;border:1px solid var(--border);border-radius:8px;font-size:13.5px;font-family:inherit;color:var(--text-900);background:var(--card);outline:none;" type="text" placeholder="{hint}">
          <span style="font-size:11.5px;color:var(--text-400);">{what this drives / format hint}</span>
        </div>

        <!-- Invalid field: add red border + error message -->
        <div style="display:flex;flex-direction:column;gap:5px;">
          <label style="font-size:12.5px;font-weight:600;color:var(--text-900);" for="f2">
            {Label} <span style="color:var(--accent);font-weight:700;">*</span>
          </label>
          <input id="f2" style="padding:9px 12px;border:1px solid #fca5a5;border-radius:8px;font-size:13.5px;font-family:inherit;color:var(--text-900);background:#fee2e2;outline:none;" type="text" aria-invalid="true" aria-describedby="f2-err">
          <span id="f2-err" style="display:flex;align-items:center;gap:4px;font-size:11.5px;color:#dc2626;font-weight:500;">
            <svg style="width:12px;height:12px;flex-shrink:0;" viewBox="0 0 12 12" fill="none"><circle cx="6" cy="6" r="5" stroke="currentColor" stroke-width="1.4"/><path d="M6 3.5v3" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><circle cx="6" cy="8.5" r=".75" fill="currentColor"/></svg>
            {Specific rule that failed}
          </span>
        </div>

        <!-- Required select -->
        <div style="display:flex;flex-direction:column;gap:5px;">
          <label style="font-size:12.5px;font-weight:600;color:var(--text-900);" for="f3">
            {Label} <span style="color:var(--accent);font-weight:700;">*</span>
          </label>
          <select id="f3" style="padding:9px 32px 9px 12px;border:1px solid var(--border);border-radius:8px;font-size:13.5px;font-family:inherit;color:var(--text-900);background:var(--card) url('data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2212%22 height=%2212%22 fill=%22none%22%3E%3Cpath d=%22M2.5 4.5l2.5 2.5 2.5-2.5%22 stroke=%22%2394a3b8%22 stroke-width=%221.4%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22/%3E%3C/svg%3E') no-repeat right 12px center;appearance:none;outline:none;">
            <option value="">Select…</option>
            <option>{Option A}</option>
          </select>
          <span style="font-size:11.5px;color:var(--text-400);">{constraint on the options}</span>
        </div>

      </div>
    </div>
  </div>

  <!-- Form footer -->
  <div style="display:flex;align-items:center;justify-content:space-between;padding:16px 0;gap:12px;flex-wrap:wrap;">
    <span style="font-size:12.5px;color:var(--text-400);">Fields marked <span style="color:var(--accent);font-weight:700;">*</span> are required.</span>
    <div style="display:flex;gap:10px;">
      <button type="button" class="btn-ghost">Cancel</button>
      <button type="submit" style="padding:9px 20px;border:none;border-radius:8px;background:var(--accent-mid);color:var(--accent-light);font-size:13.5px;font-family:inherit;font-weight:600;cursor:not-allowed;" disabled>{Submit}</button>
    </div>
  </div>
</form>
```

---

## Record detail — header band + meta grid + related panels

```html
<!-- Detail header band -->
<div class="card" style="padding:20px 24px;display:flex;align-items:center;justify-content:space-between;gap:16px;flex-wrap:wrap;">
  <div>
    <div style="display:flex;align-items:center;gap:10px;margin-bottom:4px;">
      <span style="font-family:'Courier New',monospace;font-size:12px;color:var(--text-400);background:var(--surface);border:1px solid var(--border);border-radius:4px;padding:2px 8px;">{ID}</span>
      <span class="status-pill active"><span class="status-dot"></span>{State}</span>
    </div>
    <div style="font-size:20px;font-weight:700;color:var(--text-900);letter-spacing:-.3px;">
      {Name} <span class="cat-tag tech" style="vertical-align:middle;">{Category}</span>
    </div>
    <div style="font-size:13px;color:var(--text-400);margin-top:2px;">{Scope line}</div>
  </div>
  <div style="display:flex;gap:10px;flex-shrink:0;">
    <button class="btn-ghost">{Action}</button>
    <button class="btn-primary">Edit</button>
  </div>
</div>

<!-- Meta grid (3 columns; adjust to taste) -->
<div class="card" style="overflow:hidden;">
  <div style="display:grid;grid-template-columns:repeat(3,1fr);">
    <div style="padding:16px 20px;border-right:1px solid var(--border);border-bottom:1px solid var(--border);">
      <div style="font-size:10.5px;text-transform:uppercase;letter-spacing:.6px;font-weight:700;color:var(--text-400);margin-bottom:4px;">{FIELD}</div>
      <div style="font-size:13.5px;font-weight:600;color:var(--text-900);">{value}</div>
      <div style="font-size:11.5px;color:var(--text-400);margin-top:2px;">{sub}</div>
    </div>
    <!-- More cells; nth-child(3n) gets border-right:none; nth-last-child(-n+3) gets border-bottom:none -->
  </div>
</div>

<!-- Two-column related panels: 7fr 5fr -->
<div style="display:grid;grid-template-columns:7fr 5fr;gap:16px;">
  <div class="card"><!-- Sub-records table or status-board rows --></div>
  <div class="card"><!-- Activity / timeline feed --></div>
</div>
```
