# Azure Rail Admin — Paste-ready Layout Skeletons

Domain-neutral HTML fragments for each archetype region. Replace placeholder labels with the real domain's entities, metrics, and terminology.

---

## Sidebar — fixed dark rail (260 px)

```html
<aside class="sidebar">
  <!-- Logo zone (60 px) -->
  <div class="sidebar-logo">
    <svg width="28" height="28" viewBox="0 0 28 28" fill="none">
      <rect width="28" height="28" rx="6" fill="var(--accent)"/>
      <path d="M7 14h14M14 7v14" stroke="#fff" stroke-width="2.5" stroke-linecap="round"/>
    </svg>
    <div class="sidebar-logo-text">App Name</div>
  </div>

  <!-- Navigation list -->
  <nav class="nav">
    <div class="nav-label">Primary section</div>
    <a class="nav-item active" href="#">
      <!-- 16×16 SVG icon -->
      Nav item (active)
    </a>
    <a class="nav-item" href="#">
      <!-- 16×16 SVG icon -->
      Nav item
      <!-- Optional badge: <span class="nav-badge">3</span> -->
    </a>

    <div class="nav-label">Secondary section</div>
    <a class="nav-item" href="#"><!-- icon -->Nav item</a>
  </nav>

  <!-- User chip (pinned bottom) -->
  <div class="sidebar-footer">
    <div style="display:flex;align-items:center;gap:10px">
      <div style="width:34px;height:34px;border-radius:50%;background:var(--accent);
                  display:flex;align-items:center;justify-content:center;
                  color:#fff;font-size:13px;font-weight:700">AB</div>
      <div>
        <div style="font-size:13px;font-weight:600;color:#fff">Full Name</div>
        <div style="font-size:11px;color:var(--sidebar-text)">Role</div>
      </div>
    </div>
  </div>
</aside>
```

---

## Header bar — sticky top (60 px)

```html
<header class="header">
  <!-- Breadcrumb / page title -->
  <div style="font-size:15px;font-weight:600;color:var(--text-primary);flex:1">
    Page title
  </div>

  <!-- Search field -->
  <div class="header-search">
    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor"
         stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/>
    </svg>
    <input type="text" placeholder="Search…">
  </div>

  <!-- Icon actions -->
  <div style="display:flex;align-items:center;gap:6px">
    <button class="icon-btn"><!-- bell SVG --></button>
    <button class="icon-btn"><!-- grid SVG --></button>
    <!-- Avatar -->
    <button style="width:34px;height:34px;border-radius:50%;background:var(--accent);
                   color:#fff;font-size:13px;font-weight:700;border:none;cursor:pointer;
                   display:flex;align-items:center;justify-content:center">AB</button>
  </div>
</header>
```

---

## KPI tile — 4-up grid

```html
<!-- Wrap in: <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:20px;margin-bottom:24px"> -->
<div class="kpi-card">
  <div style="display:flex;align-items:flex-start;justify-content:space-between;margin-bottom:12px">
    <!-- Icon chip (color class: .blue | .green | .amber | .red) -->
    <div class="kpi-icon blue"><!-- 18×18 SVG icon --></div>
    <!-- Trend badge -->
    <span class="kpi-badge up">▲ 8.4%</span>
    <!-- or: <span class="kpi-badge down">▼ 3</span> -->
  </div>
  <div class="kpi-figure">1,284</div>
  <div class="kpi-label">Metric Label</div>
  <div class="kpi-sub">Supporting sub-line text</div>
</div>
```

---

## Status overview panel — labeled rows with progress bars

```html
<div class="card">
  <div class="card-header">
    <span class="card-title">Status Overview</span>
    <span class="card-count">1,284 total</span>
  </div>
  <div class="status-rows">
    <!-- Repeat per state -->
    <div class="status-row">
      <span class="status-dot blue"></span>  <!-- blue | green | amber | red | gray -->
      <span class="status-label">State label</span>
      <span class="status-count">412</span>
      <div class="status-bar-wrap">
        <div class="status-bar blue" style="width:82%"></div>
      </div>
      <span class="status-pct">82%</span>
    </div>
  </div>
</div>
```

---

## Inline SVG chart panel (line/area)

```html
<div class="card">
  <div class="card-header">
    <span class="card-title">Trend Chart</span>
    <button class="btn btn-ghost" style="padding:4px 10px;font-size:12px">Period</button>
  </div>
  <svg viewBox="0 0 320 140" width="100%" fill="none" xmlns="http://www.w3.org/2000/svg">
    <!-- Horizontal gridlines -->
    <line x1="0" y1="20"  x2="320" y2="20"  stroke="#ebecec" stroke-width="1"/>
    <line x1="0" y1="55"  x2="320" y2="55"  stroke="#ebecec" stroke-width="1"/>
    <line x1="0" y1="90"  x2="320" y2="90"  stroke="#ebecec" stroke-width="1"/>
    <line x1="0" y1="125" x2="320" y2="125" stroke="#ebecec" stroke-width="1"/>
    <!-- Area fill (primary) -->
    <path d="M24 90 L…fill-path… L288 125 L24 125 Z" fill="rgba(21,114,232,.10)"/>
    <!-- Line (primary) -->
    <polyline points="24,90 …data-points…" stroke="#1572e8" stroke-width="2.5"
              stroke-linejoin="round" stroke-linecap="round"/>
    <!-- X-axis labels -->
    <text x="20" y="138" font-size="9" fill="#9daec5">Mon</text>
    <!-- …repeat for each tick… -->
  </svg>
  <!-- Legend -->
  <div style="display:flex;gap:16px;margin-top:12px;flex-wrap:wrap">
    <div style="display:flex;align-items:center;gap:6px;font-size:12px;color:var(--text-muted)">
      <div style="width:16px;height:3px;border-radius:2px;background:#1572e8"></div>
      Series A
    </div>
  </div>
</div>
```

---

## Records table — full-width panel

```html
<div class="table-wrap">
  <!-- Table header -->
  <div class="table-header">
    <div>
      <span class="card-title">Records</span>
      <span class="card-count">124</span>
    </div>
    <div style="display:flex;align-items:center;gap:10px">
      <!-- optional filter input -->
      <button class="btn btn-primary">
        <svg …>…</svg> Add
      </button>
    </div>
  </div>

  <table>
    <thead>
      <tr>
        <th><input type="checkbox"></th>
        <th>ID</th>
        <th>Name</th>
        <th>Category</th>
        <th>Status</th>
        <th><!-- actions, no label --></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><input type="checkbox"></td>
        <td class="td-mono">#REC-0001</td>
        <td>
          <div style="font-weight:600;color:var(--text-primary)">Primary label</div>
          <div style="font-size:11px;color:var(--text-muted)">Sub-label</div>
        </td>
        <td>Category name</td>
        <td><span class="pill pill-info">Active</span></td>
        <td>
          <div style="display:flex;gap:6px">
            <button class="action-btn" title="View"><!-- eye SVG --></button>
            <button class="action-btn" title="Edit"><!-- pencil SVG --></button>
          </div>
        </td>
      </tr>
    </tbody>
  </table>

  <div class="table-footer">
    <span class="table-info">Showing 1–5 of 124 entries</span>
    <div class="pager">
      <button class="page-btn">‹</button>
      <button class="page-btn active">1</button>
      <button class="page-btn">2</button>
      <button class="page-btn">›</button>
    </div>
  </div>
</div>
```

---

## Form section — inline-validated fields

```html
<div class="card">
  <div class="card-title">Section heading</div>
  <div style="font-size:12px;color:var(--text-muted);margin-bottom:20px">Section description</div>

  <!-- Required field — valid state -->
  <div style="margin-bottom:16px">
    <label class="label">Field label <span style="color:var(--state-danger)">*</span></label>
    <input class="input valid" type="text" value="Valid input value">
    <div style="font-size:11px;color:var(--state-success);margin-top:4px">Looks good!</div>
  </div>

  <!-- Required field — error state -->
  <div style="margin-bottom:16px">
    <label class="label">Field label <span style="color:var(--state-danger)">*</span></label>
    <input class="input error" type="text" value="bad-value">
    <div style="font-size:11px;color:var(--state-danger);margin-top:4px;
                display:flex;align-items:center;gap:4px">
      <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor"
           stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <circle cx="12" cy="12" r="10"/>
        <line x1="12" y1="8" x2="12" y2="12"/>
        <line x1="12" y1="16" x2="12.01" y2="16"/>
      </svg>
      Inline validation message describing what went wrong.
    </div>
  </div>

  <!-- Optional field with helper text -->
  <div style="margin-bottom:16px">
    <label class="label">Optional field</label>
    <input class="input" type="text" placeholder="Placeholder text">
    <div class="helper">Helper text explaining format or constraints.</div>
  </div>

  <!-- Submit (disabled until required fields pass) -->
  <button class="btn btn-primary" disabled>Submit</button>
</div>
```

---

## Detail header band

```html
<!-- Record detail: header + status pill + actions -->
<div style="background:var(--card-bg);border-radius:var(--card-radius);
            box-shadow:var(--card-shadow);padding:20px;margin-bottom:20px">
  <div style="display:flex;align-items:center;gap:16px;flex-wrap:wrap">
    <div style="flex:1">
      <div style="font-size:11px;font-weight:700;text-transform:uppercase;
                  letter-spacing:.5px;color:var(--text-muted);margin-bottom:4px">
        #REC-0001
      </div>
      <div style="font-size:20px;font-weight:700;color:var(--text-primary)">Record title</div>
    </div>
    <span class="pill pill-info">Active</span>
    <button class="btn btn-ghost">Secondary action</button>
    <button class="btn btn-primary">Primary action</button>
  </div>
</div>

<!-- Meta grid below the header band -->
<div style="background:var(--card-bg);border-radius:var(--card-radius);
            box-shadow:var(--card-shadow);padding:20px;margin-bottom:20px">
  <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px">
    <!-- Repeat per meta field -->
    <div>
      <div style="font-size:11px;font-weight:700;text-transform:uppercase;
                  letter-spacing:.4px;color:var(--text-muted);margin-bottom:4px">Field label</div>
      <div style="font-size:14px;color:var(--text-primary);font-weight:500">Field value</div>
    </div>
  </div>
</div>
```

---

## Status pill reference

| Class | Use |
|-------|-----|
| `pill pill-success`   | completed, online, active, resolved, approved |
| `pill pill-warning`   | pending, degraded, in-review, expiring-soon   |
| `pill pill-danger`    | flagged, failed, error, critical, overdue     |
| `pill pill-info`      | active, in-progress, open, processing         |
| `pill pill-secondary` | archived, inactive, closed, draft             |

---

## CSS custom property reference

| Token | Value | Usage |
|-------|-------|-------|
| `--page-bg`            | `#f5f7fd` | Page/body background |
| `--sidebar-bg`         | `#1a2035` | Sidebar background |
| `--sidebar-text`       | `#a9b7d0` | Sidebar default text |
| `--sidebar-active-bg`  | `#1572e8` | Sidebar active item chip |
| `--card-bg`            | `#ffffff` | Card/panel background |
| `--accent`             | `#1572e8` | Primary blue accent |
| `--accent-light`       | `rgba(21,114,232,.12)` | Icon chips, badge tints |
| `--text-primary`       | `#444444` | Headings, strong labels |
| `--text-body`          | `#5a5a5a` | Body copy |
| `--text-muted`         | `#9daec5` | Labels, sub-lines, hints |
| `--border`             | `#ebecec` | Dividers, input borders |
| `--state-success`      | `#31ce36` | Success/complete state |
| `--state-warning`      | `#ffad46` | Warning/pending state |
| `--state-danger`       | `#f25961` | Error/critical state |
| `--state-info`         | `#48abf7` | Informational/active state |
| `--state-secondary`    | `#6c757d` | Neutral/archived state |
