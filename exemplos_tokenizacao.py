
"""
Exemplos didáticos de tokenização em Python

Inclui exemplos com os modelos mais utilizados:
- OpenAI/tiktoken (BPE)
- Hugging Face: BERT (WordPiece), T5 (SentencePiece), GPT2 (BPE)

Execute este arquivo para ver as diferenças e entender como cada tokenizador funciona.
"""

from transformers import AutoTokenizer
import tiktoken

texts = [
    "Erro no auth-service às 14:32",
    "JSON.parse(user_id)",
    "inconstitucionalissimamente"
]


# OpenAI encodings
openai_encodings = ["cl100k_base", "o200k_base"]

# Hugging Face models e algoritmos
hf_models = [
    ("bert-base-uncased", "WordPiece (BERT)"),
    ("distilbert-base-uncased", "WordPiece (DistilBERT)"),
    ("roberta-base", "BPE (RoBERTa)"),
    ("gpt2", "BPE (GPT-2)"),
    ("t5-small", "SentencePiece (T5)"),
    ("xlnet-base-cased", "SentencePiece (XLNet)"),
    ("albert-base-v2", "SentencePiece (ALBERT)")
]

for text in texts:
    print("\n" + "=" * 80)
    print(f"TEXTO: {text}")

    # OpenAI/tiktoken
    for enc_name in openai_encodings:
        enc = tiktoken.get_encoding(enc_name)
        ids = enc.encode(text)
        pieces = [enc.decode([tok]) for tok in ids]
        print(f"\nOpenAI encoding: {enc_name} (BPE)")
        print("Qtd tokens:", len(ids))
        print("IDs:", ids)
        print("Partes:", pieces)

    # Hugging Face - cada modelo com seu algoritmo
    for model_name, algo in hf_models:
        try:
            tokenizer = AutoTokenizer.from_pretrained(model_name)
            tokens = tokenizer.tokenize(text)
            ids = tokenizer.encode(text, add_special_tokens=False)
            print(f"\nModelo HF: {model_name} [{algo}]")
            print("Qtd tokens:", len(tokens))
            print("Tokens:", tokens)
            print("IDs:", ids)
        except Exception as e:
            print(f"\nModelo HF: {model_name} [{algo}] - ERRO ao carregar/tokenizar: {e}")

print("\n" + "="*30)
print("FIM DOS EXEMPLOS")
print("="*30)

print("\nObservações:")
print("- Cada tokenizador pode dividir o texto de forma diferente.")
print("- O número de tokens e os IDs variam conforme o modelo.")
print("- Para testar outros textos, altere a lista 'texts'.")
