import webbrowser


class Browser:

    def __init__(self):

        self.websites = {
            "google": "https://www.google.com",
            "youtube": "https://www.youtube.com",
            "github": "https://github.com",
            "chatgpt": "https://chatgpt.com",
            "gmail": "https://mail.google.com",
            "instagram": "https://instagram.com",
            "facebook": "https://facebook.com",
            "netflix": "https://netflix.com",
            "amazon": "https://amazon.in",
            "linkedin": "https://linkedin.com",
            "spotify": "https://spotify.com",
            "x": "https://x.com"
        }

    def open_site(self, site):

        site = site.lower()

        if site in self.websites:
            webbrowser.open(self.websites[site])
            return True

        return False

    def google_search(self, query):

        url = "https://www.google.com/search?q=" + query.replace(" ", "+")

        webbrowser.open(url)
