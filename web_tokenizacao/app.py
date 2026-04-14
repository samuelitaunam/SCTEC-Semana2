from flask import Flask, render_template, request
import tiktoken
from transformers import AutoTokenizer

app = Flask(__name__)

# Modelos Hugging Face
HF_MODELS = [
    ("bert-base-uncased", "WordPiece (BERT)"),
    ("distilbert-base-uncased", "WordPiece (DistilBERT)"),
    ("roberta-base", "BPE (RoBERTa)"),
    ("gpt2", "BPE (GPT-2)"),
    ("t5-small", "SentencePiece (T5)"),
    ("xlnet-base-cased", "SentencePiece (XLNet)"),
    ("albert-base-v2", "SentencePiece (ALBERT)")
]
OPENAI_ENCODINGS = ["cl100k_base", "o200k_base"]

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    text = ''
    if request.method == 'POST':
        text = request.form['text']
        result = {}
        # OpenAI/tiktoken
        for enc_name in OPENAI_ENCODINGS:
            enc = tiktoken.get_encoding(enc_name)
            ids = enc.encode(text)
            pieces = [enc.decode([tok]) for tok in ids]
            result[f"OpenAI: {enc_name}"] = {
                'algo': 'BPE',
                'tokens': pieces,
                'ids': ids
            }
        # Hugging Face
        for model_name, algo in HF_MODELS:
            try:
                tokenizer = AutoTokenizer.from_pretrained(model_name)
                tokens = tokenizer.tokenize(text)
                ids = tokenizer.encode(text, add_special_tokens=False)
                result[f"HF: {model_name}"] = {
                    'algo': algo,
                    'tokens': tokens,
                    'ids': ids
                }
            except Exception as e:
                result[f"HF: {model_name}"] = {
                    'algo': algo,
                    'tokens': [f"Erro: {e}"],
                    'ids': []
                }
    return render_template('index.html', result=result, text=text)

if __name__ == '__main__':
    app.run(debug=True)
