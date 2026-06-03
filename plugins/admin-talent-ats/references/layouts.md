# Light Indigo Admin — layout skeletons

Paste-ready, domain-neutral fragments for the light indigo / pink accent skin.
Each skeleton is labeled by archetype slot, not by a domain noun. Copy the shell
from `assets/template.html` first (it carries the `:root` tokens + sidebar +
topbar + content slot), then drop the region skeletons below into `<div class="content">`.
Replace every placeholder with the real domain's equivalent.

Token recap (full block in `template.html`): canvas `#f8f8fc`, card/sidebar
`#ffffff`, border `#e8e8f2`; text ramp `#1e1b4b / #334155 / #475569 / #94a3b8`;
primary `var(--c-primary)` = `#4f46e5`; accent `var(--c-accent)` = `#ec4899`;
put `font-variant-numeric: tabular-nums` on every numeric cell.

---

## Page header (every screen)

```html
<div class="page-header">
  <h1>{Screen Title}</h1>
  <div class="date-chip">{Period label}</div>   <!-- optional -->
  <button class="btn btn-ghost btn-sm">{Secondary action}</button>
  <button class="btn btn-primary btn-sm">+ {Primary action}</button>
</div>
```

---

## KPI card (repeat ×4 in a `.kpi-row` grid)

```html
<div class="kpi-row">  <!-- grid-template-columns: repeat(4,1fr); gap:14px -->
  <div class="kpi">    <!-- background:#fff; border-radius:12px; padding:16px; box-shadow:0 1px 4px rgba(79,70,229,.04) -->
    <div class="kpi-top">
      <div>
        <div class="kpi-label">{UPPERCASE METRIC NAME}</div>
        <div class="kpi-value">{figure}</div>   <!-- font-variant-numeric:tabular-nums -->
      </div>
      <div class="kpi-icon" style="background:var(--c-primary-bg)"><!-- inline SVG, stroke=var(--c-primary) --></div>
    </div>
    <!-- inline sparkline SVG (polyline + area-fill gradient) -->
    <svg width="100%" height="28" viewBox="0 0 120 28" preserveAspectRatio="none">
      <defs><linearGradient id="gN" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%" stop-color="var(--c-primary)" stop-opacity=".18"/>
        <stop offset="100%" stop-color="var(--c-primary)" stop-opacity="0"/>
      </linearGradient></defs>
      <path d="{M…polyline}" fill="none" stroke="var(--c-primary)" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
      <path d="{M…area close}" fill="url(#gN)"/>
    </svg>
    <div class="kpi-bottom">
      <span class="delta-up">▲ {delta}</span>   <!-- .delta-up / .delta-dn -->
      <span class="kpi-sub" style="font-size:11px;color:var(--c-muted)">{context line}</span>
    </div>
  </div>
  <!-- 3 more cards; swap icon color + gradient stop to violet / accent / success as needed -->
</div>
```

---

## Stage board (kanban columns)

```html
<div class="stage-board">  <!-- grid-template-columns: repeat(4,1fr); gap:12px -->
  <div class="stage-col">  <!-- background:#f4f4fa; border:1px solid var(--c-border); border-radius:12px; padding:12px -->
    <div class="col-hd">
      <div class="stage-dot" style="background:{stage-color}"></div>
      <div class="col-stage">{Stage Name}</div>
      <div class="col-count">{count}</div>
    </div>
    <!-- entity mini-card (repeat 3-4) -->
    <div class="entity-card {s0|s1|s2|s3}">  <!-- left-bar set via .s0–.s3 -->
      <div class="ec-top">
        <div class="ec-av" style="background:{color}">{Initials}</div>
        <div>
          <div class="ec-name">{Entity name}</div>
          <div class="ec-role">{Type / sub-label}</div>
        </div>
      </div>
      <div class="ec-meta">
        <span class="tag {tag-a|tag-b|tag-c|tag-d}">{Source label}</span>
        <span class="ec-days">{elapsed}</span>
      </div>
    </div>
  </div>
  <!-- repeat for each stage; left-bar colors: s0=#94a3b8, s1=violet, s2=accent/pink, s3=success -->
</div>
```

---

## Conversion funnel (inline SVG, lower-left panel)

```html
<div class="card" style="padding:18px">
  <div class="section-title">{Funnel Title}</div>
  <svg viewBox="0 0 520 200" height="200" style="width:100%">
    <defs>
      <linearGradient id="fg" x1="0" y1="0" x2="1" y2="0">
        <stop offset="0%" stop-color="#4f46e5"/>
        <stop offset="100%" stop-color="#ec4899"/>
      </linearGradient>
    </defs>
    <!-- Each stage: label @ x=0, bar from x=90, count after bar, % at end -->
    <!-- Bar width = (stage_count / max_count) * 340; minimum visible width = 15 -->
    <text x="0"  y="22" font-size="11" fill="#475569" font-family="Inter,system-ui,sans-serif">{Stage 1}</text>
    <rect x="90" y="8"   width="{w1}" height="20" rx="4" fill="url(#fg)" opacity=".9"/>
    <text x="{90+w1+6}" y="22" font-size="11" fill="#475569" font-family="Inter,system-ui,sans-serif">{count1}</text>
    <text x="{90+w1+50}" y="22" font-size="11" fill="#94a3b8" font-family="Inter,system-ui,sans-serif">100%</text>
    <!-- Repeat pattern at y += 40 for each subsequent stage -->
    <!-- Reduce opacity by ~0.05 per stage; reduce bar width proportionally -->
  </svg>
</div>
```

---

## Upcoming-items side panel (lower-right)

```html
<div class="card" style="padding:16px">
  <div class="section-title">{Panel Title}</div>
  <div class="iv-group">
    <div class="iv-date">{Date group label}</div>
    <div class="iv-item">
      <div class="iv-time">{HH:MM}</div>
      <div class="iv-body">
        <div class="iv-name">{Entity name}</div>
        <div class="iv-role">{Sub-label · Participant}</div>
        <div class="iv-meta">
          <span class="badge-mode {bm-video|bm-onsite|bm-phone}">{Format}</span>
        </div>
      </div>
    </div>
    <!-- more items -->
  </div>
  <!-- more date groups -->
</div>
```

---

## Records table (dashboard footer or list screen)

```html
<div class="table-card">
  <div class="table-hd">
    <h2>{Records Title}</h2>
    <a href="#" style="font-size:12px;color:var(--c-primary)">View all</a>
    <button class="btn btn-ghost btn-sm">{Export}</button>
    <button class="btn btn-primary btn-sm" style="margin-left:4px">+ {Add}</button>
  </div>
  <table class="tbl">
    <thead>
      <tr>
        <th>{Entity}</th>
        <th>{Type}</th>
        <th>Stage</th>
        <th>Source</th>
        <th>Rating</th>
        <th>Actions</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>
          <div class="cand-cell">
            <div class="cc-av" style="background:{color}">{Initials}</div>
            <div><div class="cc-name">{Name}</div><div class="cc-email">{sub-label}</div></div>
          </div>
        </td>
        <td>{type}</td>
        <td><span class="stage-pill pill-{s0|s1|s2|s3}">{Stage}</span></td>
        <td><span class="tag {tag-a|b|c|d}">{Source}</span></td>
        <td><span class="stars">★★★★<span class="empty">★</span></span></td>
        <td>
          <div class="tbl-actions">
            <button class="act-btn">View</button>
            <button class="act-btn">{action}</button>
          </div>
        </td>
      </tr>
    </tbody>
  </table>
  <div class="tbl-footer">
    <span>Showing {a}–{b} of {n}</span>
    <button class="pg-btn">‹</button>
    <button class="pg-btn active">1</button>
    <button class="pg-btn">2</button>
    <button class="pg-btn">›</button>
  </div>
</div>
```

### List toolbar (search + filter chips)

```html
<div class="toolbar">
  <div class="tb-search">
    <svg><!-- magnifier --></svg>
    <input type="text" placeholder="Filter {entities}…">
  </div>
  <div class="filter-group">
    <span class="filter-label">{Facet}</span>
    <span class="chip active">All <span class="chip-count">{n}</span></span>
    <span class="chip">{Value} <span class="chip-count">{n}</span></span>
  </div>
</div>
```

---

## Record form — fields with inline validation

Rules live ON the field: required mark (`*`), helper text, inline error on invalid
field. Submit stays `disabled` until the form is valid. Never add a separate
rules/validation-status panel.

```html
<form class="form-wrap" novalidate>
  <div class="card">
    <div class="card-section-title"><!-- icon + {Section name} --></div>
    <div class="card-body">
      <div class="field-grid">  <!-- grid-template-columns:1fr 1fr; gap:16px; .field.full spans both -->

        <!-- Valid field -->
        <div class="field">
          <label class="field-label" for="f1">{Label} <span class="req">*</span></label>
          <input id="f1" class="control" type="text" value="{value}">
          <span class="helper">{format hint / constraint}</span>
        </div>

        <!-- Invalid field: add .invalid; render .error-msg -->
        <div class="field invalid">
          <label class="field-label" for="f2">{Label} <span class="req">*</span></label>
          <input id="f2" class="control" type="text" aria-invalid="true">
          <span class="error-msg"><svg><!-- alert icon --></svg>{Specific rule that failed}</span>
        </div>

        <!-- Select with required -->
        <div class="field">
          <label class="field-label" for="f3">{Label} <span class="req">*</span></label>
          <select id="f3" class="control"><option value="">Select…</option></select>
          <span class="helper">{constraint on options}</span>
        </div>

      </div>
    </div>
  </div>

  <div class="form-footer">
    <span class="form-hint">Fields marked <span class="req">*</span> are required.</span>
    <div class="footer-actions">
      <button type="button" class="btn btn-ghost">Cancel</button>
      <button type="submit" class="btn btn-primary" disabled>{Submit}</button>
    </div>
  </div>
</form>
```

---

## Record detail — header band + meta grid + related panels

```html
<div class="breadcrumb">
  <a href="#">{Parent list}</a><span>›</span>{Entity name or ID}
</div>

<div class="detail-header">
  <div class="dh-avatar" style="background:{color}">{Initials}</div>
  <div class="dh-info">
    <div class="dh-name">{Primary name}</div>
    <div class="dh-role">{Sub-label / role}</div>
    <div class="dh-meta">
      <span class="stage-pill pill-{s0|s1|s2|s3}">{Stage}</span>
      <span class="tag {tag-a|b|c|d}">{Tag}</span>
      <span style="font-size:11.5px;color:var(--c-muted)">{date / applied}</span>
    </div>
  </div>
  <div class="dh-actions">
    <button class="btn btn-ghost btn-sm">{Action}</button>
    <button class="btn btn-primary btn-sm">Edit</button>
  </div>
</div>

<!-- Meta grid: 3-col label/value cells -->
<div class="card">
  <div class="card-hd"><!-- icon + title --></div>
  <div class="meta-grid">  <!-- grid-template-columns:repeat(3,1fr) -->
    <div class="meta-cell">
      <div class="meta-label">{FIELD}</div>
      <div class="meta-value">{value}</div>
      <div class="meta-sub">{sub}</div>    <!-- optional -->
    </div>
    <!-- more cells -->
  </div>
</div>

<!-- Two-col related panels (7fr 5fr) -->
<div class="two-col">
  <div class="panel">
    <div class="panel-hd"><!-- icon + {Panel title} --></div>
    <!-- stage-history progress rows or mini-table -->
  </div>
  <div class="panel">
    <div class="panel-hd"><!-- icon + Activity --></div>
    <!-- activity feed: act-item rows (avatar dot + text + timestamp) -->
  </div>
</div>
```
