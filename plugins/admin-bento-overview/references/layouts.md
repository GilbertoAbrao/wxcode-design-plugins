# Bento Overview — layout skeletons

Paste-ready, domain-neutral fragments for the light bento-grid admin skin. Each
skeleton is labelled by archetype slot, not by a domain noun. Copy the shell from
`assets/template.html` first (it carries the `:root` tokens + sticky header +
base `.tile` rules), then drop the region skeletons below into the appropriate
page area. Replace every `{placeholder}` with the real domain's equivalent.

Token recap (full block in `template.html`): canvas `#f6f7f9`, tile `#ffffff`,
border `#e8eaee`; text `#1e293b / #334155 / #64748b / #94a3b8`; accents
`--c-indigo / --c-teal / --c-amber / --c-rose` each with `-d` and `-lt` variants.
Use `font-variant-numeric: tabular-nums` on every numeric cell.

---

## Sticky header (every screen)

```html
<header class="header">
  <div class="header-brand">
    <svg width="30" height="30" viewBox="0 0 30 30" fill="none" aria-hidden="true">
      <rect width="30" height="30" rx="8" fill="var(--c-indigo)"/>
      <!-- domain monogram here -->
    </svg>
    {App Name}
  </div>
  <!-- period chips: show on dashboard; hide on list/form/detail -->
  <div class="header-period">
    <button class="period-chip">Today</button>
    <button class="period-chip active">7D</button>
    <button class="period-chip">30D</button>
    <button class="period-chip">Custom</button>
  </div>
  <div class="header-spacer"></div>
  <div class="header-sub">{context label or timestamp}</div>
  <div class="header-right">
    <div class="icon-btn" aria-label="Notifications">
      <!-- bell SVG -->
      <span class="notif-dot"></span>
    </div>
    <div class="avatar">{XX}</div>
  </div>
</header>
```

---

## Bento grid (dashboard screen)

```html
<main class="bento">
  <!-- Hero tile (col-span 5, row-span 2): dominant metric -->
  <article class="tile tile-hero" aria-label="{Primary metric}">
    <div class="hero-accent"></div>
    <div class="tile-inner" style="padding-left:26px">
      <p class="tile-label">{METRIC NAME}</p>
      <div class="hero-value">{figure}</div>
      <p class="hero-sub">{period / context}</p>
      <div><span class="delta-chip delta-up">↑ {delta}</span></div>
      <div class="hero-sparkline">
        <svg viewBox="0 0 220 48" width="100%" preserveAspectRatio="none" aria-hidden="true">
          <!-- sparkline polyline + area fill using var(--c-indigo) -->
        </svg>
      </div>
    </div>
  </article>

  <!-- Chart tile (col-span 7, row-span 3): area chart -->
  <article class="tile tile-chart" aria-label="{Chart title}">
    <div class="tile-inner">
      <div class="chart-header">
        <span class="chart-title">{Title}</span>
        <div class="chart-tabs">
          <span class="chart-tab">24H</span>
          <span class="chart-tab active">7D</span><!-- teal active -->
        </div>
      </div>
      <div class="chart-legend">
        <!-- legend-item × N with legend-dot colored via style="background:var(--c-*)" -->
      </div>
      <div class="chart-wrap">
        <!-- inline SVG area chart; teal series + amber dashed series -->
      </div>
    </div>
  </article>

  <!-- KPI tile (col-span 3, row-span 1): compact metric + delta + icon -->
  <article class="tile tile-kpi-a kpi-amber" aria-label="{KPI label}">
    <div class="tile-inner" style="justify-content:center">
      <div class="kpi-row">
        <div>
          <p class="tile-label">{LABEL}</p>
          <div class="kpi-value" style="color:var(--c-amber-d)">{value}</div>
          <span class="delta-chip delta-up" style="font-size:11px;padding:2px 7px;">↑ {delta}</span>
        </div>
        <div class="kpi-icon"><!-- SVG glyph --></div>
      </div>
    </div>
  </article>
  <!-- Repeat for rose-accented KPI: replace kpi-amber with kpi-rose, color with --c-rose-d -->

  <!-- Activity feed tile (col-span 5, row-span 3): timestamped events -->
  <article class="tile tile-activity tile-teal-border" aria-label="{Feed title}">
    <div class="tile-inner">
      <p class="feed-title">{Title}</p>
      <div class="feed-list">
        <!-- feed-item × 5-6: .feed-dot-success / warn / info / error + feed-text + feed-time -->
        <div class="feed-item">
          <span class="feed-dot feed-dot-{severity}"></span>
          <div>
            <span class="feed-text">{event description}</span>
            <time class="feed-time">{elapsed}</time>
          </div>
        </div>
      </div>
    </div>
  </article>

  <!-- Donut tile (col-span 4, row-span 3): distribution chart -->
  <article class="tile tile-donut" aria-label="{Donut title}">
    <div class="tile-inner">
      <p class="donut-title">{Title}</p>
      <div class="donut-wrap">
        <div class="donut-center">
          <!-- SVG donut: r=38, circ≈238.76; 3-4 strokes with stroke-dasharray offsets -->
          <!-- centre label: donut-center-val + donut-center-sub -->
        </div>
        <div class="donut-legend">
          <!-- 2-col grid of donut-legend-item: swatch + label + donut-legend-val -->
        </div>
      </div>
    </div>
  </article>

  <!-- Mini-table tile (col-span 8, row-span 3): top-N records -->
  <article class="tile tile-table" aria-label="{Table title}">
    <div class="tile-inner">
      <div class="table-header">
        <span class="table-title">{Title}</span>
        <a href="#" class="view-all">View all →</a>
      </div>
      <table class="mini-table">
        <thead><tr>
          <th>{Entity}</th><th>{Dimension}</th>
          <th>{Numeric}</th><th>{Rate}</th><th>Status</th>
        </tr></thead>
        <tbody>
          <tr>
            <td class="entity">{name}</td>
            <td>{dim}</td>
            <td style="font-variant-numeric:tabular-nums">{value}</td>
            <td style="font-variant-numeric:tabular-nums">{rate}</td>
            <td><span class="pill pill-ok">{state}</span></td>
          </tr>
          <!-- 4 more rows; pill variants: pill-ok / pill-blue / pill-warn / pill-error -->
        </tbody>
      </table>
    </div>
  </article>

  <!-- Status tile (col-span 4, row-span 2): service health -->
  <article class="tile tile-status tile-rose-border" aria-label="{Health title}">
    <div class="tile-inner">
      <p class="status-title">{Title}</p>
      <div class="status-list">
        <!-- status-item × 4: status-dot-ok / warn / error + status-name + status-uptime -->
        <div class="status-item">
          <span class="status-dot status-dot-{state}"></span>
          <span class="status-name">{Service}</span>
          <span class="status-uptime">{uptime %}</span>
        </div>
      </div>
    </div>
  </article>
</main>
```

---

## List screen (toolbar + table)

```html
<div class="page">
  <div class="page-header">
    <div>
      <div class="page-title">{Entities}</div>
      <div class="page-subtitle">{scope description}</div>
    </div>
    <div style="display:flex;gap:8px">
      <button class="btn-ghost">Export</button>
      <button class="btn-primary">+ New {Entity}</button>
    </div>
  </div>

  <div class="toolbar">
    <div class="toolbar-search">
      <!-- magnifier SVG -->
      <input type="text" placeholder="Search by {fields}…">
    </div>
    <div class="filter-group">
      <span class="filter-label">{Facet}</span>
      <span class="chip active">All <span class="chip-count">{n}</span></span>
      <span class="chip">{Value} <span class="chip-count">{n}</span></span>
      <!-- more filter chips -->
    </div>
  </div>

  <div class="card">
    <div class="rec-table-wrap">
      <table class="rec-table">
        <thead><tr>
          <th>{ID col}</th><th>{Primary}</th><th>{Dim 1}</th>
          <th>{Dim 2}</th><th>{Date}</th>
          <th style="text-align:right">{Numeric}</th><th>Status</th>
        </tr></thead>
        <tbody>
          <tr>
            <td><span class="rec-id">{ID}</span></td>
            <td>{primary value}</td>
            <td>{dim 1}</td><td>{dim 2}</td><td>{date}</td>
            <td class="num">{numeric}</td>
            <td><span class="pill pill-teal">{state}</span></td>
          </tr>
          <!-- 6-9 more rows -->
        </tbody>
      </table>
    </div>
    <div class="rec-footer">
      <span>Showing {a}–{b} of {n}</span>
      <div class="pagination">
        <button class="page-btn">‹</button>
        <button class="page-btn active">1</button>
        <button class="page-btn">2</button>
        <button class="page-btn">›</button>
      </div>
    </div>
  </div>
</div>
```

---

## Form screen — inline field validation

Rules live ON the field: required mark (`*`), helper text, inline error.
Submit stays `disabled` until valid. Never add a rules/validation-status panel.

```html
<div class="page" style="max-width:860px">
  <div class="breadcrumb"><a href="#">{Parent}</a> › New {Entity}</div>
  <div class="page-title">New {Entity}</div>

  <form novalidate>
    <div class="card">
      <div class="card-section-title">{Section}</div>
      <div class="card-body">
        <div class="field-grid"><!-- grid: 1fr 1fr; .field.full spans both -->

          <!-- Valid field -->
          <div class="field">
            <label class="field-label" for="f1">{Label} <span class="req">*</span></label>
            <select id="f1" class="control" required>
              <option value="">Select…</option>
            </select>
            <span class="helper">{constraint on the options}</span>
          </div>

          <!-- Invalid field: add .invalid on .field, show .error-msg -->
          <div class="field invalid">
            <label class="field-label" for="f2">{Label} <span class="req">*</span></label>
            <input id="f2" class="control" type="number" aria-invalid="true" required>
            <span class="error-msg"><!-- alert SVG --> {Specific rule that failed}</span>
          </div>

          <!-- Optional field -->
          <div class="field full">
            <label class="field-label" for="f3">{Label}</label>
            <textarea id="f3" class="control" rows="3" placeholder="…"></textarea>
          </div>

        </div>
      </div>
    </div>

    <div class="form-footer">
      <span class="form-hint">Fields marked <span class="req">*</span> are required.</span>
      <div class="footer-actions">
        <button type="button" class="btn-ghost">Cancel</button>
        <button type="submit" class="btn-primary" disabled>{Submit}</button>
      </div>
    </div>
  </form>
</div>
```

---

## Detail screen — header + meta grid + related panels

```html
<div class="page">
  <div class="breadcrumb"><a href="#">{Parent}</a> › <span>{ID}</span></div>

  <div class="detail-header">
    <div>
      <div class="detail-id-row">
        <span class="detail-id">{ID}</span>
        <span class="pill pill-teal">{State}</span>
      </div>
      <div class="detail-name">{primary label}</div>
    </div>
    <div class="detail-actions">
      <button class="btn-ghost">{Action}</button>
      <button class="btn-primary">Edit</button>
    </div>
  </div>

  <!-- Meta grid: 3-col label/value cells -->
  <div class="card">
    <div class="meta-grid"><!-- repeat(3,1fr); border-right/bottom on cells -->
      <div class="meta-cell">
        <div class="meta-label">{FIELD}</div>
        <div class="meta-value">{value}</div>
        <div class="meta-sub">{sub}</div>
      </div>
      <!-- 5 more cells -->
    </div>
  </div>

  <!-- Two-column: 7fr related table + 5fr activity feed -->
  <div class="two-col">
    <div class="card">
      <!-- events / operations table -->
    </div>
    <div class="card">
      <!-- activity feed: feed-list + feed-item rows -->
    </div>
  </div>
</div>
```
