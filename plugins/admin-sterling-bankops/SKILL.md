---
name: admin-sterling-bankops
description: |
  Retail banking back-office operations dashboard archetype:
  sober light-mode, slate-blue (#475569 / #334155) + emerald (#10b981)
  accent palette. Left sidebar with branch/unit switcher and grouped
  nav, topbar with global search + period selector + avatar, 4 KPI
  cards (pending approvals, transactions today, flagged items, SLA met %),
  an approvals queue with Approve / Reject inline actions, a transactions
  table with status pills, a risk/exceptions side panel, and an inline
  SVG throughput chart. Use when the brief involves banking operations,
  back-office workflows, compliance queues, or treasury/clearing rooms.
triggers:
  - "banking operations dashboard"
  - "bank back-office admin"
  - "approvals queue dashboard"
  - "retail banking admin"
  - "transaction operations"
  - "clearing operations"
  - "compliance dashboard"
  - "painel operações bancárias"
  - "银行运营后台"
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
    requires: [pixel-discipline, laws-of-ux]
  example_prompt: "Build me a retail banking back-office operations admin dashboard — left sidebar with branch switcher, topbar with period picker, 4 KPI cards (pending approvals, transactions today, flagged items, SLA met %), an approvals queue with Approve/Reject actions, a transactions table, a risk/exceptions side panel, and a throughput chart."
---

# Sterling Bank Ops Admin Skill

Produce the canonical retail banking back-office operations layout —
the kind of interface used by operations staff at regional and national
banks to manage daily transaction flow, approvals, risk flags, and SLA
compliance.

## Palette contract

All chromatic tokens live on `:root` as CSS custom properties.
No chromatic hex literals appear in rules or inline SVG.

| Token | Value | Use |
|---|---|---|
| `--accent` | `#475569` | Sidebar, nav active, primary buttons |
| `--accent-deep` | `#334155` | Sidebar bg, pressed states |
| `--accent-tint` | `#f1f5f9` | Nav item hover, tile bg tint |
| `--emerald` | `#10b981` | Positive status pills, Approve button |
| `--emerald-tint` | `#d1fae5` | Approved pill bg |
| `--amber` | `#f59e0b` | Warning flags |
| `--amber-tint` | `#fef3c7` | Warning pill bg |
| `--red` | `#ef4444` | Rejected, flagged, SLA-breach |
| `--red-tint` | `#fee2e2` | Flagged pill bg |

Neutrals are hardcoded (never overridden by palette swap):
`#ffffff` cards, `#f7f8fa` page bg, `#e4e7ec` borders,
`#1e293b` primary text, `#64748b` secondary text, `#94a3b8` muted.

## Workflow

1. Read the active DESIGN.md (if present); if a brand color is defined,
   map it onto `--accent` and `--accent-deep`. Otherwise use the
   sterling defaults above.
2. Extract from the brief: institution name, branch list (default:
   "Main Branch · All Units"), operator name for the avatar.
3. Invent plausible banking data: account refs (format `SB-XXXXX`),
   transaction amounts in local currency, staff names, queue depths.
   Never use Lorem Ipsum. All copy must read as real bank-ops content.

## Layout

### Left sidebar (240px, fixed)

- **Top**: bank logo mark (inline SVG shield/column motif) + institution
  name in `--accent-deep`. Below: branch/unit dropdown switcher with
  a chevron icon.
- **Nav sections** (MAIN, OPERATIONS, COMPLIANCE, SETTINGS), each item:
  inline SVG icon (16 px, `currentColor`) + label. Active item gets a
  3px `--accent` left bar and `--accent-tint` background. Hover uses
  `--accent-tint`.
- **Bottom**: operator avatar initials bubble + name + role label +
  gear/settings icon.

### Top bar (56px, white, 1px border-bottom `#e4e7ec`)

Left: page title "Operations Center" + breadcrumb (Home / Operations).
Center: search input (`placeholder="Search accounts, refs, staff…"`).
Right: period selector tabs (Today / Week / Month / Quarter), then
notification bell with amber badge, then avatar.

### KPI cards strip (4 cards, equal width)

Each card: white, 10px radius, subtle shadow. Contents:
- Tiny inline SVG icon (24 px, `currentColor`, colored via icon wrapper).
- Small uppercase label (`font-size:11px; letter-spacing:.06em`).
- Large figure (`font-size:32px; font-weight:700; font-variant-numeric:tabular-nums`).
- Delta chip: green ↑ or amber/red ↓ + percent.
- Tiny label "vs yesterday" or "vs last week".

Cards (in order):
1. **Pending Approvals** — accent icon, figure ~38, amber delta chip.
2. **Transactions Today** — emerald icon, figure ~1,247, green chip.
3. **Flagged Items** — red icon, figure ~12, red delta chip.
4. **SLA Met** — emerald icon, figure ~96.4 %, green chip.

### Main grid (2/3 left + 1/3 right)

**Left column (2/3)**:

*Approvals Queue card* — title "Pending Approvals" + "View all →" link.
Table: Request ID / Requestor / Type / Amount / Submitted / Actions.
5–6 rows. Types: Wire Transfer, Loan Disbursement, Account Override,
Limit Increase, FX Trade. Actions: `<button>Approve</button>` (emerald,
small) + `<button>Reject</button>` (red-tinted, small).

*Transactions card* (below approvals) — title "Today's Transactions" +
filter tabs (All / Credit / Debit / Pending / Flagged).
Table columns: Txn ID / Account / Type / Amount / Time / Status.
6–8 rows with status pills: Settled (emerald), Pending (amber),
Flagged (red), Reversed (muted). Amounts use `tabular-nums`.

**Right column (1/3)**:

*Risk & Exceptions panel* — title "Risk & Exceptions". List of 5–6
exception items, each: severity dot (red/amber/emerald) + short
description + account ref + timestamp. "Acknowledge" text-link per item.

*Throughput chart card* — title "Transaction Throughput" + subtitle
"Settlements per hour — today". Inline SVG bar chart (12 hourly bars,
8 AM–7 PM). Bars colored `--accent`, tallest bar highlighted
`--emerald`. X-axis hour labels, Y-axis count. No external libraries.

## Type rules

- Font stack inline only: `"Inter", system-ui, -apple-system, "Segoe UI", Roboto, sans-serif`.
- No `@import` or `<link>` for fonts.
- `font-variant-numeric: tabular-nums` on all numeric cells and KPI figures.
- Uppercase section labels: `font-size:10px; letter-spacing:.08em; font-weight:600`.

## Output contract

```
<artifact identifier="admin-sterling-bankops" type="text/html" title="Sterling Bank Ops Admin">
<!doctype html>...</artifact>
```

Single `<style>` block, semantic HTML5, all CSS inline in `<style>`,
all SVG inline, no external assets, no CDNs, 10–30 KB target.
