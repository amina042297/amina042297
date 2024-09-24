
# Statement Checker

This project provides a tool to check the correctness of statements against text extracted from PPT or PDF files using mpnet (Sentence Transformer) and GPT models.

## Project Structure

statement_checker/
│
├── main.py # Main entry point for the Streamlit application
├── functions.py # functions for text processing and statement checking
├── gpt_utils.py # Functions related to GPT-4
├── requirements.txt # Python dependencies required to run the project
└── __init__.py # Marks the directory as a package



## Setup Instructions

- Create a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate 

- Install the required dependencies:

pip install -r requirements.txt

- Run the Streamlit application with the following command:

streamlit run main.py

- in Streamlite application you can upload ppt/pdf documents, write statements to check.
