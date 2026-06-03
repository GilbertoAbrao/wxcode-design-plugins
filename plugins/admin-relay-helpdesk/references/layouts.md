# Relay Admin — layout skeletons

Paste-ready, domain-neutral fragments for the Relay violet/light-mode skin. Each
skeleton is labelled by archetype slot, not by a domain noun. Copy the shell from
`assets/template.html` first (it carries the `:root` tokens + sidebar + topbar +
content slot), then drop the region skeletons below into the `<div class="content">`.
Replace every `{placeholder}` with the real domain's equivalent.

Token recap (full block in `template.html`): page `#f1f5f9`; card `#ffffff`; sidebar
`#ffffff`; `--accent: #7c3aed` / `--accent-light: #8b5cf6` / `--accent-tint: #ede9fe`;
status tokens `--status-green/amber/red` each with `-bg` tint; muted text `#94a3b8`.

---

## KPI tile (repeat ×4 in `.kpi-row`)

```html
<div class="kpi-row">  <!-- display:grid; grid-template-columns:repeat(4,1fr); gap:16px -->
  <div class="card kpi-card">
    <div class="kpi-label">{METRIC NAME}</div>
    <div class="kpi-value-row">
      <div class="kpi-value">{figure}<span>{unit}</span></div>
      <span class="kpi-chip up">↑ {delta}</span>  <!-- .up / .down / .neutral -->
    </div>
    <div class="kpi-sparkline">
      <!-- inline SVG: bar chart, area polyline, arc, or star motif -->
    </div>
  </div>
  <!-- 3 more tiles -->
</div>
```

---

## Priority-tier bar strip

```html
<div class="card tier-card">
  <div class="tier-card-header">
    <div>
      <div class="card-title">{Title}</div>
      <div class="card-subtitle">{scope line}</div>
    </div>
    <a href="#" class="card-link">Details →</a>
  </div>

  <div class="tier-row">
    <div class="tier-label">{T1}</div>
    <div class="tier-row-inner">
      <div class="tier-meta"><span>{descriptor}</span><span>{N} items</span></div>
      <div class="bar-track"><div class="bar-fill amber" style="width:{pct}%"></div></div>
      <!-- bar-fill class: .green / .amber / .red based on compliance -->
    </div>
    <div class="tier-pct amber">{pct}%</div>
  </div>
  <!-- more tier rows -->
</div>
```

---

## Records table card (dashboard footer or list screen)

```html
<div class="card table-card">
  <div class="table-header">
    <div style="display:flex;align-items:baseline;gap:8px;">
      <div class="card-title">{Records title}</div>
      <span class="table-count">{N} records</span>
    </div>
    <a href="#" class="card-link">View all →</a>
  </div>
  <table>
    <thead>
      <tr>
        <th>#</th>
        <th>{Subject}</th>
        <th>{Requester}</th>
        <th>{Tier pill}</th>
        <th>{State pill}</th>
        <th>{Assignee}</th>
        <th>{Age}</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><span class="rec-id">#{ID}</span></td>
        <td>
          <span style="font-weight:500;color:#1e293b">{Subject text}
            <small style="display:block;font-size:11px;color:#94a3b8;font-weight:400">{Category}</small>
          </span>
        </td>
        <td>
          <div style="display:flex;align-items:center;gap:8px;">
            <div class="av av-blue">{XX}</div>{Name}
          </div>
        </td>
        <td><span class="pill pill-t1">{T1}</span></td>  <!-- pill-t1/t2/t3 -->
        <td><span class="pill pill-a">{State A}</span></td> <!-- pill-a/b/c/d -->
        <td>
          <div style="display:flex;align-items:center;gap:7px;">
            <div class="av av-violet">{XX}</div>{Name}
          </div>
        </td>
        <td style="font-size:12px;color:#94a3b8">{elapsed}</td>
      </tr>
    </tbody>
  </table>
  <div class="table-footer">
    <span class="table-footer-info">Showing {a}–{b} of {n}</span>
    <div class="table-footer-pager">
      <div class="pager-btn">‹</div>
      <div class="pager-btn active">1</div>
      <div class="pager-btn">2</div>
      <div class="pager-btn">›</div>
    </div>
  </div>
</div>
```

---

## List toolbar (search + filter chips)

```html
<div style="display:flex;align-items:center;gap:12px;flex-wrap:wrap;">
  <!-- Search -->
  <div style="display:flex;align-items:center;gap:8px;background:#fff;border:1px solid #e2e8f0;border-radius:8px;padding:7px 12px;flex:1;max-width:320px;">
    <svg width="14" height="14" viewBox="0 0 14 14" fill="none"><circle cx="6" cy="6" r="4.25" stroke="#94a3b8" stroke-width="1.25"/><path d="M9.5 9.5L12 12" stroke="#94a3b8" stroke-width="1.25" stroke-linecap="round"/></svg>
    <input type="text" placeholder="Filter by {fields}…" style="background:transparent;border:none;outline:none;font-size:13px;color:#334155;width:100%;font-family:inherit;">
  </div>
  <!-- Filter chips -->
  <span style="font-size:12px;color:#94a3b8;font-weight:500">{Facet}:</span>
  <span class="pill" style="padding:5px 10px;background:var(--accent-tint);border:1px solid var(--accent-light);color:var(--accent);font-weight:700;font-size:12px;cursor:pointer;">
    All <span style="font-size:11px;background:rgba(124,58,237,.15);padding:0 5px;border-radius:10px;margin-left:4px;">{n}</span>
  </span>
  <span style="display:inline-flex;align-items:center;gap:5px;padding:5px 10px;border:1px solid #e2e8f0;border-radius:20px;font-size:12px;font-weight:500;color:#475569;cursor:pointer;background:#fff;">
    {Value A} <span style="font-size:11px;color:inherit;background:rgba(0,0,0,.06);padding:0 5px;border-radius:10px;">{n}</span>
  </span>
</div>
```

---

## Right load panel (260px aside)

```html
<aside class="content-aside">
  <div class="card aside-card" style="height:100%;overflow-y:auto;">
    <div class="aside-header">
      <div class="card-title">{Panel title}</div>
      <div class="card-subtitle" style="margin-top:2px;">{subtitle}</div>
    </div>
    <div class="item-list">
      <div class="item-row">
        <div class="presence-indicator online"></div>  <!-- .online / .away / .offline -->
        <div class="item-av av-violet">{XX}</div>
        <div>
          <div class="item-name">{Name}</div>
          <div class="item-role">{Role}</div>
        </div>
        <div class="item-count">{N}</div>
      </div>
      <!-- more rows -->
    </div>
    <div class="aside-footer"><a href="#">{Manage link} →</a></div>
  </div>
</aside>
```

---

## Record form — fields with inline validation

Rules live ON the field: a required mark (`*`), helper text, and an inline error on
an invalid field. Submit disabled until valid. Never add a separate rules panel.

```html
<form class="form-wrap" novalidate>  <!-- max-width:720px;margin:0 auto;display:flex;flex-direction:column;gap:16px -->

  <div class="card">
    <!-- card-section-title -->
    <div class="card-body" style="padding:20px;display:flex;flex-direction:column;gap:16px;">
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;">

        <!-- valid field -->
        <div style="display:flex;flex-direction:column;gap:6px;">
          <label style="font-size:12.5px;font-weight:600;color:#334155;"
                 for="f1">{Label} <span style="color:var(--accent);font-weight:700;">*</span></label>
          <input id="f1" type="text" value="{value}"
                 style="background:#fff;border:1px solid #e2e8f0;border-radius:7px;padding:9px 12px;color:#1e293b;font-size:13px;font-family:inherit;outline:none;width:100%;">
          <span style="font-size:11.5px;color:#94a3b8;">{helper / format hint}</span>
        </div>

        <!-- invalid field — add red border + error-msg -->
        <div style="display:flex;flex-direction:column;gap:6px;">
          <label style="font-size:12.5px;font-weight:600;color:#334155;"
                 for="f2">{Label} <span style="color:var(--accent);font-weight:700;">*</span></label>
          <input id="f2" type="text" value="{bad value}" aria-invalid="true"
                 style="background:#fff;border:1px solid var(--status-red);border-radius:7px;padding:9px 12px;color:#1e293b;font-size:13px;font-family:inherit;outline:none;width:100%;">
          <span style="font-size:11.5px;color:var(--status-red);display:flex;align-items:center;gap:5px;">
            <svg width="13" height="13" viewBox="0 0 13 13" fill="none"><circle cx="6.5" cy="6.5" r="5.5" stroke="currentColor" stroke-width="1.3"/><path d="M6.5 4v3M6.5 8.5v.5" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"/></svg>
            {Specific rule that failed}
          </span>
        </div>

        <!-- required select spanning full width -->
        <div style="display:flex;flex-direction:column;gap:6px;grid-column:1/-1;">
          <label style="font-size:12.5px;font-weight:600;color:#334155;"
                 for="f3">{Label} <span style="color:var(--accent);font-weight:700;">*</span></label>
          <select id="f3"
                  style="background:#fff;border:1px solid #e2e8f0;border-radius:7px;padding:9px 12px;color:#1e293b;font-size:13px;font-family:inherit;outline:none;width:100%;appearance:none;background-image:url(\"data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='14' height='14' viewBox='0 0 24 24' fill='none' stroke='%2394a3b8' stroke-width='2.5' stroke-linecap='round' stroke-linejoin='round'><polyline points='6 9 12 15 18 9'/></svg>\");background-repeat:no-repeat;background-position:right 12px center;padding-right:34px;">
            <option value="">Select…</option>
            <option value="a">{Option A}</option>
            <option value="b">{Option B}</option>
          </select>
          <span style="font-size:11.5px;color:#94a3b8;">{constraint on options}</span>
        </div>

      </div>
    </div>
  </div>

  <div style="display:flex;align-items:center;justify-content:space-between;gap:12px;padding-top:4px;">
    <span style="font-size:12px;color:#94a3b8;">Fields marked <span style="color:var(--accent);font-weight:700;">*</span> are required.</span>
    <div style="display:flex;gap:8px;">
      <button type="button" class="btn-ghost">Cancel</button>
      <button type="submit" class="btn-primary" disabled>{Submit}</button>
    </div>
  </div>

</form>
```

---

## Record detail — breadcrumb + header + meta grid + related panels

```html
<!-- breadcrumb -->
<div style="display:flex;align-items:center;gap:7px;font-size:12px;color:#94a3b8;">
  <a href="#" style="color:#475569;text-decoration:none;">{Parent}</a>
  <svg width="12" height="12" viewBox="0 0 12 12" fill="none"><path d="M4 2l4 4-4 4" stroke="#cbd5e1" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
  <span>#{ID}</span>
</div>

<!-- header band -->
<div style="display:flex;align-items:flex-start;justify-content:space-between;gap:16px;flex-wrap:wrap;">
  <div>
    <div style="display:flex;align-items:center;gap:10px;margin-bottom:4px;">
      <span style="font-family:'SF Mono','Fira Code',monospace;font-size:15px;color:var(--accent);font-weight:700;">#{ID}</span>
      <span class="pill pill-a">{State A}</span>
      <span class="pill pill-t2">{Tier 2}</span>
    </div>
    <div style="font-size:17px;font-weight:700;color:#1e293b;">{Subject}</div>
    <div style="font-size:13px;color:#94a3b8;margin-top:2px;">{Category} · {Context}</div>
  </div>
  <div style="display:flex;gap:8px;">
    <button class="btn-ghost">{Action}</button>
    <button class="btn-primary">Edit</button>
  </div>
</div>

<!-- meta grid: repeat(3,1fr) -->
<div class="card">
  <div style="display:grid;grid-template-columns:repeat(3,1fr);">
    <div style="padding:16px 20px;border-right:1px solid #f1f5f9;border-bottom:1px solid #f1f5f9;">
      <div style="font-size:10px;font-weight:600;text-transform:uppercase;letter-spacing:.07em;color:#94a3b8;margin-bottom:5px;">{FIELD A}</div>
      <div style="font-size:13px;font-weight:600;color:#1e293b;">{value}</div>
      <div style="font-size:11px;color:#94a3b8;margin-top:2px;">{sub}</div>
    </div>
    <!-- 5 more cells; last 3 have border-bottom:none, right cells have border-right:none -->
  </div>
</div>

<!-- two-col: related sub-table + activity feed — grid-template-columns:7fr 5fr -->
<div style="display:grid;grid-template-columns:7fr 5fr;gap:16px;align-items:start;">
  <div class="card"><!-- sub-table (same table CSS) --></div>
  <div class="card"><!-- activity timeline: dot-col + avatar + body --></div>
</div>
```
