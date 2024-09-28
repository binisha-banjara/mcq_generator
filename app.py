from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_mcqs(grade, subject, subtopic, num_questions):
    messages = [
        {
            "role": "system",
            "content": f"""
I want you to act as a helpful assistant that generates well-structured multiple-choice questions (MCQs) based on the following instructions.
Create {num_questions} multiple-choice questions for students in grade {grade} on the subject of {subject} and the topic "{subtopic}".
The questions should be tailored to the knowledge level of {grade} grade students.

For each question:
- Provide 4 answer options (labeled A, B, C, and D).
- Ensure one of the options is the correct answer, and clearly label it as the correct one.
- Use simple language for younger grades (e.g., 1st-4th), but incorporate more complex and analytical thinking for higher grades (e.g., 9th-12th).
- Avoid ambiguous or misleading options.

Make sure the questions effectively assess the students' understanding of the topic.

           """.strip(),
        }
    ]
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages)  
            
    generated_text = response.choices[0].message.content
    print(generated_text)
    
    return generated_text


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate_mcqs", methods=["POST"])
def get_mcqs():
    grade = request.form["grade"]
    subject = request.form["subject"]
    subtopic = request.form["subtopic"]
    num_questions = request.form["num_questions"]
    mcqs = generate_mcqs(grade, subject, subtopic, num_questions)

    return jsonify({"mcqs": mcqs})


if __name__ == "__main__":
    app.run(debug=True)
