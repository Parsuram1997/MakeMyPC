import sys, io, glob, re, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

SKIP = {'admin-dashboard.html','admin-dashboard-overview.html','orders-management.html','product-management.html'}

# Matches any comment variant before the orphan flex-col div
# e.g. <!-- TopNavBar --> or <!-- Top Navigation Bar (Shared Component) --> etc.
PATTERN = re.compile(
    r'\s*<!--\s*Top[\w\s().-]*-->\s*'
    r'<div class="flex flex-col gap-6[^"]*"[^>]*>.*?</div>\s*</div>',
    re.DOTALL
)

for fpath in sorted(glob.glob('c:/Projects/MakeMyPC/*.html')):
    bn = os.path.basename(fpath)
    if bn in SKIP:
        continue
    c = open(fpath, encoding='utf-8').read()
    new = PATTERN.sub('', c)
    if new != c:
        open(fpath, 'w', encoding='utf-8').write(new)
        print('CLEANED', bn)
    else:
        print('clean  ', bn)
