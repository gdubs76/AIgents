import openai
import os
import time
import sys
from dotenv import load_dotenv

'''
This simple job assistant program takes 4 inputs and outputs 4 files:
    inputs:
        job_title, company_name, job_description, and original_resume
    outputs:
        new_resume, coverletter, interview_questions, interviewee questions

Usage:
    python -m jobassistant <job_title> <company_name>
    
Upload your original resume and a job description in a directory where this program will run.
You can name them however you wish but you will have to edit the script to reflect your desired nameing convention. 
This script uses "original_resume" and "job_description" for those names.
An OPENAI_API_KEY will be required as well as a funded account.
The OPENAI_API_KEY for this sript is saved in a .env file in the same directory.
The format for the .env file is:
    OPENAI_API_KEY = "<YOUR_OPENAI_API_KEY>"
    
'''
# Define global variables -- they can also be included in a .env file
company_name = sys.argv[2]
job_title = sys.argv[1]

# Load .env file
load_dotenv()

# Set your OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

# Define generic Agent Class
class Agent:
    def __init__(self, name):
        self.name = name

    def communicate(self, message):
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message}
            ],
            max_tokens=1500
        )
        return response['choices'][0]['message']['content'].strip()

# Specific agent class inheriting from Agent class
class ResumeAgent(Agent):
    def __init__(self):
        super().__init__("Resume Agent")

    def write_resume(self, original_resume, job_description, job_title, company_name):
        message = f"Using the provided resume and job description, rewrite a new more ideal resume for the {job_title} position at {company_name}: {original_resume}, {job_description}."
        new_resume = self.communicate(message)
        save_output_to_file(f'resume_{company_name}.txt', new_resume)
        return new_resume

class CoverletterAgent(Agent):
    def __init__(self):
        super().__init__("Coverletter Agent")

    def write_coverletter(self, job_description, job_title, company_name):
        message = f"Using the following job description, write a cover letter for an application for the {job_title} position at {company_name}: {job_description}"
        coverletter = self.communicate(message)
        save_output_to_file(f'coverletter_{company_name}.txt', coverletter)
        return coverletter

class HiringManagerAgent(Agent):
    def __init__(self):
        super().__init__("Reviewer Agent")

    def write_interview_questions(self, job_description):
        message = f"Compile a list of interview questions for the following job description as well as their appropriate answers: {job_description}."
        interview_questions = self.communicate(message)
        save_output_to_file(f'interview_questions_{company_name}.txt', interview_questions)
        return interview_questions

class IntervieweeAgent(Agent):
    def __init__(self):
        super().__init__("Recoder Agent")

    def write_myQuestions(self, job_description, job_title):
        message = f"Using the attached {job_description}, please provide questions an interviewee should ask a potential employer to let the potential employer know one is qualified to fit the {job_title} position."
        my_questions = self.communicate(message)
        save_output_to_file(f'my_questions_{company_name}.txt', my_questions)
        return my_questions

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
    job_description = read_prompt_from_file('job_description.txt')
    if not job_description:
        print("No job description provided.")
    
    original_resume = read_prompt_from_file('original_resume.txt')
    if not original_resume:
        print("No resume provided.")
    
    # Instantiate agents
    resume = ResumeAgent()
    cover = CoverletterAgent()
    manager = HiringManagerAgent()
    me = IntervieweeAgent()

    # Execute the workflow
    new_resume = resume.write_resume(original_resume, job_description, job_title, company_name)
    time.sleep(10)
    coverletter = cover.write_coverletter(job_description, job_title, company_name)
    time.sleep(10)
    interview_questions = manager.write_interview_questions(job_description)
    time.sleep(10)
    interviewee = me.write_myQuestions(job_description, job_title)
    time.sleep(10)

if __name__ == "__main__":
    main()
