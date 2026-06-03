# Jetstream Admin — layout skeletons

Paste-ready, domain-neutral fragments for the Jetstream dark-navy skin. Each
skeleton is labelled by archetype slot, not by a domain noun. Copy the shell
from `assets/template.html` first (it carries the `:root` tokens + navbar +
icon rail + main slot), then drop the region skeletons below into
`<main class="main">`. Replace every `{placeholder}` with the real domain's
equivalent.

Token recap (full block in `template.html`):
- Canvas: `#0a0f1a`, surface `#111a2b`, card `#18243a`, hairline `#24314a`
- Text: `#e4ecf6` / muted `#8a98ad`
- Accent: `var(--accent-indigo)` = `#6366f1`; `var(--accent-sky)` = `#38bdf8`
- State tokens: `--state-active #22c55e`, `--state-warn #f59e0b`,
  `--state-sky #38bdf8`, `--state-muted #8a98ad`, each with `*-dim` tint.
- Put `font-variant-numeric: tabular-nums` on every numeric cell.

---

## Page header (every screen)

```html
<div class="page-header">
  <div>
    <div class="page-title">{Screen title}</div>
    <div class="page-sub">{Hub · context · timestamp}</div>
  </div>
  <div class="hdr-spacer"></div>
  <button class="btn-ghost">{Secondary}</button>
  <button class="btn-primary">+ {Primary action}</button>
</div>
```

---

## KPI tile row (×4 in a `.kpi-grid`)

```html
<div class="kpi-grid">  <!-- repeat(4,1fr); collapses to 2×2 below 900px -->
  <div class="kpi-card">
    <div class="kpi-top">
      <span class="kpi-label">{METRIC NAME}</span>
      <span class="kpi-icon {indigo|sky|green|amber}">
        <!-- 16×16 inline SVG glyph, stroke=currentColor -->
      </span>
    </div>
    <div class="kpi-num">{figure}</div>   <!-- font-variant-numeric:tabular-nums -->
    <div class="kpi-footer">
      <span class="delta {up|warn|neutral}">
        <!-- ▲/▼ arrow SVG --> {±delta}
      </span>
      <span class="kpi-since">{context / comparison label}</span>
    </div>
  </div>
  <!-- 3 more tiles -->
</div>
```

---

## Live status board (full-width card with state pills)

```html
<div class="card">
  <div class="card-hdr">
    <div class="card-title">{Board title}</div>
    <span class="badge-live">LIVE</span>
    <div class="card-hdr-space"></div>
    <button class="btn-ghost" style="font-size:11px;padding:4px 10px">Refresh</button>
  </div>
  <table class="tbl">
    <thead>
      <tr>
        <th>{Identifier}</th>
        <th>{Route / Relation}</th>
        <th>{Location}</th>
        <th>{Scheduled}</th>
        <th>Status</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><span class="rec-id">{ID}</span></td>
        <td>{origin} → {dest}</td>
        <td><span class="loc-pill">{Bay / Zone}</span></td>
        <td>{HH:MM}</td>
        <td>
          <span class="state-pill {active|sky|warn|muted|queued}">
            <span class="state-dot {active|sky|warn|muted|queued}"></span>
            {State label}
          </span>
        </td>
      </tr>
      <!-- repeat rows; state variants: .active .sky .warn .muted .queued -->
    </tbody>
  </table>
</div>
```

---

## Two-column grid (chart + side panel)

```html
<div class="mid-grid">  <!-- grid-template-columns: 1fr 340px; gap:18px -->

  <!-- LEFT: bar chart card -->
  <div class="card">
    <div class="card-hdr">
      <div class="card-title">{Chart title}</div>
      <div class="card-hdr-space"></div>
      <span style="font-size:11px;color:#8a98ad">{scope label}</span>
    </div>
    <div style="padding:16px 18px">
      <!-- chart legend -->
      <div style="display:flex;gap:14px;margin-bottom:12px">
        <div style="display:flex;align-items:center;gap:5px;font-size:11px;color:#8a98ad">
          <span style="width:10px;height:10px;border-radius:3px;background:var(--accent-indigo);flex-shrink:0"></span>Peak
        </div>
        <div style="display:flex;align-items:center;gap:5px;font-size:11px;color:#8a98ad">
          <span style="width:10px;height:10px;border-radius:3px;background:var(--accent-sky);flex-shrink:0"></span>Current
        </div>
        <div style="display:flex;align-items:center;gap:5px;font-size:11px;color:#8a98ad">
          <span style="width:10px;height:10px;border-radius:3px;background:#18243a;border:1px solid #24314a;flex-shrink:0"></span>Off-peak
        </div>
      </div>
      <!-- Inline SVG histogram: N bars, x-axis labels, y-axis gridlines -->
      <svg viewBox="0 0 480 140" xmlns="http://www.w3.org/2000/svg" style="width:100%;display:block">
        <!-- gridlines at y=10,40,70,100 (stroke #24314a) -->
        <!-- peak bars: fill="var(--accent-indigo)" -->
        <!-- current bar: fill="var(--accent-sky)" -->
        <!-- off-peak bars: fill="#24314a" -->
        <!-- x-axis labels every 3 units, fill="#8a98ad", font-size="8.5" -->
      </svg>
    </div>
  </div>

  <!-- RIGHT: resource side panel -->
  <div class="card" style="display:flex;flex-direction:column">
    <!-- Sub-card 1: Personnel -->
    <div style="border-bottom:1px solid #24314a">
      <div style="padding:12px 16px 10px;font-size:11px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:#8a98ad">{Personnel label}</div>
      <!-- 3 rows: avatar + name/sub + status dot -->
      <div style="display:flex;align-items:center;gap:10px;padding:9px 16px;border-bottom:1px solid rgba(36,49,74,.5)">
        <div style="width:28px;height:28px;border-radius:50%;background:linear-gradient(135deg,var(--accent-indigo),#818cf8);display:flex;align-items:center;justify-content:center;font-size:10px;font-weight:700;color:#fff;flex-shrink:0">{IN}</div>
        <div style="flex:1;min-width:0">
          <div style="font-size:12px;font-weight:600;color:#e4ecf6">{Name}</div>
          <div style="font-size:10px;color:#8a98ad">{Role · Base}</div>
        </div>
        <div style="display:flex;align-items:center;gap:4px;font-size:10px;font-weight:600;color:var(--state-active)">
          <span class="state-dot active"></span>Available
        </div>
      </div>
      <!-- repeat rows with .on-duty (sky) / .rest (muted) variants -->
    </div>
    <!-- Sub-card 2: Equipment -->
    <div>
      <div style="padding:12px 16px 10px;font-size:11px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:#8a98ad">{Equipment label}</div>
      <!-- 3 rows: icon-chip + id/type + next-assignment -->
      <div style="display:flex;align-items:center;gap:10px;padding:9px 16px;border-bottom:1px solid rgba(36,49,74,.5)">
        <div style="width:28px;height:28px;border-radius:7px;background:var(--accent-indigo-dim);display:flex;align-items:center;justify-content:center;color:var(--accent-indigo);flex-shrink:0">
          <!-- 14×14 inline SVG -->
        </div>
        <div style="flex:1;min-width:0">
          <div style="font-size:12px;font-weight:700;color:#e4ecf6;font-variant-numeric:tabular-nums">{UNIT-ID}</div>
          <div style="font-size:10px;color:#8a98ad">{type}</div>
        </div>
        <div>
          <div style="color:#e4ecf6;font-size:11px;font-weight:600;font-variant-numeric:tabular-nums">{REC-ID}</div>
          <div style="color:#8a98ad;font-size:10px;font-variant-numeric:tabular-nums">{HH:MM UTC}</div>
        </div>
      </div>
    </div>
  </div>

</div>
```

---

## Records table (list screen or dashboard footer)

```html
<div class="card">
  <div class="card-hdr" style="flex-wrap:wrap;gap:8px">
    <div class="card-title">{Records title}</div>
    <div class="card-hdr-space"></div>
    <!-- search + filter chips -->
    <div style="position:relative;max-width:220px">
      <svg width="12" height="12" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" style="position:absolute;left:8px;top:50%;transform:translateY(-50%);color:#8a98ad"><circle cx="7" cy="7" r="5"/><path d="M11 11l3 3"/></svg>
      <input type="text" placeholder="Search…" style="width:100%;background:#0a0f1a;border:1px solid #24314a;border-radius:6px;color:#e4ecf6;font-size:12px;padding:5px 8px 5px 28px;outline:none;font-family:inherit">
    </div>
    <div style="display:flex;gap:6px">
      <button class="chip active">All</button>
      <button class="chip">{Facet A}</button>
      <button class="chip">{Facet B}</button>
    </div>
  </div>
  <table class="tbl">
    <thead>
      <tr>
        <th>{Record}</th>
        <th>{Unit}</th>
        <th>{Route}</th>
        <th>{Scheduled}</th>
        <th>Status</th>
        <th class="num">{Capacity}</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><span class="rec-id">{REC-000}</span></td>
        <td>{unit type}</td>
        <td>{origin} → {dest}</td>
        <td>{HH:MM}</td>
        <td><span class="state-pill active"><span class="state-dot active"></span>{State}</span></td>
        <td style="text-align:right"><span style="font-weight:600;font-variant-numeric:tabular-nums">{n}</span><span style="color:#8a98ad">/{max}</span></td>
      </tr>
      <!-- status variants: .active .sky .warn .muted .queued -->
    </tbody>
  </table>
  <div style="display:flex;align-items:center;justify-content:space-between;padding:12px 18px;border-top:1px solid #24314a">
    <span style="font-size:12px;color:#8a98ad">Showing {a}–{b} of {n}</span>
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

## Record form — fields with inline validation

Rules live ON the field: required mark (`*`), helper text under the field,
inline error on an invalid field. Submit stays `disabled` until form is valid.
Never add a separate rules/validation-status/checklist panel.

```html
<form novalidate style="display:flex;flex-direction:column;gap:16px;max-width:760px">

  <div class="card">
    <div style="display:flex;align-items:center;gap:8px;padding:14px 18px;border-bottom:1px solid #24314a;font-size:12px;font-weight:700;color:#8a98ad;letter-spacing:.05em;text-transform:uppercase">
      <!-- inline SVG section icon --> {Section}
    </div>
    <div style="padding:18px">
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px 20px">

        <!-- valid field -->
        <div class="field">
          <label class="field-label" for="f1">{Label} <span class="req">*</span></label>
          <input id="f1" class="control" type="text" value="">
          <span class="helper">{format hint / constraint}</span>
        </div>

        <!-- invalid field -->
        <div class="field invalid">
          <label class="field-label" for="f2">{Label} <span class="req">*</span></label>
          <input id="f2" class="control" type="text" aria-invalid="true">
          <span class="error-msg">
            <svg width="12" height="12" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="8" cy="8" r="6"/><line x1="8" y1="5" x2="8" y2="8"/><circle cx="8" cy="11" r=".5" fill="currentColor"/></svg>
            {Specific rule that failed}
          </span>
        </div>

        <!-- required select -->
        <div class="field">
          <label class="field-label" for="f3">{Label} <span class="req">*</span></label>
          <select id="f3" class="control"><option value="">Select…</option></select>
          <span class="helper">{constraint on the options}</span>
        </div>

      </div>
    </div>
  </div>

  <!-- Form footer -->
  <div style="display:flex;align-items:center;justify-content:space-between;padding:16px 18px;background:#18243a;border:1px solid #24314a;border-radius:10px">
    <span style="font-size:12px;color:#8a98ad">Fields marked <span class="req">*</span> are required.</span>
    <div style="display:flex;gap:8px">
      <button type="button" class="btn-ghost">Cancel</button>
      <button type="submit" class="btn-primary" disabled>{Submit}</button>
    </div>
  </div>

</form>
```

---

## Record detail — header + meta grid + related panels

```html
<!-- Breadcrumb -->
<div style="font-size:12px;color:#8a98ad;margin-bottom:16px">
  <a href="#" style="color:#8a98ad;text-decoration:none">{Parent}</a> › <span style="color:#e4ecf6">{ID}</span>
</div>

<!-- Detail header -->
<div style="display:flex;align-items:flex-start;gap:16px;margin-bottom:20px;flex-wrap:wrap">
  <div style="flex:1;min-width:0">
    <div style="display:flex;align-items:center;gap:10px;flex-wrap:wrap">
      <span style="font-size:22px;font-weight:800;color:#e4ecf6;font-variant-numeric:tabular-nums;letter-spacing:-.02em">{ID}</span>
      <span class="state-pill sky"><span class="state-dot sky"></span>{State}</span>
    </div>
    <div style="font-size:13px;color:#8a98ad;margin-top:4px">{unit · type · route · location}</div>
  </div>
  <div style="display:flex;gap:8px;flex-shrink:0">
    <button class="btn-ghost">{Action}</button>
    <button class="btn-primary">Edit</button>
  </div>
</div>

<!-- Meta grid (3-col) -->
<div class="card">
  <div style="display:grid;grid-template-columns:repeat(3,1fr)">
    <div style="padding:16px 18px;border-right:1px solid #24314a;border-bottom:1px solid #24314a">
      <div style="font-size:10px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;color:#8a98ad;margin-bottom:4px">{FIELD}</div>
      <div style="font-size:14px;font-weight:600;color:#e4ecf6;font-variant-numeric:tabular-nums">{value}</div>
      <div style="font-size:11px;color:#8a98ad;margin-top:2px">{sub}</div>
    </div>
    <!-- repeat cells; last row cells omit border-bottom -->
  </div>
</div>

<!-- Two-col: route/stops + activity -->
<div class="two-col">  <!-- 7fr 5fr -->
  <div class="card"><!-- route/stops table --></div>
  <div class="card"><!-- activity feed --></div>
</div>
```
