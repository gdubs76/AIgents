import openai
import os
from dotenv import load_dotenv
import time

load_dotenv()

# Set your OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

class Agent:
    def __init__(self, name):
        self.name = name

    def communicate(self, message):
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=message,
            max_tokens=1500
        )
        return response.choices[0].text.strip()

class PlannerAgent(Agent):
    def __init__(self):
        super().__init__("Planner Agent")

    def plan_task(self, task):
        message = f"Plan the following coding task: {task}"
        plan = self.communicate(message)
        save_output_to_file('plan.txt', plan)
        return plan

class CoderAgent(Agent):
    def __init__(self):
        super().__init__("Coder Agent")

    def write_code(self, plan):
        message = f"Write the code according to this plan: {plan}"
        code = self.communicate(message)
        save_output_to_file('code.py', code)
        return code

class ReviewerAgent(Agent):
    def __init__(self):
        super().__init__("Reviewer Agent")

    def review_code(self, code):
        message = f"Review the following code and suggest improvements: {code}"
        review = self.communicate(message)
        save_output_to_file('review.txt', review)
        return review

class RecoderAgent(Agent):
    def __init__(self):
        super().__init__("Recoder Agent")

    def rewrite_code(self, code, review):
        message = f"Rewrite the code according to this review and the original code: {review}\n\nOriginal Code:\n{code}"
        revised_code = self.communicate(message)
        save_output_to_file('revised_code.py', revised_code)
        return revised_code

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
    task = input("Enter the coding task: ").strip()
    if not task:
        task = read_prompt_from_file('prompt.txt')
        if not task:
            print("No task provided.")
            return

    # Instantiate agents
    planner = PlannerAgent()
    coder = CoderAgent()
    reviewer = ReviewerAgent()
    recoder = RecoderAgent()

    # Execute the workflow
    plan = planner.plan_task(task)
    time.sleep(10)
    code = coder.write_code(plan)
    time.sleep(10)
    review = reviewer.review_code(code)
    time.sleep(10)
    recoded_code = recoder.rewrite_code(code, review)
    time.sleep(10)

    # Output the results
    print("Plan:\n", plan)
    print("Code:\n", code)
    print("Review:\n", review)
    print("Revised Code:\n", recoded_code)

if __name__ == "__main__":
    main()
