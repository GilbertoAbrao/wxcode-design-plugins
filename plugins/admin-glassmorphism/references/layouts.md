# Glassmorphism Admin — layout skeletons

Paste-ready, domain-neutral fragments for the frosted-glass dark skin. Each
skeleton is labelled by archetype slot, not by a domain noun. Copy the shell from
`assets/template.html` first (it carries the `:root` tokens + aurora + grain +
sidebar + topbar + `<main class="content">`), then drop the region skeletons
below into `<main class="content">`. Replace every `{placeholder}` with the real
domain's equivalent.

Token recap (full block in `template.html`): canvas `#0d1117`, glass
`rgba(255,255,255,0.04)` + `blur(18px)`, glass border `1px solid rgba(255,255,255,0.10)`,
accent `var(--cyan)` = `#4dd0e1`, state tokens `--green/pink/amber/violet-glass + -text`.

---

## Page header (every screen)

```html
<div style="display:flex;align-items:center;justify-content:space-between;">
  <div>
    <div style="font-size:22px;font-weight:800;color:var(--white-95)">{Screen title}</div>
    <div style="font-size:13px;color:var(--white-60);margin-top:3px">{scope · context · timestamp}</div>
  </div>
  <div style="display:flex;gap:10px;align-items:center;">
    <button class="btn-ghost">{Secondary action}</button>
    <button class="btn-primary">+ {Primary action}</button>
  </div>
</div>
```

---

## KPI tile row (repeat ×4)

```html
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:16px;">

  <div class="glass" style="padding:20px;display:flex;flex-direction:column;gap:10px;">
    <div style="font-size:10px;font-weight:600;letter-spacing:0.12em;text-transform:uppercase;color:var(--white-60)">{METRIC NAME}</div>
    <div style="font-size:28px;font-weight:800;color:var(--white-95);line-height:1;letter-spacing:-0.02em">{figure}</div>
    <div style="display:flex;align-items:center;justify-content:space-between;margin-top:4px;">
      <span class="status-pill status-active" style="font-size:11px">▲ {delta}</span>  <!-- or status-hold for negative -->
      <!-- 64×24 sparkline SVG: see assets/dashboard.html for the pattern -->
      <svg width="64" height="24" viewBox="0 0 64 24">
        <defs><linearGradient id="spN" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#4dd0e1" stop-opacity="0.5"/><stop offset="100%" stop-color="#4dd0e1" stop-opacity="0"/></linearGradient></defs>
        <polyline fill="none" stroke="#4dd0e1" stroke-width="1.5" points="{point-list}"/>
        <polygon fill="url(#spN)" points="{point-list} 64,24 0,24"/>
      </svg>
    </div>
  </div>

  <!-- 3 more tiles -->
</div>
```

---

## 2-column main grid (chart panel + top-N list)

```html
<div style="display:grid;grid-template-columns:1fr 340px;gap:20px;">

  <!-- Left: area chart panel -->
  <div class="glass" style="padding:24px;">
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:20px;">
      <div style="font-size:15px;font-weight:700;color:var(--white-95)">{Chart title}</div>
      <div style="display:flex;gap:8px;">
        <span class="chip">{Period 1}</span>
        <span class="chip active">{Period 2}</span>
        <span class="chip">{Period 3}</span>
      </div>
    </div>
    <div style="display:flex;gap:20px;margin-bottom:16px;">
      <!-- legend items -->
      <div style="display:flex;align-items:center;gap:6px;font-size:11.5px;color:var(--white-60)">
        <span style="width:8px;height:8px;border-radius:50%;background:#4dd0e1;display:inline-block"></span>{Series 1}
      </div>
      <div style="display:flex;align-items:center;gap:6px;font-size:11.5px;color:var(--white-60)">
        <span style="width:8px;height:8px;border-radius:50%;background:#818cf8;display:inline-block"></span>{Series 2}
      </div>
    </div>
    <!-- Area chart — see assets/dashboard.html for the full SVG pattern -->
    <svg viewBox="0 0 560 180" width="100%" height="180" style="overflow:visible">
      <!-- y-axis gridlines at white-06, y-labels at white-35, area + polyline per series -->
    </svg>
  </div>

  <!-- Right: top-N list panel -->
  <div class="glass" style="padding:24px;">
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:18px;">
      <div style="font-size:15px;font-weight:700;color:var(--white-95)">{List title}</div>
      <a href="#" style="font-size:11.5px;color:var(--cyan);text-decoration:none">See all</a>
    </div>
    <!-- Repeat: entity row -->
    <div style="display:flex;align-items:center;gap:12px;padding:10px 0;border-bottom:1px solid var(--white-06);">
      <div style="width:36px;height:36px;border-radius:50%;flex-shrink:0;display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:700;color:#fff;background:linear-gradient(135deg,#4dd0e1,#818cf8)">{IN}</div>
      <div style="flex:1;min-width:0;">
        <div style="font-size:13px;font-weight:600;color:var(--white-95)">{Primary name}</div>
        <div style="font-size:11px;color:var(--white-60);margin-top:1px">{Secondary}</div>
      </div>
      <div style="font-size:13px;font-weight:700;color:var(--cyan);white-space:nowrap">{metric}</div>
    </div>
    <!-- more rows; last row has no border-bottom -->
  </div>

</div>
```

---

## Full-width glass records table

```html
<div class="glass" style="overflow:hidden;">
  <div style="display:flex;align-items:center;justify-content:space-between;padding:20px 24px 16px;border-bottom:1px solid var(--white-10);background:rgba(255,255,255,0.03);backdrop-filter:blur(8px);">
    <div style="font-size:15px;font-weight:700;color:var(--white-95)">{Table title}</div>
    <a href="#" style="font-size:11.5px;color:var(--cyan);text-decoration:none">{Secondary action}</a>
  </div>
  <table style="width:100%;border-collapse:collapse;font-size:13px;">
    <thead>
      <tr>
        <th style="padding:12px 20px;text-align:left;font-size:10px;font-weight:600;letter-spacing:0.10em;text-transform:uppercase;color:var(--white-60);background:rgba(255,255,255,0.025);border-bottom:1px solid var(--white-06)">{Column}</th>
        <!-- more th -->
        <th style="…">Status</th>
      </tr>
    </thead>
    <tbody>
      <tr style="border-bottom:1px solid var(--white-06);">
        <td style="padding:13px 20px;color:var(--white-95)">
          <div style="display:flex;align-items:center;gap:10px;">
            <div style="width:30px;height:30px;border-radius:8px;flex-shrink:0;display:flex;align-items:center;justify-content:center;font-size:11px;font-weight:700;color:#fff;background:linear-gradient(135deg,#4dd0e1,#818cf8)">{IN}</div>
            <div>
              <div style="font-weight:600;font-size:13px">{Primary}</div>
              <div style="font-size:11px;color:var(--white-60)">{Secondary}</div>
            </div>
          </div>
        </td>
        <!-- more td -->
        <td><span class="status-pill status-active">{State}</span></td>
      </tr>
      <!-- even rows: background:var(--white-02) -->
    </tbody>
  </table>
  <!-- optional footer: result count + pagination -->
  <div style="display:flex;align-items:center;justify-content:space-between;padding:14px 20px;border-top:1px solid var(--white-06);">
    <span style="font-size:12px;color:var(--white-60)">Showing {a}–{b} of {n}</span>
    <div style="display:flex;gap:4px;">
      <!-- page buttons: width:30px;height:30px;border-radius:8px;border:1px solid var(--white-10);background:var(--white-04);color:var(--white-60);font-size:12px;cursor:pointer -->
      <!-- active page: background:var(--cyan-dim);border-color:rgba(77,208,225,0.25);color:var(--cyan) -->
    </div>
  </div>
</div>
```

### List toolbar (search + filter chips)

```html
<div style="display:flex;align-items:center;gap:16px;padding:14px 20px;background:rgba(255,255,255,0.03);border-bottom:1px solid var(--white-06);flex-wrap:wrap;">
  <div style="display:flex;align-items:center;gap:8px;background:var(--white-06);border:1px solid var(--white-10);border-radius:10px;padding:7px 12px;flex:1;min-width:200px;max-width:320px;">
    <!-- magnifier icon -->
    <input type="text" placeholder="Filter by {fields}…" style="background:none;border:none;outline:none;font-size:13px;color:var(--white-95);width:100%">
  </div>
  <div style="display:flex;align-items:center;gap:8px;">
    <span style="font-size:11px;font-weight:600;letter-spacing:0.08em;text-transform:uppercase;color:var(--white-60)">{Facet}</span>
    <span class="chip active">All <span style="font-size:10px;opacity:0.7">{n}</span></span>
    <span class="chip">{Value} <span style="font-size:10px;opacity:0.7">{n}</span></span>
  </div>
</div>
```

---

## Record form — fields with inline validation

Rules live ON the field: a required mark (`*`), helper text under the field, and
an inline error message on an invalid field. The submit stays `disabled` until the
form is valid. Never add a separate rules/validation-status summary panel.

```html
<form novalidate>
  <div class="glass" style="margin-bottom:16px;">
    <div style="display:flex;align-items:center;gap:8px;font-size:12px;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;color:var(--white-60);padding:18px 24px 14px;border-bottom:1px solid var(--white-06);">
      <!-- section icon --> {Section title}
    </div>
    <div style="padding:20px 24px;">
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:18px;">

        <!-- valid field -->
        <div style="display:flex;flex-direction:column;gap:5px;">
          <label style="font-size:12px;font-weight:600;color:var(--white-95)" for="f1">{Label} <span style="color:#f472b6">*</span></label>
          <input id="f1" type="text" placeholder="{hint}" style="background:rgba(255,255,255,0.05);border:1px solid var(--white-10);border-radius:10px;padding:9px 12px;font-size:13px;color:var(--white-95);outline:none;width:100%;font-family:inherit">
          <span style="font-size:11px;color:var(--white-60)">{what the value drives / format hint}</span>
        </div>

        <!-- invalid field: border: 1px solid rgba(244,114,182,0.55) + box-shadow -->
        <div style="display:flex;flex-direction:column;gap:5px;">
          <label style="font-size:12px;font-weight:600;color:var(--white-95)" for="f2">{Label} <span style="color:#f472b6">*</span></label>
          <input id="f2" type="text" aria-invalid="true" style="background:rgba(255,255,255,0.05);border:1px solid rgba(244,114,182,0.55);box-shadow:0 0 0 3px rgba(244,114,182,0.07);border-radius:10px;padding:9px 12px;font-size:13px;color:var(--white-95);outline:none;width:100%;font-family:inherit">
          <span style="font-size:11px;color:#f472b6;display:flex;align-items:center;gap:4px;">
            <!-- alert icon 12px --> {Specific rule that failed}
          </span>
        </div>

        <!-- required select -->
        <div style="display:flex;flex-direction:column;gap:5px;">
          <label style="font-size:12px;font-weight:600;color:var(--white-95)" for="f3">{Label} <span style="color:#f472b6">*</span></label>
          <select id="f3" style="background:rgba(255,255,255,0.05);border:1px solid var(--white-10);border-radius:10px;padding:9px 12px;font-size:13px;color:var(--white-95);outline:none;width:100%;font-family:inherit;-webkit-appearance:none;">
            <option value="">Select…</option>
            <!-- options -->
          </select>
          <span style="font-size:11px;color:var(--white-60)">{constraint on the options}</span>
        </div>

        <!-- full-width textarea -->
        <div style="display:flex;flex-direction:column;gap:5px;grid-column:1/-1;">
          <label style="font-size:12px;font-weight:600;color:var(--white-95)" for="f4">{Label}</label>
          <textarea id="f4" rows="3" style="background:rgba(255,255,255,0.05);border:1px solid var(--white-10);border-radius:10px;padding:9px 12px;font-size:13px;color:var(--white-95);outline:none;width:100%;font-family:inherit;resize:vertical"></textarea>
          <span style="font-size:11px;color:var(--white-60)">{helper text}</span>
        </div>

      </div>
    </div>
  </div>

  <!-- Form footer -->
  <div class="glass" style="display:flex;align-items:center;justify-content:space-between;padding:16px 24px;">
    <span style="font-size:12px;color:var(--white-60)">Fields marked <span style="color:#f472b6">*</span> are required.</span>
    <div style="display:flex;gap:10px;">
      <button type="button" class="btn-ghost">Cancel</button>
      <button type="submit" class="btn-primary" disabled>{Submit action}</button>
    </div>
  </div>
</form>
```

---

## Record detail — header card + meta grid + related panels

```html
<!-- breadcrumb -->
<div style="font-size:12px;color:var(--white-60);display:flex;align-items:center;gap:6px;">
  <a href="#" style="color:var(--cyan);text-decoration:none">{Parent list}</a>
  <span>›</span> <span>{Entity name}</span>
</div>

<!-- header card -->
<div class="glass" style="display:flex;align-items:center;gap:20px;padding:24px;">
  <!-- entity avatar / icon -->
  <div style="width:64px;height:64px;border-radius:50%;flex-shrink:0;display:flex;align-items:center;justify-content:center;font-size:22px;font-weight:800;color:#fff;background:linear-gradient(135deg,#f472b6,#818cf8);border:2px solid rgba(77,208,225,0.30)">{IN}</div>
  <div style="flex:1;">
    <div style="font-size:22px;font-weight:800;color:var(--white-95)">{Entity name}</div>
    <div style="font-size:14px;color:var(--cyan);margin-top:3px">{identifier / handle}</div>
    <div style="font-size:12px;color:var(--white-60);margin-top:5px;display:flex;align-items:center;gap:12px;">
      <span class="status-pill status-active">{State}</span>
      <span>{key descriptor}</span>
    </div>
  </div>
  <div style="display:flex;gap:10px;flex-shrink:0;">
    <button class="btn-ghost">{Action}</button>
    <button class="btn-primary">Edit</button>
  </div>
</div>

<!-- meta grid: 3-col label/value cells -->
<div class="glass">
  <div style="display:grid;grid-template-columns:repeat(3,1fr);">
    <div style="padding:18px 24px;border-right:1px solid var(--white-06);">
      <div style="font-size:10px;font-weight:600;letter-spacing:0.10em;text-transform:uppercase;color:var(--white-60);margin-bottom:5px">{FIELD}</div>
      <div style="font-size:16px;font-weight:700;color:var(--white-95)">{value}</div>
      <div style="font-size:11px;color:var(--white-60);margin-top:3px">{sub}</div>
    </div>
    <!-- 2 more cells in row 1; 3 cells in row 2 with border-top:1px solid var(--white-06) -->
  </div>
</div>

<!-- related panels: two-column -->
<div style="display:grid;grid-template-columns:1fr 340px;gap:20px;align-items:start;">
  <div class="glass"><!-- sub-table or top-N list --></div>
  <div class="glass"><!-- activity feed using entity-row or activity-row pattern --></div>
</div>
```
