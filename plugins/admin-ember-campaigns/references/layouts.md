# Ember Admin — layout skeletons

Paste-ready, domain-neutral fragments for the Ember vibrant-but-clean
rose-accent skin. Each skeleton is labelled by archetype slot, not by a domain
noun. Copy the shell from `assets/template.html` first (it carries the `:root`
tokens + sidebar + topbar + main slot), then drop the region skeletons below
into `<main class="content">`. Replace every placeholder label with the real
domain's equivalent.

Token recap (full block in `template.html`): canvas `#fafafa`, cards `#ffffff`,
border `#ececf0`; text `#0f172a / #334155 / #64748b / #94a3b8`; accent
`var(--color-accent)` = `#e11d48`, soft `#ec4899`, bg `#fff1f5`; secondary
`--color-indigo #4f46e5`, sky `--color-sky #0ea5e9`, amber `--color-amber
#d97706`; state tokens `--color-success/warning/danger` with `*-bg` tints.
Put `font-variant-numeric: tabular-nums` on every numeric cell.

---

## Page header (every screen)

```html
<div style="display:flex;align-items:center;justify-content:space-between;">
  <div>
    <h1 style="font-size:20px;font-weight:700;color:#0f172a;">{Screen title}</h1>
    <p style="font-size:13px;color:#64748b;margin-top:2px;">{Scope · context · timestamp}</p>
  </div>
  <div style="display:flex;gap:10px;">
    <button class="btn-ghost">{Secondary action}</button>
    <button class="btn-primary">+ {Primary action}</button>
  </div>
</div>
```

---

## KPI card row (4 tiles)

```html
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:16px;">
  <div style="background:#fff;border:1px solid #ececf0;border-radius:12px;padding:18px 20px;box-shadow:0 2px 8px rgba(0,0,0,.04);display:flex;flex-direction:column;gap:10px;">
    <div style="font-size:10.5px;font-weight:600;text-transform:uppercase;letter-spacing:0.65px;color:#94a3b8;">{METRIC LABEL}</div>
    <div style="display:flex;align-items:flex-end;justify-content:space-between;gap:8px;">
      <div style="font-size:26px;font-weight:800;letter-spacing:-0.5px;color:#0f172a;font-variant-numeric:tabular-nums;">{figure}</div>
      <!-- inline SVG sparkline 52×26, stroke var(--color-accent), area fill 10% alpha -->
      <svg width="52" height="26" viewBox="0 0 52 26" fill="none">
        <polyline points="{x1,y1 x2,y2 ...}" stroke="var(--color-accent)" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
        <polyline points="{path close to 26,26 2,26}" fill="var(--color-accent)" opacity="0.10"/>
      </svg>
    </div>
    <div style="display:flex;align-items:center;gap:6px;">
      <!-- .kpi-delta.up: success-bg / success; .kpi-delta.down: danger-bg / danger -->
      <span style="display:inline-flex;align-items:center;gap:3px;font-size:11.5px;font-weight:600;padding:2px 7px;border-radius:20px;background:var(--color-success-bg);color:var(--color-success);">
        <!-- arrow SVG -->▲ {delta}
      </span>
      <span style="font-size:11px;color:#94a3b8;">{period}</span>
    </div>
  </div>
  <!-- repeat ×3 -->
</div>
```

---

## 7/5 middle split

```html
<div style="display:grid;grid-template-columns:7fr 5fr;gap:16px;">

  <!-- LEFT: multi-series line chart -->
  <div style="background:#fff;border:1px solid #ececf0;border-radius:12px;padding:20px;box-shadow:0 2px 8px rgba(0,0,0,.04);">
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:16px;">
      <div>
        <div style="font-size:15px;font-weight:700;color:#0f172a;">{Chart title}</div>
        <div style="font-size:12px;color:#94a3b8;margin-top:2px;">{Series A · Series B · Series C — {period}}</div>
      </div>
      <div style="display:flex;gap:16px;">
        <span style="display:flex;align-items:center;gap:5px;font-size:12px;color:#64748b;"><span style="width:8px;height:8px;border-radius:50%;background:var(--color-accent)"></span>{Label A}</span>
        <span style="display:flex;align-items:center;gap:5px;font-size:12px;color:#64748b;"><span style="width:8px;height:8px;border-radius:50%;background:var(--color-indigo-soft)"></span>{Label B}</span>
        <span style="display:flex;align-items:center;gap:5px;font-size:12px;color:#64748b;"><span style="width:8px;height:8px;border-radius:50%;background:var(--color-sky)"></span>{Label C}</span>
      </div>
    </div>
    <!-- SVG chart: gridlines (stroke #ececf0), y-axis text (9px #94a3b8), x-axis text,
         3 polygon fills (rose/indigo/sky at 0.13–0.18 opacity),
         3 polyline series (2px stroke), peak data dots (3.5px filled circles) -->
    <svg width="100%" height="180" viewBox="0 0 560 180" preserveAspectRatio="none">
      <!-- gridlines -->
      <!-- y-axis labels: right-anchored, x=34 -->
      <!-- x-axis labels: center-anchored, y=174 -->
      <!-- defs: linearGradients for area fills -->
      <!-- polygon area fills -->
      <!-- polyline series -->
      <!-- data dots on peaks -->
    </svg>
  </div>

  <!-- RIGHT: conversion funnel -->
  <div style="background:#fff;border:1px solid #ececf0;border-radius:12px;padding:20px;box-shadow:0 2px 8px rgba(0,0,0,.04);">
    <div style="margin-bottom:16px;">
      <div style="font-size:15px;font-weight:700;color:#0f172a;">{Funnel title}</div>
      <div style="font-size:12px;color:#94a3b8;margin-top:2px;">{Scope}</div>
    </div>
    <div style="display:flex;flex-direction:column;gap:10px;">
      <!-- Funnel step row (repeat for each step, proportional width) -->
      <div style="display:flex;flex-direction:column;gap:4px;">
        <div style="display:flex;justify-content:space-between;align-items:center;font-size:12px;">
          <span style="font-weight:600;color:#0f172a;">{Step label}</span>
          <span style="color:#64748b;font-variant-numeric:tabular-nums;">{count}</span>
        </div>
        <div style="height:12px;background:#f1f5f9;border-radius:6px;overflow:hidden;">
          <div style="height:100%;border-radius:6px;width:{pct}%;background:linear-gradient(90deg,var(--color-accent),var(--color-accent-soft));transition:width 0.3s;"></div>
        </div>
      </div>
      <!-- Connector (between steps) -->
      <div style="display:flex;align-items:center;gap:6px;font-size:11px;">
        <div style="flex:1;height:1px;background:#e2e8f0;"></div>
        <span style="color:var(--color-danger);font-weight:600;">↓ {drop}% drop</span>
        <div style="flex:1;height:1px;background:#e2e8f0;"></div>
      </div>
      <!-- ...more steps... -->
      <!-- Aggregate rate chip at foot -->
      <div style="margin-top:14px;padding:10px 12px;background:var(--color-success-bg);border-radius:8px;display:flex;align-items:center;justify-content:space-between;">
        <span style="font-size:12px;font-weight:600;color:#15803d;">{Rate label}</span>
        <span style="font-size:15px;font-weight:800;color:var(--color-success);font-variant-numeric:tabular-nums;">{rate}%</span>
      </div>
    </div>
  </div>

</div>
```

---

## Records table (full-width)

```html
<div style="background:#fff;border:1px solid #ececf0;border-radius:12px;box-shadow:0 2px 8px rgba(0,0,0,.04);overflow:hidden;">
  <div style="display:flex;align-items:center;justify-content:space-between;padding:18px 20px 14px;">
    <div>
      <div style="font-size:15px;font-weight:700;color:#0f172a;">{Records title}</div>
      <div style="font-size:12px;color:#94a3b8;margin-top:2px;">{scope · count}</div>
    </div>
    <div style="display:flex;gap:10px;align-items:center;">
      <a href="#" style="font-size:12px;color:var(--color-accent);font-weight:600;text-decoration:none;">View all →</a>
      <button class="btn-primary">+ {New}</button>
    </div>
  </div>
  <table style="width:100%;border-collapse:collapse;">
    <thead>
      <tr>
        <th style="padding:10px 16px;text-align:left;font-size:10.5px;font-weight:600;letter-spacing:0.5px;text-transform:uppercase;color:#94a3b8;background:#f8fafc;border-bottom:1px solid #ececf0;">{Name}</th>
        <th style="...">Channel</th>
        <th style="...">Volume</th>
        <th style="...">Engagement</th>
        <th style="...">Value</th>
        <th style="...">Status</th>
      </tr>
    </thead>
    <tbody>
      <tr style="border-bottom:1px solid #f1f5f9;">
        <td style="padding:12px 16px;vertical-align:middle;">
          <div style="font-weight:600;color:#0f172a;">{Name}</div>
          <div style="font-size:11px;color:#94a3b8;margin-top:1px;">{description}</div>
        </td>
        <td style="padding:12px 16px;vertical-align:middle;">
          <!-- channel-chip variants: channel-a(indigo) / channel-b(rose) / channel-c(sky) / channel-d(amber) -->
          <span style="display:inline-flex;align-items:center;gap:4px;padding:3px 9px;border-radius:20px;font-size:11px;font-weight:600;background:var(--color-indigo-bg);color:var(--color-indigo);">{Channel}</span>
        </td>
        <td style="padding:12px 16px;font-variant-numeric:tabular-nums;">{numeric}</td>
        <td style="padding:12px 16px;font-variant-numeric:tabular-nums;">{numeric}</td>
        <td style="padding:12px 16px;font-variant-numeric:tabular-nums;">{numeric}</td>
        <td style="padding:12px 16px;">
          <!-- status-pill variants: success(green) / warning(amber) / danger(red) -->
          <span style="display:inline-flex;align-items:center;gap:5px;padding:4px 10px;border-radius:20px;font-size:11px;font-weight:600;background:var(--color-success-bg);color:var(--color-success);">
            <span style="width:6px;height:6px;border-radius:50%;background:currentColor;"></span>Live
          </span>
        </td>
      </tr>
      <!-- more rows; hover: background #fff7f8 -->
    </tbody>
  </table>
  <!-- Table footer: "Showing N–M of T" + pagination chips -->
  <div style="display:flex;align-items:center;justify-content:space-between;padding:14px 20px;border-top:1px solid #ececf0;font-size:12.5px;color:#64748b;">
    <span>Showing {a}–{b} of {n}</span>
    <div style="display:flex;gap:4px;">
      <button style="min-width:32px;height:32px;border:1px solid #ececf0;border-radius:6px;background:#fff;font-size:12.5px;color:#334155;cursor:pointer;">‹</button>
      <button style="min-width:32px;height:32px;border:1px solid var(--color-accent);border-radius:6px;background:var(--color-accent);font-size:12.5px;color:#fff;font-weight:600;cursor:pointer;">1</button>
      <button style="min-width:32px;height:32px;border:1px solid #ececf0;border-radius:6px;background:#fff;font-size:12.5px;color:#334155;cursor:pointer;">2</button>
      <button style="min-width:32px;height:32px;border:1px solid #ececf0;border-radius:6px;background:#fff;font-size:12.5px;color:#334155;cursor:pointer;">›</button>
    </div>
  </div>
</div>
```

---

## List toolbar (search + filter chips)

```html
<div style="background:#fff;border:1px solid #ececf0;border-radius:12px;padding:14px 16px;display:flex;align-items:center;gap:16px;flex-wrap:wrap;box-shadow:0 2px 8px rgba(0,0,0,.04);">
  <div style="display:flex;align-items:center;gap:6px;background:#f8fafc;border:1px solid #ececf0;border-radius:8px;padding:7px 12px;min-width:240px;">
    <!-- magnifier SVG -->
    <input type="text" placeholder="Filter by {fields}…" style="border:none;background:transparent;font-size:13px;color:#0f172a;outline:none;width:100%;">
  </div>
  <div style="display:flex;align-items:center;gap:8px;">
    <span style="font-size:11.5px;color:#64748b;font-weight:500;">{Facet}:</span>
    <!-- .chip.active: accent-bg + accent color + accent border -->
    <span style="padding:4px 12px;border-radius:20px;font-size:12px;font-weight:600;background:var(--color-accent-bg);color:var(--color-accent);border:1px solid var(--color-accent);cursor:pointer;">All <span style="font-size:10.5px;opacity:0.75;">{n}</span></span>
    <span style="padding:4px 12px;border-radius:20px;font-size:12px;font-weight:500;background:#f1f5f9;color:#64748b;border:1px solid transparent;cursor:pointer;">{Value}</span>
    <!-- more chips -->
  </div>
  <div style="flex:1;"></div>
  <span style="font-size:12.5px;color:#64748b;">Showing {n} of {total}</span>
</div>
```

---

## Record form — inline field validation

Rules live on the field: required mark (`*`), helper text, inline error on
invalid. The submit stays `disabled` until the form is valid. Never add a
separate rules / validation-status panel.

```html
<form novalidate>
  <div style="background:#fff;border:1px solid #ececf0;border-radius:12px;box-shadow:0 2px 8px rgba(0,0,0,.04);overflow:hidden;margin-bottom:16px;">
    <div style="padding:16px 20px;border-bottom:1px solid #ececf0;display:flex;align-items:center;gap:10px;">
      <!-- icon SVG, color var(--color-accent) -->
      <div>
        <div style="font-size:14px;font-weight:700;color:#0f172a;">{Section title}</div>
        <div style="font-size:11.5px;color:#64748b;margin-top:1px;">{Description}</div>
      </div>
    </div>
    <div style="padding:20px;">
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px 20px;">

        <!-- valid required field -->
        <div style="display:flex;flex-direction:column;gap:4px;">
          <label style="font-size:12.5px;font-weight:600;color:#334155;">{Label} <span style="color:var(--color-accent);">*</span></label>
          <input type="text" style="padding:9px 12px;border:1px solid #ececf0;border-radius:8px;font-size:13.5px;color:#0f172a;background:#fff;outline:none;font-family:inherit;">
          <span style="font-size:11.5px;color:#94a3b8;">{What this value drives / format hint}</span>
        </div>

        <!-- invalid field: danger border + danger-bg + error-msg -->
        <div style="display:flex;flex-direction:column;gap:4px;">
          <label style="font-size:12.5px;font-weight:600;color:#334155;">{Label} <span style="color:var(--color-accent);">*</span></label>
          <input type="text" aria-invalid="true" style="padding:9px 12px;border:1px solid var(--color-danger);border-radius:8px;font-size:13.5px;color:#0f172a;background:var(--color-danger-bg);outline:none;font-family:inherit;">
          <span style="display:flex;align-items:center;gap:4px;font-size:11.5px;color:var(--color-danger);font-weight:500;">
            <!-- alert icon SVG -->
            {Specific rule that failed — e.g. "Must be greater than 0"}
          </span>
        </div>

        <!-- required select -->
        <div style="display:flex;flex-direction:column;gap:4px;">
          <label style="font-size:12.5px;font-weight:600;color:#334155;">{Label} <span style="color:var(--color-accent);">*</span></label>
          <select style="padding:9px 12px;border:1px solid #ececf0;border-radius:8px;font-size:13.5px;color:#0f172a;background:#fff;outline:none;font-family:inherit;appearance:none;">
            <option value="">Select…</option>
            <!-- options -->
          </select>
          <span style="font-size:11.5px;color:#94a3b8;">{Constraint on the options}</span>
        </div>

        <!-- full-width field: add grid-column:1/-1 -->
        <div style="display:flex;flex-direction:column;gap:4px;grid-column:1/-1;">
          <label style="font-size:12.5px;font-weight:600;color:#334155;">{Label}</label>
          <textarea style="padding:9px 12px;border:1px solid #ececf0;border-radius:8px;font-size:13.5px;color:#0f172a;background:#fff;outline:none;font-family:inherit;resize:vertical;min-height:80px;"></textarea>
        </div>

      </div>
    </div>
    <!-- form footer -->
    <div style="display:flex;align-items:center;justify-content:space-between;padding:16px 20px;border-top:1px solid #ececf0;background:#f8fafc;border-radius:0 0 12px 12px;">
      <span style="font-size:12px;color:#94a3b8;">Fields marked <span style="color:var(--color-accent);">*</span> are required.</span>
      <div style="display:flex;gap:10px;">
        <button type="button" class="btn-ghost">Cancel</button>
        <button type="submit" class="btn-primary" disabled style="opacity:0.45;cursor:not-allowed;">{Submit}</button>
      </div>
    </div>
  </div>
</form>
```

---

## Record detail — header + meta grid + two-col panels

```html
<div style="display:flex;flex-direction:column;gap:20px;">

  <!-- Breadcrumb -->
  <div style="font-size:12px;color:#94a3b8;display:flex;align-items:center;gap:6px;">
    <a href="#" style="color:var(--color-accent);text-decoration:none;font-weight:500;">{Parent}</a>
    <!-- chevron SVG -->
    <span>{ID}</span>
  </div>

  <!-- Detail header card -->
  <div style="background:#fff;border:1px solid #ececf0;border-radius:12px;padding:20px 24px;box-shadow:0 2px 8px rgba(0,0,0,.04);display:flex;align-items:flex-start;justify-content:space-between;gap:16px;">
    <div>
      <div style="display:flex;align-items:center;gap:10px;margin-bottom:6px;">
        <span style="font-size:12px;font-weight:600;color:#94a3b8;font-family:monospace;">{REC-ID}</span>
        <!-- status-pill -->
        <!-- channel-chip -->
      </div>
      <div style="font-size:22px;font-weight:800;color:#0f172a;letter-spacing:-0.3px;">{Record name}</div>
      <div style="font-size:13px;color:#64748b;margin-top:4px;">{Channel · sub-line · date}</div>
    </div>
    <div style="display:flex;gap:10px;flex-shrink:0;">
      <button class="btn-ghost">{Action}</button>
      <button class="btn-primary">Edit</button>
    </div>
  </div>

  <!-- Meta grid (3-col label/value) -->
  <div style="background:#fff;border:1px solid #ececf0;border-radius:12px;box-shadow:0 2px 8px rgba(0,0,0,.04);">
    <div style="padding:16px 20px;border-bottom:1px solid #ececf0;">
      <div style="font-size:14px;font-weight:700;color:#0f172a;">Details</div>
    </div>
    <div style="display:grid;grid-template-columns:repeat(3,1fr);padding:20px;gap:20px 16px;">
      <div>
        <div style="font-size:10.5px;font-weight:600;letter-spacing:0.5px;text-transform:uppercase;color:#94a3b8;margin-bottom:4px;">{FIELD}</div>
        <div style="font-size:14px;font-weight:600;color:#0f172a;">{value}</div>
        <div style="font-size:11px;color:#94a3b8;margin-top:2px;">{sub}</div>
      </div>
      <!-- more cells -->
    </div>
  </div>

  <!-- Two-col (7fr 5fr): performance bars + activity feed -->
  <div style="display:grid;grid-template-columns:7fr 5fr;gap:16px;">
    <div style="background:#fff;border:1px solid #ececf0;border-radius:12px;box-shadow:0 2px 8px rgba(0,0,0,.04);">
      <div style="padding:16px 20px;border-bottom:1px solid #ececf0;">
        <div style="font-size:14px;font-weight:700;color:#0f172a;">Weekly Performance</div>
      </div>
      <!-- perf-row: label(90px) + bar-track(flex:1, 8px tall) + value(70px right) -->
      <!-- bar-fill: rose gradient, proportional width -->
    </div>
    <div style="background:#fff;border:1px solid #ececf0;border-radius:12px;box-shadow:0 2px 8px rgba(0,0,0,.04);">
      <div style="padding:16px 20px;border-bottom:1px solid #ececf0;">
        <div style="font-size:14px;font-weight:700;color:#0f172a;">Recent Activity</div>
      </div>
      <!-- activity-item: dot-col(dot 10px + vertical line) + body(event 13px + meta 11px) -->
      <!-- dot colors: accent, indigo, sky, success by event type -->
    </div>
  </div>

</div>
```
