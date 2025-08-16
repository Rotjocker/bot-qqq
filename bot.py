

#import librarys that we well use
#import librarys that we well use
import os

import telebot

import requests as re
import os
#token
g = "6132467800:AAHMgLbhF6f2XE8eB8uOTCJuANRgkZFvtYw"
#Initializing bot
bot = telebot.TeleBot(g)


def tt():
  @bot.message_handler(commands=["start"])
  def Star(message):
    id = message.from_user.id
    a = message.from_user.first_name
    b = message.from_user.username
    
    channel = "vlod2" #قناتك
    x =re.get(f"https://api.telegram.org/bot{g}/getChatMember?chat_id=@vlod2&user_id={id}").text
    if x.count("left") or x.count("Bad Request: user not found"):
      bot.reply_to(message,"عليكم الاشتراك في القناه @vlod2")
    else:
      bot.reply_to(message,"""هذا البوت البسيط يستطيع اعطائك اي صفحه من القران الكريم
    عليك فقط ارسال رقم الصفحه فقط
    ارسل رقم الصفحه ب الانكليزيه فقط رجائاً
    DEV/ @p9i_u""")
#when user send page number
  @bot.message_handler()
  def page_num(message):
    text = message.text
    id = message.chat.id
    if text.isdigit() == True:
        
        if int(text) <= 604 and int(text)>=1:
            
            img_name = f"{text}.png"
            img_data = re.get(f"https://image.slidesharecdn.com/random-160202103353/95/-{text}-1024.jpg").content

            with open(img_name, 'wb') as handler:
                handler.write(img_data) 

            bot.send_photo(id,open(img_name,"rb") , caption=f"صفحه رقم : {text}")
            os.remove(img_name)
    
        
        
       

  
      


tt()

bot.polling()
