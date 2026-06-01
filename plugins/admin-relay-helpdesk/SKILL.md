---
name: admin-relay-helpdesk
description: |
  Friendly violet-accent helpdesk operations dashboard: light mode with
  left inbox/views sidebar, search + assignee-filter topbar, 4 KPI cards
  (open tickets, avg first response, SLA compliance, CSAT), a compact
  SLA-by-priority bar set (P1/P2/P3), a full-width ticket queue table with
  priority and status pills, and a right-side team load panel showing agent
  workloads with presence indicators. Use when the brief mentions support,
  helpdesk, ticketing, SLA, or CSAT and asks for an ops-style admin layout.
triggers:
  - "helpdesk dashboard"
  - "support admin"
  - "ticket queue"
  - "sla dashboard"
  - "csat dashboard"
  - "customer support admin"
  - "painel de suporte"
  - "工单管理后台"
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
  example_prompt: "Build me a helpdesk admin dashboard — left inbox sidebar, topbar with search and assignee filter, 4 KPI cards (open tickets, first response time, SLA compliance, CSAT), SLA priority bars, ticket queue table with priority and status pills, and a team load panel."
---

# Relay Helpdesk Admin Skill

Produce a friendly, well-structured helpdesk operations dashboard with violet
accent, status-semantic colors, and clear SLA visibility — the shape a support
team lead wants to see at a glance.

## Workflow

1. Read the active DESIGN.md (if present); otherwise use violet (#7c3aed / #8b5cf6)
   on a near-white slate canvas (#f8fafc). Status palette: green (#16a34a)
   resolved, amber (#d97706) pending/at-risk, red (#dc2626) breached/urgent.

2. Extract from the brief: product/team name, ticket volume range, SLA tiers
   (P1/P2/P3 or equivalent), agent roster size, and CSAT target.

3. Layout — three-column shell: sidebar | main | right panel.

   **Left sidebar (240px)**
   - Logo mark + product name at top (violet icon, slate text).
   - Section: INBOX — items: All Open (with badge count), Unassigned,
     My Tickets, Mentions. Active item: violet left-bar + tinted bg.
   - Section: VIEWS — items: By Priority, By SLA Breach, Awaiting Reply,
     Resolved Today.
   - Section: SETTINGS — items: Queues, Automations, SLA Policies.
   - Slim bottom row: current-user avatar + name + presence dot.

   **Topbar (56px, white, 1px bottom border)**
   - Left: page title "Ticket Queue" + breadcrumb (Support / Ticket Queue).
   - Center: search input with magnifier icon ("Search tickets…").
   - Right: assignee-filter dropdown (avatar + "All Agents"), notification
     bell with amber badge, current-user avatar.

   **Main area**
   - **4 KPI cards** (equal-width row, white, 10px radius, soft shadow):
     1. Open Tickets — count, small delta chip (vs yesterday), tiny inline
        SVG bar trend.
     2. Avg First Response — time value (e.g. "1h 24m"), delta chip.
     3. SLA Compliance — percentage + progress arc SVG, delta chip.
     4. CSAT Score — "4.6 / 5" star motif, delta chip.
   - **SLA by Priority strip** (compact horizontal bars, P1 / P2 / P3):
     each row: priority label, thin bar fill (green / amber / red based on
     compliance %) + percentage label. White card, same radius.
   - **Ticket Queue table card** (full-width, white):
     Header: "Ticket Queue" title + "View all" link + row count.
     Columns: # (ticket id, violet monospace), Subject (truncated), Requester
     (name + avatar initial), Priority (pill: P1 red / P2 amber / P3 violet),
     Status (pill: Open slate / Pending amber / Resolved green / Breached red),
     Assigned to (avatar initial + name), Age (relative time).
     8 representative rows, hover tint, no external images.

   **Right panel (260px, white card)**
   - Title "Team Load" + subtitle "Active agents".
   - List of 6 agents: presence dot (green = online, amber = away, slate =
     offline), avatar initial circle, name, and ticket count badge.
   - Footer: small "Manage team →" link.

4. Typography: system font stack only — "Inter", system-ui, -apple-system,
   "Segoe UI", Roboto, sans-serif. No external font loads.
   - KPI labels: 10px uppercase, letter-spacing 0.06em, slate-500.
   - KPI values: 28px, 600 weight, slate-800.
   - Table header: 11px uppercase, letter-spacing 0.05em, slate-400.
   - Body text: 13–14px, slate-700.

5. Colors: ALL chromatic colors on :root CSS custom properties. SVG fills use
   var(--token) or currentColor. Only neutrals (slate grays, near-white bg,
   borders) may be hardcoded.

6. One inline `<style>`, semantic HTML5, no external assets, no CDNs,
   no lorem ipsum — all copy is realistic helpdesk domain language.

## Output contract

```
<artifact identifier="admin-relay-helpdesk" type="text/html" title="Relay Helpdesk Admin">
<!doctype html>...</artifact>
```
