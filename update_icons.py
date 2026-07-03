import re

def main():
    filepath = 'c:/Projects/MakeMyPC/js/builder-app.js'
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    # Replace the Amazon button
    amazon_regex = re.compile(r'<a href="https://amazon.in/s\?k=[^"]+" target="_blank" title="Buy on Amazon" class="w-12 h-12 flex-shrink-0 flex items-center justify-center border border-white/10 rounded-lg hover:bg-\[#FF9900\]/10 transition-all text-\[#FF9900\] group/amz">.*?</a>', re.DOTALL)
    
    new_amazon = '''<a href="https://amazon.in/s?k=${encodeURIComponent(part.brand + ' ' + part.model)}" target="_blank" title="Buy on Amazon" class="w-12 h-12 flex-shrink-0 flex items-center justify-center border border-white/10 rounded-lg hover:bg-[#FF9900]/10 transition-all text-[#FF9900] group/amz p-2">
                            <svg role="img" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" fill="currentColor" class="w-full h-full group-hover/amz:scale-110 transition-transform">
                                <path d="M13.882 17.587c-2.316.924-4.708 1.4-6.848 1.4-2.825 0-4.664-.476-4.664-.476.368.96 1.637 1.777 3.328 2.053 2.378.435 5.094.343 7.568-.313 1.15-.316 2.062-.843 2.062-.843l-1.446-1.82zM12.22 8.718c-.802 0-1.39.29-1.724.97-.13.3-.223.774-.223 1.258 0 1.22.28 1.968.805 2.502.493.523 1.144.693 1.956.693.687 0 1.206-.21 1.576-.412v-1.61c-.413.284-.91.433-1.343.433-.61 0-1.015-.226-1.223-.54-.22-.32-.224-.8-.224-1.35v-1.1h2.984v-1.2h-2.984V6.02h-1.61v2.33h-.995v1.2h.995v1.48c0 .927.203 1.636.577 2.128.434.524.966.71 1.868.71.97 0 1.79-.24 2.158-.403v-1.18c-.428-.276-1.14-.6-2.18-.6z"/>
                            </svg>
                        </a>'''

    content = amazon_regex.sub(new_amazon, content)

    # Replace the Flipkart button
    flipkart_regex = re.compile(r'<a href="https://www.flipkart.com/search\?q=[^"]+" target="_blank" title="Buy on Flipkart" class="w-12 h-12 flex-shrink-0 flex items-center justify-center border border-white/10 rounded-lg hover:bg-\[#2874F0\]/10 transition-all text-\[#2874F0\] group/fk">.*?</a>', re.DOTALL)

    new_flipkart = '''<a href="https://www.flipkart.com/search?q=${encodeURIComponent(part.brand + ' ' + part.model)}" target="_blank" title="Buy on Flipkart" class="w-12 h-12 flex-shrink-0 flex items-center justify-center border border-white/10 rounded-lg hover:bg-[#2874F0]/10 transition-all group/fk p-2">
                            <img src="images/flipkart-icon.png" alt="Flipkart" class="w-full h-full object-contain group-hover/fk:scale-110 transition-transform">
                        </a>'''

    content = flipkart_regex.sub(new_flipkart, content)

    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully updated icons in builder-app.js")
    except Exception as e:
        print(f"Error writing file: {e}")

if __name__ == "__main__":
    main()
