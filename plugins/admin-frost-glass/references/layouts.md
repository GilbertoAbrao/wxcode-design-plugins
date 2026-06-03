# Frost Glass Admin — layout skeletons

Paste-ready, domain-neutral fragments for the frost-glass / dark-gradient skin.
Each skeleton is labelled by archetype slot, not by a domain noun. Copy the shell
from `assets/template.html` first (it carries `:root` tokens + sidebar + topbar +
main slot), then drop the region skeletons below into `<main class="content">`.
Replace every `{brace}` placeholder with the real domain's equivalent.

Token recap (full block in `template.html`): gradient canvas `--grad-a/b/c/d`;
accent `--accent-cyan #22d3ee`, `--accent-violet #a78bfa`, `--accent-rose #f472b6`,
`--accent-emerald #34d399`, `--accent-amber #fbbf24`; glass surfaces
`--glass-bg rgba(255,255,255,0.06)`, `--glass-border rgba(255,255,255,0.12)`,
`--glass-blur blur(16px)`, `--glass-shadow 0 8px 32px rgba(0,0,0,0.36)`;
text `--text-primary / --text-muted / --text-faint`.

---

## Page header (every screen)

```html
<div style="display:flex;align-items:flex-start;justify-content:space-between;gap:16px">
  <div>
    <div style="font-size:20px;font-weight:700;letter-spacing:-0.02em">{Screen title}</div>
    <div style="font-size:12px;color:var(--text-muted);margin-top:4px">{scope · context · timestamp}</div>
  </div>
  <div style="display:flex;gap:10px;flex-shrink:0">
    <button class="btn-ghost">{Secondary action}</button>
    <button class="btn-primary">+ {Primary action}</button>
  </div>
</div>
```

---

## KPI tile row (repeat ×4 in a 4-col grid)

```html
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:16px">

  <div class="glass-card" style="padding:20px;position:relative;overflow:hidden">
    <!-- Accent dot top-right: change color per metric using var(--accent-*) -->
    <div style="position:absolute;top:16px;right:16px;width:8px;height:8px;border-radius:50%;background:var(--accent-cyan)" aria-hidden="true"></div>
    <div style="font-size:10px;font-weight:600;letter-spacing:0.1em;text-transform:uppercase;color:var(--text-muted);margin-bottom:10px">{METRIC LABEL}</div>
    <div style="font-size:28px;font-weight:700;letter-spacing:-0.03em;line-height:1;margin-bottom:10px">{figure}</div>
    <!-- Inline SVG sparkline — 120×36, gradient area fill -->
    <svg width="100%" height="36" viewBox="0 0 120 36" preserveAspectRatio="none" style="display:block;margin-bottom:10px" aria-hidden="true">
      <defs>
        <linearGradient id="sp-{n}" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stop-color="var(--accent-cyan)" stop-opacity="0.3"/>
          <stop offset="100%" stop-color="var(--accent-cyan)" stop-opacity="0"/>
        </linearGradient>
      </defs>
      <!-- Replace points with real relative y values (0=top, 36=bottom) -->
      <path d="M0 30 L20 24 L40 28 L60 18 L80 14 L100 8 L120 4" fill="none" stroke="var(--accent-cyan)" stroke-width="1.8" stroke-linecap="round"/>
      <path d="M0 30 L20 24 L40 28 L60 18 L80 14 L100 8 L120 4 L120 36 L0 36Z" fill="url(#sp-{n})"/>
    </svg>
    <!-- Delta chip: .delta-up (emerald) or .delta-down (rose) -->
    <span style="display:inline-flex;align-items:center;gap:4px;font-size:11px;font-weight:600;padding:2px 8px;border-radius:99px;background:rgba(52,211,153,0.14);color:var(--accent-emerald)">▲ {delta}</span>
  </div>

  <!-- Repeat 3 more tiles; change accent dot color and delta chip class -->
</div>
```

---

## Two-column grid (chart + side panel)

```html
<div style="display:grid;grid-template-columns:2fr 1fr;gap:16px">

  <!-- LEFT — primary area/line chart -->
  <div class="glass-card" style="padding:24px">
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:16px">
      <span style="font-size:14px;font-weight:700">{Chart title}</span>
      <!-- Period-tab strip -->
      <div style="display:flex;gap:4px;background:rgba(255,255,255,0.04);border:1px solid var(--glass-border);border-radius:99px;padding:3px" role="tablist" aria-label="Time period">
        <button style="font-size:11px;font-weight:600;padding:4px 10px;border-radius:99px;border:none;font-family:inherit;background:var(--accent-cyan);color:#0f0c29;cursor:pointer" role="tab" aria-selected="true">1H</button>
        <button style="font-size:11px;font-weight:600;padding:4px 10px;border-radius:99px;border:none;font-family:inherit;background:transparent;color:var(--text-muted);cursor:pointer" role="tab" aria-selected="false">24H</button>
        <button style="font-size:11px;font-weight:600;padding:4px 10px;border-radius:99px;border:none;font-family:inherit;background:transparent;color:var(--text-muted);cursor:pointer" role="tab" aria-selected="false">7D</button>
        <button style="font-size:11px;font-weight:600;padding:4px 10px;border-radius:99px;border:none;font-family:inherit;background:transparent;color:var(--text-muted);cursor:pointer" role="tab" aria-selected="false">30D</button>
      </div>
    </div>
    <!-- Legend row -->
    <div style="display:flex;gap:16px;margin-bottom:16px">
      <span style="display:flex;align-items:center;gap:6px;font-size:11px;color:var(--text-muted)"><span style="width:8px;height:8px;border-radius:50%;background:var(--chart-1);display:inline-block"></span>{Series A}</span>
      <span style="display:flex;align-items:center;gap:6px;font-size:11px;color:var(--text-muted)"><span style="width:8px;height:8px;border-radius:50%;background:var(--chart-2);display:inline-block"></span>{Series B}</span>
    </div>
    <!-- Inline SVG area chart — 600×180 viewBox, multiple series -->
    <svg width="100%" height="180" viewBox="0 0 600 180" preserveAspectRatio="none" aria-label="{Chart title}" role="img">
      <defs>
        <linearGradient id="area1" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="var(--chart-1)" stop-opacity="0.25"/><stop offset="100%" stop-color="var(--chart-1)" stop-opacity="0"/></linearGradient>
        <linearGradient id="area2" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="var(--chart-2)" stop-opacity="0.18"/><stop offset="100%" stop-color="var(--chart-2)" stop-opacity="0"/></linearGradient>
      </defs>
      <!-- Horizontal grid lines -->
      <line x1="0" y1="36"  x2="600" y2="36"  stroke="rgba(255,255,255,0.05)" stroke-width="1"/>
      <line x1="0" y1="72"  x2="600" y2="72"  stroke="rgba(255,255,255,0.05)" stroke-width="1"/>
      <line x1="0" y1="108" x2="600" y2="108" stroke="rgba(255,255,255,0.05)" stroke-width="1"/>
      <line x1="0" y1="144" x2="600" y2="144" stroke="rgba(255,255,255,0.05)" stroke-width="1"/>
      <!-- Series A area — replace path with real data curve -->
      <path d="M0 130 C100 100 200 80 300 60 C400 40 500 30 600 20" fill="none" stroke="var(--chart-1)" stroke-width="2"/>
      <path d="M0 130 C100 100 200 80 300 60 C400 40 500 30 600 20 L600 180 L0 180Z" fill="url(#area1)"/>
      <!-- Series B area -->
      <path d="M0 150 C100 130 200 115 300 95 C400 75 500 65 600 55" fill="none" stroke="var(--chart-2)" stroke-width="2"/>
      <path d="M0 150 C100 130 200 115 300 95 C400 75 500 65 600 55 L600 180 L0 180Z" fill="url(#area2)"/>
    </svg>
  </div>

  <!-- RIGHT — live alerts / side panel -->
  <div class="glass-card" style="padding:20px;display:flex;flex-direction:column">
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:16px">
      <span style="font-size:13px;font-weight:700">{Panel title}</span>
      <a href="#" style="font-size:11px;color:var(--accent-cyan);text-decoration:none;opacity:0.8">View all</a>
    </div>
    <!-- Alert row: [accent dot] [message + strong entity] [elapsed] -->
    <!-- Repeat 5-6 times; use var(--accent-rose/amber/cyan/emerald/violet) for dot -->
    <div style="display:flex;align-items:flex-start;gap:10px;padding:10px 0;border-bottom:1px solid rgba(255,255,255,0.05)">
      <span style="width:8px;height:8px;border-radius:50%;background:var(--accent-rose);flex-shrink:0;margin-top:4px" aria-hidden="true"></span>
      <div>
        <div style="font-size:12px;line-height:1.45">{Event message — <strong>{entity}</strong>}</div>
        <div style="font-size:10px;color:var(--text-muted);margin-top:2px">{elapsed}</div>
      </div>
    </div>
    <!-- more alert rows -->
  </div>

</div>
```

---

## Records table (dashboard footer or list screen)

```html
<div class="glass-card" style="padding:24px">
  <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:16px">
    <span style="font-size:14px;font-weight:700">{Records title}</span>
    <div style="display:flex;gap:8px;align-items:center">
      <button class="btn-ghost">Export</button>
      <button class="btn-primary">+ {New record}</button>
    </div>
  </div>
  <table style="width:100%;border-collapse:collapse">
    <thead>
      <tr>
        <th style="font-size:10px;font-weight:600;text-transform:uppercase;letter-spacing:0.08em;color:var(--text-faint);text-align:left;padding:0 12px 10px;border-bottom:1px solid rgba(255,255,255,0.06)">{Entity}</th>
        <th style="font-size:10px;font-weight:600;text-transform:uppercase;letter-spacing:0.08em;color:var(--text-faint);text-align:left;padding:0 12px 10px;border-bottom:1px solid rgba(255,255,255,0.06)">{Category}</th>
        <th style="font-size:10px;font-weight:600;text-transform:uppercase;letter-spacing:0.08em;color:var(--text-faint);text-align:right;padding:0 12px 10px;border-bottom:1px solid rgba(255,255,255,0.06)">{Value}</th>
        <th style="font-size:10px;font-weight:600;text-transform:uppercase;letter-spacing:0.08em;color:var(--text-faint);text-align:left;padding:0 12px 10px;border-bottom:1px solid rgba(255,255,255,0.06)">{Dim}</th>
        <th style="font-size:10px;font-weight:600;text-transform:uppercase;letter-spacing:0.08em;color:var(--text-faint);text-align:left;padding:0 12px 10px;border-bottom:1px solid rgba(255,255,255,0.06)">Status</th>
      </tr>
    </thead>
    <tbody>
      <tr style="transition:background 0.12s">
        <!-- Entity cell: icon chip + name + sub -->
        <td style="padding:13px 12px;font-size:13px;border-bottom:1px solid rgba(255,255,255,0.04);vertical-align:middle">
          <div style="display:flex;align-items:center;gap:10px">
            <div style="width:30px;height:30px;border-radius:8px;display:flex;align-items:center;justify-content:center;flex-shrink:0;background:rgba(34,211,238,0.12);color:var(--accent-cyan)">
              <!-- inline SVG icon -->
            </div>
            <div>
              <div style="font-weight:600;font-size:13px">{name}</div>
              <div style="font-size:11px;color:var(--text-muted)">{sub}</div>
            </div>
          </div>
        </td>
        <td style="padding:13px 12px;font-size:13px;border-bottom:1px solid rgba(255,255,255,0.04);color:var(--text-muted)">{category}</td>
        <td style="padding:13px 12px;font-size:13px;border-bottom:1px solid rgba(255,255,255,0.04);text-align:right;font-variant-numeric:tabular-nums">{value}</td>
        <td style="padding:13px 12px;font-size:13px;border-bottom:1px solid rgba(255,255,255,0.04);color:var(--text-muted)">{dim}</td>
        <td style="padding:13px 12px;font-size:13px;border-bottom:1px solid rgba(255,255,255,0.04)">
          <!-- Status pill variants: pill-active / pill-pending / pill-critical / pill-info -->
          <span class="pill pill-active">Active</span>
        </td>
      </tr>
      <!-- more rows; last row: no border-bottom on td -->
    </tbody>
  </table>
</div>
```

### List toolbar (search + filter chips)

```html
<div style="display:flex;align-items:center;gap:12px;flex-wrap:wrap;padding:16px 20px;border-bottom:1px solid rgba(255,255,255,0.06)">
  <!-- Frosted pill search -->
  <div style="position:relative;flex:1;min-width:200px;max-width:340px">
    <svg style="position:absolute;left:11px;top:50%;transform:translateY(-50%);color:var(--text-faint)" width="14" height="14" viewBox="0 0 14 14" fill="none" aria-hidden="true"><circle cx="6" cy="6" r="4.5" stroke="currentColor" stroke-width="1.3"/><path d="M9.5 9.5L13 13" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"/></svg>
    <input type="text" placeholder="Filter by {fields}…" aria-label="Filter records"
      style="width:100%;padding:8px 12px 8px 34px;background:rgba(255,255,255,0.06);border:1px solid var(--glass-border);border-radius:99px;color:var(--text-primary);font-size:13px;font-family:inherit;outline:none;transition:border-color 0.15s">
  </div>
  <!-- Filter chips group -->
  <div style="display:flex;align-items:center;gap:8px">
    <span style="font-size:11px;color:var(--text-faint);font-weight:600;text-transform:uppercase;letter-spacing:0.06em">{Facet}</span>
    <!-- Active chip -->
    <span style="font-size:11px;font-weight:600;padding:4px 10px;border-radius:99px;background:rgba(34,211,238,0.14);color:var(--accent-cyan);border:1px solid rgba(34,211,238,0.3);cursor:pointer">All <span style="opacity:0.7">{n}</span></span>
    <!-- Inactive chip -->
    <span style="font-size:11px;font-weight:600;padding:4px 10px;border-radius:99px;background:transparent;color:var(--text-muted);border:1px solid var(--glass-border);cursor:pointer;transition:background 0.15s,color 0.15s">{Value} <span style="opacity:0.7">{n}</span></span>
  </div>
  <span style="margin-left:auto;font-size:12px;color:var(--text-muted)">{n} records</span>
</div>
```

### Pager footer

```html
<div style="display:flex;align-items:center;justify-content:space-between;padding:14px 16px;border-top:1px solid rgba(255,255,255,0.06);font-size:12px;color:var(--text-muted)">
  <span>Showing {a}–{b} of {n}</span>
  <div style="display:flex;gap:4px">
    <button style="width:28px;height:28px;border-radius:8px;background:transparent;border:1px solid var(--glass-border);color:var(--text-muted);font-size:12px;font-weight:600;font-family:inherit;cursor:pointer;display:flex;align-items:center;justify-content:center;transition:background 0.15s,color 0.15s" aria-label="Previous">‹</button>
    <button style="width:28px;height:28px;border-radius:8px;background:rgba(34,211,238,0.14);border:1px solid rgba(34,211,238,0.3);color:var(--accent-cyan);font-size:12px;font-weight:600;font-family:inherit;cursor:pointer;display:flex;align-items:center;justify-content:center" aria-current="page">1</button>
    <button style="width:28px;height:28px;border-radius:8px;background:transparent;border:1px solid var(--glass-border);color:var(--text-muted);font-size:12px;font-weight:600;font-family:inherit;cursor:pointer;display:flex;align-items:center;justify-content:center;transition:background 0.15s,color 0.15s">2</button>
    <button style="width:28px;height:28px;border-radius:8px;background:transparent;border:1px solid var(--glass-border);color:var(--text-muted);font-size:12px;font-weight:600;font-family:inherit;cursor:pointer;display:flex;align-items:center;justify-content:center;transition:background 0.15s,color 0.15s" aria-label="Next">›</button>
  </div>
</div>
```

---

## Record form — fields with inline validation

Rules live ON the field: a required mark (`*`), helper text, and an inline error
message on an invalid field. The submit stays `disabled` until the form is valid.
Never add a separate rules / validation-status summary panel.

Suggested CSS additions to `template.html`:

```css
.field-grid { display:grid; grid-template-columns:1fr 1fr; gap:16px; }
.field { display:flex; flex-direction:column; gap:6px; }
.field.full { grid-column: 1 / -1; }
.field-label { font-size:12px; font-weight:600; color:var(--text-muted); }
.req { color:var(--accent-rose); margin-left:2px; }
.control { padding:9px 12px; background:rgba(255,255,255,0.06); border:1px solid var(--glass-border); border-radius:var(--radius-sm); color:var(--text-primary); font-size:13px; font-family:inherit; outline:none; transition:border-color 0.15s,background 0.15s; -webkit-appearance:none; }
.control::placeholder { color:var(--text-faint); }
.control:focus { border-color:rgba(34,211,238,0.4); background:rgba(255,255,255,0.09); }
.helper { font-size:11px; color:var(--text-faint); }
.field.invalid .control { border-color:rgba(244,114,182,0.5); background:rgba(244,114,182,0.05); }
.error-msg { display:flex; align-items:center; gap:5px; font-size:11px; color:var(--accent-rose); font-weight:500; }
```

```html
<form class="glass-card" style="padding:24px" novalidate>
  <div style="font-size:13px;font-weight:700;text-transform:uppercase;letter-spacing:0.06em;color:var(--text-muted);margin-bottom:20px;padding-bottom:12px;border-bottom:1px solid rgba(255,255,255,0.06)">{Section title}</div>

  <div class="field-grid">

    <!-- Valid field with helper text -->
    <div class="field">
      <label class="field-label" for="f1">{Label} <span class="req">*</span></label>
      <input id="f1" class="control" type="text" value="{value}" placeholder="{hint}">
      <span class="helper">{What the value drives or format constraint}</span>
    </div>

    <!-- Invalid field: add class="field invalid" + aria-invalid + .error-msg -->
    <div class="field invalid">
      <label class="field-label" for="f2">{Label} <span class="req">*</span></label>
      <input id="f2" class="control" type="text" value="" aria-invalid="true" aria-describedby="f2-err" placeholder="{hint}">
      <span class="error-msg" id="f2-err">
        <svg width="12" height="12" viewBox="0 0 12 12" fill="none" aria-hidden="true"><circle cx="6" cy="6" r="5" stroke="currentColor" stroke-width="1.3"/><path d="M6 4v2.5M6 8.5v.2" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"/></svg>
        {Specific rule that failed}
      </span>
    </div>

    <!-- Required select -->
    <div class="field">
      <label class="field-label" for="f3">{Label} <span class="req">*</span></label>
      <select id="f3" class="control" style="background-image:url(\"data:image/svg+xml,%3Csvg width='10' height='6' viewBox='0 0 10 6' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M1 1L5 5L9 1' stroke='rgba(255,255,255,0.4)' stroke-width='1.5' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E\");background-repeat:no-repeat;background-position:right 12px center;padding-right:32px">
        <option value="">Select…</option>
        <option value="a">{Option A}</option>
      </select>
      <span class="helper">{Constraint on the options}</span>
    </div>

  </div>

  <div style="display:flex;align-items:center;justify-content:space-between;margin-top:20px;padding-top:16px;border-top:1px solid rgba(255,255,255,0.06)">
    <span style="font-size:12px;color:var(--text-muted)">Fields marked <span class="req">*</span> are required.</span>
    <div style="display:flex;gap:10px">
      <button type="button" class="btn-ghost">Cancel</button>
      <button type="submit" class="btn-primary" disabled aria-disabled="true">{Submit action}</button>
    </div>
  </div>
</form>
```

---

## Record detail — header + meta grid + related panels

```html
<!-- Detail header band -->
<div class="glass-card" style="display:flex;align-items:flex-start;justify-content:space-between;gap:16px;padding:24px">
  <div>
    <div style="display:flex;align-items:center;gap:10px;margin-bottom:6px">
      <span style="font-size:13px;font-weight:600;color:var(--text-faint);font-family:'Courier New',monospace">{ID}</span>
      <!-- Status pill: .pill-active / .pill-pending / .pill-critical / .pill-info -->
      <span class="pill pill-active">{State}</span>
    </div>
    <div style="font-size:20px;font-weight:700;letter-spacing:-0.02em">{Record name}</div>
    <div style="font-size:12px;color:var(--text-muted);margin-top:4px">{key · dimension · context}</div>
  </div>
  <div style="display:flex;gap:10px;flex-shrink:0;align-items:flex-start">
    <button class="btn-ghost">{Secondary action}</button>
    <button class="btn-primary">Edit</button>
  </div>
</div>

<!-- Meta grid: 3-col label/value cells -->
<div class="glass-card">
  <!-- 3-col grid; cells separated by subtle inner borders -->
  <div style="display:grid;grid-template-columns:repeat(3,1fr)">
    <div style="padding:14px 16px;border-right:1px solid rgba(255,255,255,0.05);border-bottom:1px solid rgba(255,255,255,0.05)">
      <div style="font-size:10px;font-weight:600;text-transform:uppercase;letter-spacing:0.08em;color:var(--text-faint);margin-bottom:6px">{FIELD}</div>
      <div style="font-size:13px;font-weight:600">{value}</div>
      <div style="font-size:11px;color:var(--text-muted);margin-top:2px">{sub}</div>
    </div>
    <!-- more cells; nth-child(3n) = border-right:none; nth-last-child(-n+3) = border-bottom:none -->
  </div>
</div>

<!-- Related data panels: 2-col (2fr/1fr) -->
<div style="display:grid;grid-template-columns:2fr 1fr;gap:16px">
  <div class="glass-card" style="padding:20px">
    <div style="font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:0.07em;color:var(--text-muted);margin-bottom:14px;padding-bottom:10px;border-bottom:1px solid rgba(255,255,255,0.06)">{Related data title}</div>
    <!-- sub-table or status-board rows -->
  </div>
  <div class="glass-card" style="padding:20px">
    <div style="font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:0.07em;color:var(--text-muted);margin-bottom:14px;padding-bottom:10px;border-bottom:1px solid rgba(255,255,255,0.06)">Activity</div>
    <!-- activity feed rows: [icon chip] [message + time] -->
  </div>
</div>
```
