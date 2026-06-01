---
name: admin-verdant-clinic
description: |
  Calm, clinical light-mode admin dashboard for clinic and healthcare
  operations. Emerald-to-teal accent (#10b981 / #0d9488), soft slate
  text on white/#f7faf9 surfaces, #e3ece9 borders. Triage status
  colors (green / amber / red). Left sidebar with department switcher
  and clinical nav, topbar with search, date, and clinician avatar,
  4 KPI cards, today's appointment schedule list, inline SVG occupancy
  mini-chart, and a recent patients table. Use when the brief targets
  a clinic, hospital department, or healthcare operations panel.
triggers:
  - "clinic admin"
  - "clinic dashboard"
  - "healthcare admin"
  - "hospital dashboard"
  - "patient management"
  - "appointment schedule dashboard"
  - "painel clínica"
  - "clínica saúde admin"
  - "诊所管理后台"
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
  example_prompt: "Build me a clinic operations admin dashboard — left sidebar with department switcher, topbar with search and clinician avatar, 4 KPI cards (patients today, appointments, avg wait, bed occupancy), a today's appointments schedule list, a mini occupancy chart, and a recent patients table."
---

# Verdant Clinic Admin Skill

Produce a calm, clinical light-mode dashboard suited for a clinic or
hospital department operations view. Every color token must live in
`:root` CSS custom properties. No chromatic hex literal in CSS rules
or inline SVG — use `var(--token)` / `currentColor` throughout.

## Design language

- **Accent**: emerald `#10b981` → teal `#0d9488`. Interactive hover
  shifts emerald → teal.
- **Surfaces**: near-white `#f7faf9` page background; white `#ffffff`
  cards; `#e3ece9` subtle borders.
- **Text**: slate hierarchy — primary `#1e293b`, secondary `#475569`,
  muted `#94a3b8`.
- **Triage status pills**:
  - Stable / Completed → emerald bg `#d1fae5`, text `#065f46`.
  - Pending / In Progress → amber bg `#fef3c7`, text `#92400e`.
  - Urgent / Cancelled → rose bg `#fce7f3`, text `#9d174d`.
- **Shadows**: `0 1px 4px rgba(0,0,0,0.06)` card, `0 2px 10px
  rgba(0,0,0,0.08)` modal.
- **Radius**: `12px` cards, `8px` inputs/pills.

## Workflow

1. Read the active DESIGN.md (if present); otherwise fall back to
   the emerald-teal token set above.
2. Extract from the brief: clinic name, clinician name, departments
   list, today's date.
3. Layout:

   **Left sidebar (240px)**
   - Top logo area: green cross SVG mark + "Verdant Clinic" wordmark.
   - Department switcher dropdown (General Practice, Cardiology,
     Radiology, Emergency).
   - Nav groups — OVERVIEW (Dashboard, Schedule, Patients), CLINICAL
     (Appointments, Triage, Lab Results, Prescriptions), OPERATIONS
     (Rooms, Staff, Reports), SETTINGS. Active item has emerald
     left-bar and `#ecfdf5` tinted background.
   - Bottom: clinician avatar chip + "Dr. [Name]" + "Sign out" icon.

   **Topbar (60px)**
   - Left: clinic name breadcrumb (Verdant Clinic / Dashboard).
   - Center: search input with magnifier icon ("Search patients,
     appointments…").
   - Right: today's date badge, bell icon, clinician avatar circle
     with initials in emerald.

   **KPI card row (4 cards)**
   Each card: white, 12px radius, soft shadow. Fields:
   - Patients Today — big number, emerald sparkline SVG, delta chip.
   - Appointments — count, teal mini-bar SVG, delta chip.
   - Avg Wait Time — minutes, amber inline trend SVG.
   - Bed Occupancy — percentage, rose inline bar + delta chip.

   **Today's appointments schedule list**
   Column headers: Time / Patient / Visit Type / Room / Status.
   8 rows with invented names (no real personal data). Status pill
   colors use the triage set above.

   **Occupancy mini-chart**
   Inline SVG bar chart (7 days × 4 departments). Emerald/teal
   gradient bars; all fill/stroke via `var(--token)`.

   **Recent patients table**
   Columns: Name + MRN / Age / Department / Last Visit / Status.
   8 rows with invented names and MRN codes. Tinted hover row,
   "View all" link.

4. Typography: system font stack only — `"Inter", system-ui,
   -apple-system, "Segoe UI", Roboto, sans-serif`. No external load.
5. One inline `<style>` block. Semantic HTML. No external assets,
   no CDNs. Target 10–30 KB total.
6. Every chromatic color is a `:root` CSS custom property.
   SVG fill/stroke chromatic colors use `var(--token)` or
   `currentColor`. Only neutrals (grays, near-black text,
   near-white bg, borders) may be hardcoded.

## Output contract

```
<artifact identifier="admin-verdant-clinic" type="text/html" title="Verdant Clinic Admin">
<!doctype html>...</artifact>
```
