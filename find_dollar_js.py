import glob, re

js_files = glob.glob(r'c:\Projects\MakeMyPC\js\*.js')
for f in js_files:
    with open(f, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            # Find all indices of '$'
            for match in re.finditer(r'\$', line):
                idx = match.start()
                # Check if it's not followed by '{'
                if idx + 1 < len(line) and line[idx+1] != '{':
                    print(f'{f}:{i+1}: {line.strip()}')
                    break # just print once per line
