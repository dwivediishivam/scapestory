from flask import Flask, render_template, request, jsonify
import openai
import os

app = Flask(__name__)

device = 'cpu'


model_mapping = {
    'adventure': 'ft:gpt-3.5-turbo-0125:the-dot-store:adv3:9HEuqfo9',
    'horror': 'horror-model-name',
    'sci-fi': 'sci-fi-model-name'
}
openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        data = request.get_json()
        prompt = data.get("storyStart", "")
        theme = data.get("storyTheme", "").lower()

        model_name = model_mapping.get(theme, 'gpt-3.5-turbo-0125')

        try:
            response = openai.Completion.create(
                model=model_name,
                prompt=prompt,
                max_tokens=150,
                temperature=0.7
            )
            story = response.choices[0].text.strip()
        except Exception as e:
            return jsonify(error=str(e)), 500
        
        return jsonify(story=story)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)