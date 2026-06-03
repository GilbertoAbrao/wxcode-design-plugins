# Neobrutalist Admin — layout skeletons

Paste-ready, domain-neutral fragments for the neo-brutalist skin. Each skeleton
is labelled by archetype slot, not by a domain noun. Copy the shell from
`assets/template.html` first (it carries the `:root` tokens + sidebar + topbar
+ main slot), then drop the region skeletons below into `<main class="content">`.
Replace every placeholder label with the real domain's equivalent.

Token recap (full block in `template.html`): canvas `#ffffff`, cream surface
`#FFF5E6`, coral accent `#F5A86E`, lime accent `#8FD14F`, lavender `#B8A4FF`,
yellow `#FDE74C`, cyan `#90E0EF`, ink `#000000`. ALL borders `2–3px solid #000`,
ALL panel/tile shadows `4px 4px 0 #000`, `border-radius: 0` everywhere.
Monospace type on all figures, labels, nav items, buttons, IDs, codes, and times.

---

## Stat tiles (4-up grid — dashboard)

```html
<div class="stat-row">
  <!-- tile 1: coral top accent -->
  <div class="stat-tile">
    <div class="stat-label">{METRIC LABEL}</div>
    <div class="stat-value">{figure}</div>
    <div class="stat-delta up">
      <svg width="10" height="10" viewBox="0 0 10 10" fill="none"><polyline points="1,8 5,2 9,8" stroke="#2a7a00" stroke-width="1.5" stroke-linejoin="miter"/></svg>
      {delta text}
    </div>
  </div>
  <!-- tile 2: lime top accent -->
  <!-- tile 3: lavender top accent -->
  <!-- tile 4: yellow top accent -->
  <!-- Use .stat-delta.down { color:#c00; } + down-arrow SVG for negative deltas -->
</div>
```

CSS: `.stat-tile:nth-child(1){border-top:6px solid var(--coral)}` and so on per
token order: coral → lime → lav → yell.

---

## Panel (black-header card — wraps table, feed, or form section)

```html
<div class="panel">
  <div class="panel-header">
    <span class="panel-title">{PANEL TITLE}</span>
    <span class="panel-meta">{count or context}</span>
  </div>
  <!-- content: table / activity-feed / form fields -->
</div>
```

CSS rule: `.panel { border: 3px solid var(--ink); box-shadow: 4px 4px 0 var(--ink); }`.

---

## 2-column content grid (dashboard)

```html
<div class="main-grid">  <!-- grid-template-columns: 1fr 340px; gap: 16px; align-items: start -->
  <!-- LEFT: records table panel (below) -->
  <div>
    <div class="section-label">{SECTION LABEL}</div>
    <!-- panel + rec-table -->
  </div>
  <!-- RIGHT: activity feed panel (below) -->
  <div>
    <div class="section-label">{SECTION LABEL}</div>
    <!-- panel + activity-feed -->
  </div>
</div>
```

---

## Records table

```html
<div class="panel">
  <div class="panel-header">
    <span class="panel-title">{RECORDS TITLE}</span>
    <span class="panel-meta">{n} of {total} shown</span>
  </div>
  <table class="rec-table">
    <thead>
      <tr>
        <th>{Column 1}</th>
        <th>{Column 2}</th>
        <th>{Column 3}</th>
        <th>Status</th>
        <th>{Date / Metric}</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>{value}</td>
        <td>{value}</td>
        <td>{value}</td>
        <td><span class="status-pill pill-lime">Active</span></td>
        <td>{date}</td>
      </tr>
      <!-- status-pill variants: .pill-lime .pill-coral .pill-yell .pill-lav .pill-grey -->
      <!-- overdue date: add class="due-overdue" on the <td> + append "!" -->
    </tbody>
  </table>
</div>
```

---

## List toolbar (search slab + filter chips)

```html
<div class="toolbar">
  <div class="tool-search">
    <svg width="14" height="14" viewBox="0 0 14 14" fill="none"><circle cx="5.5" cy="5.5" r="4" stroke="#000" stroke-width="1.5"/><line x1="9" y1="9" x2="13" y2="13" stroke="#000" stroke-width="1.5" stroke-linecap="square"/></svg>
    <input type="text" placeholder="Filter by {fields}…">
  </div>
  <div class="filter-group">
    <span class="filter-label">{Facet}</span>
    <span class="chip active">All <span class="chip-count">{n}</span></span>
    <span class="chip">{Value} <span class="chip-count">{n}</span></span>
  </div>
</div>
```

CSS: `.chip { border: 2px solid var(--ink); border-radius: 0; font-family: var(--font-mono); }`
Active chip: `.chip.active { background: var(--lime); box-shadow: 2px 2px 0 var(--ink); }`.

---

## Pager footer (list screen)

```html
<div class="panel-footer">
  <span class="result-count">Showing {a}–{b} of {n}</span>
  <div class="pager">
    <button class="page-btn">‹</button>
    <button class="page-btn active">1</button>
    <button class="page-btn">2</button>
    <button class="page-btn">›</button>
  </div>
</div>
```

CSS: `.page-btn { border: 2px solid var(--ink); border-radius: 0; font-family: var(--font-mono); }`
Active: `.page-btn.active { background: var(--lime); box-shadow: 2px 2px 0 var(--ink); }`.

---

## Activity feed (dashboard right panel)

```html
<div class="activity-feed">
  <div class="activity-card">
    <div class="activity-top">
      <div class="activity-icon c1"><!-- inline SVG glyph, stroke #000 --></div>
      <div class="activity-body">
        <div class="activity-event">{one-line event}</div>
        <div class="activity-sub">{actor · context}</div>
      </div>
      <div class="activity-time">{timestamp}</div>
    </div>
  </div>
  <!-- more cards; rotate .c1–.c5 for icon fill: lime/coral/yell/lav/cyan -->
</div>
```

---

## Record form — fields with inline validation

Rules live ON the field: a required mark (`*`), helper text, and an inline error
on invalid input. Submit stays `disabled` until the form is valid. Never add a
separate rules/validation-status summary panel.

```html
<form novalidate>
  <div class="form-card">
    <div class="form-card-header">
      <div class="form-section-title">{SECTION}</div>
    </div>
    <div class="form-card-body">
      <div class="field-grid">  <!-- 1fr 1fr; .field.full spans both -->

        <!-- valid required field -->
        <div class="field">
          <label class="field-label" for="f1">{Label} <span class="req">*</span></label>
          <input id="f1" class="control" type="text" value="">
          <span class="helper">{format / constraint hint}</span>
        </div>

        <!-- invalid field: add .invalid on .field, render .error-msg -->
        <div class="field invalid">
          <label class="field-label" for="f2">{Label} <span class="req">*</span></label>
          <input id="f2" class="control" type="text" aria-invalid="true">
          <span class="error-msg">
            <svg width="10" height="10" viewBox="0 0 10 10" fill="none"><circle cx="5" cy="5" r="4.5" stroke="#c00" stroke-width="1"/><line x1="5" y1="2.5" x2="5" y2="5.5" stroke="#c00" stroke-width="1.5" stroke-linecap="square"/><circle cx="5" cy="7.5" r="0.75" fill="#c00"/></svg>
            {Specific rule that failed.}
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

  <div class="form-footer">
    <span class="form-hint">Fields marked <span class="req">*</span> are required.</span>
    <div class="footer-actions">
      <button type="button" class="btn-cancel">Cancel</button>
      <button type="submit" class="btn-submit" disabled>{Submit}</button>
    </div>
  </div>
</form>
```

---

## Record detail — header + meta grid + related panels

```html
<div class="breadcrumb"><a href="#">{Parent}</a> › <span>{ID or Name}</span></div>

<div class="detail-header">
  <div class="detail-title-block">
    <div class="detail-id-row">
      <span class="detail-id">{RECORD-ID}</span>
      <span class="status-pill pill-lime">{State}</span>  <!-- pill variant to match state -->
    </div>
    <div class="detail-name">{Record Title}</div>
    <div class="detail-sub">{key context line}</div>
  </div>
  <div class="detail-actions">
    <button class="btn-ghost">{Secondary action}</button>
    <button class="btn-primary">Edit</button>
  </div>
</div>

<!-- Meta grid: 3-column label/value -->
<div class="meta-panel">
  <div class="meta-panel-header"><span class="meta-panel-title">{SECTION TITLE}</span></div>
  <div class="meta-grid">  <!-- repeat(3,1fr) -->
    <div class="meta-cell">
      <div class="meta-label">{FIELD}</div>
      <div class="meta-value">{value}</div>
      <div class="meta-sub">{sub-label}</div>
    </div>
    <!-- repeat for each field; skip meta-sub when unused -->
  </div>
</div>

<!-- Related data: two-column 1fr + 340px -->
<div class="two-col">
  <div class="panel"><!-- mini-table of related records --></div>
  <div class="panel"><!-- activity feed (use activity-feed skeleton above) --></div>
</div>
```

Button styles:
```
.btn-ghost   { background:var(--paper); border:2px solid var(--ink); box-shadow:none; }
.btn-primary { background:var(--lime);  border:2px solid var(--ink); box-shadow:4px 4px 0 var(--ink); }
```
Both: `font-family:var(--font-mono); font-size:12px; font-weight:700; text-transform:uppercase; border-radius:0;`.
