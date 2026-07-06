text = open('index.html', encoding='utf-8').read()
start = text.find('NAVBAR START')
end = text.find('NAVBAR END')
nav_block = text[start:end+50]

# Find Shop href more precisely
idx2 = nav_block.find('>Shop<')
if idx2 > 0:
    chunk = nav_block[max(0, idx2-250):idx2+30]
    print('Full Shop link area:')
    print(chunk)
    print()

# Also check mobile menu
idx3 = nav_block.find('Shop <span')
if idx3 < 0:
    idx3 = nav_block.find('Shop\n')
if idx3 > 0:
    chunk2 = nav_block[max(0, idx3-200):idx3+80]
    print('Mobile Shop area:')
    print(chunk2)
