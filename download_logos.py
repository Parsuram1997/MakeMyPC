import urllib.request
import os

def main():
    os.makedirs('c:/Projects/MakeMyPC/images', exist_ok=True)
    
    # Download Amazon Icon (Square PNG)
    amazon_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Amazon_icon.svg/1024px-Amazon_icon.svg.png"
    try:
        urllib.request.urlretrieve(amazon_url, 'c:/Projects/MakeMyPC/images/amazon-icon.png')
        print("Downloaded Amazon icon.")
    except Exception as e:
        print(f"Failed to download Amazon: {e}")

    # Download Flipkart Icon (Square PNG)
    # Since Wikipedia might not have a reliable square PNG for Flipkart, we use a known good one.
    flipkart_url = "https://seeklogo.com/images/F/flipkart-logo-3F33927DAA-seeklogo.com.png"
    # Alternative Flipkart URL if seeklogo blocks python urllib (403 Forbidden)
    flipkart_alt_url = "https://cdn.iconscout.com/icon/free/png-256/free-flipkart-226594.png"
    try:
        req = urllib.request.Request(flipkart_alt_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response, open('c:/Projects/MakeMyPC/images/flipkart-icon.png', 'wb') as out_file:
            out_file.write(response.read())
        print("Downloaded Flipkart icon.")
    except Exception as e:
        print(f"Failed to download Flipkart: {e}")

if __name__ == "__main__":
    main()
