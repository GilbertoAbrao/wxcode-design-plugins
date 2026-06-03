# Sterling Admin — layout skeletons

Paste-ready, domain-neutral fragments for the Sterling light-mode/slate-blue skin.
Copy the shell from `assets/template.html` first (it carries the `:root` tokens +
sidebar + topbar + `.body` scroll container), then drop the region skeletons below
into `<div class="body">`. Replace every `{Placeholder}` with the real domain
equivalent.

Token recap (full block in `template.html`): page `#f7f8fa`, card `#ffffff`,
sidebar `var(--accent-deep)` = `#334155`; text `#1e293b / #475569 / #64748b /
#94a3b8`; accent `--accent` = `#475569`; positive `--emerald` = `#10b981`;
warn `--amber` = `#f59e0b`; critical `--red` = `#ef4444`.
Put `font-variant-numeric: tabular-nums` on every numeric cell and KPI figure.

---

## Page header (every screen)

```html
<div class="page-header">
  <div>
    <div class="page-title">{Screen title}</div>
    <div class="page-sub">{record count · scope · last-updated}</div>
  </div>
  <div class="header-actions">
    <button class="btn-ghost">{Secondary action}</button>
    <button class="btn-primary">+ {Primary action}</button>
  </div>
</div>
```

---

## KPI card strip (4 cards)

```html
<div class="kpi-strip">  <!-- repeat(4,1fr); gap:16px; margin-bottom:20px -->

  <div class="kpi">
    <div class="kpi-head">
      <div>
        <div class="kpi-label">{METRIC NAME}</div>
        <div class="kpi-val">{figure}</div>
      </div>
      <div class="kpi-icon amber"><!-- or .emerald / .red / .accent -->
        <!-- inline SVG 20×20 glyph -->
      </div>
    </div>
    <div class="kpi-foot">
      <span class="chip-kpi warn">↑ {n}%</span>   <!-- .up / .down / .warn -->
      <span class="kpi-sub">vs yesterday</span>
    </div>
  </div>

  <!-- 3 more .kpi tiles -->
</div>
```

---

## 2-column grid (action-queue left + severity feed right)

```html
<div style="display:grid;grid-template-columns:1fr 340px;gap:16px;">

  <!-- LEFT COLUMN: action-queue card + records table card -->
  <div>
    <!-- Action-queue card (below) -->
    <!-- Records table card (below) -->
  </div>

  <!-- RIGHT COLUMN: severity feed + bar chart -->
  <div style="display:flex;flex-direction:column;gap:0;">
    <!-- Severity feed card (below) -->
    <!-- Bar chart card (below) -->
  </div>

</div>
```

### Action-queue card (inline approve / reject)

```html
<div class="card">
  <div class="card-head">
    <span class="card-title">{Queue title}</span>
    <a class="card-link" href="#">View all →</a>
  </div>
  <table class="tbl">
    <thead>
      <tr>
        <th>{ID}</th><th>{Person}</th><th>{Type}</th>
        <th class="right">{Amount}</th><th>{Time}</th><th>Actions</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td class="mono">{ID-00000}</td>
        <td>{Person name}</td>
        <td>{Type label}</td>
        <td class="amount">{$n,nnn.nn}</td>
        <td class="mono">{HH:MM}</td>
        <td>
          <div class="action-pair">
            <button class="btn-approve">Approve</button>
            <button class="btn-reject">Reject</button>
          </div>
        </td>
      </tr>
      <!-- 4–5 more rows -->
    </tbody>
  </table>
</div>
```

### Records table card (with filter tabs)

```html
<div class="card">
  <div class="card-head">
    <span class="card-title">{Table title}</span>
    <a class="card-link" href="#">Export CSV →</a>
  </div>
  <div style="display:flex;gap:2px;padding:12px 16px 0;border-bottom:1px solid #f1f5f9;">
    <button style="padding:6px 14px;border:none;background:transparent;border-radius:7px 7px 0 0;font-size:12px;font-weight:600;color:var(--accent-deep);border-bottom:2px solid var(--accent);font-family:inherit;cursor:pointer;">All</button>
    <button style="padding:6px 14px;border:none;background:transparent;border-radius:7px 7px 0 0;font-size:12px;font-weight:500;color:#64748b;border-bottom:2px solid transparent;font-family:inherit;cursor:pointer;">{Sub-type A}</button>
    <button style="padding:6px 14px;border:none;background:transparent;border-radius:7px 7px 0 0;font-size:12px;font-weight:500;color:#64748b;border-bottom:2px solid transparent;font-family:inherit;cursor:pointer;">{Sub-type B}</button>
  </div>
  <table class="tbl">
    <thead>
      <tr>
        <th>{ID}</th><th>{Account / entity}</th><th>{Type}</th>
        <th class="right">{Amount}</th><th>{Time}</th><th>Status</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td class="mono">{ID}</td>
        <td>{name} <span style="color:#94a3b8;font-size:11px;">··{last4}</span></td>
        <td>{type}</td>
        <td class="amount">{±$n,nnn.nn}</td>
        <td class="mono">{HH:MM}</td>
        <td><span class="pill s-positive">{Settled}</span></td>
        <!-- pill variants: .s-positive .s-warning .s-critical .s-neutral .s-muted -->
      </tr>
      <!-- 5–7 more rows -->
    </tbody>
  </table>
</div>
```

### Severity-feed card

```html
<div class="card">
  <div class="card-head">
    <span class="card-title">{Exceptions title}</span>
    <a class="card-link" href="#">View all →</a>
  </div>
  <ul class="risk-list">
    <li class="risk-item">
      <span class="risk-dot red"></span>   <!-- .red / .amber / .emerald -->
      <div class="risk-body">
        <div class="risk-desc">{One-line exception description}</div>
        <div class="risk-meta">
          <span class="risk-ref">{entity ref}</span>
          <span class="risk-time">{HH:MM}</span>
        </div>
        <button class="risk-ack">Acknowledge</button>
      </div>
    </li>
    <!-- 4–5 more items -->
  </ul>
</div>
```

### Bar chart card

```html
<div class="card" style="margin-top:16px;">
  <div class="card-head">
    <span class="card-title">{Chart title}</span>
  </div>
  <div class="chart-wrap">
    <div class="chart-sub">{Unit label — period}</div>
    <div class="bar-chart">
      <!-- One .bar-col per interval; add .peak on the tallest bar -->
      <div class="bar-col">
        <div class="bar" style="height:{px}px"></div>
        <span class="bar-lbl">{label}</span>
      </div>
      <!-- ... -->
    </div>
    <div class="chart-yaxis">
      <span>0</span><span>{mid}</span><span>{max}</span>
    </div>
  </div>
</div>
```

---

## List screen (full-width, search + filter chips)

```html
<!-- Page header above -->

<!-- Toolbar (top of table, rounded top) -->
<div style="background:#fff;border-radius:10px 10px 0 0;border:1px solid #e4e7ec;border-bottom:none;padding:12px 16px;display:flex;align-items:center;gap:12px;flex-wrap:wrap;">
  <div style="position:relative;flex:1;max-width:320px;">
    <svg style="position:absolute;left:10px;top:50%;transform:translateY(-50%);color:#94a3b8;" width="14" height="14" viewBox="0 0 14 14" fill="none">
      <circle cx="6" cy="6" r="4.5" stroke="currentColor" stroke-width="1.4"/>
      <path d="M9.5 9.5l3 3" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/>
    </svg>
    <input type="text" style="width:100%;padding:7px 12px 7px 34px;border:1px solid #e4e7ec;border-radius:7px;background:#f7f8fa;font-size:13px;font-family:inherit;outline:none;" placeholder="Filter by {fields}…">
  </div>
  <!-- Filter chips group -->
  <div style="display:flex;align-items:center;gap:6px;">
    <span style="font-size:11px;color:#94a3b8;font-weight:600;text-transform:uppercase;letter-spacing:.05em;">{Facet}</span>
    <!-- Active chip -->
    <span style="display:inline-flex;align-items:center;gap:4px;padding:4px 10px;border-radius:20px;font-size:12px;font-weight:600;cursor:pointer;border:1px solid var(--accent);background:var(--accent-tint);color:var(--accent-deep);">
      {Value} <span style="font-size:11px;color:var(--accent);">{N}</span>
    </span>
    <!-- Inactive chip -->
    <span style="display:inline-flex;align-items:center;gap:4px;padding:4px 10px;border-radius:20px;font-size:12px;font-weight:500;cursor:pointer;border:1px solid #e4e7ec;background:#fff;color:#64748b;">
      {Value} <span style="font-size:11px;color:#94a3b8;">{N}</span>
    </span>
  </div>
  <span style="margin-left:auto;font-size:12px;color:#94a3b8;">{N} results</span>
</div>

<!-- Table (bottom rounded) -->
<div style="background:#fff;border-radius:0 0 10px 10px;border:1px solid #e4e7ec;overflow:hidden;">
  <table class="tbl">
    <thead>
      <tr>
        <th>{ID}</th><th>{Entity}</th><th>{Type}</th>
        <th class="right">{Numeric}</th><th>{Dimension}</th><th>{Date}</th><th>Status</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td class="mono">{ID}</td>
        <td><div style="display:flex;flex-direction:column;"><span style="font-size:13px;font-weight:500;">{Name}</span><span style="font-size:11px;color:#94a3b8;">{sub}</span></div></td>
        <td>{type}</td>
        <td class="amount">{n}</td>
        <td>{dim}</td>
        <td class="mono">{date}</td>
        <td><span class="pill s-warning">{Pending}</span></td>
      </tr>
      <!-- more rows -->
    </tbody>
  </table>
  <div class="tbl-footer">
    <span>Showing {a}–{b} of {n}</span>
    <div class="pagination">
      <button class="page-btn">‹</button>
      <button class="page-btn active">1</button>
      <button class="page-btn">2</button>
      <button class="page-btn">›</button>
    </div>
  </div>
</div>
```

---

## Record form — fields with inline validation

Rules live ON the field: required mark (`*`), helper text, inline error on invalid.
Submit stays disabled until the form is valid. Never add a separate
rules/validation-status panel.

```html
<form novalidate>

  <div class="card">
    <div class="card-head">
      <div>
        <div style="font-size:13px;font-weight:700;color:#1e293b;">{Section title}</div>
        <div style="font-size:12px;color:#94a3b8;margin-top:1px;">{Section context}</div>
      </div>
    </div>
    <div style="padding:20px 24px;">
      <div class="field-grid">

        <!-- Valid field -->
        <div class="field">
          <label class="field-label" for="f1">{Label} <span class="req">*</span></label>
          <input id="f1" class="control" type="text" placeholder="{hint}">
          <span class="helper">{What the value drives / format constraint}</span>
        </div>

        <!-- Invalid field (add .invalid to .field) -->
        <div class="field invalid">
          <label class="field-label" for="f2">{Label} <span class="req">*</span></label>
          <input id="f2" class="control" type="text" value="{bad value}" aria-invalid="true">
          <span class="error-msg">
            <svg width="12" height="12" viewBox="0 0 12 12" fill="none">
              <circle cx="6" cy="6" r="5.5" stroke="currentColor" stroke-width="1.2"/>
              <path d="M6 3.5v3M6 8.5v.5" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"/>
            </svg>
            {Specific rule that failed — e.g. "Must be greater than zero."}
          </span>
        </div>

        <!-- Required select -->
        <div class="field">
          <label class="field-label" for="f3">{Label} <span class="req">*</span></label>
          <select id="f3" class="control" style="appearance:none;background-image:url(\"data:image/svg+xml,%3Csvg width='12' height='7' viewBox='0 0 12 7' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M1 1l5 5 5-5' stroke='%2394a3b8' stroke-width='1.5' stroke-linecap='round'/%3E%3C/svg%3E\");background-repeat:no-repeat;background-position:right 10px center;padding-right:32px;cursor:pointer;">
            <option value="">Select…</option>
            <option>{Option A}</option>
            <option>{Option B}</option>
          </select>
          <span class="helper">{Constraint on the available options}</span>
        </div>

        <!-- Full-width textarea -->
        <div class="field full">
          <label class="field-label" for="f4">{Label}</label>
          <textarea id="f4" class="control" rows="3" style="resize:vertical;" placeholder="{hint}"></textarea>
          <span class="helper">{Optional guidance}</span>
        </div>

      </div>
    </div>
  </div>

  <!-- Form footer -->
  <div style="background:#fff;border-radius:10px;box-shadow:0 1px 4px rgba(0,0,0,.05);padding:16px 24px;display:flex;align-items:center;justify-content:space-between;">
    <span style="font-size:12px;color:#94a3b8;">Fields marked <span class="req">*</span> are required.</span>
    <div style="display:flex;gap:8px;">
      <button type="button" class="btn-ghost">Cancel</button>
      <button type="submit" class="btn-primary" disabled>{Submit action}</button>
    </div>
  </div>

</form>
```

---

## Record detail — breadcrumb + header + meta grid + sub-panels

```html
<div style="font-size:12px;color:#94a3b8;margin-bottom:16px;">
  <a href="#" style="color:var(--accent);text-decoration:none;">{Parent}</a> ›
  <a href="#" style="color:var(--accent);text-decoration:none;">{List}</a> ›
  <span>{ID}</span>
</div>

<!-- Header band -->
<div style="background:#fff;border-radius:10px;box-shadow:0 1px 4px rgba(0,0,0,.05);padding:20px 24px;margin-bottom:16px;display:flex;align-items:center;justify-content:space-between;">
  <div>
    <div style="display:flex;align-items:center;gap:10px;margin-bottom:4px;">
      <span style="font-size:11px;font-weight:700;color:#64748b;font-variant-numeric:tabular-nums;letter-spacing:.04em;">{ID}</span>
      <span class="pill s-warning">{Status}</span>
    </div>
    <div style="font-size:20px;font-weight:700;color:#1e293b;font-variant-numeric:tabular-nums;">{Title / amount}</div>
    <div style="font-size:13px;color:#64748b;margin-top:4px;">{Context line}</div>
  </div>
  <div style="display:flex;gap:8px;">
    <button class="btn-ghost">{Secondary}</button>
    <button class="btn-primary">Edit</button>
  </div>
</div>

<!-- Meta grid (3 columns) -->
<div class="card">
  <div style="display:grid;grid-template-columns:repeat(3,1fr);">
    <div style="padding:16px 20px;border-right:1px solid #f1f5f9;border-bottom:1px solid #f1f5f9;">
      <div style="font-size:10px;font-weight:600;text-transform:uppercase;letter-spacing:.07em;color:#94a3b8;margin-bottom:4px;">{FIELD}</div>
      <div style="font-size:14px;font-weight:600;color:#1e293b;font-variant-numeric:tabular-nums;">{value}</div>
      <div style="font-size:11px;color:#94a3b8;margin-top:2px;">{sub}</div>
    </div>
    <!-- 5 more meta-cells (3rd and 6th have no border-right; last 3 have no border-bottom) -->
  </div>
</div>

<!-- Two-column sub-panels (7fr 5fr) -->
<div style="display:grid;grid-template-columns:7fr 5fr;gap:16px;align-items:start;">

  <!-- Related records table -->
  <div class="card">
    <div class="card-head"><span class="card-title">{Related records}</span><a class="card-link" href="#">View all →</a></div>
    <table class="tbl">
      <thead>
        <tr><th>{Col A}</th><th>{Col B}</th><th class="right">{Numeric}</th><th>{Date}</th><th>Status</th></tr>
      </thead>
      <tbody>
        <tr>
          <td class="mono">{id}</td><td>{label}</td>
          <td class="amount">{n}</td><td class="mono">{date}</td>
          <td><span class="pill s-positive">{State}</span></td>
        </tr>
        <!-- more rows -->
      </tbody>
    </table>
  </div>

  <!-- Activity feed -->
  <div class="card">
    <div class="card-head"><span class="card-title">Activity</span></div>
    <ul style="list-style:none;padding:8px 0;">
      <li style="display:flex;align-items:flex-start;gap:12px;padding:10px 16px;border-bottom:1px solid #f7f8fa;">
        <div style="width:26px;height:26px;border-radius:50%;background:var(--accent-tint);color:var(--accent);display:flex;align-items:center;justify-content:center;flex-shrink:0;margin-top:1px;">
          <!-- inline SVG glyph 12×12 -->
        </div>
        <div style="flex:1;min-width:0;">
          <div style="font-size:13px;color:#1e293b;font-weight:500;line-height:1.3;">{Event description}</div>
          <div style="font-size:11px;color:#94a3b8;margin-top:3px;">{HH:MM AM · Actor}</div>
        </div>
      </li>
      <!-- more items -->
    </ul>
  </div>

</div>
```
