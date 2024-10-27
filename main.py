import random
import string


url_mapping = {}
click_count = {}

def generate_short_url(length=6):
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(characters) for _ in range(length))
    return short_url

def shorten_url(original_url):
    short_url = generate_short_url()

    while short_url in url_mapping:
        short_url = generate_short_url()
    url_mapping[short_url] = original_url
    click_count[short_url] = 0
    return short_url

def redirect_to_url(short_url):
    if short_url in url_mapping:
        click_count[short_url] += 1
        return url_mapping[short_url], click_count[short_url]
    else:
        return None, 0

def main():
    while True:
        print("\nURL Shortener")
        print("1. Shorten a URL")
        print("2. Redirect to a URL")
        print("3. View all URLs")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            original_url = input("Enter the original URL: ")
            short_url = shorten_url(original_url)
            print(f"Shortened URL: {short_url}")

        elif choice == '2':
            short_url = input("Enter the short URL: ")
            original_url, clicks = redirect_to_url(short_url)
            if original_url:
                print(f"Redirecting to: {original_url} (Clicks: {clicks})")
            else:
                print("Short URL not found.")

        elif choice == '3':
            print("\nAll URLs:")
            for short_url, original_url in url_mapping.items():
                print(f"Short URL: {short_url} | Original URL: {original_url} | Clicks: {click_count[short_url]}")

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
