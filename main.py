import os
from flask import Flask, request, jsonify, render_template
import openai

# Set up the OpenAI API key from Replit's secrets manager
openai.api_key = os.environ['OPENAI_API_KEY']

app = Flask(__name__)

# System prompt for ChatGPT to act as a size matcher
system_prompt = """
You are a size-matching assistant. Users will provide their known size in one brand, 
and you should respond with equivalent sizes in other brands based on the data provided.
When a user mentions a brand and size (e.g., "I wear Nike Medium"), 
respond with the equivalent size in the requested brand.
"""

# Function to handle ChatGPT responses
def get_size_match_response(user_message):
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_message}
    ]

    try:
        # Call the OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=100
        )
        # Extract and return the response content
        return response.choices[0].message['content'].strip()
    except openai.error.OpenAIError as e:
        print(f"OpenAI API error: {e}")
        return "There was an error processing your request."

# Route for the chatbot HTML interface
@app.route('/')
def index():
    return render_template('index.html')

# API route for the chatbot
@app.route('/size-match', methods=['POST'])
def size_match():
    data = request.get_json()
    user_message = data.get("message")

    # Get response from ChatGPT
    bot_response = get_size_match_response(user_message)

    return jsonify({"response": bot_response})

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
