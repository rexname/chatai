def save_chat_to_history(chat, response):
    with open('chat_history.txt', 'a') as file:
        # Format untuk chat pengguna
        user_format = f"User:\n{chat}"
        # Format untuk respons AI
        ai_format = f"AI:\n{response}\n\n"
        
        # Menulis kedua format ke dalam file
        file.write(user_format + ai_format)