# Dense Grid Admin — layout skeletons

Paste-ready, domain-neutral fragments for the Dense Grid dark/monospace skin.
Each skeleton is labelled by archetype slot, not by a domain noun. Copy the
shell from `assets/template.html` first (it carries the `:root` tokens + toolbar
+ main slot), then drop the region skeletons below into `.main-grid` or `.page`.
Replace every `{placeholder}` with the real domain's equivalent.

Token recap (full block in `template.html`):
- Page `#0c0f12`, panel `#12161b`, row-hover `#191e25`, border `#232a31`
- Text `#d7dde4 / #7b8694`
- `--up #22c55e` (positive/bid), `--dn #ef4444` (negative/ask),
  `--accent-blue #3b82f6` (actions, selected)
- All numeric figures: `font-family: var(--mono); font-variant-numeric: tabular-nums`

---

## Toolbar (36px)

```html
<header class="toolbar">
  <div class="brand">
    <div class="brand-mark">{XX}</div>
    <span class="brand-name">{Workspace}</span>
  </div>
  <div class="tb-sep"></div>
  <div class="filter-chips">
    <button class="chip active">{All}</button>
    <button class="chip">{State A}</button>
    <button class="chip">{State B}</button>
  </div>
  <div class="tb-search">
    <svg width="12" height="12" viewBox="0 0 12 12" fill="none" aria-hidden="true">
      <circle cx="5" cy="5" r="3.5" stroke="#7b8694" stroke-width="1.2"/>
      <line x1="8" y1="8" x2="11" y2="11" stroke="#7b8694" stroke-width="1.2" stroke-linecap="round"/>
    </svg>
    <input type="text" placeholder="Search…" aria-label="Search">
  </div>
  <div class="toolbar-right">
    <span class="live-clock mono">{HH:MM:SS}</span>
    <div class="conn-dot" title="Live"></div>
    <div class="avatar">{XX}</div>
  </div>
</header>
```

---

## Dashboard — 2-column main grid

```html
<div class="main-grid">
  <div class="col-left">
    <!-- Primary data table (below) -->
    <!-- Secondary mini-table (below) -->
  </div>
  <div class="col-right">
    <!-- Sparkline strip (below) -->
    <!-- Depth / book panel (below) -->
    <!-- Stats strip (below) -->
    <div style="flex:1;background:#0c0f12;"></div>
  </div>
</div>
```

---

## Primary data table

Dense 28px rows; first column bold; directional columns in `--up`/`--dn`.

```html
<div class="panel">
  <div class="panel-hdr">
    <span class="panel-title">{Primary entities}</span>
    <div style="display:flex;gap:8px;align-items:center;">
      <span style="font-size:11px;color:var(--text-muted);">{N items}</span>
      <button class="panel-action">{Action}</button>
    </div>
  </div>
  <table class="dt">
    <thead>
      <tr>
        <th>{Identifier}</th>
        <th class="mono">{Value}</th>
        <th class="mono">{Change}</th>
        <th class="mono">{Pct}</th>
        <th class="mono">{Vol / Count}</th>
        <th class="mono">{Ref A}</th>
        <th class="mono">{Ref B}</th>
        <th class="mono">{Ref C}</th>
      </tr>
    </thead>
    <tbody>
      <tr class="sel">
        <td style="font-weight:600;">{id-1}</td>
        <td class="mono">{val}</td>
        <td class="mono up">▲ {delta}</td>
        <td class="mono up">+{pct}%</td>
        <td class="mono muted">{count}</td>
        <td class="mono muted">{ref-a}</td>
        <td class="mono muted">{ref-b}</td>
        <td class="mono muted">{ref-c}</td>
      </tr>
      <!-- negative row: .dn on change/pct cells -->
      <tr>
        <td style="font-weight:600;">{id-2}</td>
        <td class="mono">{val}</td>
        <td class="mono dn">▼ {delta}</td>
        <td class="mono dn">-{pct}%</td>
        <td class="mono muted">{count}</td>
        <td class="mono muted">{ref-a}</td>
        <td class="mono muted">{ref-b}</td>
        <td class="mono muted">{ref-c}</td>
      </tr>
      <!-- 8–10 more rows -->
    </tbody>
  </table>
  <div class="wl-footer">
    <span>1–12 of {n}</span>
    <div style="display:flex;gap:4px;">
      <button class="pg-btn">‹ Prev</button>
      <button class="pg-btn">Next ›</button>
    </div>
  </div>
</div>
```

---

## Secondary mini-table

5–6 rows; two-value tag column (tag-a / tag-b); directional delta column.

```html
<div class="panel" style="flex:1;">
  <div class="panel-hdr">
    <span class="panel-title">{Secondary entities}</span>
    <div style="display:flex;gap:8px;align-items:center;">
      <span style="font-size:11px;color:var(--accent-blue);">{N open}</span>
      <button class="panel-action">{Close all}</button>
    </div>
  </div>
  <table class="dt">
    <thead>
      <tr>
        <th>{ID}</th>
        <th>{Type}</th>
        <th class="mono">{Qty}</th>
        <th class="mono">{Ref Price}</th>
        <th class="mono">{Mark}</th>
        <th class="mono">{Delta P&amp;L}</th>
        <th>{Status}</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="font-weight:600;">{id}</td>
        <td><span class="tag-a">{TYPE-A}</span></td>  <!-- or .tag-b -->
        <td class="mono">{qty}</td>
        <td class="mono">{ref}</td>
        <td class="mono">{mark}</td>
        <td class="mono up">+{delta}</td>
        <td><span style="color:var(--up);font-size:10px;">{OPEN}</span></td>
      </tr>
      <!-- more rows -->
    </tbody>
  </table>
</div>
```

---

## Sparkline strip (2×3 grid of mini-cards)

```html
<div class="panel" style="flex:0 0 auto;">
  <div style="height:26px;display:flex;align-items:center;justify-content:space-between;
              padding:0 10px;border-bottom:1px solid #232a31;background:#0c0f12;">
    <span style="font-size:11px;font-weight:600;color:var(--text-muted);
                 text-transform:uppercase;letter-spacing:.08em;">Sparklines</span>
    <span style="font-size:11px;color:var(--accent-blue);font-weight:600;">{subtitle}</span>
  </div>
  <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:4px;padding:8px;">
    <!-- Repeat for 6 entities -->
    <div style="background:#0c0f12;border:1px solid #232a31;border-radius:3px;padding:6px 8px 4px;display:flex;flex-direction:column;">
      <div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:4px;">
        <span style="font-size:10px;color:var(--text-muted);font-weight:600;text-transform:uppercase;letter-spacing:.06em;">{SYM}</span>
        <span style="font-family:var(--mono);font-size:11px;font-variant-numeric:tabular-nums;">{last}</span>
      </div>
      <svg width="100%" height="32" viewBox="0 0 100 32" preserveAspectRatio="none" aria-hidden="true">
        <defs>
          <linearGradient id="gN" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="#22c55e" stop-opacity=".25"/>   <!-- or #ef4444 for down -->
            <stop offset="100%" stop-color="#22c55e" stop-opacity="0"/>
          </linearGradient>
        </defs>
        <!-- polygon for area fill, polyline for stroke -->
        <polygon points="0,24 25,18 50,14 75,10 100,6 100,32 0,32" fill="url(#gN)"/>
        <polyline points="0,24 25,18 50,14 75,10 100,6" fill="none" stroke="#22c55e" stroke-width="1.2"/>
      </svg>
      <div style="display:flex;justify-content:flex-end;margin-top:3px;">
        <span style="font-family:var(--mono);font-size:10px;font-variant-numeric:tabular-nums;" class="up">+{pct}%</span>
      </div>
    </div>
    <!-- 5 more cards -->
  </div>
</div>
```

---

## Depth / book panel (two-column bid/ask)

```html
<div class="panel" style="flex:0 0 auto;">
  <div style="height:26px;display:flex;align-items:center;justify-content:space-between;
              padding:0 10px;border-bottom:1px solid #232a31;background:#0c0f12;">
    <span style="font-size:11px;font-weight:600;color:var(--text-muted);
                 text-transform:uppercase;letter-spacing:.08em;">{Depth title}</span>
    <span style="font-size:11px;color:var(--accent-blue);font-weight:600;">{entity}</span>
  </div>
  <div style="display:grid;grid-template-columns:1fr 1fr;">
    <!-- BID side -->
    <div style="border-right:1px solid #232a31;padding:4px 0;">
      <div style="display:grid;grid-template-columns:1fr 1fr;padding:2px 8px;
                  font-size:10px;font-weight:600;color:var(--up);letter-spacing:.08em;
                  text-transform:uppercase;border-bottom:1px solid #232a31;">
        <span>Bid</span><span style="text-align:right;">Size</span>
      </div>
      <!-- 8 rows: .ob-row .bid-row pattern (green, depth bar ::before) -->
    </div>
    <!-- ASK side -->
    <div style="padding:4px 0;">
      <div style="display:grid;grid-template-columns:1fr 1fr;padding:2px 8px;
                  font-size:10px;font-weight:600;color:var(--dn);letter-spacing:.08em;
                  text-transform:uppercase;border-bottom:1px solid #232a31;">
        <span>Ask</span><span style="text-align:right;">Size</span>
      </div>
      <!-- 8 rows: .ob-row .ask-row pattern (red, depth bar ::before) -->
    </div>
  </div>
  <div style="text-align:center;font-family:var(--mono);font-size:10px;color:var(--text-muted);
              padding:3px 0;border-top:1px solid #232a31;background:#0c0f12;">
    Spread: {spread} &nbsp;·&nbsp; Mid: {mid}
  </div>
</div>
```

---

## Stats strip (5 tiles)

```html
<div class="panel" style="flex:0 0 auto;">
  <div style="height:26px;display:flex;align-items:center;justify-content:space-between;
              padding:0 10px;border-bottom:1px solid #232a31;background:#0c0f12;">
    <span style="font-size:11px;font-weight:600;color:var(--text-muted);
                 text-transform:uppercase;letter-spacing:.08em;">{Stats title}</span>
    <span style="font-size:10px;color:var(--text-muted);">{context}</span>
  </div>
  <div style="display:grid;grid-template-columns:repeat(5,1fr);">
    <div class="stat-tile">
      <span class="stat-label">{METRIC}</span>
      <span class="stat-val mono">{val}</span>           <!-- add .up or .dn when directional -->
      <span class="stat-chip muted">{delta}</span>
    </div>
    <!-- 4 more tiles; last tile has no border-right -->
  </div>
</div>
```

---

## List screen (page layout)

```html
<main class="page">
  <!-- Page header -->
  <div style="display:flex;align-items:center;justify-content:space-between;">
    <div>
      <div style="font-size:14px;font-weight:700;">{Entities}</div>
      <div style="font-size:11px;color:var(--text-muted);">{N total · M active · updated HH:MM UTC}</div>
    </div>
    <div style="display:flex;gap:8px;">
      <button class="btn-ghost">Export CSV</button>
      <button class="btn-primary">+ Add {Entity}</button>
    </div>
  </div>

  <!-- List toolbar -->
  <div style="background:#12161b;border:1px solid #232a31;border-radius:4px;
              display:flex;align-items:center;padding:0 10px;gap:12px;height:36px;">
    <!-- search input (same as toolbar search) -->
    <!-- filter-sep + filter-group chips per facet -->
    <span style="margin-left:auto;font-size:11px;color:var(--text-muted);">{N} results</span>
  </div>

  <!-- Data table -->
  <div class="card">
    <table class="dt">
      <thead><tr><!-- columns --></tr></thead>
      <tbody><!-- rows --></tbody>
    </table>
    <!-- Table footer with pager -->
    <div style="display:flex;align-items:center;justify-content:space-between;
                padding:6px 10px;border-top:1px solid #232a31;background:#0c0f12;">
      <span style="font-size:10px;color:var(--text-muted);">Showing 1–{n} of {total}</span>
      <div style="display:flex;gap:3px;">
        <!-- .pg-btn pagination buttons; active = blue border -->
      </div>
    </div>
  </div>
</main>
```

---

## Form screen — fields with inline validation

Rules live ON the field: a required mark (`*`), helper text, and an inline error
on an invalid field. Submit stays `disabled` until the form is valid. Never add
a separate rules/validation-status summary panel.

```html
<main class="page">
  <div style="display:flex;align-items:center;justify-content:space-between;">
    <div>
      <div style="font-size:14px;font-weight:700;">Add {Entity}</div>
      <div style="font-size:11px;color:var(--text-muted);">Fields marked <span style="color:var(--dn);">*</span> are required</div>
    </div>
  </div>

  <form novalidate>
    <div class="card" style="margin-bottom:12px;">
      <div style="display:flex;align-items:center;gap:8px;padding:8px 14px;
                  border-bottom:1px solid #232a31;font-size:11px;font-weight:600;
                  color:var(--text-muted);text-transform:uppercase;letter-spacing:.08em;">
        {Section title}
      </div>
      <div style="padding:14px;">
        <div class="field-grid">

          <!-- Valid required field -->
          <div class="field">
            <label class="field-label" for="f1">{Label} <span class="req">*</span></label>
            <input id="f1" class="control" type="text" value="">
            <span class="helper">{what this drives / format hint}</span>
          </div>

          <!-- Invalid field -->
          <div class="field invalid">
            <label class="field-label" for="f2">{Label} <span class="req">*</span></label>
            <input id="f2" class="control" type="text" aria-invalid="true">
            <span class="error-msg">
              <svg width="10" height="10" viewBox="0 0 10 10" fill="none" aria-hidden="true">
                <circle cx="5" cy="5" r="4" stroke="currentColor" stroke-width="1.2"/>
                <line x1="5" y1="3" x2="5" y2="5.5" stroke="currentColor" stroke-width="1.2" stroke-linecap="round"/>
                <circle cx="5" cy="7" r=".5" fill="currentColor"/>
              </svg>
              {Specific rule that failed}
            </span>
          </div>

          <!-- Required select -->
          <div class="field">
            <label class="field-label" for="f3">{Label} <span class="req">*</span></label>
            <select id="f3" class="control"><option value="">Select…</option></select>
            <span class="helper">{constraint on the options}</span>
          </div>

        </div>

        <!-- Form footer: hint + cancel + submit -->
        <div style="display:flex;align-items:center;justify-content:space-between;
                    padding:12px 0 0;border-top:1px solid #232a31;margin-top:4px;">
          <span style="font-size:10px;color:var(--text-muted);">Fields marked <span style="color:var(--dn);">*</span> are required</span>
          <div style="display:flex;gap:8px;">
            <button type="button" class="btn-ghost">Cancel</button>
            <button type="submit" class="btn-primary" disabled>Add {Entity}</button>
          </div>
        </div>
      </div>
    </div>
  </form>
</main>
```

---

## Detail screen

```html
<main class="page">

  <!-- Header band -->
  <div style="background:#12161b;border:1px solid #232a31;border-radius:4px;
              padding:12px 16px;display:flex;align-items:center;justify-content:space-between;gap:16px;">
    <div>
      <div style="display:flex;align-items:center;gap:10px;margin-bottom:4px;">
        <span style="font-size:20px;font-weight:800;font-family:var(--mono);letter-spacing:-.5px;">{IDENTIFIER}</span>
        <span class="tag-a">{Active}</span>   <!-- or .tag-b / .tag-n -->
      </div>
      <div style="font-size:13px;color:var(--text-muted);">{name · category · sub}</div>
    </div>
    <div style="display:flex;gap:8px;">
      <button class="btn-ghost">{Secondary}</button>
      <button class="btn-primary">Edit</button>
    </div>
  </div>

  <!-- Meta grid (3 columns, label/value/sub per cell) -->
  <div class="card">
    <div style="display:grid;grid-template-columns:repeat(3,1fr);">
      <div style="padding:10px 14px;border-right:1px solid #232a31;">
        <div style="font-size:10px;color:var(--text-muted);text-transform:uppercase;letter-spacing:.08em;margin-bottom:3px;">{METRIC}</div>
        <div style="font-size:13px;font-weight:600;font-family:var(--mono);font-variant-numeric:tabular-nums;" class="up">{value}</div>
        <div style="font-size:10px;color:var(--text-muted);margin-top:2px;">{sub-line}</div>
      </div>
      <!-- repeat for 5 more cells; last column no border-right; last row no border-bottom -->
    </div>
  </div>

  <!-- Two-column: related sub-table + activity log -->
  <div style="display:grid;grid-template-columns:7fr 5fr;gap:12px;align-items:start;">
    <div class="card">
      <div class="card-hdr"><span class="card-title">{Related data title}</span></div>
      <table class="dt">
        <thead><tr><!-- columns --></tr></thead>
        <tbody><!-- rows --></tbody>
      </table>
    </div>
    <div class="card">
      <div class="card-hdr"><span class="card-title">Activity</span></div>
      <!-- activity rows: dot + desc + time -->
    </div>
  </div>

</main>
```
