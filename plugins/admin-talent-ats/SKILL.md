---
name: admin-talent-ats
description: |
  Recruiting & applicant-tracking system (ATS) admin dashboard archetype:
  light HR mode, indigo (#4f46e5 / #6366f1) + pink (#ec4899) accent palette,
  slate neutral text, white / #f8f8fc surfaces, #e8e8f2 borders.
  Left sidebar with company logo, requisition switcher, and nav groups;
  topbar with search, period selector, and avatar; 4 KPI cards
  (open roles, active candidates, interviews this week, avg time-to-hire);
  kanban-style hiring pipeline (Applied / Screening / Interview / Offer);
  inline-SVG recruiting funnel; candidates table with ratings; upcoming
  interviews side panel. Use when the brief mentions ATS, recruiting ops,
  talent acquisition, HR pipeline, or candidate tracking.
triggers:
  - "ats dashboard"
  - "applicant tracking"
  - "recruiting dashboard"
  - "talent acquisition"
  - "hr pipeline"
  - "hiring pipeline"
  - "candidate management"
  - "painel de recrutamento"
  - "招聘管理"
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
  example_prompt: "Build me a recruiting ATS admin dashboard — left sidebar with requisition switcher, 4 KPI tiles (open roles, candidates, interviews, time-to-hire), hiring pipeline board, recruiting funnel chart, candidates table, and upcoming interviews panel."
---

# Talent ATS Admin Skill

Produce the canonical recruiting / applicant-tracking system admin layout
for HR teams and talent ops — modern, light, indigo + pink accent.

## Workflow

1. Read the active DESIGN.md (if present); otherwise use indigo (#4f46e5)
   on a near-white canvas (#f8f8fc / #ffffff).
2. Extract from the brief: company name, open requisitions, KPI values
   (open roles, candidate pipeline count, interviews this week,
   time-to-hire in days).
3. Layout:

   **Left sidebar (240px)**
   - Top: company logo mark (inline SVG geometric mark) + company name
     + "Talent Ops" sub-label.
   - Requisition switcher: dropdown or select-like element showing the
     active job req (e.g. "Senior Frontend Engineer").
   - Nav groups:
     - PIPELINE: Dashboard, Candidates, Pipeline Board
     - SOURCING: Job Postings, Campaigns, Referrals
     - REPORTS: Analytics, Funnel, Export
   - Active item: indigo left-bar + indigo-tinted background.
   - Bottom: HR Ops team avatar cluster + "Settings" link.

   **Topbar (60px)**
   - Left: page title "Hiring Overview" + breadcrumb (Home / Recruiting).
   - Centre: search input ("Search candidates, roles…").
   - Right: period selector (This Month / Q2 / YTD), notification bell
     with unread dot, recruiter avatar + name.

   **4 KPI cards (row)**
   - Open Roles — big number, delta vs last month, mini inline SVG bar
     sparkline, indigo icon.
   - Active Candidates — count, delta, sparkline, violet icon.
   - Interviews This Week — count, delta, pink icon.
   - Avg. Time-to-Hire — days figure, delta, green/amber coloring.
   - Card style: white, 12px radius, subtle shadow, 1px #e8e8f2 border.

   **Hiring Pipeline board (kanban)**
   - Four columns: Applied / Screening / Interview / Offer.
   - Each column header: stage name + candidate count badge.
   - 3–4 candidate mini-cards per column: avatar initials, name, role,
     source tag (LinkedIn / Referral / Agency), days-in-stage.
   - Offer column cards use a green left-bar; Interview column uses pink.

   **Lower grid (8/4 split)**
   - LEFT (8 cols): Recruiting Funnel inline SVG — horizontal bar funnel
     showing Applied → Screened → Interviewed → Offered → Hired with
     percentage conversion labels. Indigo-to-pink gradient bars.
   - RIGHT (4 cols): Upcoming Interviews side panel — date-grouped list
     of 6 interviews: candidate name, role, interviewer, time slot,
     video/onsite badge.

   **Candidates table (full width)**
   - Header: "Active Candidates" title + "View All" link + CSV export
     ghost button + indigo "+ Add Candidate" CTA.
   - 8 rows, columns: Candidate (avatar initials + name + email),
     Applied Role, Stage pill, Source badge, Rating (star icons),
     Actions (view / schedule).
   - Tinted hover row (#f0f0fb), pagination hint.

4. Typography: system font stack only — "Inter", system-ui, -apple-system,
   "Segoe UI", Roboto, sans-serif. No external font loads.
5. Every chromatic color as a :root CSS custom property. SVG fills via
   var(--token) or currentColor. No hardcoded hex for chromatic values
   inside CSS rules or inline SVG attributes.
6. One inline <style>, semantic HTML5, no external assets, no CDNs.
   Target 10–30 KB.

## Color tokens (root)

```
--c-primary:    #4f46e5   /* indigo-600 */
--c-primary-lt: #6366f1   /* indigo-500 */
--c-accent:     #ec4899   /* pink-500   */
--c-accent-lt:  #f472b6   /* pink-400   */
--c-success:    #22c55e
--c-warning:    #f59e0b
--c-surface:    #f8f8fc
--c-border:     #e8e8f2
--c-sidebar:    #ffffff
```

## Output contract

```
<artifact identifier="admin-talent-ats" type="text/html" title="Talent ATS Admin">
<!doctype html>...</artifact>
```
