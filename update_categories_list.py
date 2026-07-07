import re

with open('product-categories.html', 'r', encoding='utf-8') as f:
    content = f.read()

categories = [
    ('OS', '14'), ('CPU', '142'), ('Board', '112'), ('RAM', '216'), 
    ('SSD', '156'), ('HDD', '42'), ('Cooler', '89'), ('PSU', '98'), 
    ('Case', '75'), ('GPU', '84'), ('Fans', '64'), ('RGB', '32'), 
    ('Accessories', '458', True)
]

tbody = ''
for cat in categories:
    name = cat[0]
    count = cat[1]
    has_sub = len(cat) > 2 and cat[2]
    
    sub_badge = '<span class="ml-3 px-2 py-0.5 rounded bg-surface-container border border-white/10 text-[10px] text-on-surface-variant">Manage Sub-categories</span>' if has_sub else ''
    btn_sub = '<button class="p-1.5 hover:text-secondary transition-colors mr-1" title="Manage Subcategories"><span class="material-symbols-outlined text-sm">account_tree</span></button>' if has_sub else ''
    
    tbody += f'''
                    <tr class="hover:bg-white/5 transition-colors">
                        <td class="p-4 font-bold text-on-surface">{name}{sub_badge}</td>
                        <td class="p-4 text-on-surface-variant">{count}</td>
                        <td class="p-4"><span class="px-2.5 py-1 rounded-full bg-cyber-teal/20 text-cyber-teal text-xs font-bold border border-cyber-teal/30">Active</span></td>
                        <td class="p-4 text-right">
                            {btn_sub}
                            <button class="p-1.5 hover:text-primary transition-colors"><span class="material-symbols-outlined text-sm">edit</span></button>
                            <button class="p-1.5 hover:text-error transition-colors"><span class="material-symbols-outlined text-sm">delete</span></button>
                        </td>
                    </tr>'''

pattern = r'<tbody class="divide-y divide-white/5">.*?</tbody>'
replacement = f'<tbody class="divide-y divide-white/5">{tbody}\n                </tbody>'
new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

with open('product-categories.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print('Categories updated successfully')
