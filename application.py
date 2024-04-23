from flask import Flask, render_template, request, jsonify
import openai
import os

app = Flask(__name__)

device = 'cpu'

model_mapping = {
    'adventure': 'adventure',
    'horror': 'horror',
    'science fiction': 'science fiction'
}
openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        data = request.get_json()
        prompt = data.get("storyStart", "")
        theme = data.get("storyTheme", "").lower()

        model_name = "ft:gpt-3.5-turbo-0125:the-dot-store:adv3:9HEuqfo9"

        story = "ir"
        response = openai.ChatCompletion.create(
            model=model_name,
            messages=[{"role": "system", "content": "Generate a story continuation in the theme" + model_mapping[theme] + "after this line - "},
                        {"role": "user", "content": prompt}],
            temperature=0.7
        )
        story = response['choices'][0]['message']['content']

        return jsonify(story=story)


    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)