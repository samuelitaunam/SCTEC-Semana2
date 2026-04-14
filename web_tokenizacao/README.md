# Web Tokenização

Demonstração web de tokenização de texto usando Python (Flask, tiktoken, transformers).

## Como executar

1. Crie e ative um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   # No Windows:
   .\venv\Scripts\activate
   # No Linux/Mac:
   source venv/bin/activate
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute o servidor Flask:
   ```bash
   python app.py
   ```
4. Acesse no navegador:
   - http://127.0.0.1:5000/

## Funcionalidade

- Digite um texto e veja como diferentes modelos de NLP (OpenAI/tiktoken e Hugging Face) tokenizam a frase.
- Visualização dos tokens e seus IDs para cada modelo.

## Estrutura

- `app.py`: Backend Flask e lógica de tokenização
- `templates/index.html`: Frontend HTML com visualização dos tokens
- `requirements.txt`: Dependências do projeto

---

Desenvolvido para fins didáticos. Para dúvidas ou sugestões, abra uma issue!
