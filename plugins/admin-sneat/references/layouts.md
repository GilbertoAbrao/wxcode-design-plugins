# Indigo SaaS Admin — Paste-ready Layout Skeletons

Domain-neutral HTML fragments for each archetype region. Copy into `assets/template.html` or any screen file. Slot labels are in angle brackets — replace with domain-appropriate content.

---

## Token block (`:root`)

```html
<style>
:root {
  --accent:        #696cff;
  --accent-hover:  #5a5dd6;
  --accent-dim:    rgba(105,108,255,.12);
  --canvas:        #f5f5f9;
  --surface:       #ffffff;
  --border:        #e4e6e8;
  --text-primary:  #333240;
  --text-body:     #646e78;
  --text-muted:    #8a9099;
  --shadow-sm:     0 2px 6px rgba(67,89,113,.12);
  --shadow-md:     0 4px 16px rgba(67,89,113,.15);
  --radius-card:   6px;
  --radius-pill:   20px;
  --radius-input:  6px;
  --state-success: #71dd37;
  --state-warning: #ffab00;
  --state-danger:  #ff3e1d;
  --state-info:    #03c3ec;
  --state-secondary:#8592a3;
}
</style>
```

---

## Navbar

```html
<nav class="navbar">
  <div class="navbar-brand">
    <!-- Logo mark SVG here -->
    <span><app-name></span>
  </div>
  <div class="navbar-search">
    <!-- search icon prefix -->
    <input type="text" placeholder="Search…" aria-label="Search">
  </div>
  <div class="navbar-actions">
    <button class="icon-btn" title="Notifications"><!-- bell SVG --></button>
    <div class="nav-avatar"><initials></div>
  </div>
</nav>
```

CSS:
```css
.navbar{position:fixed;top:0;left:0;right:0;height:60px;background:var(--surface);
  border-bottom:1px solid var(--border);display:flex;align-items:center;
  padding:0 24px;gap:16px;z-index:100;box-shadow:var(--shadow-sm)}
.navbar-brand{display:flex;align-items:center;gap:8px;width:236px}
.navbar-brand span{font-weight:700;font-size:18px;color:var(--text-primary)}
.navbar-search{flex:1;max-width:320px;position:relative}
.navbar-search input{width:100%;padding:8px 12px 8px 36px;border:1px solid var(--border);
  border-radius:var(--radius-input);font-size:14px;background:var(--canvas);outline:none}
.navbar-search input:focus{border-color:var(--accent);box-shadow:0 0 0 3px var(--accent-dim)}
.navbar-actions{margin-left:auto;display:flex;align-items:center;gap:8px}
.icon-btn{width:38px;height:38px;border-radius:50%;border:none;background:transparent;
  cursor:pointer;display:flex;align-items:center;justify-content:center}
.nav-avatar{width:38px;height:38px;border-radius:50%;background:var(--accent-dim);
  color:var(--accent);display:flex;align-items:center;justify-content:center;
  font-weight:700;font-size:14px;border:2px solid var(--accent)}
```

---

## Left sidebar

```html
<aside class="sidebar">
  <div class="nav-section-label"><section-label></div>
  <a class="nav-item active" href="#"><!-- icon SVG --> <item-label></a>
  <a class="nav-item" href="#"><!-- icon SVG --> <item-label> <span class="nav-badge">N</span></a>
  <div class="nav-section-label"><section-label></div>
  <a class="nav-item" href="#"><!-- icon SVG --> Settings</a>
</aside>
```

CSS:
```css
.sidebar{position:fixed;top:60px;left:0;width:260px;bottom:0;
  background:var(--surface);border-right:1px solid var(--border);
  overflow-y:auto;padding:16px 0}
.nav-section-label{font-size:11px;font-weight:600;text-transform:uppercase;
  letter-spacing:.08em;color:var(--text-muted);padding:16px 24px 6px}
.nav-item{display:flex;align-items:center;gap:12px;padding:10px 20px;
  color:var(--text-body);text-decoration:none;border-radius:6px;margin:1px 12px;
  font-size:14px;font-weight:500;transition:.18s}
.nav-item:hover{background:var(--canvas)}
.nav-item.active{background:var(--accent-dim);color:var(--accent)}
.nav-badge{margin-left:auto;font-size:11px;font-weight:600;padding:2px 8px;
  border-radius:var(--radius-pill);background:var(--accent-dim);color:var(--accent)}
```

---

## Main content region

```html
<main class="main">
  <div class="page-header">
    <div>
      <div class="page-title"><page-title></div>
      <div class="page-subtitle"><subtitle></div>
    </div>
    <div style="display:flex;gap:10px">
      <button class="btn btn-ghost">Secondary</button>
      <button class="btn btn-primary">+ Primary</button>
    </div>
  </div>
  <!-- cards / grids / tables here -->
</main>
```

CSS:
```css
.main{margin-left:260px;margin-top:60px;padding:24px;min-height:calc(100vh - 60px)}
.page-header{display:flex;align-items:center;justify-content:space-between;margin-bottom:24px}
.page-title{font-size:20px;font-weight:700;color:var(--text-primary)}
.page-subtitle{font-size:13px;color:var(--text-muted);margin-top:2px}
.btn{display:inline-flex;align-items:center;gap:6px;padding:9px 20px;
  border-radius:var(--radius-input);font-size:14px;font-weight:500;border:none;cursor:pointer}
.btn-primary{background:var(--accent);color:#fff}
.btn-primary:hover{background:var(--accent-hover)}
.btn-ghost{background:transparent;color:var(--accent);border:1px solid var(--accent)}
.btn-ghost:hover{background:var(--accent-dim)}
```

---

## KPI stat tile

```html
<div class="kpi-card">
  <div class="kpi-icon"><!-- metric-icon SVG --></div>
  <div>
    <div class="kpi-value"><metric-value></div>
    <div class="kpi-label"><metric-label></div>
    <div class="kpi-delta up">▲ N% vs last period</div>
    <!-- or: <div class="kpi-delta down">▼ N%</div> -->
  </div>
</div>
```

CSS:
```css
.kpi-card{background:var(--surface);border-radius:var(--radius-card);border:1px solid var(--border);
  box-shadow:var(--shadow-sm);padding:20px 24px;display:flex;align-items:flex-start;gap:16px}
.kpi-icon{width:44px;height:44px;border-radius:var(--radius-card);background:var(--accent-dim);
  display:flex;align-items:center;justify-content:center;flex-shrink:0;color:var(--accent)}
.kpi-value{font-size:24px;font-weight:700;color:var(--text-primary);font-variant-numeric:tabular-nums}
.kpi-label{font-size:13px;color:var(--text-muted);margin-top:2px}
.kpi-delta{display:inline-flex;align-items:center;gap:3px;font-size:12px;font-weight:600;
  padding:2px 8px;border-radius:var(--radius-pill);margin-top:6px}
.kpi-delta.up{background:rgba(113,221,55,.12);color:#59b027}
.kpi-delta.down{background:rgba(255,62,29,.12);color:#d63515}
```

---

## Card shell

```html
<div class="card">
  <div class="card-header">
    <div class="card-title"><title></div>
    <!-- optional: secondary text, actions -->
  </div>
  <div class="card-body">
    <!-- card content -->
  </div>
</div>
```

CSS:
```css
.card{background:var(--surface);border-radius:var(--radius-card);border:1px solid var(--border);
  box-shadow:var(--shadow-sm)}
.card-header{display:flex;align-items:center;justify-content:space-between;padding:18px 24px 0}
.card-title{font-size:14px;font-weight:600;color:var(--text-primary);
  text-transform:uppercase;letter-spacing:.05em}
.card-body{padding:16px 24px 20px}
```

---

## Records table

```html
<div class="table-card">
  <div class="table-header">
    <span class="table-title"><entity-plural></span>
    <input type="text" placeholder="Search…" class="table-search-input">
    <button class="btn btn-primary">+ Add</button>
  </div>
  <table class="data-table">
    <thead>
      <tr>
        <th><input type="checkbox" aria-label="Select all"></th>
        <th>ID</th>
        <th><entity-name></th>
        <th>Status</th>
        <th style="text-align:right"><metric></th>
        <th></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><input type="checkbox" aria-label="Select"></td>
        <td><span class="mono">#<id></span></td>
        <td>
          <div class="cell-avatar">
            <div class="avatar-sm"><initials></div>
            <div>
              <div class="cell-name"><name></div>
              <div class="cell-sub"><sub-info></div>
            </div>
          </div>
        </td>
        <td><span class="pill pill-success">Active</span></td>
        <td style="text-align:right;font-variant-numeric:tabular-nums"><value></td>
        <td><button class="icon-btn" style="width:28px;height:28px" title="Actions">⋯</button></td>
      </tr>
    </tbody>
  </table>
  <div class="table-footer">
    <span>Showing 1–N of <total></span>
    <div class="pager">
      <button class="pager-btn">‹</button>
      <button class="pager-btn active">1</button>
      <button class="pager-btn">2</button>
      <button class="pager-btn">›</button>
    </div>
  </div>
</div>
```

CSS:
```css
.table-card{background:var(--surface);border-radius:var(--radius-card);border:1px solid var(--border);
  box-shadow:var(--shadow-sm);overflow:hidden}
.table-header{display:flex;align-items:center;gap:12px;padding:18px 24px;border-bottom:1px solid var(--border)}
.table-title{font-size:14px;font-weight:600;color:var(--text-primary);text-transform:uppercase;
  letter-spacing:.05em;margin-right:auto}
.data-table{width:100%;border-collapse:collapse}
.data-table th{font-size:11px;font-weight:600;text-transform:uppercase;letter-spacing:.06em;
  color:var(--text-muted);padding:12px 16px;border-bottom:1px solid var(--border);text-align:left}
.data-table td{padding:13px 16px;border-bottom:1px solid var(--border);font-size:13px;color:var(--text-body)}
.data-table tr:last-child td{border-bottom:none}
.data-table tr:hover td{background:#f8f8fb}
.mono{font-family:"Courier New",monospace;font-size:12px;color:var(--text-muted)}
.cell-avatar{display:flex;align-items:center;gap:10px}
.avatar-sm{width:32px;height:32px;border-radius:50%;background:var(--accent-dim);color:var(--accent);
  display:flex;align-items:center;justify-content:center;font-weight:700;font-size:12px;flex-shrink:0}
.cell-name{font-weight:500;color:var(--text-primary);font-size:13px}
.cell-sub{font-size:12px;color:var(--text-muted)}
.table-footer{display:flex;align-items:center;justify-content:space-between;padding:14px 24px;
  border-top:1px solid var(--border);font-size:13px;color:var(--text-muted)}
.pager{display:flex;align-items:center;gap:4px}
.pager-btn{width:30px;height:30px;border-radius:var(--radius-input);border:1px solid var(--border);
  background:var(--surface);display:flex;align-items:center;justify-content:center;
  cursor:pointer;font-size:13px;color:var(--text-body)}
.pager-btn.active{background:var(--accent);color:#fff;border-color:var(--accent)}
```

---

## Status pills

```html
<span class="pill pill-success">Active</span>
<span class="pill pill-warning">Pending</span>
<span class="pill pill-danger">Cancelled</span>
<span class="pill pill-info">Trialing</span>
<span class="pill pill-secondary">Inactive</span>
```

CSS:
```css
.pill{display:inline-flex;align-items:center;padding:3px 10px;border-radius:var(--radius-pill);
  font-size:12px;font-weight:600}
.pill-success{background:rgba(113,221,55,.15);color:#4b9e22}
.pill-warning{background:rgba(255,171,0,.15);color:#b07a00}
.pill-danger{background:rgba(255,62,29,.12);color:#c02e14}
.pill-info{background:rgba(3,195,236,.12);color:#0296b7}
.pill-secondary{background:rgba(133,146,163,.12);color:#8592a3}
```

---

## Form section with inline-validated field

```html
<div class="card">
  <div class="card-title-bar"><section-name></div>
  <div class="card-body">

    <!-- Required field, valid state -->
    <div class="field">
      <label class="field-label" for="f-<id>">
        <field-label> <span class="required-mark">*</span>
      </label>
      <input class="field-input" id="f-<id>" type="text"
        placeholder="<placeholder>" aria-required="true" aria-describedby="f-<id>-helper">
      <div class="helper-text" id="f-<id>-helper"><helper text></div>
    </div>

    <!-- Required field, invalid state -->
    <div class="field">
      <label class="field-label" for="f-<id2>">
        <field-label> <span class="required-mark">*</span>
      </label>
      <input class="field-input is-invalid" id="f-<id2>" type="text"
        aria-invalid="true" aria-describedby="f-<id2>-err">
      <div class="error-text" id="f-<id2>-err"><!-- error icon SVG --> <error-message></div>
    </div>

    <!-- Select field -->
    <div class="field">
      <label class="field-label" for="f-<id3>">
        <field-label> <span class="required-mark">*</span>
      </label>
      <select class="field-input field-select" id="f-<id3>" aria-required="true">
        <option value="">Choose…</option>
        <option value="a"><option-a></option>
        <option value="b"><option-b></option>
      </select>
    </div>

    <div style="display:flex;justify-content:flex-end;gap:12px;margin-top:24px">
      <button class="btn btn-ghost" type="button">Cancel</button>
      <button class="btn btn-primary" type="submit">Submit</button>
    </div>
  </div>
</div>
```

CSS:
```css
.card-title-bar{padding:18px 24px;border-bottom:1px solid var(--border);
  font-size:14px;font-weight:600;color:var(--text-primary);text-transform:uppercase;letter-spacing:.05em}
.card-body{padding:24px}
.field{margin-bottom:20px}
.field-label{font-size:13px;font-weight:600;color:var(--text-primary);display:block;margin-bottom:6px}
.required-mark{color:var(--accent)}
.field-input{width:100%;padding:9px 14px;border:1px solid var(--border);border-radius:var(--radius-input);
  font-size:14px;color:var(--text-primary);background:var(--surface);outline:none;transition:.18s;font-family:inherit}
.field-input:focus{border-color:var(--accent);box-shadow:0 0 0 3px var(--accent-dim)}
.field-input.is-invalid{border-color:var(--state-danger);box-shadow:0 0 0 3px rgba(255,62,29,.1)}
.field-select{appearance:none;padding-right:36px;
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 24 24' fill='none' stroke='%238a9099' stroke-width='2'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E");
  background-repeat:no-repeat;background-position:right 12px center}
.helper-text{font-size:12px;color:var(--text-muted);margin-top:4px}
.error-text{font-size:12px;color:var(--state-danger);margin-top:4px;display:flex;align-items:center;gap:4px}
```

---

## Auth card (centered, no sidebar)

```html
<!doctype html>
<html lang="en">
<head>
<!-- tokens + reset as above -->
<style>
body{/* ... token block ... */
  min-height:100vh;display:flex;flex-direction:column;
  align-items:center;justify-content:center;
  background:var(--canvas);padding:32px 16px}
.auth-card{background:var(--surface);border-radius:10px;border:1px solid var(--border);
  box-shadow:0 8px 32px rgba(67,89,113,.16);padding:36px 40px;width:100%;max-width:420px}
</style>
</head>
<body>
  <!-- logo above card -->
  <div class="auth-card">
    <h1 class="auth-heading"><heading></h1>
    <p class="auth-sub"><sub> <a href="#"><link-text></a></p>
    <form>
      <!-- inline-validated fields -->
      <button type="submit" class="btn-primary" style="width:100%">Sign In</button>
    </form>
  </div>
  <p class="auth-footer"><footer-link></p>
</body>
</html>
```

---

## Toggle switch

```html
<div style="display:flex;align-items:center;justify-content:space-between;padding:12px 0">
  <div>
    <div style="font-size:13px;font-weight:600;color:var(--text-primary)"><toggle-label></div>
    <div style="font-size:12px;color:var(--text-muted)"><toggle-description></div>
  </div>
  <div class="toggle on" role="switch" aria-checked="true" tabindex="0"></div>
</div>
```

CSS:
```css
.toggle{width:36px;height:20px;border-radius:10px;background:var(--border);
  position:relative;cursor:pointer;flex-shrink:0;transition:.18s}
.toggle.on{background:var(--accent)}
.toggle::after{content:'';width:14px;height:14px;border-radius:50%;background:#fff;
  position:absolute;top:3px;left:3px;transition:.18s;box-shadow:0 1px 3px rgba(0,0,0,.2)}
.toggle.on::after{left:19px}
```

---

## Error / empty state (centered, no sidebar)

```html
<body style="...center flex...">
  <!-- SVG illustration (inline, no CDN) -->
  <div style="font-size:72px;font-weight:800;color:var(--text-primary)">404</div>
  <h1 style="font-size:22px;font-weight:700;color:var(--text-primary)"><heading></h1>
  <p style="font-size:14px;color:var(--text-muted);max-width:360px;text-align:center"><body-text></p>
  <div style="display:flex;gap:12px;margin-top:24px">
    <a href="#" class="btn btn-primary">Back to Home</a>
    <a href="#" class="btn btn-ghost">Contact Support</a>
  </div>
</body>
```
