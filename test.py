import app 
test = "\n".join(app.load_chat_history())
prompt = "Ya elah"
chat = "kunyuk"
test2 = prompt + " " + " ".join(app.load_chat_history()) + " " + chat
print(test2)