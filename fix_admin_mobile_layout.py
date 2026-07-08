import os
import glob
import re

def fix_admin_mobile_layout():
    project_dir = 'c:/Projects/MakeMyPC'
    html_files = glob.glob(os.path.join(project_dir, 'admin-*.html'))
    
    updated_count = 0
    
    mobile_header = """
        <!-- Mobile Header (Visible only on small screens) -->
        <header class="lg:hidden flex items-center justify-between p-4 bg-surface-deep/80 backdrop-blur-md border border-white/10 mb-6 rounded-2xl shadow-lg sticky top-4 z-40">
            <div class="flex items-center gap-2">
                <h1 class="font-bold text-electric-blue text-lg leading-none">MakeMyPC</h1>
                <span class="bg-primary/20 text-primary text-[10px] font-bold px-1.5 py-0.5 rounded uppercase tracking-wider">Admin</span>
            </div>
            <button id="mobile-menu-btn" class="p-1.5 bg-white/5 hover:bg-white/10 border border-white/10 rounded-lg text-white transition-colors">
                <span class="material-symbols-outlined block">menu</span>
            </button>
        </header>
"""
    
    close_btn = """
        <button id="mobile-menu-close" class="lg:hidden absolute top-4 right-4 p-1.5 bg-white/5 hover:bg-error/20 hover:text-error rounded-lg text-on-surface-variant transition-colors border border-white/10">
            <span class="material-symbols-outlined block text-sm">close</span>
        </button>
"""

    for filepath in html_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        modified = False
        
        # 1. Update <aside> to have ID and responsive classes
        # Look for <aside class="..."> that doesn't already have mobile-menu
        m_aside = re.search(r'<aside([^>]*)class="([^"]*)"([^>]*)>', content)
        if m_aside and 'id="mobile-menu"' not in content:
            pre_attrs = m_aside.group(1)
            classes = m_aside.group(2)
            post_attrs = m_aside.group(3)
            
            # Make sure to add the translation classes
            if '-translate-x-full' not in classes:
                classes += ' -translate-x-full lg:translate-x-0 transition-transform duration-300'
                
            new_aside = f'<aside id="mobile-menu"{pre_attrs}class="{classes}"{post_attrs}>'
            content = content[:m_aside.start()] + new_aside + content[m_aside.end():]
            modified = True

        # 2. Add close button inside the aside (after the Enterprise Admin title div)
        if close_btn.strip() not in content and 'id="mobile-menu-close"' not in content:
            m_shrink = re.search(r'<div class="px-6 mb-4 shrink-0">.*?</div>', content, re.DOTALL)
            if m_shrink:
                content = content[:m_shrink.start()] + m_shrink.group(0) + close_btn + content[m_shrink.end():]
                modified = True
                
        # 3. Inject mobile header immediately inside <main>
        if 'id="mobile-menu-btn"' not in content:
            m_main = re.search(r'<main([^>]*)>', content)
            if m_main:
                content = content[:m_main.end()] + mobile_header + content[m_main.end():]
                modified = True
                
        if modified:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            updated_count += 1
            print(f"Updated {os.path.basename(filepath)}")
            
    print(f"Successfully updated {updated_count} admin files!")

fix_admin_mobile_layout()
