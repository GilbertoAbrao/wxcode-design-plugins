---
name: admin-harbor-banking
description: |
  Digital banking / personal finance operations console: light mode,
  navy-to-blue accent (#1e3a8a → #2563eb) with teal secondary (#0d9488).
  Left sidebar with accounts list and navigation, topbar with global
  search + notification bell + avatar, hero row with an original
  stylized payment-card SVG (fictional "Harbor" brand, masked number
  ····4821) flanked by 3 KPI tiles (current balance, monthly income,
  monthly spending), a spending-by-category inline SVG donut chart,
  a recent-transactions table (date / merchant / category chip /
  amount colored +/−  / status pill), and a quick-transfer payees
  side panel. Use whenever the brief mentions banking, fintech,
  personal finance, account management, or payment dashboards.
triggers:
  - "banking dashboard"
  - "fintech admin"
  - "personal finance console"
  - "account overview"
  - "payment dashboard"
  - "bank operations"
  - "harbor banking"
  - "painel bancário"
  - "金融管理后台"
od:
  mode: prototype
  surface: web
  scenario: operations
  preview:
    type: html
    entry: index.html
  design_system:
    requires: true
    sections: [color, typography, layout, components]
  craft:
    requires: [pixel-discipline, laws-of-ux]
  example_prompt: "Build me a digital banking admin console — accounts sidebar, topbar, a stylized payment card, 3 KPI tiles (balance / income / spending), a spending-by-category chart, recent transactions table, and a quick-transfer payees panel."
---

# Harbor Banking Admin Skill

Produce the canonical personal-finance operations console: trustworthy
light mode, navy-blue primary, teal secondary, white-card surfaces on a
slate-tinted canvas.

## Workflow

1. Read the active DESIGN.md (if present); otherwise use navy (#1e3a8a)
   and blue (#2563eb) as the primary gradient, teal (#0d9488) as the
   secondary accent, and #f6f8fb as the page canvas.

2. Extract from the brief: account holder name, account types
   (checking / savings / credit / investment), currency, KPI figures
   (balance, monthly income, monthly spending), merchant/category names
   for transactions, payee names for quick transfer.

3. Layout:

   - **Left sidebar (260px)**: Harbor wordmark + shield icon at top.
     Account list section — each entry has a color-coded dot, account
     label, masked number, and balance. Below: grouped nav (OVERVIEW,
     PAYMENTS, CARDS, SETTINGS) with icon + label; active item has a
     navy left-bar and tinted background. Bottom: user avatar block.

   - **Top bar (60px)**: page title on the left, search bar in the
     center (slate border, magnifier icon), then notification bell
     (badge with unread count), then avatar + name + caret.

   - **Hero row (3 columns)**:
     - LEFT (1.4fr): Payment-card SVG — original design, navy→blue
       linear gradient, abstract circuit-trace chip SVG, fictional
       "Harbor" logotype in white, masked number ····4821, cardholder
       name, expiry. No real card-network logos.
     - CENTER-RIGHT (3 tiles at 1fr each): Balance (current total),
       Income (this month, green delta), Spending (this month, red
       delta). Each tile: white card, 10px radius, small uppercase
       label, large tabular figure, trend chip.

   - **Main grid (2/3 + 1/3)**:
     - LEFT (2/3): Spending by category — card with title + period
       selector tabs, inline SVG donut chart with 5–6 category
       segments (each segment color uses a CSS var), legend list with
       label + amount + percentage bar. Below: "Recent Transactions"
       table card — columns: date, merchant (name + category icon),
       category chip, amount (green for credit, red for debit), status
       pill (Completed / Pending / Failed).
     - RIGHT (1/3): Quick Transfer panel — "Transfer to" heading,
       payees row (avatar circle + first name, horizontally scrollable,
       active ring in teal), amount input with currency symbol, note
       field, teal "Send Money" CTA button. Below: "Scheduled
       Payments" mini list — 3 upcoming entries with merchant icon,
       name, date, amount.

4. Typography: system font stack only — "Inter", system-ui,
   -apple-system, "Segoe UI", Roboto, sans-serif. Tabular-nums class
   on all figures. Tiny uppercase labels (0.65rem, 0.08em
   letter-spacing) for tile and section titles. Navy/blue for active
   states and links; teal for CTAs and positive values; #ef4444 for
   debits and negative deltas.

5. Palette contract: every chromatic color is a :root CSS custom
   property (--c-navy, --c-blue, --c-teal, --c-green, --c-red,
   --c-surface, --c-border, --c-text-primary, --c-text-muted, etc.).
   SVG fill and stroke chromatic colors use var(--token) or
   currentColor; only neutral grays may be hardcoded.

6. One inline `<style>`, semantic HTML, no external assets, no CDNs,
   no lorem ipsum. Target 10–30 KB.

## Output contract

```
<artifact identifier="admin-harbor-banking" type="text/html" title="Harbor Banking Admin">
<!doctype html>...</artifact>
```
