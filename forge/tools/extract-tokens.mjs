// extract-tokens.mjs
// Injected via Playwright `browser_evaluate(() => extractDesignTokens(document, window))`.
// Returns design CHARACTERISTICS only (palette / type / layout signals) — never
// source markup. Capture output is transient reference for the distill phase;
// the built plugin is an original re-implementation, not a copy.
export function extractDesignTokens(doc = document, win = window) {
  const toHex = (c) => {
    const m = String(c).match(/rgba?\(([^)]+)\)/i);
    if (!m) return null;
    const [r, g, b, a] = m[1].split(',').map((x) => parseFloat(x.trim()));
    if (a === 0) return null; // skip fully transparent
    const h = (n) => Math.max(0, Math.min(255, Math.round(n || 0))).toString(16).padStart(2, '0');
    return `#${h(r)}${h(g)}${h(b)}`;
  };
  // Pills computed as enormous px (e.g. `border-radius: 50%/9999px` on a big
  // box) come back like `1.67772e+07px`; collapse those to a stable pill token.
  const normRadius = (r) => {
    const first = parseFloat(String(r));
    return Number.isFinite(first) && first > 1000 ? '9999px' : r;
  };
  const els = Array.from(doc.querySelectorAll('*')).slice(0, 4000);
  const tally = (arr) => {
    const m = new Map();
    for (const v of arr) if (v) m.set(v, (m.get(v) || 0) + 1);
    return [...m.entries()].sort((a, b) => b[1] - a[1]).map(([k]) => k);
  };
  const colors = [], fams = [], sizes = [], weights = [], radii = [], shadows = [];
  for (const el of els) {
    const s = win.getComputedStyle(el);
    if (!s) continue;
    colors.push(toHex(s.color), toHex(s.backgroundColor), toHex(s.borderColor));
    if (s.fontFamily) fams.push(s.fontFamily.trim());
    if (s.fontSize) sizes.push(s.fontSize);
    if (s.fontWeight) weights.push(String(s.fontWeight));
    if (s.borderRadius && s.borderRadius !== '0px') radii.push(normRadius(s.borderRadius));
    if (s.boxShadow && s.boxShadow !== 'none') shadows.push(s.boxShadow);
  }
  const has = (sel) => !!(doc.querySelector && doc.querySelector(sel));
  const features = [
    has('aside, nav[class*="side"], [class*="sidebar"]') && 'sidebar',
    has('header, [class*="topbar"], [class*="navbar"]') && 'topbar',
    has('table') && 'data-table',
    has('canvas, svg[class*="chart"], [class*="chart"]') && 'chart',
    has('form, input, select') && 'forms',
    has('[class*="card"], .card') && 'cards',
    has('[class*="kpi"], [class*="stat"]') && 'kpi-tiles',
  ].filter(Boolean);
  return {
    palette: tally(colors).slice(0, 12),
    fontStacks: tally(fams).slice(0, 4),
    typeScale: tally(sizes).slice(0, 10),
    weights: tally(weights).slice(0, 6),
    radii: tally(radii).slice(0, 5),
    shadows: tally(shadows).slice(0, 5),
    features,
    elementCount: els.length,
  };
}
// Browser-global fallback when injected as a plain (non-ESM) script.
if (typeof window !== 'undefined') window.extractDesignTokens = extractDesignTokens;
