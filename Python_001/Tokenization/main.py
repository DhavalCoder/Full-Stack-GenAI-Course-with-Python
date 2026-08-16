import tiktoken


enc = tiktoken.encoding_for_model("gpt-4o")

text = "My Name is Dhaval Chorwadkar"
tokens = enc.encode(text) 
print("Tokens",  tokens)

decoded = enc.decode([5444, 7317, 382, 31129, 24733, 125322, 40645, 10428])
print("text is:", decoded)