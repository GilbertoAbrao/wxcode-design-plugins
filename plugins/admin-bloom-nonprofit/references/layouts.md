# Bloom Admin — layout skeletons

Paste-ready, domain-neutral fragments for the Bloom warm light-mode skin. Each
skeleton is labelled by archetype slot, not by a domain noun. Copy the shell from
`assets/template.html` first (it carries the `:root` tokens + sidebar + topbar +
content slot), then drop the region skeletons below into `<div class="content">`.
Replace every placeholder label with the real domain's equivalent.

Token recap (full block in `template.html`): page `#f7fbf9`, card `#ffffff`,
border `#e4ede9`, hover row `#f9fdfb`; text `#1e293b / #64748b / #94a3b8`;
accent `var(--accent)` = `#10b981`; coral `var(--coral)` = `#fb7185`;
amber `var(--amber)` = `#f59e0b`. Use `font-variant-numeric: tabular-nums` on
every numeric cell.

---

## Page header (every screen)

```html
<div style="display:flex;align-items:flex-start;justify-content:space-between;gap:16px;margin-bottom:4px;">
  <div>
    <div style="font-size:11px;color:#94a3b8;margin-bottom:2px;">{breadcrumb}</div>
    <div style="font-size:20px;font-weight:700;">{Screen title}</div>
    <div style="font-size:12px;color:#64748b;margin-top:2px;">{scope · context}</div>
  </div>
  <div style="display:flex;align-items:center;gap:10px;flex-shrink:0;">
    <button class="btn-ghost">{Secondary}</button>
    <button class="btn-primary">+ {Primary action}</button>
  </div>
</div>
```

---

## KPI card row (4 equal columns)

```html
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:16px;">
  <div class="card" style="padding:18px 20px 14px;display:flex;flex-direction:column;gap:4px;">
    <div style="font-size:10px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;color:#94a3b8;">{METRIC LABEL}</div>
    <div style="display:flex;align-items:flex-end;justify-content:space-between;gap:8px;margin-top:4px;">
      <div style="font-size:26px;font-weight:700;line-height:1.1;font-variant-numeric:tabular-nums;">{figure}</div>
      <!-- 7-point inline SVG sparkline -->
      <svg width="44" height="26" viewBox="0 0 44 26" fill="none">
        <polyline points="2,{y1} 9,{y2} 16,{y3} 23,{y4} 30,{y5} 37,{y6} 44,{y7}"
          stroke="var(--accent)" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
        <polyline points="2,{y1} 9,{y2} 16,{y3} 23,{y4} 30,{y5} 37,{y6} 44,{y7} 44,26 2,26"
          fill="var(--accent)" fill-opacity="0.12"/>
      </svg>
    </div>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px;">
      <!-- .up → accent-light/dark; .down → coral-light/dark -->
      <span style="font-size:11px;font-weight:700;padding:2px 7px;border-radius:20px;background:var(--accent-light);color:var(--accent-dark);">↑ {delta}</span>
      <span style="font-size:11px;color:#94a3b8;">{context label}</span>
    </div>
  </div>
  <!-- 3 more cards -->
</div>
```

---

## Mid-row: progress list + segment donut (2 columns)

```html
<div style="display:grid;grid-template-columns:1fr 320px;gap:16px;align-items:start;">

  <!-- LEFT: progress list card -->
  <div class="card">
    <div class="card-header">
      <span class="card-title">{Primary entity list title}</span>
      <button style="font-size:12px;font-weight:600;color:var(--accent-dark);background:none;border:none;cursor:pointer;">View all →</button>
    </div>
    <table style="width:100%;border-collapse:collapse;">
      <thead>
        <tr>
          <th style="font-size:10px;font-weight:600;letter-spacing:.05em;text-transform:uppercase;color:#94a3b8;padding:8px 20px;text-align:left;background:#f7fbf9;border-bottom:1px solid #e4ede9;">{Entity}</th>
          <th style="…">Progress</th>
          <th style="…">{Amount A}</th>
          <th style="…">{Amount B}</th>
          <th style="…">{Deadline}</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td style="padding:11px 20px;border-bottom:1px solid #e4ede9;font-size:13px;">
            <div style="display:flex;flex-direction:column;gap:2px;">
              <span style="font-weight:600;">{Entity name}</span>
              <!-- status badge: .active .ending .paused -->
              <span style="display:inline-flex;align-items:center;gap:4px;font-size:10px;font-weight:700;border-radius:20px;padding:2px 7px;background:var(--accent-light);color:var(--accent-dark);">
                <svg width="7" height="7" viewBox="0 0 8 8"><circle cx="4" cy="4" r="4" fill="currentColor"/></svg>
                Active
              </span>
            </div>
          </td>
          <td style="padding:11px 20px;border-bottom:1px solid #e4ede9;font-size:13px;">
            <div style="display:flex;flex-direction:column;gap:4px;min-width:120px;">
              <div style="height:6px;border-radius:3px;background:#e4ede9;overflow:hidden;">
                <div style="height:100%;border-radius:3px;background:var(--accent);width:{pct}%;transition:width .4s;"></div>
              </div>
              <span style="font-size:10px;color:#94a3b8;">{pct}%</span>
            </div>
          </td>
          <td style="padding:11px 20px;border-bottom:1px solid #e4ede9;font-size:13px;font-variant-numeric:tabular-nums;">{raised}</td>
          <td style="padding:11px 20px;border-bottom:1px solid #e4ede9;font-size:13px;font-variant-numeric:tabular-nums;">{goal}</td>
          <td style="padding:11px 20px;border-bottom:1px solid #e4ede9;font-size:12px;color:#64748b;white-space:nowrap;">{deadline}</td>
        </tr>
        <!-- more rows -->
      </tbody>
    </table>
  </div>

  <!-- RIGHT: segment donut panel -->
  <!-- circumference = 2π×58 ≈ 364.4; each arc's dasharray = (pct/100)*364.4 -->
  <div class="card" style="display:flex;flex-direction:column;">
    <div class="card-header"><span class="card-title">{Segment title}</span></div>
    <div style="display:flex;justify-content:center;padding:20px 20px 10px;">
      <svg width="160" height="160" viewBox="0 0 160 160">
        <!-- Arc 1 (accent): pct1% -->
        <circle cx="80" cy="80" r="58" fill="none" stroke="var(--accent)" stroke-width="22"
          stroke-dasharray="{len1} {364.4-len1}" stroke-dashoffset="0"
          stroke-linecap="butt" transform="rotate(-90 80 80)"/>
        <!-- Arc 2 (accent-mid): offset = -(len1+gap) -->
        <circle cx="80" cy="80" r="58" fill="none" stroke="var(--accent-mid)" stroke-width="22"
          stroke-dasharray="{len2} {364.4-len2}" stroke-dashoffset="-{len1+4}"
          stroke-linecap="butt" transform="rotate(-90 80 80)"/>
        <!-- Arc 3 (coral): offset = -(len1+len2+2×gap) -->
        <circle cx="80" cy="80" r="58" fill="none" stroke="var(--coral)" stroke-width="22"
          stroke-dasharray="{len3} {364.4-len3}" stroke-dashoffset="-{len1+len2+8}"
          stroke-linecap="butt" transform="rotate(-90 80 80)"/>
        <!-- Arc 4 (amber): offset = -(len1+len2+len3+3×gap) -->
        <circle cx="80" cy="80" r="58" fill="none" stroke="var(--amber)" stroke-width="22"
          stroke-dasharray="{len4} {364.4-len4}" stroke-dashoffset="-{len1+len2+len3+12}"
          stroke-linecap="butt" transform="rotate(-90 80 80)"/>
        <!-- Center label -->
        <text x="80" y="74" text-anchor="middle" font-size="22" font-weight="700" fill="#1e293b">{total}</text>
        <text x="80" y="90" text-anchor="middle" font-size="10" fill="#94a3b8">{unit}</text>
      </svg>
    </div>
    <div style="padding:0 20px 18px;display:flex;flex-direction:column;gap:9px;">
      <div style="display:flex;align-items:center;gap:8px;">
        <span style="width:10px;height:10px;border-radius:50%;background:var(--accent);flex-shrink:0;"></span>
        <span style="font-size:12px;color:#64748b;flex:1;">{Segment A label}</span>
        <span style="font-size:12px;font-weight:600;font-variant-numeric:tabular-nums;">{count}</span>
        <span style="font-size:11px;color:#94a3b8;min-width:34px;text-align:right;">{pct}%</span>
      </div>
      <!-- repeat for accent-mid, coral, amber -->
    </div>
  </div>

</div>
```

---

## Full-width trend chart

```html
<div class="card">
  <div class="card-header">
    <span class="card-title">{Trend title — Last 12 Months}</span>
    <div style="display:flex;align-items:center;gap:16px;">
      <div style="display:flex;align-items:center;gap:6px;font-size:12px;color:#64748b;">
        <span style="width:12px;height:12px;border-radius:3px;background:var(--accent);"></span>{Series A}
      </div>
      <div style="display:flex;align-items:center;gap:6px;font-size:12px;color:#64748b;">
        <span style="width:12px;height:12px;border-radius:3px;background:var(--coral);"></span>{Series B}
      </div>
    </div>
  </div>
  <div style="padding:16px 20px 8px;">
    <!-- dual-area chart; viewBox 760×120; y = 120 - (val/maxVal)*120 -->
    <svg viewBox="0 0 760 120" height="140" preserveAspectRatio="none" style="display:block;width:100%;">
      <!-- grid lines at y=0,40,80,120 -->
      <line x1="0" y1="0"   x2="760" y2="0"   stroke="#e4ede9" stroke-width="1"/>
      <line x1="0" y1="40"  x2="760" y2="40"  stroke="#e4ede9" stroke-width="1"/>
      <line x1="0" y1="80"  x2="760" y2="80"  stroke="#e4ede9" stroke-width="1"/>
      <line x1="0" y1="120" x2="760" y2="120" stroke="#e4ede9" stroke-width="1"/>
      <!-- Series A (accent) — 12 monthly x-positions: 0,63.3,126.7,190,253.3,316.7,380,443.3,506.7,570,633.3,696.7 -->
      <polygon points="0,120 {series-a-pts} {last-x},{last-y} {last-x},120" fill="var(--accent)" fill-opacity="0.18"/>
      <polyline points="{series-a-pts}" fill="none" stroke="var(--accent)" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"/>
      <!-- Series B (coral) -->
      <polygon points="0,120 {series-b-pts} {last-x},{last-y-b} {last-x},120" fill="var(--coral)" fill-opacity="0.16"/>
      <polyline points="{series-b-pts}" fill="none" stroke="var(--coral)" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"/>
    </svg>
  </div>
  <div style="display:flex;justify-content:space-between;padding:4px 20px 14px;">
    <!-- 12 month labels -->
    <span style="font-size:10px;color:#94a3b8;">Jan</span>
    <span style="font-size:10px;color:#94a3b8;">Feb</span>
    <!-- … -->
    <span style="font-size:10px;color:#94a3b8;">Dec</span>
  </div>
</div>
```

---

## Records table (list screen or dashboard section)

```html
<div class="card">
  <div class="card-header">
    <span class="card-title">{Records title}</span>
    <div style="display:flex;gap:8px;align-items:center;">
      <button class="btn-ghost">Export</button>
      <button class="btn-primary">+ {New record}</button>
    </div>
  </div>
  <table style="width:100%;border-collapse:collapse;">
    <thead>
      <tr>
        <th style="font-size:10px;font-weight:600;letter-spacing:.05em;text-transform:uppercase;color:#94a3b8;padding:9px 20px;text-align:left;background:#f7fbf9;border-bottom:1px solid #e4ede9;">{Entity}</th>
        <th style="…">{Dimension}</th>
        <th style="…">{Amount}</th>
        <th style="…">Type</th>
        <th style="…">{Date}</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:10px 20px;border-bottom:1px solid #e4ede9;font-size:13px;vertical-align:middle;">
          <div style="display:flex;align-items:center;gap:9px;">
            <div style="width:30px;height:30px;border-radius:50%;background:var(--accent);color:#fff;font-size:11px;font-weight:700;display:flex;align-items:center;justify-content:center;flex-shrink:0;">{II}</div>
            <span style="font-weight:600;">{Entity name}</span>
          </div>
        </td>
        <td style="padding:10px 20px;border-bottom:1px solid #e4ede9;font-size:13px;">{dimension value}</td>
        <td style="padding:10px 20px;border-bottom:1px solid #e4ede9;font-size:13px;font-weight:700;font-variant-numeric:tabular-nums;">{amount}</td>
        <td style="padding:10px 20px;border-bottom:1px solid #e4ede9;font-size:13px;">
          <!-- .primary → accent; .recurring → coral -->
          <span style="font-size:10px;font-weight:700;padding:3px 9px;border-radius:20px;background:var(--accent-light);color:var(--accent-dark);">Primary</span>
        </td>
        <td style="padding:10px 20px;border-bottom:1px solid #e4ede9;font-size:12px;color:#94a3b8;">{date}</td>
      </tr>
      <!-- more rows -->
    </tbody>
  </table>
  <div style="display:flex;align-items:center;justify-content:space-between;padding:14px 20px;border-top:1px solid #e4ede9;background:#f7fbf9;">
    <span style="font-size:12px;color:#94a3b8;">Showing {a}–{b} of {n}</span>
    <div style="display:flex;align-items:center;gap:4px;">
      <button style="width:30px;height:30px;border:1px solid #e4ede9;border-radius:7px;background:#fff;color:#64748b;font-size:13px;cursor:pointer;">‹</button>
      <button style="width:30px;height:30px;border:1px solid var(--accent);border-radius:7px;background:var(--accent);color:#fff;font-size:13px;font-weight:500;cursor:pointer;">1</button>
      <button style="width:30px;height:30px;border:1px solid #e4ede9;border-radius:7px;background:#fff;color:#64748b;font-size:13px;cursor:pointer;">2</button>
      <button style="width:30px;height:30px;border:1px solid #e4ede9;border-radius:7px;background:#fff;color:#64748b;font-size:13px;cursor:pointer;">›</button>
    </div>
  </div>
</div>
```

### List toolbar (search + filter chips)

```html
<div style="display:flex;align-items:center;gap:16px;flex-wrap:wrap;">
  <div style="position:relative;flex:1;max-width:360px;">
    <svg style="position:absolute;left:10px;top:50%;transform:translateY(-50%);color:#94a3b8;" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
    <input type="text" placeholder="Search {entities}…" style="width:100%;height:36px;border:1px solid #e4ede9;border-radius:8px;background:#fff;padding:0 12px 0 34px;font-size:13px;outline:none;">
  </div>
  <div style="display:flex;align-items:center;gap:8px;flex-wrap:wrap;">
    <span style="font-size:11px;font-weight:600;color:#94a3b8;text-transform:uppercase;letter-spacing:.05em;">{Facet}</span>
    <!-- active chip -->
    <span style="font-size:11px;font-weight:600;padding:4px 10px;border-radius:20px;border:1px solid var(--accent-light);background:var(--accent-light);color:var(--accent-dark);cursor:pointer;">All <span style="font-size:10px;font-weight:700;">{n}</span></span>
    <!-- inactive chips -->
    <span style="font-size:11px;font-weight:600;padding:4px 10px;border-radius:20px;border:1px solid #e4ede9;background:#fff;color:#64748b;cursor:pointer;">{Value} <span style="font-size:10px;font-weight:700;">{n}</span></span>
  </div>
  <span style="margin-left:auto;font-size:12px;color:#94a3b8;">{n} {entities}</span>
</div>
```

---

## Record form — fields with inline validation

Rules live ON the field: a required mark (`*`), helper text under the field,
and an inline error message on an invalid field. The submit stays `disabled`
until the form is valid. Never add a separate rules/validation-status panel.

```html
<form style="display:flex;flex-direction:column;gap:16px;" novalidate>

  <div class="card">
    <div style="display:flex;align-items:center;gap:8px;padding:14px 20px;border-bottom:1px solid #e4ede9;">
      <div style="width:28px;height:28px;border-radius:7px;background:var(--accent-light);color:var(--accent);display:flex;align-items:center;justify-content:center;">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><!-- section icon --></svg>
      </div>
      <span style="font-size:13px;font-weight:700;">{Section title}</span>
    </div>
    <div style="padding:20px;">
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px 20px;">

        <!-- valid field -->
        <div style="display:flex;flex-direction:column;gap:5px;">
          <label style="font-size:12px;font-weight:600;color:#64748b;" for="f1">{Label} <span style="color:var(--coral);">*</span></label>
          <input id="f1" style="height:36px;border:1px solid var(--accent);border-radius:8px;background:#f7fbf9;padding:0 12px;font-size:13px;outline:none;" type="text" value="{valid value}">
          <span style="font-size:11px;color:#94a3b8;">{helper text / format hint}</span>
        </div>

        <!-- invalid field: coral border + error message -->
        <div style="display:flex;flex-direction:column;gap:5px;">
          <label style="font-size:12px;font-weight:600;color:#64748b;" for="f2">{Label} <span style="color:var(--coral);">*</span></label>
          <input id="f2" style="height:36px;border:1px solid var(--coral);border-radius:8px;background:var(--coral-light);padding:0 12px;font-size:13px;outline:none;" type="text" aria-invalid="true">
          <span style="display:flex;align-items:center;gap:4px;font-size:11px;font-weight:600;color:var(--coral-dark);">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
            {Specific rule that failed}
          </span>
        </div>

        <!-- required select -->
        <div style="display:flex;flex-direction:column;gap:5px;">
          <label style="font-size:12px;font-weight:600;color:#64748b;" for="f3">{Label} <span style="color:var(--coral);">*</span></label>
          <select id="f3" style="height:36px;border:1px solid #e4ede9;border-radius:8px;background:#f7fbf9;padding:0 12px;font-size:13px;outline:none;font-family:inherit;">
            <option value="">Select…</option>
          </select>
          <span style="font-size:11px;color:#94a3b8;">{constraint on the options}</span>
        </div>

      </div>
    </div>
  </div>

  <!-- FORM FOOTER -->
  <div style="display:flex;align-items:center;justify-content:space-between;padding:16px 20px;background:#fff;border:1px solid #e4ede9;border-radius:12px;">
    <span style="font-size:12px;color:#94a3b8;">Fields marked <span style="color:var(--coral);">*</span> are required.</span>
    <div style="display:flex;align-items:center;gap:10px;">
      <button type="button" class="btn-ghost">Cancel</button>
      <button type="submit" class="btn-primary" disabled>{Submit}</button>
    </div>
  </div>

</form>
```

---

## Record detail — header card + meta grid + related panels

```html
<div style="display:flex;flex-direction:column;gap:16px;">

  <!-- DETAIL HEADER CARD -->
  <div class="card" style="padding:20px 24px;display:flex;align-items:flex-start;justify-content:space-between;gap:20px;">
    <div style="flex:1;">
      <div style="font-size:11px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:#94a3b8;">{ID}</div>
      <div style="font-size:20px;font-weight:700;margin-top:4px;">{Entity name}</div>
      <div style="font-size:12px;color:#94a3b8;margin-top:4px;">{sub · coordinator · created}</div>
      <!-- optional progress strip below the name -->
    </div>
    <div style="display:flex;align-items:center;gap:10px;flex-shrink:0;">
      <button class="btn-ghost">{Secondary}</button>
      <button class="btn-primary">Edit</button>
    </div>
  </div>

  <!-- META GRID (3 columns) -->
  <div class="card">
    <div class="card-header"><span class="card-title">Details</span></div>
    <div style="display:grid;grid-template-columns:repeat(3,1fr);">
      <div style="padding:16px 20px;border-right:1px solid #e4ede9;border-bottom:1px solid #e4ede9;">
        <div style="font-size:10px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;color:#94a3b8;margin-bottom:4px;">{FIELD}</div>
        <div style="font-size:14px;font-weight:600;font-variant-numeric:tabular-nums;">{value}</div>
        <div style="font-size:11px;color:#94a3b8;margin-top:2px;">{sub}</div>
      </div>
      <!-- 5 more cells; nth-child(3n) has no border-right; last row has no border-bottom -->
    </div>
  </div>

  <!-- TWO-COL: sub-table + activity feed (7fr / 5fr → 1fr / 320px) -->
  <div style="display:grid;grid-template-columns:1fr 320px;gap:16px;align-items:start;">
    <div class="card"><!-- related records sub-table --></div>
    <div class="card"><!-- activity feed (dot + text + timestamp rows) --></div>
  </div>

</div>
```
