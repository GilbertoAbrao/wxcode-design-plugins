---
name: admin-sprout-iot
description: |
  Dark-mode IoT device-fleet and telemetry console — technical-fresh
  aesthetic with deep navy backgrounds (#0c1118 / #131b26 / #1a2533),
  lime (#84cc16) and cyan (#22d3ee) accents, amber/red for alerts.
  Left rail nav, site/gateway switcher in topbar, 4 KPI cards, a
  multi-series sparkline telemetry panel, an active alerts list with
  severity pills, and a devices table with signal bars, firmware
  version, and status. Use when the brief calls for IoT monitoring,
  device fleet management, edge telemetry, or any technical operations
  console in dark mode.
triggers:
  - "iot dashboard"
  - "device fleet"
  - "telemetry console"
  - "iot admin"
  - "sensor dashboard"
  - "edge device management"
  - "industrial monitoring"
  - "smart gateway"
  - "painel iot"
  - "monitoramento de dispositivos"
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
  example_prompt: "Build me a dark IoT admin console for a device fleet — left nav rail, site/gateway switcher, 4 KPI cards showing online/offline counts, average signal strength, and open alerts, a telemetry sparkline panel for temperature/humidity/power, an active alerts list with severity pills, and a devices table with firmware version and signal bars."
---

# Sprout IoT Admin Skill

Produce the canonical dark IoT fleet-operations console — precise,
technical, and data-dense without sacrificing clarity.

## Palette tokens (always emit as :root CSS custom properties)

| Token | Value | Use |
|---|---|---|
| `--c-bg-deep` | `#0c1118` | page / rail background |
| `--c-bg-surface` | `#131b26` | cards, panels |
| `--c-bg-raised` | `#1a2533` | table row hover, dropdowns |
| `--c-border` | `#223040` | all borders / dividers |
| `--c-text` | `#dfe7ef` | primary text |
| `--c-muted` | `#8597a8` | labels, captions, secondary |
| `--c-lime` | `#84cc16` | online/healthy accent |
| `--c-cyan` | `#22d3ee` | data/telemetry accent |
| `--c-amber` | `#f59e0b` | warning / medium severity |
| `--c-red` | `#ef4444` | critical / offline |

All chromatic colours must be declared as these tokens and referenced
via `var(--token)` or `currentColor` throughout CSS and inline SVG.
Only neutral dark backgrounds, borders, and gray text may be hardcoded.

## Workflow

1. Read active DESIGN.md if present; otherwise use the token table
   above exactly as specified.
2. Extract from the brief: organisation/site name, gateway count,
   device types (sensors, actuators, gateways), primary telemetry
   channels (temperature, humidity, power draw, CO₂, vibration, etc.).
3. Layout (single-file HTML, inline `<style>`, no external resources):

   **Left rail nav (64px collapsed icon-rail feel, 220px when labeled)**
   - Brand mark + "Sprout IoT" wordmark at top.
   - Nav items with small inline SVG icons: Overview, Devices, Alerts,
     Telemetry, Gateways, Firmware, Settings. Active item gets a lime
     left-bar and `--c-bg-raised` tint.
   - Footer area: connection status dot + "All systems nominal" or
     active alert count.

   **Topbar (56px)**
   - Left: site/gateway switcher pill (current site name + chevron).
   - Center: search input with magnifier icon ("Search devices,
     alerts…").
   - Right: refresh icon + bell icon (badge with alert count) +
     avatar + operator name.

   **4 KPI cards (grid, 1 row)**
   Each card: small ALL-CAPS label, large number, trend delta chip,
   tiny inline-SVG sparkline (6–8 points), subtle icon.
   - Devices Online — lime accent, upward delta.
   - Devices Offline — red/amber accent, count + delta.
   - Avg Signal Strength — cyan accent, dBm value.
   - Open Alerts — amber/red accent, count + severity breakdown.

   **Telemetry panel**
   - Card title "Live Telemetry — last 30 min" + three legend chips
     (Temperature, Humidity, Power).
   - Three inline-SVG sparklines stacked or overlaid, each with its
     own color (cyan for temp, lime for humidity, amber for power),
     Y-axis label, and current value callout.
   - Time axis tick labels at bottom.

   **Active Alerts list**
   - Card title "Active Alerts" + "View all" link.
   - 5–6 rows: severity pill (CRITICAL in red / WARNING in amber /
     INFO in cyan), device name, alert message, age ("3 min ago").
   - Hover highlight on `--c-bg-raised`.

   **Devices table**
   - Card title "Devices" + "Manage" link + filter pills (All / Online
     / Offline / Warning).
   - Columns: Device Name + type icon, Type, Firmware, Signal (4-bar
     inline SVG), Last Seen, Status pill.
   - 6–8 invented device rows with realistic names (e.g.
     "GW-ROOF-04", "SENS-COLD-A3", "ACT-VALVE-12").
   - Alternating row tint on `--c-bg-raised`.

4. Typography: `"Inter", system-ui, -apple-system, "Segoe UI", Roboto,
   sans-serif`. No external font load.
   - KPI numbers: 2rem bold, lime/cyan/red/amber per card.
   - Section headers: 0.65rem uppercase, `var(--c-muted)`,
     letter-spacing 0.08em.
5. All chromatic hex literals (lime, cyan, amber, red) live in `:root`
   only; everything else references `var(--*)` or `currentColor`.
6. Target 10–30 KB. No CDN links, no lorem ipsum.

## Output contract

```
<artifact identifier="admin-sprout-iot" type="text/html" title="Sprout IoT Admin">
<!doctype html>...</artifact>
```
