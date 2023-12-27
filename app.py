# Install necessary libraries:
# pip install Flask openai

from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Set your OpenAI GPT-3 API key
openai.api_key = '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'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_ebook():
    user_input = request.form['user_input']

    # Customize the prompt and parameters based on your needs
    prompt = f"Write an ebook on the topic: {user_input}"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=2000  # Set your desired word limit
    )

    generated_text = response['choices'][0]['text']
    return render_template('result.html', generated_text=generated_text)

if __name__ == '__main__':
    app.run(debug=True)
