---
name: admin-sneat
description: |
  Clean light-mode SaaS admin aesthetic: #f5f5f9 page canvas, pure-white card
  surfaces, indigo accent (#696cff) with a soft violet glow, Public Sans type at
  15px base, 6px card radius, multi-level box shadows, and muted #646e78 body
  text. Archetype = sticky top navbar (entity label + search + icon actions +
  avatar) + left sidebar (collapsible nav groups with icon + label) + 4-column
  KPI stat tiles + mixed-width grid of a line chart, a donut chart, and a
  recent-records mini-panel + full-width paginated records table with colored
  status pills, plus matching list, form, settings, auth, error, email, and
  calendar screens. Built for polished SaaS dashboards that feel approachable
  without sacrificing information density.
triggers:
  - "clean light-mode admin"
  - "indigo accent SaaS dashboard"
  - "soft shadow admin panel"
  - "white card admin layout"
  - "sidebar nav light admin"
  - "polished SaaS admin aesthetic"
  - "violet indigo admin dashboard"
  - "admin painel claro com índigo"
  - "dashboard SaaS limpo com cartões brancos"
  - "painel lateral admin claro"
example_prompt: "Apply this clean light-mode SaaS admin aesthetic to my domain"
od:
  mode: prototype
  surface: web
  scenario: operations
  preview:
    type: html
    entry: example.html
  design_system:
    requires: true
    sections: [color, typography, layout, components]
  craft:
    requires: [typographic-rhythm, laws-of-ux]
---

# Indigo SaaS Admin — Visual Archetype

This plugin contributes a **look** (clean light-mode SaaS admin, indigo accent, white cards, soft shadows) and a **structure** (sticky top navbar + left sidebar nav groups + KPI stat tiles + chart/panel grid + records table, plus list, form, settings, auth, error, email, and calendar screens). It does **not** contribute a domain — the subject matter comes from the Knowledge Base and the user's prompt. Treat the example below as illustration only.

## Visual language        (AUTHORITATIVE)

The non-negotiable look. Every chromatic value is declared as a `:root` CSS custom property; only true neutrals are hardcoded.

- **Canvas / surfaces:** page canvas `#f5f5f9`; card/panel surface `#ffffff`; sidebar bg `#fff`; table row hover `#f8f8fb`.
- **Custom properties:**
  ```css
  :root {
    --accent:        #696cff;
    --accent-hover:  #5a5dd6;
    --accent-dim:    rgba(105,108,255,.12);
    --accent-text:   #696cff;
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
  ```
- **Status pill colors:** success green `#71dd37` / warning amber `#ffab00` / danger red `#ff3e1d` / info cyan `#03c3ec` / secondary muted `#8592a3`; each pill uses a tinted background at ~12% alpha with the token color as text.
- **Typography:** `"Public Sans", system-ui, -apple-system, "Segoe UI", Roboto, sans-serif`. Base 15px / line-height 1.5. Headings `font-weight: 700`. Body copy `font-weight: 400`, color `var(--text-body)`. Nav labels `font-weight: 500`. Tabular numerics: `font-variant-numeric: tabular-nums`. Card titles 14px uppercase `letter-spacing: .05em` muted. Micro-labels 12px muted.
- **Density & radius:** card `padding: 24px`; table row `padding: 12px 16px`; sidebar `width: 260px`; navbar `height: 60px`; `border-radius: var(--radius-card)` on cards, `var(--radius-pill)` on pills, `var(--radius-input)` on inputs.
- **Borders & shadows:** `border: 1px solid var(--border)` separates all cards; `box-shadow: var(--shadow-sm)` lifts cards off canvas; `box-shadow: var(--shadow-md)` on dropdown and modal overlays. No inner hairlines on table rows — only a `1px solid var(--border)` bottom per row.
- **Motion:** `0.18s ease` on hover/focus color transitions; `0.22s ease` on sidebar collapse; `0.12s ease` on pill/button scale micro-interactions. Never bouncy; no spring physics.

## Layout archetype       (AUTHORITATIVE, domain-neutral)

Regions and component patterns described by shape and behavior — not meaning.

- **Top navbar** (60px, `var(--surface)`, `1px solid var(--border)` bottom, sticky, `z-index 100`): app wordmark / hamburger toggle on the left → flexible spacer → **search input** (rounded, 280px, icon prefix) → notification icon button → avatar button (40px circle) with a dropdown menu. Full width of the viewport.
- **Left sidebar** (260px, `var(--surface)`, `1px solid var(--border)` right, `min-height: 100vh`, scrollable): logo zone (60px) → scrollable **nav groups** (collapsible, with section label dividers, each item = 20px icon + label + optional badge, 40px row height, `var(--accent-dim)` background + `var(--accent)` text on active item). Collapses to icon-only rail at mobile breakpoint.
- **Main content** (`background: var(--canvas)`, left-padded by sidebar width, top-padded by navbar height, `padding: 24px`, vertical scroll): a **breadcrumb / page header** row (title 20px 700 + subtitle on the left; primary button + secondary ghost on the right), then the region stack below.
- **KPI stat tile row** (4 equal columns, `gap: 24px`): each tile = a white card (`var(--shadow-sm)`) with a colored icon chip (40px, `var(--accent-dim)` background, `var(--accent)` icon), a big numeric figure (28px 700, `var(--text-primary)`), a label (13px muted), and a delta badge (pill, green/red for up/down with `▲`/`▼` prefix).
- **Mixed-width grid (3-column, `gap: 24px`):** first row spans 2 cols (line/area chart card with time-axis + legend + smooth SVG polyline) + 1 col (donut chart + legend items). Second row spans 1 col (mini stat cards or quick-action list) + 2 cols (recent-records mini-table with avatar + name + status pill + single value column).
- **Full-width records table card:** white card with a header row (title + search input + filter dropdown + `Add` primary button), sticky thead, rows of `[checkbox] [ID mono] [avatar + 2-line name/sub] [status pill] [numeric columns] [row action icon]`, and a footer with result count + `<Prev  1  2  3  Next>` pager.
- **Records list screen:** standalone full-page version of the records-table archetype — filter chips row + search + column picker, the dense table, pager.
- **Record form screen:** white card with a `form` element split into **labeled sections** (each section = a card or card partition with a section heading); fields rendered with label above + input/select/textarea + inline helper text below; required mark (`*` in `var(--accent)`) beside the label; inline error message in `var(--state-danger)` replacing helper text on invalid. Primary submit button right-aligned, ghost Cancel left. No rules/checklist/validation-status panel.
- **Settings screen:** sidebar sub-nav (vertical pill links for profile, security, notifications, billing, etc.) + main content area showing the active tab as sectioned form cards with inline-validated fields.
- **Auth screens (login/register):** centered single-column card (`max-width: 420px`), page background `var(--canvas)`, logo above card, card has a heading + subtitle + inline-validated fields + primary submit + OAuth divider + footer link. No sidebar/navbar.
- **Error / empty screen:** centered column, large SVG illustration, heading, short message, primary CTA button. No sidebar/navbar chrome.
- **Email screen:** 3-column layout: narrow folder-list sidebar (200px) + message-list panel (320px) + message-detail pane (fills remainder); toolbar row above message list.
- **Calendar screen:** full-height 2-column (sidebar with mini-calendar widget + event-type filters + add button; main panel = month/week grid with colored event chips).

## Applying to a domain   (the contract)

The domain comes from the Knowledge Base + the user's prompt. Extract THIS domain's equivalent of the archetype slots — its primary entities, key metrics, status states, record list/columns, form fields and their rules, and detail fields — and map them onto the archetype above. If no KB/domain is supplied (standalone), use the Example instantiation below.

Do NOT invent a "rules" / "checklist" / "validation-status" panel; domain rules become inline field validation. Do NOT render build/implementation notes or designer controls — every screen is a finished product screen.

## Example instantiation (illustrative only — NOT the domain)

> One concrete example so standalone Open Design has a complete brief. In WXCode this is IGNORED — replace every label with the real domain's equivalent (entities, metrics, states, columns, fields) drawn from the KB + prompt.

```
Domain (illustrative): a subscription analytics platform.

Top navbar      → app title "Subscriptions" + search "Search reports…" + avatar "AS".
Sidebar groups  → Overview, Subscribers, Plans, Invoices, Reports, Settings.

KPI tiles (4):
  • Active Subscribers  12,480  ▲ 4.2%  vs last month
  • Monthly Revenue     $94,320  ▲ 8.7%  vs last month
  • Churn Rate          3.1%   ▼ 0.9%  vs last month (red delta)
  • Avg Revenue/User    $7.56   ▲ 1.3%  vs last month

Mixed-width grid:
  Line chart (2 cols)   → "Revenue Over Time" — 12-month area chart, two series
                           (New MRR / Expansion MRR), smooth polyline + gradient fill.
  Donut chart (1 col)   → "Plan Distribution" — Pro 48%, Starter 33%, Free 19%.
  Recent-records panel  → "New Subscribers" mini-table: avatar + Name + Plan + Revenue.

Full-width table        → "Subscribers": ID / Name / Plan / Status pill / Next
                           Billing / MRR / Actions.
  Status pills          → Active (green) / Trialing (info) / Cancelled (danger) /
                           Paused (warning).

List screen             → all subscribers, search + status filter chip + plan filter chip,
                           paginated.

Form screen             → "Add Subscriber": Email (required), Full Name (required),
                           Plan (required select), Trial Days (helper: "0 = immediate
                           billing"), Coupon Code (optional, validates format), Card
                           Token (required, PCI field). Inline errors: "Invalid email
                           format", "Plan is required". Submit "Create Subscriber"
                           disabled until valid.

Settings screen         → tabs: Profile (name, email, password section), Notifications
                           (toggle list), Billing (payment method card + invoice list),
                           API Keys (secret key + regenerate button).

Login screen            → card: "Welcome back 👋", email + password fields, "Remember
                           me" checkbox, "Forgot password?" link, "Sign In" primary,
                           OAuth divider, "Sign Up" footer link.

Register screen         → card: "Adventure starts here 🚀", name + email + password
                           (with strength meter helper), terms checkbox (required),
                           "Sign Up" primary, "Sign In" footer link.

404 screen              → SVG illustration of a broken page; "Page Not Found" heading;
                           "Oops! 😖 The requested URL was not found." body; "Back to
                           Home" button.

Email screen            → folders: Inbox (24), Sent, Drafts, Trash; message list with
                           sender avatar + subject + preview + date; detail pane showing
                           full message, reply toolbar.

Calendar screen         → mini-calendar widget; event types: Meeting (indigo), Deadline
                           (red), Release (green), Personal (orange); month grid with
                           colored event chips; "Add Event" button.
```

## Workflow

1. Read the active DESIGN.md (if present); otherwise use this plugin's Visual language tokens.
2. Extract THIS domain's equivalent of the archetype slots — primary entities, key metrics, status states, record columns, form fields + rules, detail fields — from the KB + prompt. Standalone: use the Example instantiation above.
3. Build each screen in the Visual language + Layout archetype above, imitating the example set in `assets/` (dashboard, dashboard-crm, list, form, settings, login, register, error, email, calendar) and the `assets/template.html` seed — with fresh content for the real domain, NOT the example labels.
4. Express domain rules as INLINE field validation (required marks, helper text, inline errors, disabled-until-valid submit). Never render rules/checklist/validation-status/build-note panels or designer/demo controls.
5. One inline `<style>`, semantic HTML5, `tabular-nums` on figures, no external assets, no CDNs — self-contained.

## Output contract

```
<artifact identifier="admin-sneat" type="text/html" title="Admin Console">
<!doctype html>...</artifact>
```
