import openai
import os
from dotenv import load_dotenv
import time
import sys

load_dotenv()

# Set your OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

# declare file descriptor as fisrt argument
file_name = sys.argv[1]

class Agent:
    def __init__(self, name):
        self.name = name

    def communicate(self, message):
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an expert in search optimization."},
                {"role": "user", "content": message}
            ],
            max_tokens=1500
        )
        return response['choices'][0]['message']['content'].strip()

class OptimizerAgent(Agent):
    def __init__(self):
        super().__init__("Optimizer Agent")

    def optimize_search(self, search):
        message = f"Using the following search query optimize it with better search terms: {search}"
        optimized_search = self.communicate(message)
        save_output_to_file(f'optimized_search_{file_name}.txt', optimized_search)
        return optimized_search

class SearchAgent(Agent):
    def __init__(self):
        super().__init__("Search Agent")

    def search(self, optimized_search):
        message = f"Using the following search terms find as much informations as you can and write a detailed report: {optimized_search}"
        report = self.communicate(message)
        save_output_to_file(f'report_{file_name}.txt', report)
        return report

class ReviewerAgent(Agent):
    def __init__(self):
        super().__init__("Reviewer Agent")

    def summarize_report(self, report):
        message = f"Review the following report and summarize it in bullet points: {report}"
        summary = self.communicate(message)
        save_output_to_file(f'summary_{file_name}.txt', summary)
        return summary

# Function to read prompt from file if it exists
def read_prompt_from_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return file.read().strip()
    return None

# Function to save output to a file
def save_output_to_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

# Main function to handle the workflow
def main():
    # Read task from user input or prompt.txt file
    search = input("Enter search query: ").strip()
    if not search:
        search = read_prompt_from_file('search.txt')
        if not search:
            print("No search provided.")
            return

    # Instantiate agents
    optimizer = OptimizerAgent()
    searcher = SearchAgent()
    reviewer = ReviewerAgent()
  
    # Execute the workflow
    optimized_search = optimizer.optimize_search(search)
    time.sleep(10)
    report = searcher.search(optimized_search)
    time.sleep(10)
    summary = reviewer.summarize_report(report)
    time.sleep(10)
    
    # Output the results
    print("Summary:\n", summary)
    
if __name__ == "__main__":
    main()
