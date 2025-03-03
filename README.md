# AIgents
## This is a repository for AI agents.

The intention for this project is to build a generic AI agent framework for agent collaboration using OpenAI APIs that will allow users to specify the number of agents and each agents' "expertise". 

In this repository there are some examples of how agent collaboration can be used:
  
* #coder.py:
  * _This script takes a specified coding task as either user input or a specified prompt.txt file_
  *  _creates a plan using pseudo code, writes the code, reviews the code, and_
  *  _rewrites it to the new recommended changes. Each agent creates its own file which will be saved in the current directory._

* #jobassistant.py:
  * _This script requires an original resume and a job desciption in txt format be located in the same directory._
  * _It returns a new resume, potential interview questions, a coverletter, and questions that should be asked by the interviewee at the time of interview.

* searchoptomi.py:
  * _This script takes a search query and returns new search queries,_
  * _a deatailed search of the new queries, and a summery of that report._

## Some instructions:

_To use any of the collaboration scripts you need a funded OpenAI account and API key. Use the .env file template to store your key as an environment variable._ 

_Coder.py requires the ext.py module so you can code in other supported languages and save the files in their proper format. Other programming languages can be added to the dict as needed; e.g., SQL isn't included._

