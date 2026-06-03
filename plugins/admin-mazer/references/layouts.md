# Soft Blue Admin — Paste-Ready Layout Skeletons

Domain-neutral HTML fragments for each archetype region. Label each usage site
by slot — never by a domain noun. Inline-CSS illustrates the design token usage;
import/extend from the `:root` block in `assets/template.html` in practice.

---

## Sidebar shell

```html
<aside class="sidebar">
  <!-- Brand -->
  <div class="sidebar-brand">
    <div class="brand-icon"><!-- SVG icon --></div>
    <span class="brand-name">AppName</span>
  </div>

  <!-- Nav group (repeat) -->
  <nav>
    <div class="nav-section">
      <div class="nav-label">Section</div>
      <div class="nav-item active">
        <svg class="nav-icon"><!-- icon --></svg>
        Item Label
      </div>
      <div class="nav-item">
        <svg class="nav-icon"><!-- icon --></svg>
        Item Label
      </div>
    </div>
  </nav>

  <!-- Footer: avatar + name + role -->
  <div class="sidebar-footer">
    <div class="avatar">AB</div>
    <div>
      <div style="font-size:13px;font-weight:700">Full Name</div>
      <div style="font-size:11px;color:var(--text-muted)">Role</div>
    </div>
  </div>
</aside>
```

---

## Sticky top header bar

```html
<header class="topbar">
  <!-- Breadcrumb -->
  <div class="breadcrumb">
    <span>Home</span>
    <span style="color:var(--text-muted)">/</span>
    <span style="font-weight:700;color:var(--text-body)">Current Page</span>
  </div>

  <div style="flex:1"></div><!-- spacer -->

  <!-- Search pill -->
  <div class="search-pill">
    <svg width="14" height="14"><!-- search icon --></svg>
    Search…
  </div>

  <!-- Notification icon -->
  <button class="icon-btn">
    <svg width="18" height="18"><!-- bell icon --></svg>
    <!-- Optional unread dot: -->
    <span style="position:absolute;top:6px;right:6px;width:8px;height:8px;
      border-radius:50%;background:var(--danger);border:2px solid var(--card)"></span>
  </button>

  <!-- Avatar -->
  <div style="width:36px;height:36px;border-radius:50%;background:var(--primary);
    display:flex;align-items:center;justify-content:center;
    font-size:13px;font-weight:700;color:#fff;cursor:pointer">AB</div>
</header>
```

---

## KPI tile (repeat ×4 in a `grid-4` row)

```html
<div style="background:var(--card);border-radius:var(--radius-card);
  padding:20px;box-shadow:var(--shadow-card);display:flex;align-items:center;gap:16px">
  <!-- Icon chip -->
  <div style="width:50px;height:50px;border-radius:10px;background:var(--primary-soft);
    flex-shrink:0;display:flex;align-items:center;justify-content:center">
    <svg width="22" height="22" stroke="var(--primary)"><!-- metric icon --></svg>
  </div>
  <!-- Metric -->
  <div>
    <div style="font-size:26px;font-weight:700;color:var(--text-body);line-height:1">1,234</div>
    <div style="font-size:11px;font-weight:700;text-transform:uppercase;
      letter-spacing:.6px;color:var(--text-muted);margin-top:4px">Metric Label</div>
    <!-- Delta badge -->
    <div style="display:inline-flex;align-items:center;gap:3px;font-size:11px;
      font-weight:700;margin-top:5px;padding:2px 7px;border-radius:var(--radius-pill);
      background:var(--success-soft);color:var(--success)">▲ 5% vs prior period</div>
  </div>
</div>
```

---

## Card with header + tab group

```html
<div style="background:var(--card);border-radius:var(--radius-card);
  box-shadow:var(--shadow-card);padding:20px">
  <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:16px">
    <span style="font-size:15px;font-weight:700;color:var(--text-body)">Card Title</span>
    <!-- Tab group -->
    <div style="display:flex;gap:4px">
      <div style="padding:5px 12px;border-radius:6px;font-size:12px;font-weight:600;
        background:var(--primary-soft);color:var(--primary);cursor:pointer">Tab A</div>
      <div style="padding:5px 12px;border-radius:6px;font-size:12px;font-weight:600;
        color:var(--text-secondary);cursor:pointer">Tab B</div>
    </div>
  </div>
  <!-- card body -->
</div>
```

---

## Activity feed item

```html
<div style="display:flex;align-items:flex-start;gap:12px">
  <!-- Icon chip / avatar -->
  <div style="width:36px;height:36px;border-radius:50%;flex-shrink:0;
    background:var(--success-soft);display:flex;align-items:center;
    justify-content:center;font-size:13px;font-weight:700;color:var(--success)">AB</div>
  <div>
    <div style="font-size:13px;font-weight:600;color:var(--text-body)">Action title</div>
    <div style="font-size:12px;color:var(--text-secondary);margin-top:2px">Sub-detail · Entity</div>
  </div>
  <div style="font-size:11px;color:var(--text-muted);margin-left:auto;white-space:nowrap">2h ago</div>
</div>
```

---

## Status rows (badge-pill + metric)

```html
<!-- Repeat inside a card for each status category -->
<div style="display:flex;align-items:center;gap:10px;padding:10px 0;
  border-bottom:1px solid var(--divider)">
  <!-- Icon chip -->
  <div style="width:32px;height:32px;border-radius:50%;flex-shrink:0;
    background:var(--success-soft);display:flex;align-items:center;justify-content:center">
    <svg width="14" height="14" stroke="var(--success)"><!-- icon --></svg>
  </div>
  <span style="font-size:13px;font-weight:600;flex:1">Category Label</span>
  <!-- Badge pill -->
  <span style="display:inline-flex;align-items:center;padding:3px 10px;
    border-radius:var(--radius-pill);font-size:11px;font-weight:700;
    background:var(--success-soft);color:var(--success)">Active</span>
  <!-- Count -->
  <span style="font-size:13px;font-weight:700;min-width:24px;text-align:right">24</span>
</div>
```

---

## Data table row

```html
<!-- thead -->
<thead>
  <tr>
    <th style="padding:10px 14px;text-align:left;font-size:11px;font-weight:700;
      text-transform:uppercase;letter-spacing:.5px;color:var(--text-muted);
      border-bottom:2px solid var(--divider)">Column</th>
    <!-- repeat -->
  </tr>
</thead>

<!-- tbody row -->
<tbody>
  <tr style="border-bottom:1px solid var(--divider);transition:var(--transition)">
    <!-- Two-line entity cell -->
    <td style="padding:11px 14px;vertical-align:middle">
      <div style="font-weight:600;color:var(--text-body)">Primary name</div>
      <div style="font-size:12px;color:var(--text-secondary)">Sub-detail</div>
    </td>
    <!-- Plain text -->
    <td style="padding:11px 14px;vertical-align:middle;color:var(--text-secondary)">Value</td>
    <!-- Progress -->
    <td style="padding:11px 14px;vertical-align:middle">
      <div style="height:6px;border-radius:3px;background:var(--divider);width:80px">
        <div style="height:100%;width:65%;background:var(--primary);border-radius:3px"></div>
      </div>
      <div style="font-size:11px;color:var(--text-muted);margin-top:3px">65%</div>
    </td>
    <!-- Badge status -->
    <td style="padding:11px 14px;vertical-align:middle">
      <span style="display:inline-flex;padding:3px 10px;border-radius:var(--radius-pill);
        font-size:11px;font-weight:700;background:var(--success-soft);color:var(--success)">Active</span>
    </td>
    <!-- Row action -->
    <td style="padding:11px 14px;vertical-align:middle">
      <button style="padding:5px;border-radius:6px;color:var(--text-secondary);
        transition:var(--transition);cursor:pointer;border:none;background:none">⋯</button>
    </td>
  </tr>
</tbody>
```

---

## Table pager

```html
<div style="display:flex;align-items:center;justify-content:space-between;
  margin-top:16px;font-size:13px;color:var(--text-secondary)">
  <span>Showing 1–10 of 79 records</span>
  <div style="display:flex;gap:6px">
    <button style="padding:5px 12px;border-radius:6px;border:1px solid var(--border);
      font-size:13px;font-weight:600;color:var(--text-secondary);
      background:var(--card);cursor:pointer">‹ Prev</button>
    <button style="padding:5px 12px;border-radius:6px;border:1px solid var(--primary);
      font-size:13px;font-weight:600;background:var(--primary);color:#fff;cursor:pointer">1</button>
    <button style="padding:5px 12px;border-radius:6px;border:1px solid var(--border);
      font-size:13px;font-weight:600;color:var(--text-secondary);
      background:var(--card);cursor:pointer">2</button>
    <button style="padding:5px 12px;border-radius:6px;border:1px solid var(--border);
      font-size:13px;font-weight:600;color:var(--text-secondary);
      background:var(--card);cursor:pointer">Next ›</button>
  </div>
</div>
```

---

## Form section with inline validation

```html
<!-- Section card -->
<div style="background:var(--card);border-radius:var(--radius-card);
  box-shadow:var(--shadow-card);padding:24px">
  <div style="font-size:15px;font-weight:700;margin-bottom:4px">Section Title</div>
  <div style="font-size:12px;color:var(--text-secondary);margin-bottom:18px;
    padding-bottom:14px;border-bottom:1px solid var(--divider)">
    Brief instruction for this section.
  </div>

  <!-- Two-column row -->
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:18px">
    <!-- Valid field -->
    <div style="display:flex;flex-direction:column;gap:5px;margin-bottom:16px">
      <label style="font-size:13px;font-weight:700">Field Label
        <span style="color:var(--danger);margin-left:2px">*</span>
      </label>
      <input type="text" value="Valid value"
        style="background:var(--input-bg);border:1.5px solid var(--success);
          border-radius:var(--radius-btn);padding:9px 12px;font-size:14px;
          color:var(--text-body);outline:none;width:100%">
    </div>
    <!-- Error field -->
    <div style="display:flex;flex-direction:column;gap:5px;margin-bottom:16px">
      <label style="font-size:13px;font-weight:700">Required Field
        <span style="color:var(--danger);margin-left:2px">*</span>
      </label>
      <input type="text" value=""
        style="background:#fff8f8;border:1.5px solid var(--danger);
          border-radius:var(--radius-btn);padding:9px 12px;font-size:14px;
          color:var(--text-body);outline:none;width:100%"
        placeholder="Enter a value">
      <span style="font-size:11px;color:var(--danger);display:flex;align-items:center;gap:4px">
        <!-- error icon SVG -->
        This field is required.
      </span>
    </div>
  </div>

  <!-- Helper text -->
  <div style="display:flex;flex-direction:column;gap:5px;margin-bottom:16px">
    <label style="font-size:13px;font-weight:700">Optional Field</label>
    <input type="text"
      style="background:var(--input-bg);border:1.5px solid var(--border);
        border-radius:var(--radius-btn);padding:9px 12px;font-size:14px;
        color:var(--text-body);outline:none;width:100%"
      placeholder="Optional…">
    <span style="font-size:11px;color:var(--text-muted)">Helper text explaining the field.</span>
  </div>
</div>

<!-- Action row -->
<div style="display:flex;justify-content:flex-end;gap:12px">
  <button style="background:transparent;color:var(--text-secondary);padding:9px 20px;
    border:1.5px solid var(--border);border-radius:var(--radius-btn);
    font-size:14px;font-weight:600;cursor:pointer">Cancel</button>
  <button disabled style="background:var(--primary);color:#fff;padding:10px 24px;
    border-radius:var(--radius-btn);font-size:14px;font-weight:700;
    opacity:.45;cursor:not-allowed;border:none">Save (disabled until valid)</button>
</div>
```

---

## SVG inline area/line chart skeleton

```html
<svg width="100%" height="180" viewBox="0 0 600 180" preserveAspectRatio="none">
  <defs>
    <linearGradient id="area-grad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="var(--primary)" stop-opacity=".18"/>
      <stop offset="100%" stop-color="var(--primary)" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <!-- Gridlines -->
  <line x1="0" y1="36" x2="600" y2="36" stroke="var(--divider)" stroke-width="1"/>
  <line x1="0" y1="72" x2="600" y2="72" stroke="var(--divider)" stroke-width="1"/>
  <line x1="0" y1="108" x2="600" y2="108" stroke="var(--divider)" stroke-width="1"/>
  <line x1="0" y1="144" x2="600" y2="144" stroke="var(--divider)" stroke-width="1"/>
  <!-- Area polygon (adjust points to data) -->
  <polygon
    points="0,130 100,110 200,80 300,90 400,60 500,70 600,45 600,155 0,155"
    fill="url(#area-grad)"/>
  <!-- Line (same points minus the base) -->
  <polyline
    points="0,130 100,110 200,80 300,90 400,60 500,70 600,45"
    fill="none" stroke="var(--primary)" stroke-width="2.5" stroke-linejoin="round"/>
  <!-- Data point dots (optional) -->
  <circle cx="400" cy="60" r="4" fill="var(--primary)"/>
  <!-- X-axis labels -->
  <text x="0" y="170" fill="var(--text-muted)" font-size="11" font-family="Nunito,sans-serif">L1</text>
  <!-- ... repeat per x-tick ... -->
</svg>
```

---

## Auth card (login / register)

```html
<!-- Centered layout: body { display:flex; align-items:center; justify-content:center; } -->
<div style="width:100%;max-width:420px">
  <!-- Brand row -->
  <div style="display:flex;align-items:center;justify-content:center;gap:10px;margin-bottom:32px">
    <div style="width:40px;height:40px;border-radius:10px;background:var(--primary);
      display:flex;align-items:center;justify-content:center"><!-- icon --></div>
    <span style="font-size:20px;font-weight:700">AppName</span>
  </div>
  <!-- Card -->
  <div style="background:var(--card);border-radius:var(--radius-card);
    box-shadow:var(--shadow-card);padding:36px 32px">
    <div style="font-size:22px;font-weight:700;margin-bottom:4px">Sign in</div>
    <div style="font-size:13px;color:var(--text-secondary);margin-bottom:24px">
      Welcome back — sign in to continue.
    </div>
    <!-- Fields -->
    <div style="display:flex;flex-direction:column;gap:5px;margin-bottom:18px">
      <label style="font-size:13px;font-weight:700">Email
        <span style="color:var(--danger)">*</span>
      </label>
      <input type="email" placeholder="you@example.com"
        style="background:var(--input-bg);border:1.5px solid var(--border);
          border-radius:var(--radius-btn);padding:10px 14px;font-size:14px;
          color:var(--text-body);outline:none;width:100%">
    </div>
    <!-- Primary button -->
    <button style="width:100%;background:var(--primary);color:#fff;padding:11px;
      border-radius:var(--radius-btn);font-size:15px;font-weight:700;
      border:none;cursor:pointer;margin-top:8px">Sign In</button>
  </div>
  <!-- Footer link -->
  <div style="text-align:center;margin-top:20px;font-size:13px;color:var(--text-secondary)">
    Don't have an account?
    <a href="#" style="font-weight:700;color:var(--primary)">Sign up</a>
  </div>
</div>
```

---

## Error / empty state (centered)

```html
<!-- body { display:flex; align-items:center; justify-content:center; } -->
<div style="max-width:500px;width:100%;text-align:center">
  <!-- SVG illustration placeholder -->
  <div style="width:160px;height:120px;margin:0 auto 32px;background:var(--primary-soft);
    border-radius:var(--radius-card);display:flex;align-items:center;justify-content:center">
    <svg width="60" height="60" stroke="var(--primary)"><!-- illustration --></svg>
  </div>
  <div style="font-size:72px;font-weight:700;color:var(--primary);line-height:1;margin-bottom:12px">404</div>
  <div style="font-size:22px;font-weight:700;margin-bottom:10px">Page not found</div>
  <div style="font-size:15px;color:var(--text-secondary);margin-bottom:32px;line-height:1.6">
    The page you're looking for doesn't exist.
  </div>
  <div style="display:flex;align-items:center;justify-content:center;gap:12px">
    <button style="display:inline-flex;align-items:center;gap:8px;background:var(--primary);
      color:#fff;padding:12px 28px;border-radius:var(--radius-btn);
      font-size:15px;font-weight:700;border:none;cursor:pointer">
      Back to Dashboard
    </button>
  </div>
</div>
```

---

## Toggle row (settings)

```html
<div style="display:flex;align-items:center;justify-content:space-between;
  padding:12px 0;border-bottom:1px solid var(--divider)">
  <div>
    <div style="font-size:13px;font-weight:700">Setting title</div>
    <div style="font-size:12px;color:var(--text-secondary);margin-top:2px">
      Brief description of this preference.
    </div>
  </div>
  <!-- Toggle: add class "on" to activate -->
  <div style="width:42px;height:24px;background:var(--primary);border-radius:12px;
    position:relative;cursor:pointer;flex-shrink:0">
    <div style="width:18px;height:18px;background:#fff;border-radius:50%;
      position:absolute;top:3px;left:21px;box-shadow:0 1px 4px rgba(0,0,0,.18)"></div>
  </div>
</div>
```
