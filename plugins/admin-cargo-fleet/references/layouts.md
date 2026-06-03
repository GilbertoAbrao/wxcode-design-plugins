# Cargo Fleet Admin — layout skeletons

Paste-ready, domain-neutral fragments for the industrial-clean light-mode skin.
Each skeleton is labelled by archetype slot, not by a domain noun. Copy the shell
from `assets/template.html` first (it carries the `:root` tokens + sidebar +
topbar + main slot), then drop the region skeletons below into
`<div class="page-body">`. Replace every placeholder with the real domain's
equivalent.

Token recap (full block in `template.html`): canvas `#f8f9fb`, surface `#ffffff`,
border `#e6e9ee`; sidebar `#1a2235`; accent `--accent: #ea580c`; amber
`--amber: #f59e0b`; success `#16a34a`; danger `#dc2626`. Put
`font-variant-numeric: tabular-nums` on every numeric cell.

---

## Page header (every screen)

```html
<div class="page-header">
  <div>
    <div style="font-size:18px;font-weight:800;letter-spacing:-.02em">{Screen title}</div>
    <div style="font-size:12px;color:var(--muted);margin-top:2px">{Hub · context · timestamp}</div>
  </div>
  <div style="display:flex;gap:8px">
    <button class="btn-ghost">{Secondary action}</button>
    <button class="btn-primary">+ {Primary action}</button>
  </div>
</div>
```

---

## KPI card row (4 × 1fr grid)

```html
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:16px">

  <!-- KPI card — repeat ×4 -->
  <div style="background:var(--surface);border:1px solid var(--border);border-radius:10px;padding:18px 20px 14px;box-shadow:0 1px 4px rgba(0,0,0,.06);display:flex;flex-direction:column;gap:6px">
    <div style="display:flex;align-items:center;justify-content:space-between">
      <span style="font-size:10px;font-weight:700;letter-spacing:.09em;text-transform:uppercase;color:var(--muted)">{METRIC LABEL}</span>
      <!-- icon chip: 32×32, border-radius 6px, bg=accent-light/success-light/amber-light/slate -->
      <div style="width:32px;height:32px;border-radius:6px;background:var(--accent-light);color:var(--accent);display:flex;align-items:center;justify-content:center">
        <!-- inline SVG icon 18×18 -->
      </div>
    </div>
    <div style="font-size:26px;font-weight:800;letter-spacing:-.02em;line-height:1;font-variant-numeric:tabular-nums">{value}</div>
    <div style="display:flex;align-items:center;justify-content:space-between;margin-top:2px">
      <!-- delta chip: delta-up (success bg/color) / delta-down (danger) / delta-warn (amber) -->
      <span style="font-size:11px;font-weight:600;padding:2px 6px;border-radius:4px;background:var(--success-light);color:var(--success);display:flex;align-items:center;gap:3px">
        <!-- ▲ arrow SVG 8×8 -->
        {+delta}
      </span>
      <!-- sparkline: SVG polyline 56×22, stroke=matching token -->
      <svg width="56" height="22" viewBox="0 0 56 22" fill="none">
        <polyline points="0,18 9,14 18,16 27,8 36,10 45,5 56,7" stroke="var(--accent)" stroke-width="1.8" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
    </div>
    <!-- Optional progress bar (4px, gradient) for utilization-type metrics -->
    <!-- <div style="margin-top:8px;background:var(--border);height:4px;border-radius:2px;overflow:hidden"><div style="width:{pct}%;height:100%;border-radius:2px;background:linear-gradient(90deg,var(--accent),var(--amber))"></div></div> -->
  </div>

</div>
```

---

## Two-column middle grid (7fr / 5fr)

```html
<div style="display:grid;grid-template-columns:7fr 5fr;gap:16px;align-items:start">
  <!-- Left: Kanban status board (see below) -->
  <!-- Right: network visualization (see below) -->
</div>
```

### Kanban status board

`[column header: label + count] [item cards: ID + route/desc + sub + time]`

```html
<div style="background:var(--surface);border:1px solid var(--border);border-radius:10px;box-shadow:0 1px 4px rgba(0,0,0,.06);overflow:hidden">
  <div style="display:flex;align-items:center;justify-content:space-between;padding:16px 20px;border-bottom:1px solid var(--border)">
    <span style="font-size:14px;font-weight:700">{Board title}</span>
    <span style="font-size:12px;color:var(--accent);font-weight:600;cursor:pointer">View all →</span>
  </div>
  <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:12px;padding:16px">

    <!-- Column — repeat ×4 (pending / loading / transit / delivered) -->
    <div style="display:flex;flex-direction:column;gap:8px">
      <div style="display:flex;align-items:center;justify-content:space-between;padding:6px 0 8px">
        <!-- col label: 11px / uppercase / color per state -->
        <span style="font-size:11px;font-weight:700;letter-spacing:.07em;text-transform:uppercase;color:#475569">Pending</span>
        <!-- count badge: matching tint -->
        <span style="font-size:10px;font-weight:700;padding:2px 7px;border-radius:10px;background:#f1f5f9;color:#475569">{N}</span>
      </div>

      <!-- Item card — repeat -->
      <!-- border-left 3px stripe: pending=#94a3b8, loading=amber, transit=accent, delivered=success -->
      <div style="background:var(--surface);border:1px solid var(--border);border-radius:6px;padding:10px 12px;display:flex;flex-direction:column;gap:5px;position:relative;transition:box-shadow .15s,transform .15s">
        <div style="position:absolute;left:0;top:0;bottom:0;width:3px;border-radius:3px 0 0 3px;background:#94a3b8"></div>
        <div style="font-size:11px;font-weight:700;font-family:'SF Mono','Consolas',monospace;letter-spacing:.02em">{ID}</div>
        <div style="font-size:11px;color:var(--muted)">{Origin} <span style="color:var(--accent)">›</span> {Dest}</div>
        <div style="font-size:10px;color:var(--muted)">{Carrier / detail}</div>
        <div style="font-size:10px;font-weight:600;margin-top:2px"><span style="color:var(--muted);font-weight:400">ETA:</span> {time}</div>
      </div>

    </div><!-- /column -->

  </div>
</div>
```

### Network visualization

Abstract SVG graph — nodes + bezier arcs, animated traveler dot.

```html
<div style="background:var(--surface);border:1px solid var(--border);border-radius:10px;box-shadow:0 1px 4px rgba(0,0,0,.06);overflow:hidden">
  <div style="display:flex;align-items:center;justify-content:space-between;padding:16px 20px;border-bottom:1px solid var(--border)">
    <span style="font-size:14px;font-weight:700">{Network title}</span>
    <span style="font-size:12px;color:var(--accent);font-weight:600;cursor:pointer">Full map →</span>
  </div>
  <div style="padding:16px;background:var(--bg)">
    <svg width="100%" viewBox="0 0 400 280" fill="none" style="display:block">
      <!-- Grid lines -->
      <line x1="0" y1="140" x2="400" y2="140" stroke="var(--border)" stroke-width=".7"/>
      <line x1="200" y1="0" x2="200" y2="280" stroke="var(--border)" stroke-width=".7"/>

      <!-- Idle arcs (dashed) -->
      <path d="M 80 210 Q 200 260 360 210" stroke="var(--border)" stroke-width="2" stroke-dasharray="5 4"/>

      <!-- Busy arcs (amber) -->
      <path d="M 200 50 Q 290 30 360 90" stroke="var(--amber)" stroke-width="2.2" opacity=".7"/>

      <!-- Active arcs (orange) + animated traveler -->
      <path id="route-p" d="M 80 210 Q 140 80 240 130 Q 310 170 360 90" stroke="var(--accent)" stroke-width="2.5"/>
      <circle r="5" fill="var(--accent)" opacity=".9">
        <animateMotion dur="3.2s" repeatCount="indefinite" rotate="auto"><mpath href="#route-p"/></animateMotion>
      </circle>

      <!-- Node pattern (active = orange, busy = amber, idle = slate) -->
      <!-- active node: outer glow circle (opacity .2) + filled circle + white center dot -->
      <circle cx="{x}" cy="{y}" r="10" fill="var(--accent)" opacity=".2"/>
      <circle cx="{x}" cy="{y}" r="7" fill="var(--accent)"/>
      <circle cx="{x}" cy="{y}" r="3" fill="white"/>
      <text x="{x+10}" y="{y+4}" font-family="Inter,system-ui,sans-serif" font-size="10" font-weight="600" fill="var(--text)">{Node}</text>
    </svg>
  </div>
  <!-- Legend row -->
  <div style="display:flex;gap:14px;padding:10px 16px 14px;flex-wrap:wrap">
    <span style="display:flex;align-items:center;gap:5px;font-size:11px;color:var(--muted)"><span style="width:8px;height:8px;border-radius:50%;background:var(--accent);flex-shrink:0"></span>Active Route</span>
    <span style="display:flex;align-items:center;gap:5px;font-size:11px;color:var(--muted)"><span style="width:8px;height:8px;border-radius:50%;background:var(--amber);flex-shrink:0"></span>Busy</span>
    <span style="display:flex;align-items:center;gap:5px;font-size:11px;color:var(--muted)"><span style="width:8px;height:8px;border-radius:50%;background:#94a3b8;flex-shrink:0"></span>Idle</span>
  </div>
</div>
```

---

## Full-width records table

```html
<div style="background:var(--surface);border:1px solid var(--border);border-radius:10px;box-shadow:0 1px 4px rgba(0,0,0,.06);overflow:hidden">
  <!-- Table header -->
  <div style="display:flex;align-items:center;justify-content:space-between;padding:16px 20px;border-bottom:1px solid var(--border);gap:12px;flex-wrap:wrap">
    <div style="display:flex;align-items:center;gap:10px">
      <span style="font-size:14px;font-weight:700">{Table title}</span>
      <span style="font-size:11px;font-weight:700;padding:2px 8px;border-radius:10px;background:var(--accent-light);color:var(--accent)">{N}</span>
    </div>
    <div style="display:flex;gap:8px">
      <button class="btn-ghost">Export CSV</button>
      <button class="btn-primary">+ {Action}</button>
    </div>
  </div>
  <table style="width:100%;border-collapse:collapse">
    <thead>
      <tr>
        <!-- uppercase 10px / muted / letter-spacing .08em -->
        <th style="font-size:10px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);padding:10px 20px;text-align:left;border-bottom:1px solid var(--border)">{COL}</th>
        <!-- more columns -->
        <th style="...">Status</th>
      </tr>
    </thead>
    <tbody>
      <!-- odd rows: var(--bg); hover: var(--accent-light) -->
      <tr style="border-bottom:1px solid var(--border)">
        <!-- ID cell: accent color, monospace, weight 700 -->
        <td style="padding:10px 20px;font-size:12px;font-weight:700;color:var(--accent);font-family:'SF Mono','Consolas',monospace">{ID}</td>
        <!-- route cell: flex row with muted arrow -->
        <td style="padding:10px 20px;font-size:12px">{origin} <span style="color:var(--muted)">→</span> {dest}</td>
        <!-- numeric cell: tabular-nums -->
        <td style="padding:10px 20px;font-size:12px;font-variant-numeric:tabular-nums">{value}</td>
        <!-- status pill -->
        <td style="padding:10px 20px">
          <span style="display:inline-flex;align-items:center;gap:4px;padding:3px 10px;border-radius:20px;font-size:11px;font-weight:700;letter-spacing:.04em;background:var(--accent-light);color:var(--accent)">{State}</span>
        </td>
      </tr>
    </tbody>
  </table>
  <!-- Table footer -->
  <div style="display:flex;align-items:center;justify-content:space-between;padding:12px 20px;border-top:1px solid var(--border);font-size:12px;color:var(--muted)">
    <span>Showing 1–{n} of {total} records</span>
    <!-- pager: .pager-btn; .active → accent bg -->
  </div>
</div>
```

---

## List screen — filter bar

```html
<!-- Filter bar (above table) -->
<div style="display:flex;align-items:center;gap:10px;flex-wrap:wrap">
  <!-- search input -->
  <div style="position:relative;flex:1;max-width:320px">
    <svg style="position:absolute;left:10px;top:50%;transform:translateY(-50%);color:var(--muted)" width="13" height="13" viewBox="0 0 14 14" fill="none"><circle cx="6" cy="6" r="4.5" stroke="currentColor" stroke-width="1.4"/><path d="M9.5 9.5l3 3" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/></svg>
    <input type="text" placeholder="Filter&hellip;" style="width:100%;height:34px;border:1px solid var(--border);border-radius:6px;background:var(--surface);padding:0 12px 0 34px;font-size:13px;color:var(--text)">
  </div>
  <!-- filter chips: border pill, hover/active → accent border + accent-light bg -->
  <button style="height:32px;padding:0 12px;border-radius:6px;border:1px solid var(--accent);background:var(--accent-light);font-size:12px;font-weight:500;color:var(--accent);cursor:pointer">{State}</button>
  <button style="height:32px;padding:0 12px;border-radius:6px;border:1px solid var(--border);background:var(--surface);font-size:12px;font-weight:500;color:var(--text);cursor:pointer">{State}</button>
  <span style="margin-left:auto;font-size:12px;color:var(--muted)">{N} records</span>
</div>
```

---

## Form screen — field card

```html
<div style="background:var(--surface);border:1px solid var(--border);border-radius:10px;box-shadow:0 1px 4px rgba(0,0,0,.06);overflow:hidden">
  <div style="padding:16px 20px;border-bottom:1px solid var(--border)">
    <div style="font-size:13px;font-weight:700">{Section title}</div>
    <div style="font-size:12px;color:var(--muted);margin-top:2px">{Section description}</div>
  </div>
  <div style="padding:20px;display:flex;flex-direction:column;gap:16px">

    <!-- Field grid (2-col or 3-col) -->
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px">

      <!-- Field -->
      <div style="display:flex;flex-direction:column;gap:5px">
        <label style="font-size:12px;font-weight:600;color:var(--text)">
          {Label} <span style="color:var(--accent)">*</span>
        </label>
        <input type="text" style="height:36px;border:1px solid var(--border);border-radius:6px;padding:0 12px;font-size:13px;color:var(--text);background:var(--surface);transition:border-color .15s">
        <!-- helper text: 11px muted, shows when field is empty/untouched -->
        <span style="font-size:11px;color:var(--muted)">{Helper text}</span>
      </div>

      <!-- Field with inline error (invalid state) -->
      <div style="display:flex;flex-direction:column;gap:5px">
        <label style="font-size:12px;font-weight:600;color:var(--text)">
          {Label} <span style="color:var(--accent)">*</span>
        </label>
        <select style="height:36px;border:1px solid var(--danger);border-radius:6px;padding:0 12px;font-size:13px;color:var(--text);background:var(--surface);appearance:none">
          <option value="">Select&hellip;</option>
        </select>
        <!-- inline error: 11px danger, shown when field is invalid -->
        <span style="font-size:11px;color:var(--danger);display:flex;align-items:center;gap:4px">
          <svg width="12" height="12" viewBox="0 0 12 12" fill="none"><circle cx="6" cy="6" r="5" stroke="currentColor" stroke-width="1.3"/><path d="M6 4v3M6 8.5v.5" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"/></svg>
          {Error message}
        </span>
      </div>

    </div>
  </div>

  <!-- Form footer -->
  <div style="display:flex;align-items:center;justify-content:space-between;padding:16px 20px;border-top:1px solid var(--border);background:var(--bg)">
    <span style="font-size:12px;color:var(--muted)"><span style="color:var(--accent)">*</span> Required fields</span>
    <div style="display:flex;gap:8px">
      <button class="btn-ghost">Save Draft</button>
      <!-- disabled until all required fields are valid -->
      <button class="btn-primary" disabled style="opacity:.45;cursor:not-allowed">Create {Entity}</button>
    </div>
  </div>
</div>
```

---

## Detail screen — header band

```html
<div style="background:var(--surface);border:1px solid var(--border);border-radius:10px;box-shadow:0 1px 4px rgba(0,0,0,.06);padding:20px 24px;display:flex;align-items:center;gap:16px">
  <div>
    <div style="display:flex;align-items:center;gap:10px;margin-bottom:4px">
      <span style="font-size:22px;font-weight:800;letter-spacing:-.02em;font-family:'SF Mono','Consolas',monospace">{ID}</span>
      <!-- status pill -->
      <span style="display:inline-flex;align-items:center;padding:4px 12px;border-radius:20px;font-size:12px;font-weight:700;background:var(--accent-light);color:var(--accent)">{State}</span>
    </div>
    <div style="font-size:12px;color:var(--muted)">{key fields summary}</div>
  </div>
  <div style="margin-left:auto;display:flex;gap:8px">
    <button class="btn-ghost">Archive</button>
    <button class="btn-primary">Edit</button>
  </div>
</div>
```

### Detail meta grid (2-col)

```html
<div style="background:var(--surface);border:1px solid var(--border);border-radius:10px;box-shadow:0 1px 4px rgba(0,0,0,.06);overflow:hidden">
  <div style="padding:14px 20px;border-bottom:1px solid var(--border)">
    <span style="font-size:13px;font-weight:700">{Section title}</span>
  </div>
  <div style="display:grid;grid-template-columns:1fr 1fr">
    <!-- each .meta-item: padding 12px 20px; border-bottom; last two items no border -->
    <div style="padding:12px 20px;border-bottom:1px solid var(--border)">
      <div style="font-size:10px;font-weight:700;letter-spacing:.07em;text-transform:uppercase;color:var(--muted);margin-bottom:4px">{LABEL}</div>
      <div style="font-size:13px;font-weight:600">{value}</div>
    </div>
    <!-- more pairs -->
  </div>
</div>
```

### Related sub-table

```html
<div style="background:var(--surface);border:1px solid var(--border);border-radius:10px;box-shadow:0 1px 4px rgba(0,0,0,.06);overflow:hidden">
  <div style="padding:14px 20px;border-bottom:1px solid var(--border)">
    <span style="font-size:13px;font-weight:700">{Sub-table title}</span>
  </div>
  <!-- Row pattern: grid 4 cols — [label+sub] [state pill] [notes] [time] -->
  <div style="display:grid;grid-template-columns:120px 90px 1fr 100px;align-items:center;gap:12px;padding:10px 20px;border-bottom:1px solid var(--border)">
    <div>
      <div style="font-size:12px;font-weight:600">{Stop}</div>
      <div style="font-size:11px;color:var(--muted)">{Sub}</div>
    </div>
    <span style="display:inline-flex;align-items:center;padding:2px 9px;border-radius:20px;font-size:10px;font-weight:700;background:var(--success-light);color:var(--success)">{State}</span>
    <span style="font-size:12px;color:var(--muted)">{Notes}</span>
    <span style="font-size:11px;color:var(--muted);font-variant-numeric:tabular-nums">{time}</span>
  </div>
</div>
```
