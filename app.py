import openai
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

openai.api_key = "openai-api-key"


# Function to generate MCQs using OpenAI GPT
def generate_mcqs(grade, subject, subtopic, num_questions):
    prompt = f"Create {num_questions} multiple-choice questions for a {grade} grade {subject} quiz on {subtopic}. Include 4 options with the correct answer labeled."

    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # Or  "gpt-3.5-turbo"
            prompt=prompt,
            max_tokens=1500,  
            n=1,
            stop=None,
            temperature=0.7,
        )

        generated_text = response["choices"][0]["text"].strip()
        return generated_text
    except Exception as e:
        return f"An error occurred: {e}"



if __name__ == "__main__":
    app.run(debug=True)
