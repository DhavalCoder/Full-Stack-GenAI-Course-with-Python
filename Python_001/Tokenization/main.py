import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

text = "Hey There! My name is Dhaval Chorwadkar"
tokens = enc.encode(text)

print("Tokens", tokens)