import re

file_path = "c:/Projects/MakeMyPC/smart-builder.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Change id="step-3" -> "step-4"
content = content.replace('id="step-3"', 'id="step-4"')
content = content.replace('<!-- Step 3: Result -->', '<!-- Step 4: Result -->')

# 2. Change id="step-2" -> "step-3"
content = content.replace('id="step-2"', 'id="step-3"')
content = content.replace('<!-- Step 2: Budget -->', '<!-- Step 3: Budget -->')

# 3. Change id="step-1" -> "step-2" and remove active class
content = content.replace('class="wizard-step active" id="step-1"', 'class="wizard-step" id="step-2"')
content = content.replace('<!-- Step 1: Purpose -->', '<!-- Step 2: Purpose -->')

# 4. Insert new Step 1
os_step_html = """        <!-- Step 1: OS -->
        <div class="wizard-step active" id="step-1">
            <h1 class="text-4xl font-bold text-center mb-4">Which Operating System will you use?</h1>
            <p class="text-center text-on-surface-variant mb-12">We optimize hardware choices based on OS compatibility.</p>
            
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6 max-w-4xl mx-auto">
                <div class="glass-card rounded-2xl p-6 cursor-pointer hover:-translate-y-1 transition-all group border-electric-blue/50 hardware-glow" onclick="smartBuilder.selectOS('windows')">
                    <div class="mb-4 text-electric-blue flex items-center justify-center w-16 h-16 rounded-xl bg-electric-blue/10 mx-auto group-hover:scale-110 transition-transform">
                        <span class="material-symbols-outlined text-4xl">window</span>
                    </div>
                    <h3 class="text-2xl font-bold mb-2 text-center">Windows 11</h3>
                    <p class="text-on-surface-variant text-sm text-center">Best for gaming and broad compatibility.</p>
                </div>
                <div class="glass-card rounded-2xl p-6 cursor-pointer hover:-translate-y-1 transition-all group" onclick="smartBuilder.selectOS('linux')">
                    <div class="mb-4 text-cyber-teal flex items-center justify-center w-16 h-16 rounded-xl bg-cyber-teal/10 mx-auto group-hover:scale-110 transition-transform">
                        <span class="material-symbols-outlined text-4xl">terminal</span>
                    </div>
                    <h3 class="text-2xl font-bold mb-2 text-center">Linux</h3>
                    <p class="text-on-surface-variant text-sm text-center">Optimized with AMD GPUs for open-source drivers.</p>
                </div>
                <div class="glass-card rounded-2xl p-6 cursor-pointer hover:-translate-y-1 transition-all group" onclick="smartBuilder.selectOS('none')">
                    <div class="mb-4 text-primary flex items-center justify-center w-16 h-16 rounded-xl bg-primary/10 mx-auto group-hover:scale-110 transition-transform">
                        <span class="material-symbols-outlined text-4xl">dns</span>
                    </div>
                    <h3 class="text-2xl font-bold mb-2 text-center">No OS / Custom</h3>
                    <p class="text-on-surface-variant text-sm text-center">Standard hardware recommendations.</p>
                </div>
            </div>
        </div>

        <!-- Step 2: Purpose -->"""

content = content.replace('<!-- Step 2: Purpose -->', os_step_html)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated smart-builder.html successfully.")
