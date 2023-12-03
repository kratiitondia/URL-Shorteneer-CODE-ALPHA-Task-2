#Users can input a long URL, and the program will generate a shorter, unique URL that redirects to the original link.
import string
import random

class URLShortener:
    def __init__(self):
        self.url_mapping = {}
    def generate_short_url(self):
        characters = string.ascii_letters + string.digits
        short_url = 'https://' + ''.join(random.choice(characters) for _ in range(6))
        return short_url

    def shorten_url(self, long_url):
        if long_url in self.url_mapping:
            return self.url_mapping[long_url]

        short_url = self.generate_short_url()
        self.url_mapping[long_url] = short_url
        return short_url

    def redirect_to_original(self, short_url):
        for long_url, shortened in self.url_mapping.items():
            if short_url == shortened:
                return long_url
        return None

if __name__ == "__main__":
    url_shortener = URLShortener()

    # User input for a long URL
    long_url = input("Enter a long URL: ")

    # Shorten the URL
    short_url = url_shortener.shorten_url(long_url)
    print(f"Shortened URL: {short_url}")

    # Simulate redirecting to the original URL
    user_input_short_url = input("Enter the shortened URL to redirect: ")

    # Check if the input shortened URL is valid
    original_url = url_shortener.redirect_to_original(user_input_short_url)

    if original_url:
        print(f"Redirecting to Original URL: {original_url}")
    else:
        print("Invalid or not found in mapping.")
