import tiktoken


enc = tiktoken.encoding_for_model("gpt-4o")

text = "My Name is Dhaval Chorwadkar"
tokens = enc.encode(tokens) 
print("Tokens",  tokens)