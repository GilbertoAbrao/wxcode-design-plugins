# Cobalt Admin — layout skeletons

Paste-ready, domain-neutral fragments for the Cobalt light-mode admin skin.
Each skeleton is labelled by archetype slot, not by a domain noun. Copy the
shell from `assets/template.html` first (it carries the `:root` tokens + sidebar
+ topbar + main content slot), then drop the region skeletons below into
`<main class="content">`. Replace every placeholder label with the real
domain's equivalent.

Token recap (full block in `template.html`): canvas `#f1f5f9`; sidebar/topbar
`#fff`; card `#fff` with border `#e9ecf0` and shadow `0 1px 4px rgba(0,0,0,.05)`;
accent `var(--cobalt-600)` = `#2563eb`; category chips `--cat-*` with `*-bg`
tints; status tokens `--status-*` with `*-bg` tints; priority tokens
`--prio-*`/`*-bg`. Put `font-variant-numeric: tabular-nums` on every numeric
cell.

---

## Page header (every screen)

```html
<div style="display:flex;align-items:center;justify-content:space-between;">
  <div>
    <div style="font-size:18px;font-weight:700;color:#0f172a;">{Screen title}</div>
    <div style="font-size:13px;color:#64748b;margin-top:2px;">{scope · context · timestamp}</div>
  </div>
  <div style="display:flex;gap:8px;align-items:center;">
    <button class="btn-ghost">{Secondary}</button>
    <button class="btn-primary">+ {Primary action}</button>
  </div>
</div>
```

---

## KPI tile (repeat ×4 in a grid)

```html
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:16px;">
  <div class="card" style="padding:18px 20px;">
    <div style="display:flex;align-items:flex-start;justify-content:space-between;margin-bottom:10px;">
      <div style="font-size:11px;font-weight:700;letter-spacing:.07em;text-transform:uppercase;color:#64748b;">{METRIC LABEL}</div>
      <div style="width:34px;height:34px;border-radius:8px;background:{cat-bg};display:flex;align-items:center;justify-content:center;">
        <!-- inline SVG icon, stroke={cat-color} -->
      </div>
    </div>
    <div style="font-size:26px;font-weight:800;letter-spacing:-.03em;color:#0f172a;line-height:1;font-variant-numeric:tabular-nums;">{figure}</div>
    <div style="margin-top:8px;display:flex;align-items:center;gap:6px;font-size:12px;color:#64748b;">
      <span style="display:inline-flex;align-items:center;gap:2px;font-size:11px;font-weight:600;padding:1px 6px;border-radius:6px;background:var(--delta-up-bg);color:var(--delta-up-text);">↑ {delta}</span>
      {context line}
    </div>
    <!-- optional sparkline SVG area below -->
  </div>
  <!-- 3 more tiles -->
</div>
```

---

## Timeline / Gantt strip (card)

```html
<div class="card">
  <div class="card-header">
    <div>
      <div class="card-title">{Timeline title}</div>
      <div style="font-size:12px;color:#94a3b8;margin-top:1px;">{date range · context}</div>
    </div>
    <a href="#" style="font-size:12px;font-weight:600;color:var(--cobalt-600);">View full →</a>
  </div>
  <div style="padding:0 20px 18px;overflow-x:auto;">
    <!-- Column headers: grid of 200px + 7×1fr -->
    <div style="display:grid;grid-template-columns:200px repeat(7,1fr);font-size:11px;font-weight:600;letter-spacing:.04em;text-transform:uppercase;color:#94a3b8;padding:10px 0 6px;border-bottom:1px solid #f1f5f9;">
      <div style="color:#64748b;">Task</div>
      <div style="text-align:center;">Day 1</div>
      <div style="text-align:center;color:var(--cobalt-600);">Day 2 (today)</div>
      <!-- 5 more day headers -->
    </div>
    <!-- Task row -->
    <div style="display:grid;grid-template-columns:200px repeat(7,1fr);align-items:center;padding:8px 0;border-bottom:1px solid #f8fafc;position:relative;">
      <div>
        <div style="font-size:12px;font-weight:600;color:#1e293b;">{Task name}</div>
        <div style="font-size:10px;color:#94a3b8;margin-top:1px;">{sub-label}</div>
      </div>
      <!-- Bars area: grid-column 2/span 7, position relative, height 26px -->
      <div style="grid-column:2/span 7;position:relative;height:26px;">
        <!-- Bar: position absolute, height 16px, top 5px, border-radius 4px -->
        <div style="position:absolute;height:16px;top:5px;left:{left}%;width:{width}%;background:var(--cat-{color});border-radius:4px;opacity:.92;">
          <div style="position:absolute;top:6px;left:6px;font-size:10px;font-weight:600;color:#fff;white-space:nowrap;overflow:hidden;">{label}</div>
        </div>
        <!-- Today marker: position absolute, width 2px, cobalt-500, opacity .5 -->
        <div style="position:absolute;top:0;bottom:0;left:calc({today-offset}% - 1px);width:2px;background:var(--cobalt-500);opacity:.5;border-radius:1px;">
          <div style="position:absolute;top:-3px;left:-4px;width:10px;height:10px;border-radius:50%;background:var(--cobalt-600);"></div>
        </div>
      </div>
    </div>
    <!-- repeat rows for each entity -->
  </div>
</div>
```

---

## Records table (dashboard footer or list screen)

```html
<div class="card">
  <div class="card-header">
    <div class="card-title">{Records title}</div>
    <div style="display:flex;gap:8px;align-items:center;">
      <button class="btn-ghost">{Export}</button>
      <button class="btn-primary">+ {New}</button>
    </div>
  </div>
  <table style="width:100%;border-collapse:collapse;">
    <thead>
      <tr>
        <th style="font-size:11px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:#94a3b8;padding:10px 16px;background:#f8fafc;text-align:left;border-bottom:1px solid #e9ecf0;">{Col}</th>
        <!-- more headers -->
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:11px 16px;border-bottom:1px solid #f1f5f9;vertical-align:middle;">
          <div style="font-size:13px;font-weight:600;color:#1e293b;">{primary label}</div>
          <div style="font-size:11px;color:#94a3b8;margin-top:1px;">{sub-label}</div>
        </td>
        <!-- assignee cell: flex row, 24px avatar, name 12px -->
        <!-- due date: 12px color #64748b; .overdue → color cat-rose, weight 600 -->
        <!-- priority pill: 2px 9px, 12px radius, 11px/600 -->
        <!-- status pill: same pattern -->
      </tr>
    </tbody>
  </table>
  <!-- Footer: flex space-between, page info + pagination buttons -->
  <div style="display:flex;align-items:center;justify-content:space-between;padding:12px 16px;border-top:1px solid #f1f5f9;">
    <span style="font-size:12px;color:#64748b;">Showing {a}–{b} of {n}</span>
    <div style="display:flex;gap:4px;">
      <button style="width:30px;height:30px;border:1px solid #e2e8f0;border-radius:6px;font-size:12px;color:#475569;background:#fff;">‹</button>
      <button style="width:30px;height:30px;border:1px solid var(--cobalt-600);border-radius:6px;font-size:12px;font-weight:600;color:#fff;background:var(--cobalt-600);">1</button>
      <button style="width:30px;height:30px;border:1px solid #e2e8f0;border-radius:6px;font-size:12px;color:#475569;background:#fff;">2</button>
      <button style="width:30px;height:30px;border:1px solid #e2e8f0;border-radius:6px;font-size:12px;color:#475569;background:#fff;">›</button>
    </div>
  </div>
</div>
```

### List screen toolbar (search + filter chips)

```html
<div style="display:flex;align-items:center;gap:12px;flex-wrap:wrap;">
  <div style="position:relative;">
    <!-- magnifier icon: absolute left 10px top 50% translateY(-50%) -->
    <input type="search" placeholder="Filter by {fields}…"
      style="height:34px;width:280px;border:1px solid #e2e8f0;border-radius:8px;padding:0 12px 0 34px;font-size:13px;color:#0f172a;background:#fff;outline:none;">
  </div>
  <div style="display:flex;align-items:center;gap:6px;">
    <span style="font-size:11px;font-weight:600;color:#64748b;text-transform:uppercase;letter-spacing:.05em;">{Facet}</span>
    <!-- .active chip: cobalt-50 bg, cobalt-500 border, cobalt-700 text -->
    <span style="display:inline-flex;align-items:center;gap:4px;padding:4px 10px;border:1px solid var(--cobalt-500);border-radius:20px;font-size:12px;font-weight:600;color:var(--cobalt-700);background:var(--cobalt-50);">
      All <span style="font-size:10px;font-weight:700;background:var(--cobalt-100);color:var(--cobalt-700);padding:0 5px;border-radius:8px;">{n}</span>
    </span>
    <span style="display:inline-flex;align-items:center;gap:4px;padding:4px 10px;border:1px solid #e2e8f0;border-radius:20px;font-size:12px;font-weight:500;color:#475569;background:#fff;">
      {Value} <span style="font-size:10px;font-weight:700;background:#f1f5f9;color:#64748b;padding:0 5px;border-radius:8px;">{n}</span>
    </span>
  </div>
</div>
```

---

## Record form — fields with inline validation

Rules live ON the field: a required mark (`*`), helper text under the field,
and an inline error message on an invalid field. The submit stays `disabled`
until the form is valid. Never add a separate rules/validation-status summary
panel.

```html
<form novalidate style="display:flex;flex-direction:column;gap:16px;max-width:760px;">
  <div class="card">
    <!-- Section header -->
    <div style="padding:14px 20px;border-bottom:1px solid #f1f5f9;display:flex;align-items:center;gap:8px;">
      <!-- section icon SVG, color cobalt-600 -->
      <span style="font-size:13px;font-weight:700;color:#0f172a;">{Section title}</span>
    </div>
    <div style="padding:20px;">
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px 20px;">

        <!-- Valid field -->
        <div style="display:flex;flex-direction:column;gap:4px;">
          <label style="font-size:13px;font-weight:600;color:#374151;" for="f1">
            {Label} <span style="color:#e11d48;">*</span>
          </label>
          <input id="f1" type="text" value=""
            style="height:36px;border:1px solid #e2e8f0;border-radius:7px;padding:0 12px;font-size:13px;color:#0f172a;background:#fff;outline:none;">
          <span style="font-size:11px;color:#94a3b8;">{what the value drives / format hint}</span>
        </div>

        <!-- Invalid field (add to .field: border-color #fca5a5, bg #fef2f2) -->
        <div style="display:flex;flex-direction:column;gap:4px;">
          <label style="font-size:13px;font-weight:600;color:#374151;" for="f2">
            {Label} <span style="color:#e11d48;">*</span>
          </label>
          <input id="f2" type="text" aria-invalid="true"
            style="height:36px;border:1px solid #fca5a5;border-radius:7px;padding:0 12px;font-size:13px;color:#0f172a;background:#fef2f2;outline:none;">
          <span style="display:flex;align-items:center;gap:4px;font-size:11px;color:#dc2626;font-weight:500;">
            <!-- alert icon SVG 11×11 -->
            {Specific rule that failed}
          </span>
        </div>

        <!-- Required select -->
        <div style="display:flex;flex-direction:column;gap:4px;">
          <label style="font-size:13px;font-weight:600;color:#374151;" for="f3">
            {Label} <span style="color:#e11d48;">*</span>
          </label>
          <select id="f3"
            style="height:36px;border:1px solid #e2e8f0;border-radius:7px;padding:0 12px;font-size:13px;color:#0f172a;background:#fff;outline:none;font-family:inherit;">
            <option value="">Select…</option>
          </select>
          <span style="font-size:11px;color:#94a3b8;">{constraint on the options}</span>
        </div>

      </div>
    </div>
  </div>

  <!-- Form footer -->
  <div style="display:flex;align-items:center;justify-content:space-between;padding:14px 20px;background:#f8fafc;border:1px solid #e9ecf0;border-radius:10px;">
    <span style="font-size:12px;color:#64748b;">Fields marked <span style="color:#e11d48;">*</span> are required.</span>
    <div style="display:flex;gap:8px;">
      <button type="button" class="btn-ghost">Cancel</button>
      <!-- disabled until form valid -->
      <button type="submit" class="btn-primary" disabled
        style="background:#94a3b8;cursor:not-allowed;opacity:.7;">
        {Submit action}
      </button>
    </div>
  </div>
</form>
```

---

## Record detail — header + meta grid + related panels

```html
<!-- Breadcrumb trail -->
<nav style="display:flex;align-items:center;gap:6px;font-size:12px;color:#94a3b8;">
  <a href="#" style="color:var(--cobalt-600);">{Parent list}</a>
  <span>›</span>
  <a href="#" style="color:var(--cobalt-600);">{Parent entity}</a>
  <span>›</span>
  <span style="color:#64748b;">{ID}</span>
</nav>

<!-- Detail header band -->
<div style="display:flex;align-items:flex-start;justify-content:space-between;gap:16px;">
  <div style="display:flex;flex-direction:column;gap:6px;">
    <div style="display:flex;align-items:center;gap:10px;flex-wrap:wrap;">
      <span style="font-size:12px;font-weight:600;color:#94a3b8;letter-spacing:.04em;font-family:'Courier New',monospace;">{RECORD-ID}</span>
      <!-- status pill -->
      <!-- priority pill -->
    </div>
    <div style="font-size:20px;font-weight:700;color:#0f172a;line-height:1.3;">{Record title}</div>
  </div>
  <div style="display:flex;gap:8px;align-items:center;flex-shrink:0;">
    <button class="btn-ghost">{Action}</button>
    <button class="btn-primary">Edit</button>
  </div>
</div>

<!-- Meta grid: 3-col label/value cells -->
<div class="card">
  <div style="display:grid;grid-template-columns:repeat(3,1fr);">
    <div style="padding:16px 20px;border-right:1px solid #f1f5f9;border-bottom:1px solid #f1f5f9;">
      <div style="font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.07em;color:#94a3b8;margin-bottom:4px;">{FIELD}</div>
      <div style="font-size:13px;font-weight:600;color:#1e293b;">{value}</div>
      <div style="font-size:11px;color:#94a3b8;margin-top:2px;">{sub}</div>
    </div>
    <!-- 5 more cells; nth-child(3n) has no border-right; last row has no border-bottom -->
  </div>
</div>

<!-- Related data: records sub-table + activity feed (same 2-col grid as dashboard lower-row) -->
<div style="display:grid;grid-template-columns:1fr 320px;gap:16px;align-items:start;">
  <div class="card"><!-- sub-table of related records --></div>
  <div class="card"><!-- activity feed rows --></div>
</div>
```

---

## Side panel — summary list with progress bars

```html
<div class="card" style="padding:18px;">
  <div style="font-size:13px;font-weight:700;color:#0f172a;margin-bottom:14px;">{Panel title}</div>
  <div style="display:flex;flex-direction:column;gap:12px;">
    <!-- Summary item -->
    <div>
      <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:5px;">
        <div style="font-size:12px;font-weight:600;color:#1e293b;">{Item name}</div>
        <div style="font-size:11px;color:#94a3b8;">{date}</div>
      </div>
      <div style="height:5px;border-radius:3px;background:#f1f5f9;overflow:hidden;margin-bottom:4px;">
        <div style="height:100%;border-radius:3px;width:{pct}%;background:var(--cobalt-500);"></div>
      </div>
      <div style="display:flex;align-items:center;justify-content:space-between;">
        <span style="font-size:11px;color:#64748b;font-weight:600;">{pct}%</span>
        <span style="font-size:10px;font-weight:600;padding:1px 7px;border-radius:8px;background:var(--cobalt-50);color:var(--cobalt-700);">{category chip}</span>
      </div>
    </div>
  </div>
</div>
```

## Side panel — member list

```html
<div class="card" style="padding:18px;">
  <div style="font-size:13px;font-weight:700;color:#0f172a;margin-bottom:14px;">{Panel title}</div>
  <div style="display:flex;flex-direction:column;gap:10px;">
    <div style="display:flex;align-items:center;gap:10px;">
      <!-- avatar: 30×30px, border-radius 50%, initials, position relative -->
      <!-- status dot: absolute bottom 0 right 0, 8×8px, border-radius 50%, border 1.5px white -->
      <!-- dot-online: cat-emerald; dot-away: cat-amber; dot-offline: #cbd5e1 -->
      <div style="position:relative;width:30px;height:30px;border-radius:50%;background:var(--cobalt-100);color:var(--cobalt-700);font-size:11px;font-weight:700;display:flex;align-items:center;justify-content:center;flex-shrink:0;">
        ··
        <span style="position:absolute;bottom:0;right:0;width:8px;height:8px;border-radius:50%;background:var(--cat-emerald);border:1.5px solid #fff;"></span>
      </div>
      <div>
        <div style="font-size:12px;font-weight:600;color:#1e293b;">{Name}</div>
        <div style="font-size:11px;color:#94a3b8;">{Role}</div>
      </div>
    </div>
  </div>
</div>
```
