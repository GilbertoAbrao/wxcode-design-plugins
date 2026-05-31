---
name: admin-midnight-ops
description: |
  Generates a single-file dark-mode operations and observability console for SRE and on-call engineering teams. The layout combines a slim top navbar, a compact left icon rail, four metric tiles with inline trend sparklines, a time-series throughput chart, an active incidents table with severity pills, and a live service-health status list. Use this plugin whenever a user asks for an ops dashboard, monitoring console, incident management UI, or observability admin panel in a dark-mode teal aesthetic.
triggers:
  - "ops console"
  - "observability dashboard"
  - "dark admin dashboard"
  - "operations console"
  - "incident management dashboard"
  - "monitoring console dark mode"
  - "painel de operações"
  - "painel de observabilidade"
  - "dark-mode ops admin"
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
    requires: [pixel-discipline, state-coverage]
  example_prompt: "Build me a dark-mode operations console — top navbar, icon rail, 4 metric tiles with trends, a time-series chart, an active incidents table with status pills, and a service-health list."
---

# Midnight Ops Console Skill

This skill produces a high-density observability and incident-management console targeting SRE teams, on-call engineers, and platform operations leads. The single-file output is built on a #0b1120 midnight background with teal-to-cyan accents, delivering a calm but information-dense viewport that minimises cognitive load during outages.

## Workflow

1. Read the active DESIGN.md to capture brand tokens (colours, typeface weights, border-radius scale).
2. Gather domain inputs from the brief: service names, primary SLOs (latency, throughput, error-rate, uptime), severity taxonomy, environment labels (prod / staging / canary), and number of active incidents to display.
3. Layout — build section by section:
   - **Top navbar** (slim, 56 px): logo mark (inline SVG), global search input, environment switcher pill-group, notification bell with badge, avatar button.
   - **Left icon rail** (48 px wide, full-height): six nav icon buttons — Overview, Services, Incidents, Metrics, Traces, Settings — with teal active state and muted inactive.
   - **Metric tiles row** (4 tiles, equal-width grid): each tile shows a label, the current value, a delta badge (green/red arrow + %), and a mini inline SVG sparkline (14 data points, path only, no axes). Metrics: P99 Latency, Request Throughput, Error Rate, Uptime SLO.
   - **Time-series chart** (full-width panel): inline SVG area chart with a single gradient-fill series, 24-point hourly window, Y-axis labels, X-axis hour ticks, and a crosshair line. Title: "Request Throughput — Last 24 h".
   - **Active Incidents table**: columns — Severity pill (P1/P2/P3 colour-coded), Incident ID, Title, Affected Service, Duration, Assignee, Status pill (Investigating/Mitigating/Resolved). Use at least 5 realistic rows.
   - **Service Health list** (right sidebar or below chart): each row shows a service name, a coloured status dot (healthy/degraded/down), and a short status message. Cover 8 services.
4. Write all CSS as custom properties inside a single `<style>` block; no external imports. Use the midnight palette (--bg-base #0b1120, --surface-1 #111827, --surface-2 #1e293b, --border #1f2937, --accent-teal #14b8a6, --accent-cyan #22d3ee, --text-primary #e2e8f0, --text-muted #94a3b8). System font stack only.
5. All SVG (logo, sparklines, chart) must be original inline markup; no external images, no data URIs from third-party sources.
6. Output is a single valid HTML file with no external dependencies.

## Output contract

```
<artifact identifier="admin-midnight-ops" type="text/html" title="Midnight Ops Console">
<!doctype html>
...
</html>
</artifact>
```
