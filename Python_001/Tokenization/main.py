import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

text = "Hey There! My name is Dhaval Chorwadkar"
tokens = enc.encode(text)

print("Tokens", tokens)

decoded = enc.decode([25216, 3274, 0, 3673, 1308, 382, 31129, 24733, 125322, 40645, 10428])
print("Decoded", decoded)