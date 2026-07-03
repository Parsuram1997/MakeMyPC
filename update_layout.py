import re

def main():
    filepath = 'c:/Projects/MakeMyPC/compare-products.html'
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    # 1. Remove the fixed aside and place it inside a wrapper with main
    # Find the aside
    aside_pattern = re.compile(r'(<!-- Side Stats Bar \(Locked to Right\) -->\s*<aside class="fixed right-0 xl:right-\[calc\(50vw-640px\)\] top-20 h-screen w-80 border-l border-white/10 bg-surface-glass backdrop-blur-lg shadow-2xl flex flex-col p-6 gap-y-8 z-40 hidden xl:flex">.*?</aside>)', re.DOTALL)
    
    match = aside_pattern.search(content)
    if not match:
        print("Aside not found")
        return
        
    aside_content = match.group(1)
    # Remove the aside from its original place
    content = content.replace(aside_content, '')
    
    # Change the aside class to be sticky instead of fixed
    aside_content = aside_content.replace('fixed right-0 xl:right-[calc(50vw-640px)] top-20 h-screen', 'sticky top-20 h-[calc(100vh-5rem)]')

    # Find the main tag
    main_start = '<main class="max-w-container-max mx-auto px-margin-desktop py-12 md:pr-96 lg:pr-margin-desktop xl:pr-[360px]">'
    if main_start not in content:
        print("Main start not found")
        return
        
    # Replace main start with wrapper + main start (with modified padding)
    # We remove xl:pr-[360px] from main since flex will handle it. We keep px-margin-desktop on wrapper?
    # No, it's better to keep px-margin-desktop on main and add right padding to it maybe?
    # Let's wrap them in a max-w container
    wrapper_start = '<div class="max-w-container-max mx-auto flex w-full relative">\n'
    new_main_start = '<main class="flex-1 min-w-0 px-margin-desktop py-12">'
    
    content = content.replace(main_start, wrapper_start + new_main_start)
    
    # Find the end of main
    main_end = '</main>'
    # We need to insert the aside right before the end of the wrapper
    # which is right after </main>
    wrapper_end = '</main>\n' + aside_content + '\n</div>'
    content = content.replace(main_end, wrapper_end)

    # 2. Fix the footer by removing the xl:pr-[360px]
    content = content.replace('gap-gutter xl:pr-[360px]">', 'gap-gutter">')
    content = content.replace('text-center xl:pr-[360px]">', 'text-center">')

    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully restructured layout for sticky sidebar")
    except Exception as e:
        print(f"Error writing file: {e}")

if __name__ == "__main__":
    main()
