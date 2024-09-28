# MCQ Generator

This is a simple web application built using Flask that allows users to generate multiple-choice questions (MCQs) based on the specified grade, subject, subtopic, and number of questions
by integrating OpenAI API key.

## Features

Take user input (a prompt) and return McQ based on grade, subject, subtopic and number of questions with their respective option.

- Input form to specify the grade, subject, subtopic, and number of questions.
- Generates MCQs using OpenAI's GPT model.

## Prerequisites

- Python 3.x
- Flask
- OpenAI Python package
- jQuery

## Installation

1. **Clone the repository**:

   ```bash
   git clone <https://github.com/binisha-banjara/mcq_generator>
   
2. **Set up a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
3. **Install required packages:**
   ```bash
   pip install Flask openai python-dotenv
4. ***Create a .env file in the project root and add your OpenAI API key:**
   ```bash
   OPENAI_API_KEY="your_openai_api_key"


## Usage
**Run the application:**

  ```bash
  python app.py

