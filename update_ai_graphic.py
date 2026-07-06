import sys

with open('generate_shop.py', 'r', encoding='utf-8') as f:
    text = f.read()

old_graphic = """      <!-- Right: floating visualization -->
      <div class="hidden lg:flex flex-col items-center justify-center" style="min-width:260px;">
        <div class="relative w-56 h-56">
          <div class="absolute inset-0 rounded-full" style="border:1px solid rgba(0,122,255,0.2);animation:spin 15s linear infinite;"></div>
          <div class="absolute inset-6 rounded-full" style="border:1px solid rgba(0,164,166,0.2);animation:spin 10s linear infinite reverse;"></div>
          <div class="absolute inset-12 rounded-2xl flex items-center justify-center" style="background:linear-gradient(135deg,#001a4d,#003399);border:1px solid rgba(0,122,255,0.5);box-shadow:0 0 30px rgba(0,122,255,0.3);">
            <span class="ms" style="font-size:40px;color:#007AFF;">auto_awesome</span>
          </div>
          <div class="absolute top-4 right-0 px-2 py-1 rounded-lg text-xs font-bold float-1" style="background:rgba(0,164,166,0.2);border:1px solid rgba(0,164,166,0.4);color:#00A4A6;">AI</div>
          <div class="absolute bottom-6 left-0 px-2 py-1 rounded-lg text-xs font-bold float-2" style="background:rgba(52,211,153,0.15);border:1px solid rgba(52,211,153,0.4);color:#34d399;">✓ FIT</div>
          <div class="absolute top-1/2 -right-4 px-2 py-1 rounded-lg text-xs font-bold float-3" style="background:rgba(167,139,250,0.15);border:1px solid rgba(167,139,250,0.4);color:#a78bfa;">PCIe</div>
        </div>
        <div class="text-center mt-6">
          <div style="font-size:14px;font-weight:700;color:#adc6ff;">AI Compatibility Engine</div>
          <div style="font-size:12px;color:#c1c6d7;margin-top:4px;">Checks 50+ compatibility points</div>
        </div>
      </div>"""

new_graphic = """      <!-- Right: floating visualization -->
      <div class="hidden lg:flex flex-col items-center justify-center flex-1 w-full" style="min-width:320px;">
        <div class="relative w-80 h-80">
          <div class="absolute inset-0 rounded-full" style="border:1px solid rgba(0,122,255,0.2);animation:spin 15s linear infinite;"></div>
          <div class="absolute inset-8 rounded-full" style="border:1px solid rgba(0,164,166,0.2);animation:spin 10s linear infinite reverse;"></div>
          <div class="absolute inset-16 rounded-3xl flex items-center justify-center" style="background:linear-gradient(135deg,#001a4d,#003399);border:1px solid rgba(0,122,255,0.5);box-shadow:0 0 40px rgba(0,122,255,0.4);">
            <span class="ms" style="font-size:64px;color:#007AFF;">auto_awesome</span>
          </div>
          <div class="absolute top-8 right-4 px-3 py-1.5 rounded-lg text-sm font-bold float-1" style="background:rgba(0,164,166,0.2);border:1px solid rgba(0,164,166,0.4);color:#00A4A6;">AI</div>
          <div class="absolute bottom-10 left-2 px-3 py-1.5 rounded-lg text-sm font-bold float-2" style="background:rgba(52,211,153,0.15);border:1px solid rgba(52,211,153,0.4);color:#34d399;">✓ FIT</div>
          <div class="absolute top-1/2 -right-6 px-3 py-1.5 rounded-lg text-sm font-bold float-3" style="background:rgba(167,139,250,0.15);border:1px solid rgba(167,139,250,0.4);color:#a78bfa;">PCIe</div>
        </div>
        <div class="text-center mt-10">
          <div style="font-size:18px;font-weight:700;color:#adc6ff;">AI Compatibility Engine</div>
          <div style="font-size:14px;color:#c1c6d7;margin-top:6px;">Checks 50+ compatibility points in real-time</div>
        </div>
      </div>"""

if old_graphic in text:
    text = text.replace(old_graphic, new_graphic)
    print("Graphic updated in generate_shop.py.")
    with open('generate_shop.py', 'w', encoding='utf-8') as f:
        f.write(text)
else:
    print("Pattern not found. Checking for partial match.")
    idx = text.find('floating visualization')
    print("Context around floating visualization:\n" + text[max(0, idx-100):idx+500])
