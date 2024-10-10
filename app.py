from flask import Flask, render_template, request, jsonify
from transformers import BertTokenizer, BertForSequenceClassification, pipeline
import torch
import pickle

app = Flask(__name__)

# Load the classification model
bert_model = pickle.load(open('classification.pkl', 'rb'))
bert_tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# Create the text generation pipeline directly 
gpt2_generator = pipeline('text-generation', model='gpt2')

# Home route to render the interface
@app.route('/')
def home():
    return render_template('index.html')

# text classification
@app.route('/classify', methods=['POST'])
def classify():
    input_text = request.form['text']
    tokens = bert_tokenizer.encode(input_text, return_tensors='pt')
    with torch.no_grad():
        result = bert_model(tokens).logits.argmax().item()
    sentiment = "positive" if result == 1 else "negative"
    return jsonify({'classification': sentiment})

# text generation
@app.route('/generate', methods=['POST'])
def generate():
    prompt = request.form['prompt']
    generated_text = gpt2_generator(prompt, max_length=100, num_return_sequences=1, truncation=True)
    return jsonify({'generated_text': generated_text[0]['generated_text']})

if __name__ == "__main__":
    app.run(debug=True)
