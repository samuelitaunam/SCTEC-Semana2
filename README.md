<<<<<<< HEAD
# SCTEC-Semana2
Exemplos didáticos de tokenização em Python
=======
# Exemplos Didáticos de Tokenização em Python

Este repositório contém exemplos práticos e didáticos de tokenização utilizando os principais modelos e algoritmos do mercado, incluindo OpenAI/tiktoken e modelos da Hugging Face (BERT, DistilBERT, RoBERTa, GPT-2, T5, XLNet, ALBERT).

## Objetivo

Demonstrar, de forma clara e comparativa, como diferentes tokenizadores segmentam textos, mostrando a quantidade de tokens, os IDs e as partes resultantes para cada modelo.

## Principais Modelos e Algoritmos Demonstrados

- **OpenAI/tiktoken (BPE)**: Usado em modelos GPT-3, GPT-4, ChatGPT, etc.
- **BERT (WordPiece)**: `bert-base-uncased`
- **DistilBERT (WordPiece)**: `distilbert-base-uncased`
- **RoBERTa (BPE)**: `roberta-base`
- **GPT-2 (BPE)**: `gpt2`
- **T5 (SentencePiece/Unigram)**: `t5-small`
- **XLNet (SentencePiece)**: `xlnet-base-cased`
- **ALBERT (SentencePiece)**: `albert-base-v2`

## Como Executar

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/samuelitaunam/SCTEC-Semana2.git
   cd SCTEC-Semana2
   ```
2. **(Opcional) Crie e ative um ambiente virtual:**
   ```bash
   python -m venv venv
   # No Windows:
   .\venv\Scripts\activate
   # No Linux/Mac:
   source venv/bin/activate
   ```
3. **Instale as dependências:**
   ```bash
   pip install transformers tiktoken
   ```
4. **Execute o script de exemplos:**
   ```bash
   python exemplos_tokenizacao.py
   ```

## Estrutura do Código

O script `exemplos_tokenizacao.py`:

- Define uma lista de textos de exemplo.
- Aplica cada tokenizador/modelo nos textos.
- Exibe para cada modelo:
  - Nome do modelo e algoritmo
  - Quantidade de tokens
  - Lista de tokens
  - IDs dos tokens

## Observações

- Cada tokenizador pode dividir o texto de forma diferente.
- O número de tokens e os IDs variam conforme o modelo.
- Para testar outros textos, altere a lista `texts` no início do script.
- Caso algum modelo não seja baixado automaticamente, verifique sua conexão com a internet.

## Exemplo de Saída

```
================================================================================
TEXTO: Erro no auth-service às 14:32

OpenAI encoding: cl100k_base (BPE)
Qtd tokens: 9
IDs: [...]
Partes: [...]

Modelo HF: bert-base-uncased [WordPiece (BERT)]
Qtd tokens: ...
Tokens: [...]
IDs: [...]
...
```

## Referências

- [Documentação tiktoken (OpenAI)](https://github.com/openai/tiktoken)
- [Transformers (Hugging Face)](https://huggingface.co/docs/transformers/index)
- [Tokenizers (Hugging Face)](https://huggingface.co/docs/tokenizers/index)

---

**Autor:** Samuel Marques

Dúvidas ou sugestões? Abra uma issue ou entre em contato!
>>>>>>> 2db5371 (Exemplos de tokenização e documentação)
