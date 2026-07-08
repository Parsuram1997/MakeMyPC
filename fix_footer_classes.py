def fix_footer_classes():
    with open('custom-pc-builder.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # We need to target only the footer area to replace the classes
    import re
    m_footer = re.search(r'<footer.*?</footer>', content, re.DOTALL | re.IGNORECASE)
    if not m_footer:
        print("Could not find footer in custom-pc-builder.html")
        return
        
    footer = m_footer.group(0)
    
    # Replace custom layout classes
    footer = footer.replace('max-w-container-max', 'max-w-[1280px]')
    footer = footer.replace('px-margin-desktop', 'px-6 md:px-16')
    footer = footer.replace('gap-gutter', 'gap-6')
    
    # Replace custom typography classes
    footer = footer.replace('font-headline-sm text-headline-sm', 'text-xl font-semibold')
    footer = footer.replace('font-body-sm text-body-sm', 'text-sm font-normal')
    footer = footer.replace('font-label-mono text-label-mono text-xs', 'font-mono text-xs font-medium uppercase tracking-widest')
    footer = footer.replace('font-label-mono text-label-mono text-on-surface uppercase tracking-widest', 'font-mono text-xs font-medium uppercase tracking-widest text-white')
    
    # Replace colors
    footer = footer.replace('text-electric-blue', 'text-primary')
    footer = footer.replace('text-cyber-teal', 'text-[#10B981]')
    footer = footer.replace('text-on-surface-variant', 'text-on-surface-variant') # Already mapped in tailwind config
    footer = footer.replace('text-on-surface', 'text-white')
    
    # Check for anything that causes overflow, like w-full that might be messing with padding
    footer = footer.replace('<footer class="bg-[#0B1120] border-t border-white/5 w-full">', '<footer class="bg-[#0B1120] border-t border-white/5 w-full overflow-hidden mt-8">')

    content = content.replace(m_footer.group(0), footer)
    
    with open('custom-pc-builder.html', 'w', encoding='utf-8') as f:
        f.write(content)

fix_footer_classes()
print("Fixed footer classes!")
