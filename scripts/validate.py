#!/usr/bin/env python3
"""Validate sf-agent-skills repo: JSON, frontmatter, HTML, em-dash check."""
import json, re, os, sys, glob
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
errors = []
skill_ids = set()

# 1. Validate skill-catalog.json
catalog_path = os.path.join(ROOT, 'docs/data/skill-catalog.json')
try:
    with open(catalog_path) as f:
        cat = json.load(f)
    assert 'metadata' in cat, 'Missing metadata'
    assert 'skills' in cat, 'Missing skills'
    expected = cat.get('metadata', {}).get('totalSkills')
    assert len(cat['skills']) == expected, f'Expected {expected} skills, got {len(cat["skills"])}'
    skill_ids = {s['id'] for s in cat['skills']}
    assert len(skill_ids) == len(cat['skills']), 'Duplicate skill IDs'
    for s in cat['skills']:
        for field in ['id','name','tagline','category','severity','inputs','outputs','time','phases','detail','edgeCases','prompt','exampleOutput']:
            assert field in s, f'Skill {s.get("id","?")} missing field: {field}'
        assert s['severity'] in ('CRITICAL','HIGH','MEDIUM','LOW'), f'Bad severity: {s["severity"]}'
    print('PASS: skill-catalog.json (%d skills)' % len(cat['skills']))
except Exception as e:
    errors.append(f'FAIL skill-catalog.json: {e}')

# 2. Validate SKILL.md frontmatter
skill_files = glob.glob(os.path.join(ROOT, 'skills/*/SKILL.md'))
for sf in sorted(skill_files):
    try:
        with open(sf) as f: content = f.read()
        assert content.startswith('---'), 'Missing opening ---'
        end_idx = content.find('\n---\n', 3)
        assert end_idx > 0, 'Missing closing ---'
        fm_text = content[3:end_idx]
        fm = None
        try:
            import yaml; fm = yaml.safe_load(fm_text)
        except ImportError:
            fm = {}
        required_fields = ['name','description','version','author','license']
        for rf in required_fields:
            if isinstance(fm, dict):
                assert rf in fm, f'Missing frontmatter field: {rf}'
        name = fm.get('name','') if isinstance(fm, dict) else ''
        assert len(name) <= 64, f'Name too long: {len(name)}'
        body = content[end_idx+4:].strip()
        assert body, 'Empty body'
        skill_id = os.path.basename(os.path.dirname(sf))
        assert skill_id in skill_ids, f'Skill dir {skill_id} not in catalog'
        print(f'PASS: {skill_id}')
    except Exception as e:
        errors.append(f'FAIL {sf}: {e}')

# 3. Check all skill dirs have SKILL.md
for sid in skill_ids:
    path = os.path.join(ROOT, 'skills', sid, 'SKILL.md')
    if not os.path.exists(path):
        errors.append(f'MISSING: {path}')

# 4. Validate HTML parsing
html_path = os.path.join(ROOT, 'docs/index.html')
try:
    with open(html_path) as f: html_content = f.read()
    class Validator(HTMLParser):
        def __init__(self): super().__init__(); self.stack = []; self.errors = []
        def handle_starttag(self,tag,attrs):
            if tag not in ('br','hr','img','input','meta','link'): self.stack.append(tag)
        def handle_endtag(self,tag):
            if tag not in ('br','hr','img','input','meta','link'):
                if self.stack and self.stack[-1] == tag: self.stack.pop()
    v = Validator()
    v.feed(html_content)
    assert not v.errors, 'HTML parse errors: ' + str(v.errors)
    print('PASS: docs/index.html (parsed OK)')
except Exception as e:
    errors.append(f'FAIL docs/index.html: {e}')

# 5. Em-dash check
for root_dir in ['skills','docs']:
    full = os.path.join(ROOT, root_dir)
    if os.path.exists(full):
        for dirpath, _, filenames in os.walk(full):
            for fn in filenames:
                if fn.endswith(('.md','.html','.json','.txt')):
                    fpath = os.path.join(dirpath, fn)
                    with open(fpath) as f:
                        if '\u2014' in f.read() or '\u2013' in f.read():
                            errors.append(f'EM-DASH FOUND: {fpath}')

# 6. Check .nojekyll exists
for path in [os.path.join(ROOT, '.nojekyll'), os.path.join(ROOT, 'docs', '.nojekyll')]:
    if not os.path.exists(path):
        errors.append(f'MISSING: {path}')

if errors:
    for e in errors: print(e)
    sys.exit(1)
else:
    print('\nAll validations passed.')
