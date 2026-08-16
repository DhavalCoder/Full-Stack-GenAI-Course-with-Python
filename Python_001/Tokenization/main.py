import tiktoken


enc = tiktoken.encoding_for_model("gpt-4o")

text = "My Name is Dhava Chorwadkar"
encode = text.enc
print("Tokens",  encode)