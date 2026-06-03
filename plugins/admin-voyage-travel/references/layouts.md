# Voyage Admin — layout skeletons

Paste-ready, domain-neutral fragments for the Voyage airy light-mode skin. Each
skeleton is labelled by archetype slot, not by a domain noun. Copy the shell from
`assets/template.html` first (it carries the `:root` tokens + sidebar + topbar +
content slot), then drop the region skeletons below into `<div class="content">`.
Replace every {placeholder} with the real domain's equivalent.

Token recap (full block in `template.html`): canvas `#f6fafc`, panel `#ffffff`,
border `#e2eaf0`; text `#1e293b / #64748b / #94a3b8`; accent `var(--sky)` = `#0ea5e9`;
secondary `var(--coral)` = `#fb7185`; status tokens `--green`, `--amber`, `--coral`
with matching `-bg` tints. `font-variant-numeric: tabular-nums` on every numeric cell.

---

## Page header (every screen)

```html
<div class="page-header" style="display:flex;align-items:center;justify-content:space-between;">
  <div>
    <div style="font-size:20px;font-weight:700;color:#1e293b;">{Screen title}</div>
    <div style="font-size:13px;color:#64748b;margin-top:3px;">{scope · context}</div>
  </div>
  <div style="display:flex;gap:10px;">
    <button class="btn-ghost">{Secondary}</button>
    <button class="btn-primary">+ {Primary action}</button>
  </div>
</div>
```

---

## KPI card row (repeat ×4 in a 4-column grid)

```html
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:16px;">
  <div class="card" style="padding:18px;position:relative;box-shadow:0 2px 12px rgba(14,165,233,.07);">
    <!-- Icon chip — absolute top-right -->
    <div style="position:absolute;top:16px;right:16px;width:36px;height:36px;background:var(--sky-bg);border-radius:10px;display:flex;align-items:center;justify-content:center;">
      <svg><!-- domain-relevant glyph, stroke=var(--sky) --></svg>
    </div>
    <div style="font-size:10px;font-weight:700;letter-spacing:.07em;color:#94a3b8;text-transform:uppercase;margin-bottom:8px;">{METRIC LABEL}</div>
    <div style="font-size:26px;font-weight:800;color:#1e293b;line-height:1;margin-bottom:10px;font-variant-numeric:tabular-nums;">{figure}</div>
    <div style="display:flex;align-items:center;gap:8px;">
      <span class="pill-green" style="display:inline-flex;align-items:center;gap:3px;font-size:11px;font-weight:700;padding:2px 7px;border-radius:10px;background:var(--green-bg);color:var(--green);">▲ {delta}</span>
      <!-- swap classes: .delta-down → coral bg; .delta-neutral → amber bg -->
      <span style="font-size:11px;color:#94a3b8;">{comparison context}</span>
      <!-- optional sparkline: 60×24px polyline, stroke=var(--sky) -->
      <svg width="60" height="24" viewBox="0 0 60 24" fill="none" style="margin-left:auto">
        <polyline points="{8 x,y pairs}" stroke="var(--sky)" stroke-width="1.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
    </div>
  </div>
  <!-- 3 more cards -->
</div>
```

---

## Entity board (primary panel)

`[icon chip] [entity name + sub-line] [count] [state pill]`

```html
<div class="card">
  <div class="card-head">
    <span class="card-title">{Board title}</span>
    <a href="#" style="font-size:12px;font-weight:600;color:var(--sky);text-decoration:none;">View all →</a>
  </div>
  <ul style="list-style:none;">
    <li style="display:flex;align-items:center;gap:14px;padding:13px 20px;border-bottom:1px solid var(--border);transition:background .1s;">
      <!-- on hover: background:#f8fafc -->
      <div style="width:32px;height:32px;border-radius:8px;background:var(--sky-bg);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
        <!-- icon or emoji / flag glyph -->
      </div>
      <div style="flex:1;min-width:0;">
        <div style="font-size:13px;font-weight:600;color:#1e293b;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">{Entity name}</div>
        <div style="font-size:11px;color:#94a3b8;margin-top:1px;">{sub-line: dates, scope, description}</div>
      </div>
      <div style="display:flex;align-items:center;gap:4px;font-size:12px;color:#64748b;flex-shrink:0;min-width:52px;justify-content:flex-end;">
        <svg><!-- people/count glyph --></svg>
        {count}
      </div>
      <span class="pill pill-green">{State}</span>
      <!-- variants: .pill-amber, .pill-coral -->
    </li>
    <!-- more rows -->
  </ul>
</div>
```

---

## Breakdown chart (secondary panel)

`[category label] [value (sky)] [horizontal bar (sky fill)]`

```html
<div class="card">
  <div class="card-head">
    <span class="card-title">{Chart title}</span>
    <span style="font-size:11px;color:#94a3b8">{Period label}</span>
  </div>
  <div style="padding:16px 20px;display:flex;flex-direction:column;gap:14px;">
    <div>
      <div style="display:flex;justify-content:space-between;font-size:12px;margin-bottom:5px;">
        <span style="font-weight:600;color:#1e293b;">{Category}</span>
        <span style="font-weight:700;color:var(--sky);">{value}</span>
      </div>
      <div style="height:8px;background:#e2eaf0;border-radius:4px;overflow:hidden;">
        <div style="height:100%;border-radius:4px;background:var(--sky);width:{pct}%;transition:width .3s;"></div>
      </div>
    </div>
    <!-- more rows; width = value / max * 100 -->
  </div>
</div>
```

---

## Records table (dashboard footer or list screen)

```html
<div class="card">
  <div class="card-head">
    <span class="card-title">{Records title}</span>
    <button style="font-size:12px;font-weight:600;color:var(--sky);border:1px solid var(--sky);background:var(--surface);padding:6px 14px;border-radius:20px;cursor:pointer;font-family:inherit;">{Export}</button>
  </div>
  <div style="overflow-x:auto;">
    <table>
      <thead>
        <tr>
          <th>{Ref}</th>
          <th>{Contact / name}</th>
          <th>{Category}</th>
          <th>{Dates}</th>
          <th>{Qty}</th>
          <th>{Value}</th>
          <th>Status</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="ref">{REF-XXXXX}</span></td>
          <td>
            <div style="display:flex;align-items:center;gap:8px;">
              <!-- avatar circle: gradient sky→coral, initials, font-size:10px/700/white -->
              <div style="width:28px;height:28px;border-radius:50%;background:var(--sky);display:flex;align-items:center;justify-content:center;font-size:10px;font-weight:700;color:#fff;">{IN}</div>
              <span style="font-weight:600;">{Name}</span>
            </div>
          </td>
          <td>{category}</td>
          <td style="white-space:nowrap">{date range}</td>
          <td style="font-variant-numeric:tabular-nums">{qty}</td>
          <td style="font-weight:700;font-variant-numeric:tabular-nums">{$value}</td>
          <td><span class="pill pill-green">{State}</span></td>
        </tr>
        <!-- status variants: .pill-green .pill-amber .pill-coral -->
      </tbody>
    </table>
  </div>
  <!-- optional pager -->
  <div style="display:flex;align-items:center;justify-content:space-between;padding:12px 20px;border-top:1px solid var(--border);font-size:12px;color:#94a3b8;">
    <span>Showing {a}–{b} of {n}</span>
    <div style="display:flex;gap:4px;">
      <button style="width:30px;height:30px;border-radius:8px;border:1px solid var(--border);background:var(--surface);font-size:12px;cursor:pointer;">‹</button>
      <button style="width:30px;height:30px;border-radius:8px;border:1px solid var(--border);background:var(--sky);color:#fff;font-size:12px;cursor:pointer;">1</button>
      <button style="width:30px;height:30px;border-radius:8px;border:1px solid var(--border);background:var(--surface);font-size:12px;cursor:pointer;">2</button>
      <button style="width:30px;height:30px;border-radius:8px;border:1px solid var(--border);background:var(--surface);font-size:12px;cursor:pointer;">›</button>
    </div>
  </div>
</div>
```

### List toolbar (search + filter chips)

```html
<div style="display:flex;align-items:center;gap:12px;flex-wrap:wrap;background:var(--surface);border:1px solid var(--border);border-radius:12px;padding:14px 18px;">
  <div style="display:flex;align-items:center;gap:8px;background:#f8fafc;border:1px solid var(--border);border-radius:20px;padding:7px 14px;flex:1;max-width:340px;">
    <svg><!-- magnifier --></svg>
    <input type="text" placeholder="Filter by {fields}…" style="border:none;background:transparent;outline:none;font-size:13px;font-family:inherit;width:100%;">
  </div>
  <div style="display:flex;align-items:center;gap:8px;">
    <span style="font-size:11px;font-weight:600;color:#94a3b8;text-transform:uppercase;letter-spacing:.06em;">{Facet}</span>
    <!-- active chip -->
    <span style="display:inline-flex;align-items:center;gap:5px;padding:5px 12px;border-radius:20px;font-size:12px;font-weight:600;background:var(--sky-bg);border:1px solid var(--sky);color:var(--sky);cursor:pointer;">
      All <span style="background:var(--sky);color:#fff;font-size:10px;font-weight:700;padding:1px 5px;border-radius:8px;">{n}</span>
    </span>
    <!-- inactive chip -->
    <span style="display:inline-flex;align-items:center;gap:5px;padding:5px 12px;border-radius:20px;font-size:12px;font-weight:600;border:1px solid var(--border);color:#64748b;cursor:pointer;">
      {Value} <span style="background:#e2eaf0;color:#64748b;font-size:10px;font-weight:700;padding:1px 5px;border-radius:8px;">{n}</span>
    </span>
  </div>
</div>
```

---

## Donut side panel

```html
<div class="card">
  <div class="card-head">
    <span class="card-title">{Panel title}</span>
  </div>
  <div style="padding:20px;">
    <div style="display:flex;align-items:center;gap:20px;margin-bottom:20px;">
      <!-- Donut: r=38, circumference≈239. Adjust stroke-dasharray per segment pct×239 -->
      <svg width="110" height="110" viewBox="0 0 110 110">
        <!-- Background ring -->
        <circle cx="55" cy="55" r="38" fill="none" stroke="var(--border)" stroke-width="18"/>
        <!-- Primary segment (sky) -->
        <circle cx="55" cy="55" r="38" fill="none" stroke="var(--sky)" stroke-width="18"
          stroke-dasharray="{pct×239} 239" stroke-dashoffset="0"
          stroke-linecap="round" transform="rotate(-90 55 55)"/>
        <!-- Secondary segment (amber), offset = -primary length -->
        <circle cx="55" cy="55" r="38" fill="none" stroke="var(--amber)" stroke-width="18"
          stroke-dasharray="{pct2×239} 239" stroke-dashoffset="-{primary-len}"
          stroke-linecap="round" transform="rotate(-90 55 55)"/>
        <!-- Center text -->
        <text x="55" y="51" text-anchor="middle" font-size="18" font-weight="800" fill="#1e293b" font-family="Inter,system-ui,sans-serif">{pct}%</text>
        <text x="55" y="64" text-anchor="middle" font-size="9" fill="#94a3b8" font-family="Inter,system-ui,sans-serif" letter-spacing=".05em">{LABEL}</text>
      </svg>
      <!-- Legend -->
      <div style="display:flex;flex-direction:column;gap:8px;">
        <div style="display:flex;align-items:center;gap:8px;font-size:12px;">
          <div style="width:10px;height:10px;border-radius:50%;background:var(--sky);flex-shrink:0;"></div>
          <span style="color:#64748b;">{Label A}</span>
          <span style="font-weight:700;color:#1e293b;margin-left:auto;padding-left:12px;">{val}%</span>
        </div>
        <div style="display:flex;align-items:center;gap:8px;font-size:12px;">
          <div style="width:10px;height:10px;border-radius:50%;background:var(--amber);flex-shrink:0;"></div>
          <span style="color:#64748b;">{Label B}</span>
          <span style="font-weight:700;color:#1e293b;margin-left:auto;padding-left:12px;">{val}%</span>
        </div>
        <div style="display:flex;align-items:center;gap:8px;font-size:12px;">
          <div style="width:10px;height:10px;border-radius:50%;background:var(--border);flex-shrink:0;"></div>
          <span style="color:#64748b;">{Label C}</span>
          <span style="font-weight:700;color:#1e293b;margin-left:auto;padding-left:12px;">{val}%</span>
        </div>
      </div>
    </div>
    <!-- Sub-category rows -->
    <div style="display:flex;flex-direction:column;gap:12px;">
      <div>
        <div style="display:flex;justify-content:space-between;font-size:12px;margin-bottom:5px;">
          <span style="font-weight:600;color:#1e293b;">{Sub-category}</span>
          <span style="font-weight:700;color:var(--sky);">{pct}%</span>
        </div>
        <div style="height:6px;background:#e2eaf0;border-radius:3px;overflow:hidden;">
          <div style="height:100%;border-radius:3px;background:var(--sky);width:{pct}%;"></div>
        </div>
      </div>
      <!-- more rows -->
    </div>
  </div>
</div>
```

---

## Record form — fields with inline validation

Rules live ON the field: a required mark (`*`), helper text under the field, and
an inline error message on an invalid field. Submit stays `disabled` until valid.
Never add a separate rules/validation-status summary panel.

```html
<form novalidate style="display:flex;flex-direction:column;gap:16px;">
  <div class="card">
    <!-- Section header -->
    <div style="display:flex;align-items:center;gap:8px;padding:14px 20px;border-bottom:1px solid var(--border);font-size:13px;font-weight:700;color:#1e293b;">
      <svg style="color:var(--sky);"><!-- section glyph --></svg>
      {Section title}
    </div>
    <div style="padding:20px;">
      <!-- 2-col grid; .full spans both cols -->
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;">

        <!-- Valid field -->
        <div style="display:flex;flex-direction:column;gap:4px;">
          <label style="font-size:12px;font-weight:600;color:#1e293b;" for="f1">{Label} <span style="color:var(--coral);">*</span></label>
          <input id="f1" type="text" value="{value}" style="padding:9px 12px;border:1px solid var(--border);border-radius:8px;font-size:13px;color:#1e293b;background:var(--surface);font-family:inherit;outline:none;">
          <span style="font-size:11px;color:#94a3b8;">{helper text / format hint}</span>
        </div>

        <!-- Invalid field: border coral + error message -->
        <div style="display:flex;flex-direction:column;gap:4px;">
          <label style="font-size:12px;font-weight:600;color:#1e293b;" for="f2">{Label} <span style="color:var(--coral);">*</span></label>
          <input id="f2" type="number" value="0" aria-invalid="true" style="padding:9px 12px;border:1px solid var(--coral);border-radius:8px;font-size:13px;color:#1e293b;background:#fff8f8;font-family:inherit;outline:none;">
          <span style="display:flex;align-items:center;gap:5px;font-size:11px;font-weight:600;color:var(--coral);">
            <svg width="12" height="12" viewBox="0 0 12 12" fill="none"><circle cx="6" cy="6" r="5" stroke="currentColor" stroke-width="1.3"/><path d="M6 4v2.5" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"/><circle cx="6" cy="9" r=".6" fill="currentColor"/></svg>
            {Specific rule that failed}
          </span>
        </div>

        <!-- Required select -->
        <div style="display:flex;flex-direction:column;gap:4px;">
          <label style="font-size:12px;font-weight:600;color:#1e293b;" for="f3">{Label} <span style="color:var(--coral);">*</span></label>
          <select id="f3" style="padding:9px 12px;border:1px solid var(--border);border-radius:8px;font-size:13px;color:#1e293b;background:var(--surface);font-family:inherit;outline:none;">
            <option value="">Select…</option>
          </select>
          <span style="font-size:11px;color:#94a3b8;">{constraint on the options}</span>
        </div>

      </div>
    </div>
  </div>

  <!-- Form footer -->
  <div style="display:flex;align-items:center;justify-content:space-between;background:var(--surface);border:1px solid var(--border);border-radius:12px;padding:16px 20px;">
    <span style="font-size:12px;color:#94a3b8;">Fields marked <span style="color:var(--coral);">*</span> are required.</span>
    <div style="display:flex;gap:10px;">
      <button type="button" class="btn-ghost">Cancel</button>
      <button type="submit" class="btn-primary" disabled>{Submit}</button>
    </div>
  </div>
</form>
```

---

## Record detail — header + meta grid + related panels

```html
<div style="display:flex;flex-direction:column;gap:16px;">
  <div style="font-size:12px;color:#94a3b8;">
    <a href="#" style="color:var(--sky);text-decoration:none;">{Parent list}</a> › <span>{ID}</span>
  </div>

  <!-- Detail header -->
  <div style="display:flex;align-items:center;justify-content:space-between;">
    <div>
      <div style="display:flex;align-items:center;gap:10px;">
        <span style="font-family:'Courier New',monospace;font-size:13px;font-weight:700;color:#64748b;">{ID}</span>
        <span class="pill pill-green">{State}</span>
      </div>
      <div style="font-size:22px;font-weight:800;color:#1e293b;margin-top:4px;">{Entity name / title}</div>
      <div style="font-size:12px;color:#94a3b8;margin-top:4px;">{Created / managed by}</div>
    </div>
    <div style="display:flex;gap:8px;">
      <button class="btn-ghost">{Secondary action}</button>
      <button class="btn-primary">Edit</button>
    </div>
  </div>

  <!-- Meta grid (3-col) -->
  <div class="card">
    <div style="display:grid;grid-template-columns:repeat(3,1fr);">
      <div style="padding:16px 20px;border-right:1px solid var(--border);">
        <div style="font-size:10px;font-weight:700;letter-spacing:.06em;color:#94a3b8;text-transform:uppercase;margin-bottom:6px;">{FIELD}</div>
        <div style="font-size:14px;font-weight:600;color:#1e293b;">{value}</div>
        <div style="font-size:11px;color:#94a3b8;margin-top:3px;">{sub}</div>
      </div>
      <!-- repeat; 3rd cell: border-right:none; last row: border-bottom:none -->
    </div>
  </div>

  <!-- Two-col: entity sub-table + activity feed -->
  <div style="display:grid;grid-template-columns:7fr 5fr;gap:16px;">
    <div class="card">
      <!-- records sub-table using the same <table> shell above -->
    </div>
    <div class="card">
      <!-- Activity feed: list of items with a colored dot + text + timestamp -->
    </div>
  </div>
</div>
```
