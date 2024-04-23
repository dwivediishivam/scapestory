from flask import Flask, render_template, request, jsonify
import transformers

app = Flask(__name__)

device = 'cpu'

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        data = request.get_json()
        prompt = data.get("storyStart")
        theme = data.get("storyTheme", "").lower()

        if not prompt or not theme:
            return jsonify({"error": "Missing story start or theme"}), 400

        # model_path = f"/path/to/{theme}_story_model"
        # model = transformers.AutoModelForCausalLM.from_pretrained(model_path)
        # tokenizer = transformers.AutoTokenizer.from_pretrained(model_path)

        # prompt_text = f"Generate a {theme} story given the beginning of the story: {prompt}"
        # inputs = tokenizer(prompt_text, return_tensors="pt", add_special_tokens=True).to(device)

        # outputs = model.generate(**inputs, max_new_tokens=500, do_sample=True, pad_token_id=tokenizer.eos_token_id)
        # story = tokenizer.decode(outputs[0], skip_special_tokens=True)

        story = prompt + theme

        return jsonify(story=story)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
