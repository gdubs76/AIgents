## AIgents
This is a repository for AI agents.

The intention for this project is to build a generic AI agent framework for agent collaboration using OpenAI APIs that will allow users to specify the number of agents and each agents' "expertise".
It will allow users to provide a prompt from user input or a specified "prompt.txt" file.

In this repository there are some examples of how agent collaboration can be used:
  
  coder.py: This script takes a specified coding task as either user input or a specified prompt.txt file, creates a plan using pseudo code, writes the code, reviews the code, and rewrites it to the new recommended changes. Each agent creates its own file which will be saved in the current directory.

  jobassistant.py: This script requires an original resume and a job desciption in txt format be located in the same directory. It returns a new resume, potential interview questions, a coverletter, and questions that should be asked by the interviewee at the time of interview.

searchoptomi.py: This script takes a search query and returns new search queries, a deatailed search of the new queries, and a summery of that report.
