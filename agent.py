from crewai import Agent
from langchain_ollama import ChatOllama
from scraper import WebScraper

class WebScraperAgent(Agent):
    def __init__(self):
        llm = ChatOllama(model="llama3.1", base_url="http://localhost:11434")
        super().__init__(
            role='Web Scraper',
            goal='Scrape the website and analyze the HTML, CSS, and JS content',
            backstory='30 years of experience in web design, former SDE at Amazon, and extensive experience in architecture design',
            verbose=True,
            allow_delegation=False,
            llm=llm
        )

    def scrape_website(self, url: str):
        scraper = WebScraper(url)
        return scraper.scrape()
