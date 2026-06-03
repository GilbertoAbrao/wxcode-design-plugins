# Admin Console — Paste-ready Layout Skeletons

Domain-neutral HTML fragments for each archetype region.
Copy the relevant skeleton into `assets/template.html` or a new screen file.
Replace `[PLACEHOLDER]` labels with domain content.

---

## Navbar (60px, sticky)

```html
<nav class="navbar" style="position:sticky;top:0;z-index:50;height:60px;background:var(--card);border-bottom:1px solid var(--border);display:flex;align-items:center;padding:0 20px;gap:16px;">
  <a href="#" style="display:flex;align-items:center;gap:8px;text-decoration:none;color:var(--text-primary);font-size:18px;font-weight:700;">
    <div style="width:32px;height:32px;border-radius:var(--radius);background:var(--accent-gradient);display:flex;align-items:center;justify-content:center;">
      <!-- brand SVG icon here -->
      <svg width="18" height="18" viewBox="0 0 18 18" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="9" r="7"/><path d="M9 5v4l3 2"/></svg>
    </div>
    [App Name]
  </a>
  <!-- search pill (optional) -->
  <div style="position:relative;max-width:280px;flex:1;">
    <svg style="position:absolute;left:11px;top:50%;transform:translateY(-50%);color:var(--text-muted);width:14px;height:14px;pointer-events:none;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/></svg>
    <input type="text" placeholder="Search…" style="width:100%;background:var(--canvas);border:1px solid var(--border);border-radius:20px;padding:6px 14px 6px 36px;color:var(--text-primary);font-family:inherit;font-size:13px;outline:none;">
  </div>
  <div style="flex:1;"></div>
  <!-- notification icon -->
  <button style="position:relative;width:36px;height:36px;border-radius:50%;border:none;background:transparent;color:var(--text-muted);cursor:pointer;display:flex;align-items:center;justify-content:center;">
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"/><path d="M13.73 21a2 2 0 0 1-3.46 0"/></svg>
    <!-- badge dot: <span style="position:absolute;top:4px;right:4px;width:8px;height:8px;border-radius:50%;background:var(--state-error);border:2px solid var(--card);"></span> -->
  </button>
  <!-- avatar -->
  <div style="width:36px;height:36px;border-radius:50%;background:var(--accent-gradient);display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:600;color:#fff;cursor:pointer;margin-left:4px;">[XX]</div>
</nav>
```

---

## Left icon sidebar (240px)

```html
<aside style="width:240px;min-height:calc(100vh - 60px);background:var(--card);border-right:1px solid var(--border);display:flex;flex-direction:column;padding:20px 0;flex-shrink:0;">
  <div style="padding:0 20px 8px;font-size:10px;font-weight:600;text-transform:uppercase;letter-spacing:.8px;color:var(--text-muted);">Main Menu</div>

  <!-- Active nav item -->
  <a href="#" style="display:flex;align-items:center;gap:12px;padding:10px 20px;text-decoration:none;color:#fff;background:var(--accent-gradient);">
    <!-- icon SVG --> [Icon] [Nav Label]
  </a>

  <!-- Default nav item -->
  <a href="#" style="display:flex;align-items:center;gap:12px;padding:10px 20px;text-decoration:none;color:var(--text-muted);transition:background .15s,color .15s;">
    <!-- icon SVG --> [Icon] [Nav Label]
    <!-- optional badge: <span style="margin-left:auto;font-size:10px;font-weight:600;padding:1px 6px;border-radius:10px;background:var(--state-error);color:#fff;">3</span> -->
  </a>

  <div style="flex:1;"></div>
  <a href="#" style="display:flex;align-items:center;gap:12px;padding:10px 20px;text-decoration:none;color:var(--text-muted);">
    <!-- settings icon --> Settings
  </a>

  <!-- Profile tile -->
  <div style="display:flex;align-items:center;gap:12px;padding:16px 20px;border-top:1px solid var(--border);">
    <div style="width:36px;height:36px;border-radius:50%;background:var(--accent-gradient);display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:600;color:#fff;flex-shrink:0;">[XX]</div>
    <div>
      <div style="font-size:13px;font-weight:500;color:var(--text-primary);">[User Name]</div>
      <div style="font-size:11px;color:var(--text-muted);">[Role]</div>
    </div>
  </div>
</aside>
```

---

## KPI tile (one of four in a grid)

```html
<!-- Wrap 4 of these in: <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:16px;"> -->
<div style="background:var(--card);border:1px solid var(--border);border-radius:var(--radius);padding:20px;display:flex;align-items:center;gap:16px;box-shadow:0 2px 8px rgba(0,0,0,.25);">
  <!-- Icon chip: swap class color (violet/green/amber/red) -->
  <div style="width:48px;height:48px;border-radius:var(--radius);background:var(--accent-dim);color:var(--accent);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
    <!-- metric icon SVG (24×24) -->
  </div>
  <div style="flex:1;">
    <div style="font-size:28px;font-weight:700;font-variant-numeric:tabular-nums;color:var(--text-primary);line-height:1;">[0,000]</div>
    <div style="font-size:12px;color:var(--text-muted);margin-top:4px;text-transform:uppercase;letter-spacing:.5px;">[Metric Label]</div>
    <!-- Delta chip: .up or .down -->
    <div style="display:inline-flex;align-items:center;gap:3px;font-size:11px;font-weight:500;padding:2px 6px;border-radius:10px;margin-top:6px;color:var(--delta-up);background:var(--state-active-dim);">▲ [+X%] [context]</div>
  </div>
</div>
```

---

## 2-column grid (chart + status list)

```html
<div style="display:grid;grid-template-columns:7fr 5fr;gap:16px;">

  <!-- LEFT: chart panel -->
  <div style="background:var(--card);border:1px solid var(--border);border-radius:var(--radius);box-shadow:0 2px 8px rgba(0,0,0,.25);">
    <div style="padding:16px 20px;border-bottom:1px solid var(--border);display:flex;align-items:center;justify-content:space-between;">
      <span style="font-size:14px;font-weight:500;color:var(--text-primary);">[Chart Title]</span>
      <!-- period tabs (24h / 7d / 30d) -->
    </div>
    <div style="padding:20px;">
      <!-- inline SVG chart here (viewBox="0 0 600 180") -->
      <!-- Legend row below chart -->
    </div>
  </div>

  <!-- RIGHT: status list panel -->
  <div style="background:var(--card);border:1px solid var(--border);border-radius:var(--radius);box-shadow:0 2px 8px rgba(0,0,0,.25);">
    <div style="padding:16px 20px;border-bottom:1px solid var(--border);">
      <span style="font-size:14px;font-weight:500;color:var(--text-primary);">[List Title]</span>
    </div>
    <div style="padding:0 20px;">
      <!-- status rows -->
    </div>
    <div style="padding:12px 20px;border-top:1px solid var(--border);">
      <a href="#" style="font-size:12px;color:var(--accent);text-decoration:none;">View all →</a>
    </div>
  </div>

</div>
```

---

## Status list row

```html
<!-- Repeat inside a flex-direction:column container with border-bottom per row -->
<div style="display:flex;align-items:center;gap:12px;padding:12px 0;border-bottom:1px solid var(--border);">
  <!-- icon chip (swap color class: green/amber/red/info) -->
  <div style="width:36px;height:36px;border-radius:var(--radius);background:var(--state-active-dim);color:var(--state-active);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
    <!-- 16×16 SVG icon -->
  </div>
  <div style="flex:1;">
    <div style="font-size:13px;font-weight:500;color:var(--text-primary);">[Entity Label]</div>
    <div style="font-size:11px;color:var(--text-muted);margin-top:1px;">[Sub-label / detail]</div>
  </div>
  <!-- status pill -->
  <span style="display:inline-flex;align-items:center;padding:3px 9px;border-radius:var(--pill-radius);font-size:11px;font-weight:500;background:var(--state-active-dim);color:var(--state-active);">Active</span>
  <!-- timestamp -->
  <span style="font-size:11px;color:var(--text-muted);white-space:nowrap;">2m ago</span>
</div>
```

---

## Data table row (inside `<tbody>`)

```html
<!-- thead row -->
<tr>
  <th style="font-size:11px;font-weight:600;text-transform:uppercase;letter-spacing:.6px;color:var(--text-muted);padding:10px 16px;text-align:left;border-bottom:1px solid var(--border);">ID</th>
  <th style="...">Name</th>
  <th style="...">Category</th>
  <th style="...;text-align:right;">Qty</th>
  <th style="...">Status</th>
  <th style="...">Updated</th>
  <th></th>
</tr>

<!-- tbody row -->
<tr style="border-bottom:1px solid var(--border);transition:background .12s;">
  <td style="padding:12px 16px;font-family:'Courier New',monospace;font-size:12px;color:var(--text-muted);">#R-0001</td>
  <td style="padding:12px 16px;">
    <div style="font-size:13px;font-weight:500;color:var(--text-primary);">[Record Name]</div>
    <div style="font-size:11px;color:var(--text-muted);margin-top:2px;">[Sub-label]</div>
  </td>
  <td style="padding:12px 16px;color:var(--text-secondary);">[Category]</td>
  <td style="padding:12px 16px;text-align:right;font-variant-numeric:tabular-nums;">0</td>
  <td style="padding:12px 16px;">
    <!-- pill: swap color -->
    <span style="display:inline-flex;align-items:center;padding:3px 9px;border-radius:var(--pill-radius);font-size:11px;font-weight:500;background:var(--state-active-dim);color:var(--state-active);">Active</span>
  </td>
  <td style="padding:12px 16px;color:var(--text-muted);font-size:12px;">Today</td>
  <td style="padding:12px 16px;"><button style="background:transparent;border:none;color:var(--text-muted);cursor:pointer;padding:4px 8px;border-radius:var(--radius);">···</button></td>
</tr>
```

---

## Form section with inline-validated field

```html
<div style="background:var(--card);border:1px solid var(--border);border-radius:var(--radius);box-shadow:0 2px 8px rgba(0,0,0,.25);">
  <div style="padding:16px 20px;border-bottom:1px solid var(--border);">
    <div style="font-size:14px;font-weight:500;color:var(--text-primary);">[Section Title]</div>
    <div style="font-size:12px;color:var(--text-muted);margin-top:2px;">[Section description]</div>
  </div>
  <div style="padding:20px;display:flex;flex-direction:column;gap:16px;">

    <!-- Required field — valid state -->
    <div style="display:flex;flex-direction:column;gap:6px;">
      <label style="font-size:13px;font-weight:500;color:var(--text-secondary);" for="f1">
        [Field Label] <span style="color:var(--state-error);margin-left:2px;" aria-hidden="true">*</span>
      </label>
      <input id="f1" type="text" placeholder="[Placeholder]"
        style="width:100%;background:var(--canvas);border:1px solid var(--border);border-radius:var(--radius);padding:9px 12px;color:var(--text-primary);font-family:inherit;font-size:13px;outline:none;">
      <span style="font-size:11px;color:var(--text-muted);">[Helper text — constraints, format, etc.]</span>
    </div>

    <!-- Required field — error state -->
    <div style="display:flex;flex-direction:column;gap:6px;">
      <label style="font-size:13px;font-weight:500;color:var(--text-secondary);" for="f2">
        [Field Label] <span style="color:var(--state-error);margin-left:2px;" aria-hidden="true">*</span>
      </label>
      <input id="f2" type="text" value="[invalid input]"
        style="width:100%;background:rgba(239,68,68,.04);border:1px solid var(--state-error);border-radius:var(--radius);padding:9px 12px;color:var(--text-primary);font-family:inherit;font-size:13px;outline:none;">
      <span style="font-size:11px;color:var(--state-error);display:flex;align-items:center;gap:4px;">
        <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
        [Inline error message — specific, actionable]
      </span>
    </div>

  </div>
  <!-- Form actions footer -->
  <div style="padding:16px 20px;border-top:1px solid var(--border);display:flex;justify-content:flex-end;gap:10px;">
    <button style="padding:9px 20px;border-radius:var(--radius);border:1px solid var(--border);background:transparent;color:var(--text-secondary);font-family:inherit;font-size:13px;cursor:pointer;">Cancel</button>
    <button style="padding:9px 20px;border-radius:var(--radius);border:none;background:var(--accent-gradient);color:#fff;font-family:inherit;font-size:13px;font-weight:500;cursor:pointer;" disabled>Save [Entity]</button>
  </div>
</div>
```

---

## Auth card (centered, no sidebar)

```html
<!-- body: display:flex;align-items:center;justify-content:center;min-height:100vh -->
<div style="width:100%;max-width:420px;background:var(--card);border:1px solid var(--border);border-radius:var(--radius);box-shadow:0 8px 32px rgba(0,0,0,.35);padding:40px;">
  <!-- logo + app name centered -->
  <div style="display:flex;align-items:center;gap:10px;justify-content:center;margin-bottom:28px;">
    <div style="width:40px;height:40px;border-radius:var(--radius);background:var(--accent-gradient);display:flex;align-items:center;justify-content:center;"><!-- icon --></div>
    <span style="font-size:22px;font-weight:700;">[App Name]</span>
  </div>
  <div style="font-size:20px;font-weight:500;text-align:center;margin-bottom:6px;">[Auth Title]</div>
  <div style="font-size:13px;color:var(--text-muted);text-align:center;margin-bottom:24px;">[Auth subtitle]</div>
  <!-- fields -->
  <!-- gradient CTA -->
  <button style="width:100%;padding:11px;border-radius:var(--radius);border:none;background:var(--accent-gradient);color:#fff;font-family:inherit;font-size:14px;font-weight:500;cursor:pointer;">[Sign In / Create Account]</button>
  <div style="text-align:center;margin-top:20px;font-size:13px;color:var(--text-muted);">
    [Alternate action text] <a href="#" style="color:var(--accent);text-decoration:none;">[Link]</a>
  </div>
</div>
```

---

## Error page (full-page centered)

```html
<!-- body: display:flex;flex-direction:column;align-items:center;justify-content:center;min-height:100vh -->
<div style="max-width:520px;display:flex;flex-direction:column;align-items:center;gap:24px;text-align:center;">
  <!-- SVG geometric illustration (~280×200) -->
  <!-- error code -->
  <div style="font-size:80px;font-weight:700;line-height:1;background:var(--accent-gradient);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;">[4xx / 5xx]</div>
  <div style="font-size:24px;font-weight:500;">[Error Title]</div>
  <div style="font-size:14px;color:var(--text-muted);max-width:380px;line-height:1.7;">[Short description]</div>
  <!-- primary CTA -->
  <a href="#" style="padding:10px 24px;border-radius:var(--radius);border:none;background:var(--accent-gradient);color:#fff;font-family:inherit;font-size:14px;font-weight:500;cursor:pointer;text-decoration:none;">[Go Home / Retry]</a>
</div>
```

---

## Period-picker tab strip

```html
<div style="display:flex;gap:4px;">
  <button style="font-size:11px;padding:3px 10px;border-radius:10px;cursor:pointer;border:1px solid transparent;color:var(--text-muted);background:transparent;font-family:inherit;">24h</button>
  <button style="font-size:11px;padding:3px 10px;border-radius:10px;cursor:pointer;border:1px solid var(--accent);color:var(--accent);background:var(--accent-dim);font-family:inherit;">7d</button>
  <button style="font-size:11px;padding:3px 10px;border-radius:10px;cursor:pointer;border:1px solid transparent;color:var(--text-muted);background:transparent;font-family:inherit;">30d</button>
</div>
```

---

## Pager

```html
<div style="display:flex;gap:4px;">
  <button style="width:28px;height:28px;border-radius:var(--radius);border:1px solid var(--border);background:transparent;color:var(--text-muted);font-size:12px;cursor:pointer;">‹</button>
  <button style="width:28px;height:28px;border-radius:var(--radius);border:none;background:var(--accent-gradient);color:#fff;font-size:12px;cursor:pointer;">1</button>
  <button style="width:28px;height:28px;border-radius:var(--radius);border:1px solid var(--border);background:transparent;color:var(--text-muted);font-size:12px;cursor:pointer;">2</button>
  <button style="width:28px;height:28px;border-radius:var(--radius);border:1px solid var(--border);background:transparent;color:var(--text-muted);font-size:12px;cursor:pointer;">›</button>
</div>
```
