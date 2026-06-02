import { test } from 'node:test';
import assert from 'node:assert/strict';
import { lintPlugin } from './lint-plugin.mjs';

const COMPLIANT = `---
name: admin-x
description: |
  Dark industrial-grade admin aesthetic; archetype = navbar + icon rail + KPI tiles + status board + records table.
triggers:
  - "dark industrial admin"
  - "dense data terminal"
example_prompt: "Apply this dark industrial admin aesthetic to my domain"
---
# X — Visual Archetype
## Visual language        (AUTHORITATIVE)
tokens...
## Layout archetype       (AUTHORITATIVE, domain-neutral)
navbar, rail, KPI tiles...
## Applying to a domain   (the contract)
Extract THIS domain's primary entities and key metrics from the KB + prompt.
## Example instantiation (illustrative only — NOT the domain)
> Illustrative only; replace every label with the real domain.
MES example...
## Output contract
<artifact...>
`;

test('compliant plugin passes', () => {
  const r = lintPlugin(COMPLIANT, { description: 'Dark industrial admin aesthetic.' });
  assert.equal(r.ok, true, r.violations.join('; '));
});

test('domain triggers fail', () => {
  const bad = COMPLIANT.replace('"dark industrial admin"', '"mes dashboard"')
                       .replace('"dense data terminal"', '"oee dashboard"');
  const r = lintPlugin(bad, { description: 'Dark industrial admin aesthetic.' });
  assert.equal(r.ok, false);
  assert.ok(r.violations.some(v => /trigger/i.test(v) && /mes|oee/i.test(v)));
});

test('missing required heading fails', () => {
  const bad = COMPLIANT.replace('## Applying to a domain   (the contract)', '## Notes');
  const r = lintPlugin(bad, { description: 'Dark industrial admin aesthetic.' });
  assert.equal(r.ok, false);
  assert.ok(r.violations.some(v => /Applying to a domain/.test(v)));
});

test('authoritative markers required', () => {
  const bad = COMPLIANT.replace('## Visual language        (AUTHORITATIVE)', '## Visual language');
  const r = lintPlugin(bad, { description: 'Dark industrial admin aesthetic.' });
  assert.equal(r.ok, false);
  assert.ok(r.violations.some(v => /AUTHORITATIVE/i.test(v)));
});

test('domain extraction in workflow fails', () => {
  const bad = COMPLIANT.replace(
    "Extract THIS domain's primary entities and key metrics from the KB + prompt.",
    'Extract from the brief: plant name, production lines, OEE targets, work-order list.'
  );
  const r = lintPlugin(bad, { description: 'Dark industrial admin aesthetic.' });
  assert.equal(r.ok, false);
  assert.ok(r.violations.some(v => /extract.*brief/i.test(v)));
});

test('domain words in manifest description fail', () => {
  const r = lintPlugin(COMPLIANT, { description: 'Manufacturing Execution System for OEE and production lines.' });
  assert.equal(r.ok, false);
  assert.ok(r.violations.some(v => /description/i.test(v)));
});

test('build-meta in example HTML fails', () => {
  const html = '<section class="panel"><h2>Regras ativas</h2><p>Persistência real depende do backend</p></section>';
  const r = lintPlugin(COMPLIANT, { description: 'Dark industrial admin aesthetic.' }, { exampleHtml: [html] });
  assert.equal(r.ok, false);
  assert.ok(r.violations.some(v => /meta|build|rules panel|on-screen/i.test(v)));
});

test('single-screen plugin warns, does not fail', () => {
  const r = lintPlugin(COMPLIANT, { description: 'Dark industrial admin aesthetic.' },
                       { assetHtmlNames: ['dashboard.html'], hasLayoutsMd: false });
  assert.equal(r.ok, true);                       // warn-level, not a violation yet
  assert.ok((r.warnings || []).some(w => /example set|single.screen|crud/i.test(w)));
});
