import telebot
from inline_button_maker import make_button as button
from exchanger_function import exchange,get_rate,get_rates
from time import sleep
from config import token

bot=telebot.TeleBot(token, parse_mode="MARKDOWN")


@bot.message_handler(commands=["commands"])
def commands(message):
    mid=message.chat.id
    bot.send_message(mid,"*/start - botni qayta ishga tushurish.\n/info - bot haqida maʼlumot\n/developer - bot dasturchisi*")
@bot.message_handler(commands=["start"])
def start(message):
    global mid
    mid=message.chat.id
    user=message.from_user
    bot.send_message(mid,f"*Assalomu alaykum* _{format(user.first_name)}._\n*Bot buyruqlari bilan tanishib chiqing:\n/commands\n{get_rates()}\nKonvertatsiya miqdorini yuboring.\n\n@Exchanger_NewBot*")
@bot.message_handler(commands=["rates"])
def rates(message):
    mid=message.chat.id
    bot.send_message(mid,f"*{get_rates()}*")
        
@bot.message_handler(commands=["info"])
def info(message):
    mid=message.chat.id
    bot.send_message(mid,f"*Bu  bot orqali 10 xil yo'nalishda valyuta miqdorini eng so'nggi ma'lumot asosida kerakli valyuta miqdoriga hisoblab olishingiz mumkin.\nValyuta miqdorini yuboring va kerakli yo'nalishni tanlang.*\nValyuta kodlari:\n🇺🇿UZS=O'zbek so'mi\n🇺🇸USD=AQSH dollari\n🇷🇺RUB=Rossiya rubli\n🇹🇷TRY=Turkiya lirasi")
@bot.message_handler(commands=["developer"])
def developer(message):
    mid=message.chat.id
    bot.send_message(mid,"*Bot dasturchisi:\n@Beginner_python*")
@bot.message_handler(content_types=["text"])
def text(message):
    global main_button
    main_button=button("mbutton")
    global msg
    msg=message.text
    mid=message.chat.id
    user=message.from_user
    bot.send_message(mid,f"*{msg}\n\nKonvertatsiya yo'nalishini tanlang▼*",reply_markup=main_button)
@bot.callback_query_handler(func=lambda call:True)
def answer(call):
    if call:
        if call.data=="delete":
            bot.delete_message(call.message.chat.id,call.message.id)
        elif call.data=="update":
            bot.edit_message_text(f"*⚡Yangilanmoqda●10%*",call.message.chat.id,call.message.id)
            sleep(1)
            bot.edit_message_text(f"*⚡Yangilanmoqda●●20%*",call.message.chat.id,call.message.id)
            sleep(1)
            bot.edit_message_text(f"*⚡Yangilanmoqda●●●30%*",call.message.chat.id,call.message.id)
            sleep(1)
            bot.edit_message_text(f"*⚡Yangilanmoqda●●●●40%*",call.message.chat.id,call.message.id)
            sleep(1)
            bot.edit_message_text(f"*⚡Yangilanmoqda●●●●●50%*",call.message.chat.id,call.message.id)
            sleep(1)
            bot.edit_message_text(f"*⚡Yangilanmoqda●●●●●●60%*",call.message.chat.id,call.message.id)
            sleep(1)
            bot.edit_message_text(f"*⚡Yangilanmoqda●●●●●●●70%*",call.message.chat.id,call.message.id)
            sleep(1)
            bot.edit_message_text(f"*⚡Yangilanmoqda●●●●●●●●80%*",call.message.chat.id,call.message.id)
            sleep(1)
            bot.edit_message_text(f"*⚡Yangilanmoqda●●●●●●●●●90%*",call.message.chat.id,call.message.id)
            sleep(1)
            bot.edit_message_text(f"*⚡Yangilanmoqda●●●●●●●●●●100%*",call.message.chat.id,call.message.id)
            sleep(1)
            bot.edit_message_text(f"*{msg}\n\nKonvertatsiya yo'nalishini tanlang▼\n\n@Exchanger_NewBot*",call.message.chat.id,call.message.id,reply_markup=main_button)
            bot.send_message(call.message.chat.id,"*⚡Ma'lumotlar yangilandi✅*")
        elif call.data=="":
            pass
        else:
            try:
                response=exchange(call.data,msg)
                bot.edit_message_text(f"{response}\n\n*@Exchanger_NewBot*",call.message.chat.id,call.message.id,reply_markup=main_button)
            except:
                bot.send_message(call.message.chat.id,"*Xatolik yuz berdi.*")
                
     

bot.polling(none_stop=True)
    