import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

text = "hey , I am prolay."
token = enc.encode(text)
print("text", token)
# text [48467, 1366, 357, 939, 440, 8639, 13]

decoded = enc.decode([48467, 1366, 357, 939, 440, 8639, 13])
print("decoded text-", decoded)