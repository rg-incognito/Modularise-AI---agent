import requests
from bs4 import BeautifulSoup

class WebScraper:
    def __init__(self, url):
        self.url = url
        self.html_content = ""
        self.css_content = []
        self.js_content = []

    def scrape(self):
        try:
            response = requests.get(self.url)
            if response.status_code != 200:
                raise Exception(f"Failed to retrieve the URL. Status code: {response.status_code}")

            soup = BeautifulSoup(response.text, 'html.parser')
            self.html_content = soup.prettify()
            self._scrape_css(soup)
            self._scrape_js(soup)
            return self._format_result()

        except Exception as e:
            return {"error": str(e)}

    def _scrape_css(self, soup):
        for style in soup.find_all('style'):
            self.css_content.append(style.get_text())
        for link in soup.find_all('link', rel='stylesheet'):
            css_url = link['href']
            if not css_url.startswith('http'):
                css_url = requests.compat.urljoin(self.url, css_url)
            css_response = requests.get(css_url)
            if css_response.status_code == 200:
                self.css_content.append(css_response.text)

    def _scrape_js(self, soup):
        for script in soup.find_all('script'):
            if script.get('src'):
                js_url = script['src']
                if not js_url.startswith('http'):
                    js_url = requests.compat.urljoin(self.url, js_url)
                js_response = requests.get(js_url)
                if js_response.status_code == 200:
                    self.js_content.append(js_response.text)
            else:
                self.js_content.append(script.get_text())

    def _format_result(self):
        return {
            "html": self.html_content,
            "css": "\n".join(self.css_content),
            "javascript": "\n".join(self.js_content)
        }
