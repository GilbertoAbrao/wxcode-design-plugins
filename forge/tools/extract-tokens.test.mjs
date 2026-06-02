// extract-tokens.test.mjs — run: node --test forge/tools/extract-tokens.test.mjs
// Dependency-free fake-DOM unit test for the aggregation logic.
import assert from 'node:assert/strict';
import { extractDesignTokens } from './extract-tokens.mjs';

function fakeDoc() {
  const mk = (styles, tag = 'div') => ({ tagName: tag.toUpperCase(), __s: styles });
  const els = [
    mk({ color: 'rgb(17, 24, 39)', backgroundColor: 'rgb(255, 255, 255)', borderColor: 'rgb(229, 231, 235)', fontFamily: 'Inter, sans-serif', fontSize: '16px', fontWeight: '400', borderRadius: '8px', boxShadow: 'none' }),
    mk({ color: 'rgb(17, 24, 39)', backgroundColor: 'rgb(37, 99, 235)', borderColor: 'rgba(0,0,0,0)', fontFamily: 'Inter, sans-serif', fontSize: '24px', fontWeight: '700', borderRadius: '8px', boxShadow: '0 1px 2px rgba(0,0,0,.06)' }, 'h1'),
    mk({ color: 'rgb(107, 114, 128)', backgroundColor: 'rgba(0, 0, 0, 0)', borderColor: 'rgba(0,0,0,0)', fontFamily: 'Inter, sans-serif', fontSize: '14px', fontWeight: '400', borderRadius: '0px', boxShadow: 'none' }, 'span'),
    mk({ color: 'rgb(17, 24, 39)', backgroundColor: 'rgb(255, 255, 255)', borderColor: 'rgba(0,0,0,0)', fontFamily: 'Inter, sans-serif', fontSize: '14px', fontWeight: '400', borderRadius: '1.67772e+07px', boxShadow: 'none' }, 'button'),
  ];
  const present = new Set(['table', '.card']);
  return {
    querySelectorAll: () => els,
    querySelector: (sel) => (sel.split(',').some((s) => present.has(s.trim())) ? els[0] : null),
    body: els[0],
  };
}
const win = { getComputedStyle: (el) => el.__s };

const t = extractDesignTokens(fakeDoc(), win);
assert.ok(t.palette.includes('#111827'), 'dominant text color present');
assert.ok(t.palette.includes('#2563eb'), 'accent color present');
assert.equal(t.fontStacks[0], 'Inter, sans-serif');
assert.ok(t.typeScale.includes('16px'), 'base size captured');
assert.ok(t.radii.includes('8px'));
assert.ok(t.radii.includes('9999px'), 'enormous pill radius normalized');
assert.ok(!t.radii.some((r) => /e\+/.test(r)), 'no scientific-notation radii leak');
assert.ok(Array.isArray(t.features));
assert.ok(t.features.includes('data-table'), 'table feature detected');
assert.ok(t.features.includes('cards'), 'card feature detected');
console.log('ok extract-tokens');
