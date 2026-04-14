import tiktoken

text = "Erro no auth-service às 14:32"

for enc_name in ["r50k_base", "cl100k_base", "o200k_base"]:
	enc = tiktoken.get_encoding(enc_name)
	ids = enc.encode(text)
	pieces = [enc.decode([tok]) for tok in ids]

	print("=" * 70)
	print("Encoding:", enc_name)
	print("Qtd tokens:", len(ids))
	print("IDs:", ids)
	print("Partes:", pieces)
