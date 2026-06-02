// Deterministic plugin linter for the WXCode Open Design plugin authoring toolkit.
//
// Enforces the aesthetic/semantic split documented in forge/AUTHORING.md
// ("Lint" section + authority rules 1–6). A plugin is a skin + skeleton; its
// example domain is illustration and standalone fallback, never the product
// authority. This linter rejects plugins that hard-code their example domain
// into frontmatter, drop the authoritative structure, or render build/design
// metadata as product UI.
//
// Pure ESM, no external dependencies, Node ≥18.

/**
 * Industry/domain nouns that must not appear in a plugin's aesthetic surfaces
 * (frontmatter `triggers` / `description` and `manifest.description`).
 * Seed list — kept as one exported const so it stays maintainable. Extend here.
 */
export const BANNED_DOMAIN = [
  /\bmes\b/i,
  /\boee\b/i,
  /production line/i,
  /work[- ]order/i,
  /shop[- ]floor/i,
  /\bcrypto\b/i,
  /\btreasury\b/i,
  /\bhelpdesk\b/i,
  /\bairline\b/i,
  /\bbanking\b/i,
  /\binsurance\b/i,
  /\bclinic\b/i,
  /\bpos\b/i,
  /\bcommerce\b/i,
  /\blms\b/i,
  /\bats\b/i,
  /\bcrm\b/i,
  /\bdevops\b/i,
  /manufactur/i,
];

/**
 * Heuristic for build/design metadata rendered as UI (AUTHORING.md rule 6).
 * Catches validation-status / checklist / "depends on backend" / build-report
 * panels in example HTML, in both English and pt-BR phrasings.
 */
export const BUILD_META =
  /checklist|depends on (the )?backend|regras ativas|valida(ç|c)(ã|a)o ativa|build report|status de valida/i;

const REQUIRED_HEADINGS = [
  '## Visual language',
  '## Layout archetype',
  '## Applying to a domain',
  '## Example instantiation',
];

const AUTHORITATIVE_HEADINGS = ['## Visual language', '## Layout archetype'];

/**
 * Split frontmatter (between the first two `---` fences) from the body.
 * Returns { frontmatter, body }; if there is no frontmatter block the whole
 * input is treated as the body.
 */
function splitFrontmatter(skillMd) {
  const text = String(skillMd ?? '');
  const fence = /^---\s*$/m;
  if (!fence.test(text)) return { frontmatter: '', body: text };
  // Find first fence.
  const lines = text.split('\n');
  let start = -1;
  let end = -1;
  for (let i = 0; i < lines.length; i += 1) {
    if (/^---\s*$/.test(lines[i])) {
      if (start === -1) {
        start = i;
      } else {
        end = i;
        break;
      }
    }
  }
  if (start === -1 || end === -1) return { frontmatter: '', body: text };
  return {
    frontmatter: lines.slice(start + 1, end).join('\n'),
    body: lines.slice(end + 1).join('\n'),
  };
}

/**
 * Parse `triggers:` (quoted strings on `- "..."` lines) and `description:`
 * (inline value or a `|` block) from the frontmatter via a simple line scan.
 * No YAML dependency.
 */
function parseFrontmatter(frontmatter) {
  const lines = frontmatter.split('\n');
  const triggers = [];
  let description = '';

  for (let i = 0; i < lines.length; i += 1) {
    const line = lines[i];

    const trig = line.match(/^triggers:\s*$/);
    if (trig) {
      // Consume subsequent `- "..."` list items until a non-list / non-indented line.
      for (let j = i + 1; j < lines.length; j += 1) {
        const item = lines[j].match(/^\s*-\s*"([^"]*)"\s*$/);
        if (item) {
          triggers.push(item[1]);
          continue;
        }
        // Stop when we hit a new top-level key or a blank-then-key boundary.
        if (/^\S/.test(lines[j]) && lines[j].trim() !== '') break;
        if (lines[j].trim() === '') continue;
        // Indented non-list content under triggers is unexpected; stop.
        break;
      }
      continue;
    }

    const descBlock = line.match(/^description:\s*\|\s*$/);
    if (descBlock) {
      const block = [];
      for (let j = i + 1; j < lines.length; j += 1) {
        // Block scalar lines are indented; an unindented non-empty line ends it.
        if (lines[j].trim() === '') {
          block.push('');
          continue;
        }
        if (/^\s+/.test(lines[j])) {
          block.push(lines[j].replace(/^\s+/, ''));
          continue;
        }
        break;
      }
      description = block.join('\n').trim();
      continue;
    }

    const descInline = line.match(/^description:\s*(.+?)\s*$/);
    if (descInline) {
      description = descInline[1].replace(/^["']|["']$/g, '');
      continue;
    }
  }

  return { triggers, description };
}

/** First matching BANNED_DOMAIN regex source-term for a string, or null. */
function matchBanned(value) {
  if (!value) return null;
  for (const rx of BANNED_DOMAIN) {
    const m = String(value).match(rx);
    if (m) return m[0];
  }
  return null;
}

/** Return the body line that starts with the given heading, or null. */
function findHeadingLine(body, heading) {
  const lines = body.split('\n');
  for (const line of lines) {
    if (line.startsWith(heading)) return line;
  }
  return null;
}

/**
 * Lint a plugin's SKILL.md + manifest (+ optional file context).
 *
 * @param {string} skillMd - raw SKILL.md content.
 * @param {{ description?: string }} manifest - parsed open-design.json.
 * @param {{ exampleHtml?: string[], assetHtmlNames?: string[], hasLayoutsMd?: boolean }} [files]
 * @returns {{ ok: boolean, violations: string[], warnings: string[] }}
 */
export function lintPlugin(skillMd, manifest = {}, files = {}) {
  const violations = [];
  const warnings = [];

  const { frontmatter, body } = splitFrontmatter(skillMd);
  const { triggers, description } = parseFrontmatter(frontmatter);

  // Rule 4 — frontmatter triggers must carry no domain semantics.
  for (const trigger of triggers) {
    const hit = matchBanned(trigger);
    if (hit) {
      violations.push(
        `trigger "${trigger}" contains domain term "${hit}"; triggers must describe style, not industry/domain`,
      );
    }
  }

  // Rule 4 — frontmatter description AND manifest description must be aesthetic-only.
  const fmDescHit = matchBanned(description);
  if (fmDescHit) {
    violations.push(
      `frontmatter description contains domain term "${fmDescHit}"; the description must describe style, not industry/domain`,
    );
  }
  const manifestDescHit = matchBanned(manifest?.description);
  if (manifestDescHit) {
    violations.push(
      `manifest description contains domain term "${manifestDescHit}"; the description must describe style, not industry/domain`,
    );
  }

  // Required headings (rule 1/2 structure).
  for (const heading of REQUIRED_HEADINGS) {
    if (!findHeadingLine(body, heading)) {
      violations.push(`missing required heading "${heading}"`);
    }
  }

  // Authoritative markers on Visual language + Layout archetype (rule 1).
  for (const heading of AUTHORITATIVE_HEADINGS) {
    const line = findHeadingLine(body, heading);
    if (line && !/AUTHORITATIVE/.test(line)) {
      violations.push(`heading "${heading}" must be marked AUTHORITATIVE`);
    }
  }

  // Rule 3 — Workflow must not say "extract <domain fields> from the brief".
  if (/extract[^.\n]*from the brief/i.test(body)) {
    violations.push(
      'workflow must not "extract ... from the brief" with domain fields; use the domain-neutral archetype-slot phrasing instead',
    );
  }

  // Example instantiation must be labeled illustrative-only (rule 2 / authoring §63).
  const exampleLine = findHeadingLine(body, '## Example instantiation');
  if (exampleLine && !/illustrative/i.test(exampleLine)) {
    violations.push(
      'heading "## Example instantiation" must be labeled illustrative-only (the example is not the domain authority)',
    );
  }

  // Rule 6 — no build/design metadata rendered as UI in example HTML.
  for (const html of files?.exampleHtml ?? []) {
    if (BUILD_META.test(String(html))) {
      violations.push(
        'example HTML renders build/design metadata as on-screen UI (rules panel / validation-status / build note); domain rules must become inline field validation',
      );
      break;
    }
  }

  // Rule 5 — ship a meta-free multi-screen example set (warn-level for now).
  const screenCount = files?.assetHtmlNames?.length ?? 0;
  if (screenCount < 2 && !files?.hasLayoutsMd) {
    warnings.push(
      'single-screen plugin: ship the meta-free CRUD example set (dashboard + list + form) or a references/layouts.md, not just one screen',
    );
  }

  return { ok: violations.length === 0, violations, warnings };
}

// CLI tail: `node lint-plugin.mjs <plugin-dir>`
if (import.meta.url === `file://${process.argv[1]}`) {
  const { readFileSync, existsSync, readdirSync } = await import('node:fs');
  const { join } = await import('node:path');

  const dir = process.argv[2];
  if (!dir) {
    console.error('usage: lint-plugin.mjs <plugin-dir>');
    process.exit(2);
  }

  const skillMd = readFileSync(join(dir, 'SKILL.md'), 'utf8');
  let manifest = {};
  const manifestPath = join(dir, 'open-design.json');
  if (existsSync(manifestPath)) {
    try {
      manifest = JSON.parse(readFileSync(manifestPath, 'utf8'));
    } catch (err) {
      console.error(`failed to parse open-design.json: ${err.message}`);
      process.exit(2);
    }
  }

  const listHtml = (base) => {
    if (!existsSync(base)) return [];
    return readdirSync(base, { withFileTypes: true })
      .filter((e) => e.isFile() && e.name.endsWith('.html'))
      .map((e) => e.name);
  };

  const rootHtmlNames = listHtml(dir);
  const assetsDir = join(dir, 'assets');
  const assetHtmlNamesRaw = listHtml(assetsDir);

  const exampleHtml = [
    ...rootHtmlNames.map((n) => readFileSync(join(dir, n), 'utf8')),
    ...assetHtmlNamesRaw.map((n) => readFileSync(join(assetsDir, n), 'utf8')),
  ];

  const assetHtmlNames = assetHtmlNamesRaw.length ? assetHtmlNamesRaw : rootHtmlNames;
  const hasLayoutsMd = existsSync(join(dir, 'references', 'layouts.md'));

  const result = lintPlugin(skillMd, manifest, { exampleHtml, assetHtmlNames, hasLayoutsMd });

  for (const v of result.violations) console.error(`VIOLATION: ${v}`);
  for (const w of result.warnings) console.warn(`WARNING: ${w}`);
  if (result.ok) console.log('ok: no violations');

  process.exit(result.violations.length ? 1 : 0);
}
