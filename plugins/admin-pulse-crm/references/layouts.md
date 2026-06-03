# Pulse Admin — layout skeletons

Paste-ready, domain-neutral fragments for the Pulse airy light-mode skin. Each
skeleton is labelled by archetype slot, not by a domain noun. Copy the shell from
`assets/template.html` first (it carries the `:root` tokens + sidebar with
workspace switcher + topbar + content slot), then drop the region skeletons below
into `<div class="content">`. Replace every placeholder label with the real
domain's equivalent.

Token recap (full block in `template.html`): page `#f8fafc`, card `#ffffff`,
inset `#f1f5f9`, hairline `#e2e8f0`; text `#0f172a / #334155 / #475569 /
#64748b / #94a3b8`; accent `var(--accent)` = `#0ea5e9`, dark `#2563eb`,
bg `#e0f2fe`; state tokens `--state-*` with `*-bg` tints.
Put `font-variant-numeric: tabular-nums` on every numeric cell.

---

## Page header (every screen)

```html
<div style="display:flex;align-items:flex-start;justify-content:space-between;margin-bottom:16px;gap:16px">
  <div>
    <div style="font-size:17px;font-weight:700;color:#0f172a">{Screen title}</div>
    <div style="font-size:13px;color:#64748b;margin-top:2px">{Scope · context}</div>
  </div>
  <div style="display:flex;gap:8px;align-items:center">
    <button class="btn-ghost">{Secondary action}</button>
    <button class="btn-primary">+ {Primary action}</button>
  </div>
</div>
```

---

## KPI tile row (repeat ×4 in a grid)

```html
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-bottom:18px">
  <div class="card" style="padding:16px 18px">
    <div style="font-size:10px;font-weight:700;letter-spacing:.07em;text-transform:uppercase;color:#94a3b8;margin-bottom:10px">{METRIC LABEL}</div>
    <div style="display:flex;align-items:flex-end;justify-content:space-between;gap:8px">
      <div style="font-size:26px;font-weight:800;color:#0f172a;line-height:1;font-variant-numeric:tabular-nums">{figure}</div>
      <div style="display:flex;flex-direction:column;align-items:flex-end;gap:6px">
        <!-- SVG sparkline (line or bar), stroke/fill = var(--accent) -->
        <svg width="64" height="28" viewBox="0 0 64 28" fill="none">
          <polyline points="0,22 16,18 32,14 48,10 64,5"
            stroke="var(--accent)" stroke-width="2" fill="none"
            stroke-linecap="round" stroke-linejoin="round"/>
          <polygon points="0,22 16,18 32,14 48,10 64,5 64,28 0,28"
            fill="var(--accent)" opacity=".1"/>
        </svg>
        <!-- delta chip: .up = green, .down = red -->
        <span style="display:inline-flex;align-items:center;gap:3px;font-size:11px;font-weight:600;padding:2px 7px;border-radius:20px;color:var(--delta-up);background:var(--delta-up-bg)">▲ {delta}</span>
      </div>
    </div>
  </div>
  <!-- 3 more tiles -->
</div>
```

---

## Stage-progress strip (full-width card)

```html
<div class="card" style="padding:16px 18px;margin-bottom:18px">
  <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:14px">
    <span style="font-size:14px;font-weight:700;color:#0f172a">{Strip title}</span>
    <a href="#" style="font-size:12px;font-weight:500;color:var(--accent)">Manage stages →</a>
  </div>
  <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:0">
    <!-- Repeat one .stage-col per stage -->
    <div style="padding:0 14px;border-right:1px solid #e2e8f0">   <!-- first: padding-left:0; last: border-right:none;padding-right:0 -->
      <div style="font-size:11px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:#64748b;margin-bottom:4px">{Stage name}</div>
      <div style="font-size:11px;color:#94a3b8;margin-bottom:2px">{N items}</div>
      <div style="font-size:18px;font-weight:800;color:#0f172a;margin-bottom:8px;font-variant-numeric:tabular-nums">{total value}</div>
      <div style="height:6px;background:#f1f5f9;border-radius:4px;overflow:hidden">
        <div style="height:100%;border-radius:4px;width:{pct}%;background:var(--accent);opacity:{0.35|0.55|0.75|1};transition:width .3s"></div>
      </div>
    </div>
  </div>
</div>
```

---

## Two-column split (records table + side panel)

```html
<div style="display:grid;grid-template-columns:1fr 340px;gap:14px">

  <!-- LEFT — records table card -->
  <div class="card" style="overflow:hidden">
    <div style="display:flex;align-items:center;justify-content:space-between;padding:14px 18px 0">
      <span style="font-size:14px;font-weight:700;color:#0f172a">{Table title}</span>
      <a href="#" style="font-size:12px;color:var(--accent)">View all →</a>
    </div>
    <table style="width:100%;border-collapse:collapse">
      <thead>
        <tr>
          <!-- th: font-size:10px; font-weight:700; letter-spacing:.07em; text-transform:uppercase; color:#94a3b8; padding:10px 12px; background:#f8fafc; border-bottom:1px solid #e2e8f0 -->
          <th style="...">Item</th>
          <th style="...">Account</th>
          <th style="...">Owner</th>
          <th style="...">Value</th>
          <th style="...">Stage</th>
          <th style="...">Due</th>
        </tr>
      </thead>
      <tbody>
        <tr style="border-bottom:1px solid #f1f5f9">
          <td style="padding:11px 12px;vertical-align:middle">
            <div style="font-weight:600;color:#0f172a">{name}</div>
            <div style="font-size:12px;color:#64748b">{sub}</div>
          </td>
          <td style="padding:11px 12px;font-size:13px;color:#334155">{account}</td>
          <td style="padding:11px 12px">
            <div style="display:flex;align-items:center;gap:7px">
              <div style="width:24px;height:24px;border-radius:50%;background:{color};color:#fff;font-size:10px;font-weight:700;display:flex;align-items:center;justify-content:center">{initials}</div>
              {name}
            </div>
          </td>
          <td style="padding:11px 12px;font-weight:700;color:#0f172a;font-variant-numeric:tabular-nums">{value}</td>
          <td style="padding:11px 12px">
            <!-- status pill: padding:3px 10px; border-radius:20px; font-size:11px; font-weight:600; bg + color from --state-*-bg / --state-* -->
            <span style="...">{Stage}</span>
          </td>
          <td style="padding:11px 12px;font-size:12px;color:#64748b">{date}</td>
        </tr>
        <!-- more rows -->
      </tbody>
    </table>
    <div style="display:flex;align-items:center;justify-content:space-between;padding:10px 18px;border-top:1px solid #f1f5f9;font-size:12px;color:#94a3b8">
      <span>Showing {a}–{b} of {n}</span>
      <div style="display:flex;gap:2px">
        <!-- page buttons: width:26px;height:26px;border:1px solid #e2e8f0;border-radius:5px;font-size:12px; active gets background:var(--accent);color:#fff -->
        <button style="...">‹</button>
        <button style="...;background:var(--accent);border-color:var(--accent);color:#fff">1</button>
        <button style="...">2</button>
        <button style="...">›</button>
      </div>
    </div>
  </div>

  <!-- RIGHT — activity / tasks side panel -->
  <div class="card" style="display:flex;flex-direction:column;overflow:hidden">
    <div style="display:flex;align-items:center;justify-content:space-between;padding:14px 16px 0">
      <span style="font-size:14px;font-weight:700;color:#0f172a">{Panel title}</span>
    </div>
    <!-- Tasks section -->
    <div style="padding:10px 16px 6px;font-size:10px;font-weight:700;letter-spacing:.07em;text-transform:uppercase;color:#94a3b8;border-top:none">Tasks</div>
    <div style="padding:0 16px">
      <!-- task row -->
      <div style="display:flex;align-items:flex-start;gap:10px;padding:9px 0;border-bottom:1px solid #f1f5f9">
        <!-- checkbox: width:16px;height:16px;border-radius:4px;border:1.5px solid #cbd5e1; done: background:var(--state-won) -->
        <div style="..."></div>
        <span style="font-size:13px;color:#334155;flex:1">{task text}</span>
        <span style="font-size:11px;color:#94a3b8;white-space:nowrap;margin-left:auto">{time}</span>
      </div>
      <!-- more task rows -->
    </div>
    <!-- Feed section -->
    <div style="padding:10px 16px 6px;font-size:10px;font-weight:700;letter-spacing:.07em;text-transform:uppercase;color:#94a3b8;border-top:1px solid #f1f5f9">Activity</div>
    <div style="padding:0 16px 12px">
      <!-- feed row -->
      <div style="display:flex;align-items:flex-start;gap:10px;padding:8px 0;border-bottom:1px solid #f1f5f9">
        <div style="width:28px;height:28px;border-radius:50%;background:{color};color:#fff;font-size:11px;font-weight:700;display:flex;align-items:center;justify-content:center;flex-shrink:0;margin-top:1px">{initials}</div>
        <div>
          <div style="font-size:12px;color:#334155"><strong style="color:#0f172a">{User}</strong> {verb} <strong style="color:#0f172a">{target}</strong></div>
          <div style="font-size:11px;color:#94a3b8;margin-top:1px">{relative time}</div>
        </div>
      </div>
      <!-- more feed rows -->
    </div>
  </div>

</div>
```

---

## List toolbar (search + filter chips)

```html
<div style="display:flex;align-items:center;gap:10px;margin-bottom:14px;flex-wrap:wrap">
  <!-- search pill -->
  <div style="position:relative;display:flex;align-items:center;min-width:260px">
    <svg width="15" height="15" viewBox="0 0 15 15" fill="none" style="position:absolute;left:10px;color:#94a3b8;pointer-events:none">
      <circle cx="6.5" cy="6.5" r="5" stroke="#94a3b8" stroke-width="1.4"/>
      <path d="M10.5 10.5l3 3" stroke="#94a3b8" stroke-width="1.4" stroke-linecap="round"/>
    </svg>
    <input type="text" placeholder="Filter {entity} by {fields}…"
      style="width:100%;padding:7px 12px 7px 34px;border:1px solid #e2e8f0;border-radius:8px;background:#fff;color:#334155;font-size:13px;outline:none">
  </div>
  <!-- filter label + chip group -->
  <span style="font-size:12px;color:#64748b;font-weight:500">{Facet label}</span>
  <button class="chip chip-active">All <span style="display:inline-block;margin-left:4px;background:rgba(255,255,255,.25);padding:0 5px;border-radius:8px;font-size:10px">{n}</span></button>
  <button class="chip">{Stage 1} <span style="...">{n}</span></button>
  <button class="chip">{Stage 2} <span style="...">{n}</span></button>
  <!-- count -->
  <span style="margin-left:auto;font-size:12px;color:#94a3b8">{n} results</span>
</div>
```

---

## Record form — fields with inline validation

Rules live ON the field: a required mark (`*`), helper text under the field, and
an inline error on invalid input. The submit stays `disabled` until the form is
valid. Never add a separate rules/validation-status summary panel.

```html
<form style="display:flex;flex-direction:column;gap:16px;max-width:760px" novalidate>
  <div class="card">
    <div style="display:flex;align-items:center;gap:8px;padding:14px 20px 12px;font-size:13px;font-weight:700;color:#0f172a;border-bottom:1px solid #e2e8f0">
      <!-- optional SVG icon -->
      {Section label}
    </div>
    <div style="padding:20px">
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px 20px">

        <!-- valid field -->
        <div style="display:flex;flex-direction:column;gap:4px">
          <label style="font-size:12px;font-weight:600;color:#475569" for="f1">
            {Label} <span style="color:#ef4444;margin-left:2px">*</span>
          </label>
          <input id="f1" type="text" value="{value}"
            style="padding:8px 12px;border:1px solid #e2e8f0;border-radius:7px;color:#0f172a;font-size:13px;background:#fff;outline:none">
          <span style="font-size:11px;color:#94a3b8">{helper text — format hint or constraint}</span>
        </div>

        <!-- invalid field: border #ef4444, bg #fffafa, + error-msg -->
        <div style="display:flex;flex-direction:column;gap:4px">
          <label style="font-size:12px;font-weight:600;color:#475569" for="f2">
            {Label} <span style="color:#ef4444;margin-left:2px">*</span>
          </label>
          <input id="f2" type="text" aria-invalid="true"
            style="padding:8px 12px;border:1px solid #ef4444;border-radius:7px;color:#0f172a;font-size:13px;background:#fffafa;outline:none">
          <span style="display:flex;align-items:center;gap:5px;font-size:11px;color:#ef4444;font-weight:500">
            <!-- small alert SVG -->
            {Specific rule that failed — e.g. "Must be greater than 0."}
          </span>
        </div>

        <!-- required select -->
        <div style="display:flex;flex-direction:column;gap:4px">
          <label style="font-size:12px;font-weight:600;color:#475569" for="f3">
            {Label} <span style="color:#ef4444;margin-left:2px">*</span>
          </label>
          <select id="f3" style="padding:8px 12px;border:1px solid #e2e8f0;border-radius:7px;color:#0f172a;font-size:13px;background:#fff;outline:none;appearance:none">
            <option value="">Select…</option>
          </select>
          <span style="font-size:11px;color:#94a3b8">{constraint on the options}</span>
        </div>

      </div>
    </div>
  </div>

  <div style="display:flex;align-items:center;justify-content:space-between;padding:14px 20px;background:#fff;border:1px solid #e2e8f0;border-radius:10px">
    <span style="font-size:12px;color:#94a3b8">Fields marked <span style="color:#ef4444">*</span> are required.</span>
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
<!-- Breadcrumb trail -->
<div style="display:flex;align-items:center;gap:6px;font-size:12px;color:#94a3b8;margin-bottom:14px">
  <a href="#" style="color:var(--accent)">{Parent list}</a>
  <span>›</span>
  <span>{Record title}</span>
</div>

<!-- Detail header -->
<div style="display:flex;align-items:flex-start;justify-content:space-between;margin-bottom:16px;gap:16px">
  <div>
    <div style="display:flex;align-items:center;gap:10px;margin-bottom:4px">
      <span style="font-size:12px;font-weight:700;color:#94a3b8;font-family:'Courier New',monospace;background:#f1f5f9;padding:2px 8px;border-radius:4px">{#ID}</span>
      <!-- status pill -->
      <span style="padding:3px 12px;border-radius:20px;font-size:12px;font-weight:600;background:var(--state-stage3-bg);color:var(--state-stage3)">{Stage}</span>
    </div>
    <div style="font-size:20px;font-weight:800;color:#0f172a;letter-spacing:-.3px">{Record title}</div>
    <div style="font-size:13px;color:#64748b;margin-top:3px">{Account} · {Type} · Opened {date}</div>
  </div>
  <div style="display:flex;gap:8px;align-items:center;flex-shrink:0">
    <button class="btn-ghost">{Action}</button>
    <button class="btn-primary">Edit</button>
  </div>
</div>

<!-- Meta grid (3-col) -->
<div class="card" style="margin-bottom:14px">
  <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:0">
    <div style="padding:16px 20px;border-right:1px solid #f1f5f9">
      <div style="font-size:10px;font-weight:700;letter-spacing:.07em;text-transform:uppercase;color:#94a3b8;margin-bottom:4px">{FIELD}</div>
      <div style="font-size:14px;font-weight:600;color:#0f172a;font-variant-numeric:tabular-nums">{value}</div>
      <div style="font-size:11px;color:#64748b;margin-top:2px">{sub}</div>
    </div>
    <!-- 5 more cells; last in each row has no border-right -->
  </div>
</div>

<!-- Two-column: related data + activity feed (same 1fr / 340px split as dashboard) -->
<div style="display:grid;grid-template-columns:1fr 340px;gap:14px">
  <div class="card"><!-- related items table --></div>
  <div class="card"><!-- activity feed --></div>
</div>
```
