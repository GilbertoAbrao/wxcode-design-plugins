# Volt Admin — layout skeletons

Paste-ready, domain-neutral fragments for the deep-navy / dual-accent skin. Each
skeleton is labelled by archetype slot, not by a domain noun. Copy the shell from
`assets/template.html` first (it carries the `:root` tokens + navbar + region
switcher + icon rail + main slot), then drop the region skeletons below into
`<main class="main">`. Replace every placeholder label with the real domain's
equivalent.

Token recap (full block in `template.html`): canvas `#0a0e14`, panel `#121822`,
card `#1a2230`, hairline `#28323f`; text `#e4ecf4 / #8794a4`; amber `#fbbf24`
(primary CTA, active state, alert); cyan `#22d3ee` (trend series, output figures);
state tokens `--state-online / --state-degraded / --state-offline`.
Put `font-variant-numeric: tabular-nums` on every numeric cell.

---

## Page header (every screen)

```html
<div class="page-header"
  style="display:flex;align-items:flex-start;justify-content:space-between">
  <div>
    <h1 style="font-size:17px;font-weight:700;color:var(--text-hi)">{Screen title}</h1>
    <div style="font-size:12px;color:var(--text-muted);margin-top:2px">{scope · context · timestamp}</div>
  </div>
  <div style="display:flex;gap:8px;align-items:center">
    <!-- optional live dot -->
    <span class="live-dot">{Live label}</span>
    <button class="btn-ghost">{Secondary}</button>
    <button class="btn-primary">+ {Primary action}</button>
  </div>
</div>
```

Live-dot CSS (add to `<style>`):
```css
.live-dot{display:flex;align-items:center;gap:6px;font-size:11px;color:var(--state-online);font-weight:600;letter-spacing:.05em;text-transform:uppercase}
.live-dot::before{content:'';width:7px;height:7px;border-radius:50%;background:var(--state-online);box-shadow:0 0 6px var(--state-online);animation:pulse 2s ease-in-out infinite}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.4}}
```

---

## KPI tile row (repeat ×4 in a 4-column grid)

```html
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:12px">
  <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:8px;padding:16px;display:flex;flex-direction:column;gap:8px">
    <div style="font-size:10px;font-weight:600;text-transform:uppercase;letter-spacing:.08em;color:var(--text-muted);display:flex;align-items:center;justify-content:space-between">
      {METRIC LABEL}
      <!-- icon SVG (14×14, stroke var(--accent-cyan) or var(--accent-amber)) -->
    </div>
    <div style="font-size:28px;font-weight:700;letter-spacing:-.5px;color:var(--accent-cyan)">
      {figure} <span style="font-size:16px;font-weight:500;color:var(--text-muted)">{unit}</span>
    </div>
    <div style="display:flex;align-items:center;justify-content:space-between">
      <!-- delta chip -->
      <div style="display:flex;align-items:center;gap:4px;font-size:11px;font-weight:600;color:var(--state-online)">
        {▲/▼} {delta label}
      </div>
      <!-- sparkline SVG OR arc SVG OR .kpi-sub text -->
      <svg class="sparkline" width="72" height="24" viewBox="0 0 72 24">
        <polyline points="…" fill="none" stroke="var(--accent-cyan)" stroke-width="1.5"
          stroke-linecap="round" stroke-linejoin="round" opacity=".8"/>
      </svg>
    </div>
  </div>
  <!-- 3 more tiles; color: .cyan / .amber / .green / .red -->
</div>
```

---

## Full-width status board

```html
<div style="background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">
  <div style="padding:12px 16px;border-bottom:1px solid var(--border);display:flex;align-items:center;justify-content:space-between">
    <div style="font-size:13px;font-weight:600;color:var(--text-hi)">{Board title}</div>
    <div style="font-size:11px;color:var(--text-muted)">{N entities · N degraded · N offline}</div>
  </div>
  <table style="width:100%;border-collapse:collapse">
    <thead>
      <tr>
        <th style="text-align:left;padding:8px 16px;font-size:10px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--text-muted);border-bottom:1px solid var(--border)">{Entity}</th>
        <th style="…">{Type/Source}</th>
        <th style="…">{Metric}</th>
        <th style="…">State</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:10px 16px;border-bottom:1px solid var(--border);vertical-align:middle">
          <span style="display:inline-block;font-size:10px;font-weight:600;letter-spacing:.05em;text-transform:uppercase;padding:2px 7px;border-radius:3px;margin-right:6px;background:rgba(255,255,255,.06);color:var(--text-muted)">{Zone}</span>
          <span style="font-weight:600;color:var(--text-hi);font-size:12px">{Entity name}</span>
        </td>
        <td style="…"><span style="font-size:11px;color:var(--text-muted)">{Type}</span></td>
        <td style="…"><span style="font-weight:700;font-size:13px;color:var(--text-hi)">{value}</span><span style="font-size:11px;color:var(--text-muted);margin-left:2px">{unit}</span></td>
        <td style="…"><span class="pill pill-online">Online</span></td>
      </tr>
      <!-- state variants: .pill-online / .pill-degraded / .pill-offline -->
    </tbody>
  </table>
</div>
```

---

## Dual-series trend chart

```html
<div style="background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">
  <div style="padding:14px 16px;border-bottom:1px solid var(--border);display:flex;align-items:center;justify-content:space-between">
    <div>
      <div style="font-size:13px;font-weight:600;color:var(--text-hi)">{Series A} vs. {Series B} — {Period}</div>
      <div style="font-size:11px;color:var(--text-muted)">{scope · timestamp}</div>
    </div>
    <div style="display:flex;gap:16px">
      <span style="display:flex;align-items:center;gap:6px;font-size:11px;color:var(--text-muted)">
        <span style="width:8px;height:8px;border-radius:50%;background:var(--accent-cyan)"></span>{Series A}
      </span>
      <span style="display:flex;align-items:center;gap:6px;font-size:11px;color:var(--text-muted)">
        <span style="width:8px;height:8px;border-radius:50%;background:var(--accent-amber)"></span>{Series B}
      </span>
    </div>
  </div>
  <div style="padding:16px">
    <svg viewBox="0 0 620 180" style="display:block;width:100%;height:180px">
      <!-- horizontal gridlines -->
      <line x1="0" y1="150" x2="620" y2="150" stroke="var(--border)" stroke-width=".8"/>
      <line x1="0" y1="112" x2="620" y2="112" stroke="var(--border)" stroke-width=".8"/>
      <line x1="0" y1="75"  x2="620" y2="75"  stroke="var(--border)" stroke-width=".8"/>
      <line x1="0" y1="37"  x2="620" y2="37"  stroke="var(--border)" stroke-width=".8"/>
      <!-- y-axis labels -->
      <text x="0" y="153" font-size="9" fill="var(--text-muted)">{low}</text>
      <text x="0" y="78"  font-size="9" fill="var(--text-muted)">{mid}</text>
      <text x="0" y="40"  font-size="9" fill="var(--text-muted)">{high}</text>
      <!-- area fill definitions -->
      <defs>
        <linearGradient id="cy-fill" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stop-color="var(--accent-cyan)" stop-opacity=".18"/>
          <stop offset="100%" stop-color="var(--accent-cyan)" stop-opacity="0"/>
        </linearGradient>
        <linearGradient id="am-fill" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stop-color="var(--accent-amber)" stop-opacity=".15"/>
          <stop offset="100%" stop-color="var(--accent-amber)" stop-opacity="0"/>
        </linearGradient>
      </defs>
      <!-- Series A (cyan): area polygon, then line polyline -->
      <polygon points="{pts} 610,155 38,155" fill="url(#cy-fill)"/>
      <polyline points="{pts}" fill="none" stroke="var(--accent-cyan)" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
      <!-- Series B (amber): area polygon, then line polyline -->
      <polygon points="{pts} 610,155 38,155" fill="url(#am-fill)"/>
      <polyline points="{pts}" fill="none" stroke="var(--accent-amber)" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
      <!-- x-axis labels -->
      <text x="35"  y="170" font-size="9" fill="var(--text-muted)" text-anchor="middle">{t0}</text>
      <text x="610" y="170" font-size="9" fill="var(--text-muted)" text-anchor="middle">{tN}</text>
    </svg>
  </div>
</div>
```

---

## Alerts table (right column)

```html
<div style="background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">
  <div style="padding:12px 16px;border-bottom:1px solid var(--border);display:flex;align-items:center;justify-content:space-between">
    <div style="font-size:13px;font-weight:600;color:var(--text-hi)">Active Alerts</div>
    <span style="background:rgba(248,113,113,.16);color:var(--state-offline);font-size:10px;font-weight:700;padding:2px 8px;border-radius:4px">{N} Open</span>
  </div>
  <table style="width:100%;border-collapse:collapse">
    <thead>
      <tr>
        <th style="text-align:left;padding:7px 12px;font-size:10px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--text-muted);border-bottom:1px solid var(--border)">ID</th>
        <th style="…">Entity</th>
        <th style="…">Sev</th>
        <th style="…">Status</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:9px 12px;border-bottom:1px solid var(--border);vertical-align:middle;font-size:12px">
          <span style="font-family:monospace;font-size:11px;color:var(--text-muted)">{ID}</span>
        </td>
        <td style="…">
          <span style="font-weight:600;font-size:12px">{Entity name}</span><br>
          <span style="color:var(--text-muted);font-size:11px">{Short message}</span>
        </td>
        <td style="…">
          <!-- severity: .sev-critical / .sev-high / .sev-info -->
          <span class="pill sev-critical">Critical</span>
        </td>
        <td style="…">
          <!-- status: open / ack / resolved -->
          <span class="pill status-open">Open</span>
        </td>
      </tr>
    </tbody>
  </table>
</div>
```

Pill CSS for severity + status (add to `<style>`):
```css
.sev-critical{background:rgba(248,113,113,.16);color:var(--state-offline)}
.sev-high{background:rgba(251,191,36,.14);color:var(--state-degraded)}
.sev-info{background:rgba(135,148,164,.12);color:var(--text-muted)}
.status-open{border:1px solid rgba(248,113,113,.5);color:var(--state-offline)}
.status-ack{border:1px solid rgba(251,191,36,.5);color:var(--state-degraded)}
.status-resolved{border:1px solid rgba(52,211,153,.5);color:var(--state-online)}
```

---

## Entity side panel (right column, stacked below alerts)

```html
<div style="background:var(--bg-panel);border:1px solid var(--border);border-radius:8px;overflow:hidden">
  <div style="padding:12px 14px;border-bottom:1px solid var(--border);display:flex;align-items:center;justify-content:space-between">
    <div style="font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:.07em;color:var(--text-muted)">{Panel title}</div>
    <span class="pill pill-online" style="font-size:9px">Online</span>
  </div>
  <div style="padding:12px 14px;display:flex;flex-direction:column;gap:10px">
    <div>
      <div style="font-size:15px;font-weight:700;color:var(--text-hi);margin-bottom:2px">{Entity name}</div>
      <div style="font-size:11px;color:var(--text-muted)">{Zone · Type}</div>
    </div>
    <div style="height:1px;background:var(--border)"></div>
    <!-- detail rows -->
    <div style="display:flex;justify-content:space-between;align-items:center;padding:6px 0;border-bottom:1px solid var(--border)">
      <span style="font-size:11px;color:var(--text-muted)">{Label}</span>
      <span style="font-size:11px;font-weight:600;color:var(--text-hi)">{Value}</span>
    </div>
    <!-- more rows; last row: border-bottom:none -->
    <!-- progress bar -->
    <div>
      <div style="height:6px;border-radius:3px;background:var(--border);overflow:hidden">
        <div style="height:100%;border-radius:3px;background:var(--state-online);width:{pct}%"></div>
      </div>
      <div style="font-size:10px;color:var(--text-muted);margin-top:4px;text-align:right">{pct}% {label}</div>
    </div>
  </div>
</div>
```

---

## Toolbar (search + filter chips — list screen)

```html
<div style="display:flex;align-items:center;gap:12px;flex-wrap:wrap;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;padding:10px 16px">
  <div style="display:flex;align-items:center;gap:8px;background:var(--bg-root);border:1px solid var(--border);border-radius:6px;padding:5px 10px;flex:1;max-width:320px">
    <!-- magnifier SVG -->
    <input type="text" placeholder="Filter by {fields}…" style="background:none;border:none;outline:none;font-size:12px;color:var(--text-hi);width:100%;font-family:inherit">
  </div>
  <div style="display:flex;align-items:center;gap:6px">
    <span style="font-size:11px;color:var(--text-muted)">{Facet}</span>
    <span class="chip active">All <span style="font-size:10px;opacity:.7">{n}</span></span>
    <span class="chip">{Value} <span style="font-size:10px;opacity:.7">{n}</span></span>
  </div>
  <div style="margin-left:auto;font-size:11px;color:var(--text-muted)">Showing {a}–{b} of {n}</div>
</div>
```

Chip CSS (add to `<style>`):
```css
.chip{display:inline-flex;align-items:center;gap:5px;padding:4px 10px;border-radius:20px;font-size:11px;font-weight:500;background:var(--bg-root);border:1px solid var(--border);color:var(--text-muted);cursor:pointer;transition:all .15s}
.chip.active{background:rgba(34,211,238,.1);border-color:var(--accent-cyan);color:var(--accent-cyan)}
```

---

## Record form — fields with inline validation

Rules live ON the field: a required mark (`*`), helper text under the field, and
an inline error message on an invalid field. The submit stays `disabled` until the
form is valid. Never add a separate rules/validation-status summary panel.

```html
<form novalidate>
  <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden;margin-bottom:14px">
    <div style="padding:12px 20px;border-bottom:1px solid var(--border);display:flex;align-items:center;gap:8px">
      <!-- section icon SVG 14×14 -->
      <div style="font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:.07em;color:var(--text-muted)">{Section}</div>
    </div>
    <div style="padding:20px;display:flex;flex-direction:column;gap:16px">
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px">

        <!-- valid field -->
        <div style="display:flex;flex-direction:column;gap:4px">
          <label style="font-size:12px;font-weight:500;color:var(--text-muted)">{Label} <span style="color:var(--accent-amber)">*</span></label>
          <input class="control" type="text" value="">
          <span style="font-size:11px;color:var(--text-muted)">{what the value drives / format hint}</span>
        </div>

        <!-- invalid field: show error-msg, add invalid styles to .control -->
        <div style="display:flex;flex-direction:column;gap:4px">
          <label style="font-size:12px;font-weight:500;color:var(--text-muted)">{Label} <span style="color:var(--accent-amber)">*</span></label>
          <input class="control" type="text" aria-invalid="true"
            style="border-color:var(--state-offline);background:rgba(248,113,113,.04)">
          <span style="display:flex;align-items:center;gap:5px;font-size:11px;color:var(--state-offline);font-weight:500">
            <!-- alert icon SVG 11×11 -->
            {Specific rule that failed}
          </span>
        </div>

        <!-- required select -->
        <div style="display:flex;flex-direction:column;gap:4px">
          <label style="font-size:12px;font-weight:500;color:var(--text-muted)">{Label} <span style="color:var(--accent-amber)">*</span></label>
          <select class="control"><option value="">Select…</option></select>
          <span style="font-size:11px;color:var(--text-muted)">{constraint on the options}</span>
        </div>

      </div>
    </div>
  </div>

  <div style="display:flex;align-items:center;justify-content:space-between;padding:14px 20px;background:var(--bg-panel);border:1px solid var(--border);border-radius:8px">
    <span style="font-size:11px;color:var(--text-muted)">Fields marked <span style="color:var(--accent-amber)">*</span> are required.</span>
    <div style="display:flex;gap:8px">
      <button type="button" class="btn-ghost">Cancel</button>
      <button type="submit" class="btn-primary" disabled>{Submit}</button>
    </div>
  </div>
</form>
```

Control base CSS (add to `<style>`):
```css
.control{width:100%;padding:8px 12px;background:var(--bg-root);border:1px solid var(--border);border-radius:6px;font-size:13px;color:var(--text-hi);font-family:inherit;transition:border-color .15s,box-shadow .15s;outline:none}
.control:focus{border-color:var(--accent-cyan);box-shadow:0 0 0 2px rgba(34,211,238,.1)}
```

---

## Record detail — header + meta grid + related panels

```html
<!-- Breadcrumb -->
<div style="font-size:12px;color:var(--text-muted);display:flex;align-items:center;gap:6px">
  <a href="#" style="color:var(--text-muted);text-decoration:none">{Parent list}</a>
  <span style="opacity:.4">›</span>
  <span>{Entity name}</span>
</div>

<!-- Detail header -->
<div style="display:flex;align-items:center;justify-content:space-between;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;padding:18px 20px">
  <div>
    <div style="display:flex;align-items:center;gap:10px">
      <span style="font-family:monospace;font-size:13px;color:var(--text-muted)">{ID}</span>
      <span class="pill pill-online">{State}</span>
    </div>
    <div style="font-size:20px;font-weight:700;color:var(--text-hi);margin-top:2px">{Entity name}</div>
    <div style="font-size:12px;color:var(--text-muted);margin-top:2px">{Zone · Type · Commissioned date}</div>
  </div>
  <div style="display:flex;gap:8px">
    <button class="btn-ghost">{Action}</button>
    <button class="btn-primary">Edit</button>
  </div>
</div>

<!-- Meta grid (3 columns) -->
<div style="background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">
  <div style="padding:12px 16px;border-bottom:1px solid var(--border);font-size:13px;font-weight:600;color:var(--text-hi)">Overview</div>
  <div style="display:grid;grid-template-columns:repeat(3,1fr)">
    <div style="padding:12px 16px;border-right:1px solid var(--border);border-bottom:1px solid var(--border)">
      <div style="font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.07em;color:var(--text-muted);margin-bottom:4px">{FIELD}</div>
      <div style="font-size:15px;font-weight:700;color:var(--text-hi)">{value}</div>
      <div style="font-size:11px;color:var(--text-muted);margin-top:2px">{sub}</div>
    </div>
    <!-- more cells; nth-child(3n): border-right:none; nth-last-child(-n+3): border-bottom:none -->
  </div>
</div>

<!-- Two-column (7fr / 5fr): events table + activity timeline -->
<div style="display:grid;grid-template-columns:7fr 5fr;gap:16px;align-items:start">
  <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">
    <!-- events/related-records table -->
  </div>
  <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">
    <!-- activity timeline -->
  </div>
</div>
```
