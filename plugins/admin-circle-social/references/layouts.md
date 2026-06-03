# Circle Admin — layout skeletons

Paste-ready, domain-neutral fragments for the Circle friendly light-mode skin.
Each skeleton is labelled by archetype slot, not by a domain noun. Copy the shell
from `assets/template.html` first (it carries the `:root` tokens + sidebar + topbar
+ page-body slot), then drop the region skeletons below into the
`<div class="page-body">`. Replace every `{placeholder}` with the real domain's
equivalent.

Token recap (full block in `template.html`): canvas `#f8f9fc`, card `#ffffff`,
sidebar `#ffffff`, hairline `#e8eaf2`; text `#0f172a / #334155 / #64748b / #94a3b8`;
accent blue `var(--accent-blue)` = `#3b82f6`; accent violet `var(--accent-violet)`
= `#8b5cf6`; status tokens `--status-{green/amber/red}` with `…-soft` tints.

---

## Page header (every screen)

```html
<div class="page-header">
  <div>
    <div class="page-title">{Screen title}</div>
    <div class="page-subtitle">{Context · scope · updated timestamp}</div>
  </div>
  <div class="header-actions">
    <button class="btn btn-ghost">{Secondary action}</button>
    <button class="btn btn-primary">+ {Primary action}</button>
  </div>
</div>
```

---

## KPI card row (4 cards, equal `1fr` grid)

```html
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:16px">

  <div class="kpi-card" style="background:#fff;border:1px solid #e8eaf2;border-radius:12px;padding:18px 20px 14px;display:flex;flex-direction:column;gap:8px;box-shadow:0 1px 4px rgba(0,0,0,0.04)">
    <div style="display:flex;align-items:center;justify-content:space-between">
      <span style="font-size:11px;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;color:#94a3b8">{METRIC LABEL}</span>
      <!-- inline SVG icon, stroke=var(--accent-blue) or var(--accent-violet) -->
    </div>
    <div style="font-size:28px;font-weight:800;color:#0f172a;letter-spacing:-0.02em;line-height:1;font-variant-numeric:tabular-nums">{Figure}</div>
    <div style="display:flex;align-items:center;justify-content:space-between;gap:8px">
      <!-- delta-up: background:var(--status-green-soft);color:#16a34a -->
      <!-- delta-down: background:var(--status-red-soft);color:#dc2626 -->
      <span style="display:inline-flex;align-items:center;gap:3px;font-size:12px;font-weight:600;padding:2px 7px;border-radius:999px;background:var(--status-green-soft);color:#16a34a">
        <!-- arrow SVG --> {±delta}
      </span>
      <!-- 5-point sparkline SVG, 64×24, stroke=var(--accent-blue) -->
    </div>
  </div>

  <!-- Repeat ×3 -->
</div>
```

---

## 2-column mid row (action-queue + side panel)

```html
<div style="display:grid;grid-template-columns:1fr 300px;gap:16px;align-items:start">

  <!-- Action-queue card -->
  <div class="card">
    <div class="card-header">
      <span class="card-title">{Queue title}</span>
      <span class="badge badge-red">{N pending}</span>
    </div>
    <div style="padding:12px 16px;display:flex;flex-direction:column;gap:12px">

      <!-- Item card -->
      <div style="border:1px solid #e8eaf2;border-radius:10px;padding:14px 16px;display:flex;flex-direction:column;gap:10px">
        <!-- Meta row: avatar + label + source + timestamp -->
        <div style="display:flex;align-items:center;gap:8px;flex-wrap:wrap">
          <div class="avatar-circle av-amber" style="width:28px;height:28px;font-size:11px">{Initials}</div>
          <span style="font-size:13px;font-weight:600;color:#0f172a">{Entity label}</span>
          <span style="font-size:11px;color:#94a3b8">{Source / reporter}</span>
          <span style="font-size:11px;color:#94a3b8;margin-left:auto">{Elapsed}</span>
        </div>
        <!-- Excerpt -->
        <div style="font-size:13px;color:#475569;font-style:italic;line-height:1.5">"{Content excerpt}"</div>
        <!-- Actions + reason -->
        <div style="display:flex;align-items:center;gap:8px;flex-wrap:wrap">
          <button class="btn btn-green-ghost btn-sm">
            <!-- checkmark SVG --> {Positive action}
          </button>
          <button class="btn btn-red btn-sm">
            <!-- X SVG --> {Negative action}
          </button>
          <!-- Reason pill pushed right -->
          <span style="margin-left:auto"><span class="badge badge-amber">{Reason}</span></span>
        </div>
      </div>
      <!-- Repeat item cards -->

    </div>
  </div>

  <!-- Side panel: 2 stacked cards -->
  <div style="display:flex;flex-direction:column;gap:16px">

    <!-- Ranked list card -->
    <div class="card">
      <div class="card-header">
        <span class="card-title">{Rank panel title}</span>
        <span class="badge badge-violet">{Period}</span>
      </div>
      <div style="padding:12px 16px;display:flex;flex-direction:column;gap:10px">
        <!-- rank item -->
        <div style="display:flex;flex-direction:column;gap:4px">
          <div style="display:flex;align-items:center;justify-content:space-between">
            <span style="font-size:13px;font-weight:600;color:var(--accent-violet)">{Label}</span>
            <span style="font-size:12px;color:#94a3b8">{Count}</span>
          </div>
          <div style="height:5px;background:#f1f5f9;border-radius:999px;overflow:hidden">
            <div style="height:100%;border-radius:999px;background:var(--accent-violet);width:{pct}%"></div>
          </div>
        </div>
        <!-- Repeat rank items -->
      </div>
    </div>

    <!-- Notable items card -->
    <div class="card">
      <div class="card-header">
        <span class="card-title">{Notable panel title}</span>
        <span class="badge badge-red">{N}</span>
      </div>
      <div style="padding:12px 16px;display:flex;flex-direction:column;gap:10px">
        <!-- notable item -->
        <div style="display:flex;align-items:center;gap:10px">
          <div class="avatar-circle av-amber" style="width:32px;height:32px;font-size:12px">{Initials}</div>
          <div style="flex:1;min-width:0">
            <div style="font-size:13px;font-weight:600;color:#0f172a">{Name/handle}</div>
            <div style="font-size:11px;color:#94a3b8">{Meta line}</div>
          </div>
          <a href="#" style="font-size:12px;font-weight:600;color:var(--accent-blue);text-decoration:none">Review</a>
        </div>
        <!-- Repeat notable items -->
      </div>
    </div>

  </div>

</div>
```

---

## Engagement / trend chart

```html
<div class="card">
  <div class="card-header">
    <span class="card-title">{Chart title}</span>
    <span style="font-size:12px;color:#94a3b8">{Period label}</span>
  </div>
  <div style="padding:16px 20px 20px">
    <!-- Legend -->
    <div style="display:flex;gap:16px;margin-bottom:14px">
      <div style="display:flex;align-items:center;gap:6px;font-size:12px;color:#64748b">
        <span style="width:10px;height:10px;border-radius:50%;flex-shrink:0;background:var(--chart-line)"></span>
        {Series 1 label}
      </div>
      <div style="display:flex;align-items:center;gap:6px;font-size:12px;color:#64748b">
        <span style="width:10px;height:10px;border-radius:50%;flex-shrink:0;background:var(--chart-violet)"></span>
        {Series 2 label}
      </div>
    </div>
    <!-- Inline SVG area chart: viewBox 520 140
         Regions: x 40–510 (plot area), y 16–120 (grid top to baseline)
         5 horizontal grid lines at y=16,44,72,100,120
         y-axis labels at x=32, x-axis labels at y=136 -->
    <svg style="width:100%;display:block" viewBox="0 0 520 140" preserveAspectRatio="xMidYMid meet">
      <!-- grid lines -->
      <line x1="40" y1="16"  x2="510" y2="16"  stroke="#e8eaf2" stroke-width="1"/>
      <line x1="40" y1="44"  x2="510" y2="44"  stroke="#e8eaf2" stroke-width="1"/>
      <line x1="40" y1="72"  x2="510" y2="72"  stroke="#e8eaf2" stroke-width="1"/>
      <line x1="40" y1="100" x2="510" y2="100" stroke="#e8eaf2" stroke-width="1"/>
      <line x1="40" y1="120" x2="510" y2="120" stroke="#e8eaf2" stroke-width="1"/>
      <!-- y-axis labels -->
      <text x="32" y="20"  text-anchor="end" font-size="10" fill="#94a3b8" font-family="system-ui,sans-serif">{max}</text>
      <text x="32" y="124" text-anchor="end" font-size="10" fill="#94a3b8" font-family="system-ui,sans-serif">0</text>
      <!-- x-axis labels (7 points: Mon–Sun or domain equivalent) -->
      <text x="74"  y="136" text-anchor="middle" font-size="10" fill="#94a3b8" font-family="system-ui,sans-serif">{T1}</text>
      <text x="143" y="136" text-anchor="middle" font-size="10" fill="#94a3b8" font-family="system-ui,sans-serif">{T2}</text>
      <text x="212" y="136" text-anchor="middle" font-size="10" fill="#94a3b8" font-family="system-ui,sans-serif">{T3}</text>
      <text x="281" y="136" text-anchor="middle" font-size="10" fill="#94a3b8" font-family="system-ui,sans-serif">{T4}</text>
      <text x="350" y="136" text-anchor="middle" font-size="10" fill="#94a3b8" font-family="system-ui,sans-serif">{T5}</text>
      <text x="419" y="136" text-anchor="middle" font-size="10" fill="#94a3b8" font-family="system-ui,sans-serif">{T6}</text>
      <text x="488" y="136" text-anchor="middle" font-size="10" fill="#94a3b8" font-family="system-ui,sans-serif">{T7}</text>
      <defs>
        <linearGradient id="areaBlue" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stop-color="#3b82f6" stop-opacity="0.18"/>
          <stop offset="100%" stop-color="#3b82f6" stop-opacity="0.02"/>
        </linearGradient>
        <linearGradient id="areaViolet" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stop-color="#8b5cf6" stop-opacity="0.15"/>
          <stop offset="100%" stop-color="#8b5cf6" stop-opacity="0.02"/>
        </linearGradient>
      </defs>
      <!-- Series 1 (blue): fill + stroke + circles -->
      <!-- <path d="M{x1},{y1} L{x2},{y2} … L{x7},{y7} L{x7},120 L{x1},120 Z" fill="url(#areaBlue)"/> -->
      <!-- <path d="M{x1},{y1} L…" stroke="#3b82f6" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/> -->
      <!-- Series 2 (violet dashed): fill + stroke -->
      <!-- <path d="…" stroke="#8b5cf6" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="4 2"/> -->
    </svg>
  </div>
</div>
```

---

## Records table (dashboard footer or list screen)

```html
<div class="card">
  <div class="card-header">
    <span class="card-title">{Records title}</span>
    <div style="display:flex;gap:8px;align-items:center">
      <button class="btn btn-ghost btn-sm">{Export}</button>
      <button class="btn btn-primary btn-sm">+ {New}</button>
    </div>
  </div>
  <div class="table-wrap">
    <table>
      <thead>
        <tr>
          <th>{Entity (avatar + name + handle)}</th>
          <th>{Role / type pill}</th>
          <th>{Date}</th>
          <th>{Secondary date}</th>
          <th style="text-align:right">{Numeric}</th>
          <th>{Status pill}</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <!-- avatar cell -->
          <td>
            <div style="display:flex;align-items:center;gap:10px">
              <div class="avatar-circle av-blue" style="width:34px;height:34px;font-size:13px">{Initials}</div>
              <div>
                <div style="font-size:13.5px;font-weight:600;color:#0f172a">{Name}</div>
                <div style="font-size:11.5px;color:#94a3b8">{Handle or sub-label}</div>
              </div>
            </div>
          </td>
          <td><span class="pill" style="background:var(--accent-blue-soft);color:var(--accent-blue)">{Role}</span></td>
          <td style="color:#64748b;font-variant-numeric:tabular-nums">{Date}</td>
          <td style="color:#64748b">{Secondary date / elapsed}</td>
          <td style="text-align:right;font-variant-numeric:tabular-nums;color:#334155">{Numeric}</td>
          <td>
            <!-- Status pill variants:
                 Active:    background:var(--status-green-soft); color:#16a34a
                 Pending:   background:var(--status-amber-soft); color:#d97706
                 Suspended: background:var(--status-red-soft);   color:#dc2626  -->
            <span class="pill" style="background:var(--status-green-soft);color:#16a34a">{Status}</span>
          </td>
        </tr>
        <!-- Repeat rows -->
      </tbody>
    </table>
  </div>
  <!-- Table footer (list screen; omit on dashboard) -->
  <div style="display:flex;align-items:center;justify-content:space-between;padding:12px 20px;border-top:1px solid #e8eaf2;background:#fafbfc">
    <span style="font-size:12px;color:#64748b">Showing {a}–{b} of {n}</span>
    <div style="display:flex;align-items:center;gap:4px">
      <!-- page-btn: min-width:32px;height:32px;border-radius:7px;border:1px solid #e8eaf2;background:#fff;
                    font-size:13px;font-weight:600;color:#475569;cursor:pointer;font-family:inherit -->
      <button style="min-width:32px;height:32px;padding:0 8px;border-radius:7px;border:1px solid #e8eaf2;background:#fff;font-size:13px;font-weight:600;color:#475569;cursor:pointer;font-family:inherit">‹</button>
      <button style="min-width:32px;height:32px;padding:0 8px;border-radius:7px;border:1px solid var(--accent-blue);background:var(--accent-blue);font-size:13px;font-weight:600;color:#fff;cursor:pointer;font-family:inherit">1</button>
      <button style="min-width:32px;height:32px;padding:0 8px;border-radius:7px;border:1px solid #e8eaf2;background:#fff;font-size:13px;font-weight:600;color:#475569;cursor:pointer;font-family:inherit">2</button>
      <button style="min-width:32px;height:32px;padding:0 8px;border-radius:7px;border:1px solid #e8eaf2;background:#fff;font-size:13px;font-weight:600;color:#475569;cursor:pointer;font-family:inherit">›</button>
    </div>
  </div>
</div>
```

### List toolbar (search + filter chips)

```html
<div style="display:flex;align-items:center;gap:12px;flex-wrap:wrap">
  <!-- Search box -->
  <div style="position:relative;flex:1;min-width:200px;max-width:360px">
    <!-- magnifier SVG at left:10px -->
    <input type="text" placeholder="Filter by {fields}…"
      style="width:100%;padding:8px 12px 8px 32px;border:1px solid #e8eaf2;border-radius:8px;font-size:13px;font-family:inherit;color:#334155;background:#fff;outline:none">
  </div>
  <!-- Filter chips -->
  <div style="display:flex;align-items:center;gap:6px;flex-wrap:wrap">
    <span style="font-size:12px;color:#64748b;font-weight:500">{Facet}:</span>
    <!-- Active chip: background:var(--accent-blue-soft);border-color:#bfdbfe;color:var(--accent-blue) -->
    <span style="display:inline-flex;align-items:center;gap:4px;padding:4px 10px;border-radius:999px;font-size:12px;font-weight:600;cursor:pointer;border:1px solid #bfdbfe;background:var(--accent-blue-soft);color:var(--accent-blue)">
      All <span style="font-size:11px;font-weight:700;background:#bfdbfe;padding:1px 5px;border-radius:999px">{n}</span>
    </span>
    <span style="display:inline-flex;align-items:center;gap:4px;padding:4px 10px;border-radius:999px;font-size:12px;font-weight:600;cursor:pointer;border:1px solid #e8eaf2;background:#fff;color:#64748b">
      {Value} <span style="font-size:11px;font-weight:700;background:#e8eaf2;padding:1px 5px;border-radius:999px">{n}</span>
    </span>
  </div>
</div>
```

---

## Record form — fields with inline validation

Rules live ON the field: required mark (`*`), helper text below the field, and an
inline error on invalid fields. Submit stays `disabled` until form is valid. Never
add a separate rules/validation-status summary panel.

```html
<form style="display:flex;flex-direction:column;gap:16px;max-width:720px" novalidate>

  <div class="card">
    <div style="display:flex;align-items:center;gap:8px;padding:16px 20px;border-bottom:1px solid #e8eaf2;font-size:13.5px;font-weight:700;color:#0f172a">
      <!-- inline SVG glyph --> {Section title}
    </div>
    <div style="padding:20px">
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px 20px">

        <!-- Valid field -->
        <div class="field">
          <label class="field-label" for="f1">{Label} <span class="req">*</span></label>
          <input id="f1" class="control" type="text" value="{value}">
          <span class="helper">{What the value drives / format hint}</span>
        </div>

        <!-- Invalid field -->
        <div class="field invalid">
          <label class="field-label" for="f2">{Label} <span class="req">*</span></label>
          <input id="f2" class="control" type="text" aria-invalid="true" aria-describedby="f2-err">
          <span class="error-msg" id="f2-err">
            <!-- alert SVG --> {Specific rule that failed}
          </span>
        </div>

        <!-- Required select -->
        <div class="field">
          <label class="field-label" for="f3">{Label} <span class="req">*</span></label>
          <select id="f3" class="control">
            <option value="">Select…</option>
            <option>{Option}</option>
          </select>
          <span class="helper">{Constraint on the options}</span>
        </div>

        <!-- Optional textarea (full-width) -->
        <div class="field" style="grid-column:1/-1">
          <label class="field-label" for="f4">{Label} <span style="font-size:11px;font-weight:500;color:#94a3b8;margin-left:4px">(optional)</span></label>
          <textarea id="f4" class="control" style="resize:vertical;min-height:80px" placeholder="{Placeholder}"></textarea>
          <span class="helper">{Helper text}</span>
        </div>

      </div>
    </div>

    <div style="display:flex;align-items:center;justify-content:space-between;gap:12px;padding:16px 20px;background:#fafbfc;border-top:1px solid #e8eaf2;border-radius:0 0 12px 12px">
      <span style="font-size:12px;color:#64748b">Fields marked <span class="req">*</span> are required.</span>
      <div style="display:flex;gap:8px">
        <button type="button" class="btn btn-ghost">Cancel</button>
        <button type="submit" class="btn btn-primary" disabled>{Submit}</button>
      </div>
    </div>
  </div>

</form>
```

---

## Record detail — header + meta grid + related panels

```html
<!-- Detail header -->
<div style="display:flex;align-items:center;gap:16px;background:#fff;border:1px solid #e8eaf2;border-radius:12px;padding:20px 24px;box-shadow:0 1px 4px rgba(0,0,0,0.04)">
  <div class="avatar-circle av-violet" style="width:56px;height:56px;font-size:20px">{Initials}</div>
  <div style="flex:1;min-width:0">
    <div style="display:flex;align-items:center;gap:10px;flex-wrap:wrap">
      <span style="font-size:20px;font-weight:700;color:#0f172a">{Name}</span>
      <span style="font-size:14px;color:#94a3b8">{Handle/code}</span>
      <!-- role pill -->
      <span class="pill" style="background:var(--accent-violet-soft);color:var(--accent-violet)">{Role}</span>
      <!-- status pill -->
      <span class="pill" style="background:var(--status-green-soft);color:#16a34a">{Status}</span>
    </div>
    <div style="font-size:13px;color:#64748b;margin-top:4px">{Sub-line: membership / context}</div>
  </div>
  <div style="display:flex;gap:8px;flex-shrink:0">
    <button class="btn btn-ghost">Edit</button>
    <button class="btn btn-danger">{Negative action}</button>
  </div>
</div>

<!-- Meta grid (3 columns) -->
<div class="card">
  <div style="display:grid;grid-template-columns:repeat(3,1fr)">
    <!-- meta cell -->
    <div style="padding:16px 20px;border-right:1px solid #f1f5f9;border-bottom:1px solid #f1f5f9">
      <div style="font-size:10.5px;font-weight:700;letter-spacing:0.06em;text-transform:uppercase;color:#94a3b8;margin-bottom:4px">{FIELD}</div>
      <div style="font-size:14px;font-weight:600;color:#0f172a">{Value}</div>
      <div style="font-size:11.5px;color:#94a3b8;margin-top:2px">{Sub}</div>
    </div>
    <!-- Repeat cells; nth-child(3n) has no border-right; last row has no border-bottom -->
  </div>
</div>

<!-- Two-col related panels -->
<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;align-items:start">

  <!-- Stats / sub-table card -->
  <div class="card">
    <div class="card-header">
      <span class="card-title">{Sub-panel title}</span>
      <span style="font-size:12px;color:#94a3b8">{Period}</span>
    </div>
    <div class="table-wrap">
      <table>
        <thead><tr><th>{Col}</th><th>{Col}</th><th style="text-align:right">{Numeric}</th></tr></thead>
        <tbody>
          <tr>
            <td style="color:#0f172a;font-weight:500">{Row label}</td>
            <td><span class="pill" style="background:var(--accent-blue-soft);color:var(--accent-blue);font-size:11px">{Tag}</span></td>
            <td style="text-align:right;font-variant-numeric:tabular-nums">{N}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- Activity timeline card -->
  <div class="card">
    <div class="card-header"><span class="card-title">Recent Activity</span></div>
    <div style="padding:4px 20px 16px;display:flex;flex-direction:column">
      <div style="display:flex;gap:12px;padding:12px 0;border-bottom:1px solid #f1f5f9">
        <div style="padding-top:3px">
          <div style="width:8px;height:8px;border-radius:50%;background:var(--accent-blue)"></div>
        </div>
        <div style="flex:1;min-width:0">
          <div style="font-size:13px;color:#334155;line-height:1.4">{Action description}</div>
          <div style="font-size:11.5px;color:#94a3b8;margin-top:2px">{Elapsed · timestamp}</div>
        </div>
      </div>
      <!-- Repeat activity rows; last row: no border-bottom -->
    </div>
  </div>

</div>
```
