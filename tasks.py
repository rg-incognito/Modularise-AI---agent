from crewai import Task
from agent import WebScraperAgent

def create_tasks():
    agent = WebScraperAgent()

    scrape_task = Task(
        description='Scrape the website and extract HTML, CSS, and JavaScript.',
        agent=agent,
        expected_output='HTML, CSS, and JavaScript content separated in a structured format.',
        method=agent.scrape_website
    )

    return [scrape_task]
