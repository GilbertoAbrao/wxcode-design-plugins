# Admin Console — Paste-Ready Layout Skeletons

Domain-neutral HTML fragments for each archetype region. Copy, fill in domain
content, discard prose. No checklist panels, no build notes.

---

## 1. App Shell (sidebar + topbar + content)

```html
<body>
  <!-- Sidebar -->
  <nav class="sidebar">
    <div class="sidebar-logo">
      <svg class="logo-icon" …/> <!-- brand icon -->
      <span class="logo-name">Brand</span>
    </div>
    <div class="sidebar-section">
      <div class="sidebar-label">Group Label</div>
      <a class="nav-item active" href="#">
        <svg …/> <!-- icon -->
        <span class="nav-label">Item</span>
        <!-- optional: <span class="badge">3</span> -->
      </a>
    </div>
    <div class="sidebar-spacer"></div>
    <div class="sidebar-bottom">
      <a class="nav-item" href="#"><svg…/>Settings</a>
    </div>
  </nav>

  <!-- Main -->
  <div class="main">
    <header class="topbar">
      <button class="hamburger"><!-- hamburger svg --></button>
      <div class="search-wrap">
        <svg class="search-icon" …/>
        <input type="text" placeholder="Search…">
      </div>
      <div class="topbar-spacer"></div>
      <div class="topbar-actions">
        <button class="icon-btn"><svg…/><span class="notif-dot"></span></button>
        <div class="avatar-chip">
          <div class="avatar-circle">AB</div>
          <div class="avatar-info">
            <span class="avatar-name">User Name</span>
            <span class="avatar-role">Role</span>
          </div>
        </div>
      </div>
    </header>
    <main class="content">
      <!-- page body here -->
    </main>
  </div>
</body>
```

---

## 2. Page Header Row

```html
<div class="page-header">
  <div>
    <div class="page-title">Page Title</div>
    <div class="page-sub">Subtitle or breadcrumb</div>
  </div>
  <div style="display:flex;gap:8px">
    <button class="btn btn-ghost">Secondary Action</button>
    <button class="btn btn-primary">+ Primary Action</button>
  </div>
</div>
```

---

## 3. KPI Tile Row (4 tiles)

```html
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:12px">
  <!-- Tile -->
  <div class="kpi-tile">
    <div class="kpi-top">
      <div class="kpi-icon">
        <svg …/> <!-- 20×20 icon -->
      </div>
      <span class="kpi-delta delta-up">▲ 12%</span>
      <!-- or delta-down / delta-warn -->
    </div>
    <div class="kpi-figure">4,218</div>
    <div class="kpi-label">Metric Label</div>
    <div class="kpi-sub">Sub-line · context</div>
  </div>
  <!-- repeat × 4 -->
</div>
```

Accent overrides for danger tile:
```html
<div class="kpi-icon" style="background:var(--s-danger-d);color:var(--s-danger)">
```

---

## 4. Status Board Row (inside a `.panel`)

```html
<div class="panel">
  <div class="panel-head">
    <div>
      <div class="panel-title">Board Title</div>
      <div class="panel-sub">N entities</div>
    </div>
    <button class="btn btn-ghost" style="padding:5px 10px;font-size:12px">View all</button>
  </div>

  <!-- row pattern: repeat for each entity -->
  <div class="status-row"
       style="display:grid;grid-template-columns:1fr 90px 1fr 60px;align-items:center;gap:8px;padding:10px 18px;border-bottom:1px solid var(--divider);transition:background .12s">
    <!-- Col 1: label + sub -->
    <div>
      <div style="font-size:13px;font-weight:600;color:var(--text-1)">Entity Name</div>
      <div style="font-size:11px;color:var(--text-3)">Sub-label · context</div>
    </div>
    <!-- Col 2: state pill -->
    <div><span class="pill pill-success">● Active</span></div>
    <!-- or pill-warn / pill-danger / pill-neutral -->

    <!-- Col 3: metric + progress bar -->
    <div style="display:flex;flex-direction:column;gap:3px">
      <div style="font-size:12px;color:var(--text-2);font-variant-numeric:tabular-nums">
        840 / 1,000 units
      </div>
      <div style="height:3px;background:var(--active-bg)">
        <div style="height:3px;background:var(--accent);width:84%"></div>
        <!-- swap fill color: var(--s-warn) / var(--s-danger) -->
      </div>
    </div>

    <!-- Col 4: count -->
    <div style="font-size:12px;color:var(--text-3);text-align:right;font-variant-numeric:tabular-nums">
      12 inst
    </div>
  </div>
  <!-- end row -->
</div>
```

---

## 5. Alerts / Side Panel Row

```html
<div class="panel">
  <div class="panel-head">
    <div class="panel-title">Alerts · Active</div>
  </div>

  <!-- alert row — repeat -->
  <div style="display:flex;align-items:flex-start;gap:10px;padding:10px 18px;border-bottom:1px solid var(--divider)">
    <!-- severity dot -->
    <div style="width:8px;height:8px;border-radius:50%;background:var(--s-danger);flex-shrink:0;margin-top:4px"></div>
    <!-- or var(--s-warn) / var(--s-info) -->

    <div style="flex:1">
      <span style="font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.4px;color:var(--accent);background:var(--accent-dim);padding:1px 6px;margin-right:6px">TAG</span>
      <div style="font-size:13px;color:var(--text-1);margin-top:2px">Alert description text</div>
      <div style="font-size:11px;color:var(--text-3);margin-top:1px">15 min ago · context</div>
    </div>
  </div>
  <!-- end alert row -->

  <div style="padding:12px 18px;border-top:1px solid var(--border)">
    <button class="btn btn-ghost" style="width:100%;justify-content:center">
      Acknowledge All
    </button>
  </div>
</div>
```

---

## 6. Full-Width Records Table

```html
<div class="panel">
  <div class="panel-head">
    <div>
      <div class="panel-title">Records Title</div>
      <div class="panel-sub">Showing N of M</div>
    </div>
    <div style="display:flex;gap:8px">
      <button class="btn btn-ghost" style="padding:5px 10px;font-size:12px">Filter</button>
      <button class="btn btn-primary" style="padding:5px 10px;font-size:12px">+ New</button>
    </div>
  </div>

  <div style="overflow-x:auto">
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Primary Field</th>
          <th>Secondary Field</th>
          <th class="right">Numeric</th>
          <th>Status</th>
          <th>Timestamp</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td class="id-cell">REC-001</td>
          <td class="primary">Name / Title</td>
          <td>Value</td>
          <td class="right">1,234</td>
          <td><span class="pill pill-success">Active</span></td>
          <td>just now</td>
        </tr>
        <!-- repeat rows -->
      </tbody>
    </table>
  </div>

  <div style="display:flex;align-items:center;justify-content:space-between;padding:10px 18px;border-top:1px solid var(--border)">
    <span style="font-size:12px;color:var(--text-3)">M total records</span>
    <div style="display:flex;gap:4px">
      <button class="pager-btn">‹ Prev</button>
      <button class="pager-btn active">1</button>
      <button class="pager-btn">2</button>
      <button class="pager-btn">Next ›</button>
    </div>
  </div>
</div>
```

Pager button styles:
```css
.pager-btn {
  background: none; border: 1px solid var(--border);
  color: var(--text-2); font-family: var(--font); font-size: 12px;
  padding: 4px 10px; cursor: pointer;
}
.pager-btn.active { background: var(--accent); border-color: var(--accent); color: #fff; }
```

---

## 7. Form Section with Inline-Validated Fields

```html
<div class="panel">
  <div class="panel-head">
    <div class="panel-title">Section Title</div>
  </div>
  <div style="padding:20px;display:flex;flex-direction:column;gap:14px">

    <!-- Two-column row -->
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:14px">

      <!-- Valid field -->
      <div class="field valid">
        <label class="field-label" for="f1">
          Field Label <span class="required-mark">*</span>
        </label>
        <div class="field-control">
          <input id="f1" type="text" value="Valid value">
          <!-- valid icon: position:absolute right:10px -->
          <svg style="position:absolute;right:10px;top:50%;transform:translateY(-50%);color:var(--s-success)" width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg>
        </div>
        <div class="field-helper">Helper text describing the rule.</div>
      </div>

      <!-- Invalid field -->
      <div class="field invalid">
        <label class="field-label" for="f2">
          Another Field <span class="required-mark">*</span>
        </label>
        <div class="field-control">
          <input id="f2" type="text" value="bad!" aria-invalid="true" aria-describedby="f2-err">
        </div>
        <div class="field-error" id="f2-err" role="alert">
          <svg width="11" height="11" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-2h2v2zm0-4h-2V7h2v6z"/></svg>
          Inline error message.
        </div>
      </div>
    </div>

    <!-- Full-width textarea -->
    <div class="field">
      <label class="field-label" for="f3">Notes</label>
      <div class="field-control">
        <textarea id="f3" rows="3" placeholder="Optional…"></textarea>
      </div>
    </div>

  </div>

  <!-- Form footer -->
  <div style="display:flex;align-items:center;justify-content:flex-end;gap:10px;padding:14px 20px;border-top:1px solid var(--border)">
    <button class="btn btn-ghost">Cancel</button>
    <button class="btn btn-primary" disabled>
      Save Record
    </button>
  </div>
</div>
```

Inline validation CSS:
```css
.field.invalid .field-control input { border-color: var(--s-danger); }
.field.valid  .field-control input  { border-color: var(--s-success); }
```

---

## 8. Auth Card (Sign-in / Sign-up)

```html
<body style="background:var(--page);display:flex;align-items:center;justify-content:center;min-height:100vh">
  <div style="width:100%;max-width:420px;display:flex;flex-direction:column;gap:28px;align-items:center">

    <!-- Logo -->
    <div style="display:flex;align-items:center;gap:10px">
      <svg style="color:var(--accent)" …/> <!-- brand icon -->
      <span style="font-size:22px;font-weight:700">Brand</span>
    </div>

    <!-- Card -->
    <div class="panel" style="width:100%">
      <div style="padding:28px 28px 0">
        <div style="font-size:20px;font-weight:700">Sign in</div>
        <div style="font-size:13px;color:var(--text-3);margin-top:4px">Subtitle</div>
      </div>
      <div style="padding:24px 28px;display:flex;flex-direction:column;gap:16px">
        <!-- fields here (see § 7) -->
        <button class="btn btn-primary" style="width:100%;justify-content:center;padding:11px">
          Sign In
        </button>
      </div>
      <div style="padding:16px 28px 24px;border-top:1px solid var(--border);text-align:center;font-size:12px;color:var(--text-3)">
        No account? <a style="color:var(--accent);text-decoration:none" href="#">Create one →</a>
      </div>
    </div>
  </div>
</body>
```

---

## 9. Error / Empty State

```html
<body style="background:var(--page);display:flex;flex-direction:column;align-items:center;justify-content:center;min-height:100vh;text-align:center;padding:24px">

  <!-- Large numeric code -->
  <div style="font-size:clamp(80px,18vw,140px);font-weight:700;color:var(--accent);letter-spacing:-4px;line-height:1;font-variant-numeric:tabular-nums">
    404
  </div>

  <div style="font-size:24px;font-weight:700;margin-bottom:8px">Title</div>
  <div style="font-size:14px;color:var(--text-3);max-width:380px;margin:0 auto 28px">
    Explanatory message. Keep it concise and actionable.
  </div>

  <div style="display:flex;gap:12px;flex-wrap:wrap;justify-content:center">
    <a class="btn btn-primary" href="#">
      <svg …/> Primary Action
    </a>
    <button class="btn btn-ghost">
      <svg …/> Secondary Action
    </button>
  </div>
</body>
```

---

## 10. Mini SVG Line Chart (inside a panel)

```html
<svg width="100%" height="180" viewBox="0 0 480 180"
     style="display:block" aria-label="Trend chart">
  <!-- Grid lines (dotted, border color) -->
  <line x1="40" y1="20" x2="460" y2="20"
        stroke="#2a2e38" stroke-width="1" stroke-dasharray="3 3"/>
  <!-- repeat at y=55,90,125,160 -->

  <!-- Y-axis labels (muted text, 10px) -->
  <text x="32" y="24" text-anchor="end"
        fill="#6c7293" font-size="10" font-family="Open Sans,sans-serif">100%</text>
  <!-- repeat at other y positions -->

  <!-- X-axis labels -->
  <text x="40" y="175" text-anchor="middle"
        fill="#6c7293" font-size="10" font-family="Open Sans,sans-serif">Mon</text>

  <!-- Area fill (accent at 18% alpha) -->
  <polygon fill="#009688" opacity=".18"
    points="40,110 110,100 180,95 250,115 320,108 390,85 460,80 460,160 40,160"/>

  <!-- Line stroke (accent, 2px) -->
  <polyline fill="none" stroke="#009688" stroke-width="2"
    points="40,110 110,100 180,95 250,115 320,108 390,85 460,80"/>

  <!-- Data dots -->
  <circle cx="460" cy="80" r="4"
          fill="#009688" stroke="#191c24" stroke-width="2"/>
</svg>
```

---

## Tokens Reference

| Token              | Value                     | Use                          |
|--------------------|---------------------------|------------------------------|
| `--page`           | `#000000`                 | Body / page background       |
| `--panel`          | `#191c24`                 | Cards, sidebar, topbar       |
| `--panel-hover`    | `#212535`                 | Hovered rows / items         |
| `--active-bg`      | `#2a2e38`                 | Inputs, selected items       |
| `--border`         | `#2a2e38`                 | Hairline borders             |
| `--divider`        | `#1e2130`                 | Table row separators         |
| `--text-1`         | `#ffffff`                 | Headings, primary text       |
| `--text-2`         | `#b1b7c1`                 | Body / cell text             |
| `--text-3`         | `#6c7293`                 | Labels, muted text           |
| `--text-4`         | `#454865`                 | Faint / disabled             |
| `--accent`         | `#009688`                 | CTA, active nav, figures     |
| `--accent-hov`     | `#00b09c`                 | Hovered accent               |
| `--accent-dim`     | `rgba(0,150,136,.15)`     | Active nav background        |
| `--s-success`      | `#00c897`                 | Running / healthy            |
| `--s-warn`         | `#ffab00`                 | Degraded / warning           |
| `--s-danger`       | `#ff4c61`                 | Offline / critical           |
| `--s-info`         | `#5b73e8`                 | Informational / provisioning |
| `--s-neutral`      | `#6c7293`                 | Maintenance / neutral        |
| `--radius`         | `0px`                     | Zero radius — sharp corners  |
