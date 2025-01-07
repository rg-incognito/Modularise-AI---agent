from crewai import Crew, Process
from tasks import create_tasks

def run_crew(url: str):
    tasks = create_tasks()
    crew = Crew(
        agents=[task.agent for task in tasks],
        tasks=tasks,
        verbose=1,
        process=Process.sequential  # Ensure tasks run sequentially
    )

    results = []
    for task in tasks:
        result = task.execute(url=url)
        results.append(result)

    # Log the results
    print('#######################################')
    for result in results:
        print(result)

    return results

if __name__ == "__main__":
    url = "https://llama.meta.com/docs/model-cards-and-prompt-formats"
    run_crew(url)
