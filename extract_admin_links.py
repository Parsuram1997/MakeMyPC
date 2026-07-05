import glob, re
with open('admin-dashboard.html', 'r', encoding='utf-8') as f:
    content = f.read()
    links = re.findall(r'<a[^>]+href=[\'\"]([^\'\"]+)[\'\"][^>]*>(.*?)</a>', content, re.DOTALL)
    for href, text in links:
        clean_text = re.sub(r'<[^>]+>', '', text).strip()
        print(f'  {clean_text} -> {href}')
