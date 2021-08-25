import os
import telebot

API_KEY = os.environ['API_KEY']
bot = telebot.TeleBot(API_KEY)

chats = dict()

@bot.message_handler(commands=["Hello"])
def hello(message):
  bot.send_message(message.chat.id, "What are the events that happen in youu company? ")

@bot.message_handler(content_types=['voice'])
def voice_processing(message):
    file_info = bot.get_file(message.voice.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    with open('new_file.ogg', 'wb') as new_file:
        new_file.write(downloaded_file)
        
    if str(message.chat.id) in chats : 
      chats[str(message.chat.id)] += 1
    else : 
      chats[str(message.chat.id)] = 1

    if chats[str(message.chat.id)] == 1 :
      bot.send_message(message.chat.id, "How would you have donne better")
    elif chats[str(message.chat.id)] == 2 :
      bot.send_message(message.chat.id, "What do you think you can do it make it better")
    elif chats[str(message.chat.id)] == 3 :
      bot.send_message(message.chat.id, "Thanks for you inputs")

bot.polling(True);

