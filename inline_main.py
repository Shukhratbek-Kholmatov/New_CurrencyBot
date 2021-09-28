import telebot
from inline_button_maker import make_button as button
from exchanger_function import exchange,get_rate,get_rates
from time import sleep
token="1929039546:AAGbmdkxz95boqIRa4sVDxS9rPXgLELiAOg"
admin="904185120"
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
    bot.send_message(mid,f"*Assalomu alaykum* _{format(user.first_name)}._\n*Bot buyruqlari bilan tanishib chiqing:\n/commands\n{get_rates()}\nKonvertatsiya miqdorini yuboring.\n\n@New_CurrencyBot*")
    bot.send_message(admin,f"*/start bosildi.\n👤Foydalanuvchi:{format(user.first_name)}\n👤 Useri:\n@{format(user.username)}\n🆔 Foydalanuvchi id raqami:\n{message.chat.id}*")
@bot.message_handler(commands=["rates"])
def rates(message):
    mid=message.chat.id
    bot.send_message(mid,f"*{get_rates()}*")
        
@bot.message_handler(commands=["info"])
def info(message):
    mid=message.chat.id
    bot.send_message(mid,f"*Bu  bot orqali 10 xil yo'nalishda valyuta miqdorini eng so'nggi ma'lumot asosida kerakli valyuta miqdoriga hisoblab olishingiz mumkin.\nValyuta hisoblash yo'nalishini tanlang va botga kerakli miqdorni yuboring.\nMasalan:🇺🇿UZS➙🇺🇸USD yo'nalishini tanlaganingizda so'm miqdorini yuborishingiz kerak va bot sizga dollar kursiga hisoblab matn yuboradi.*\n_Masalan:10000;\nNatija:1 USD_\nValyuta kodlari:\n🇺🇿UZS=O'zbek so'mi\n🇺🇸USD=AQSH dollari\n🇷🇺RUB=Rossiya rubli\n🇹🇷TRY=Turkiya lirasi")
@bot.message_handler(commands=["developer"])
def developer(message):
    mid=message.chat.id
    bot.send_message(mid,"*Bot dasturchisi:\n@shukhrat_2602*")
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
            bot.edit_message_text(f"*{msg}\n\nKonvertatsiya yo'nalishini tanlang▼\n\n@New_CurrencyBot*",call.message.chat.id,call.message.id,reply_markup=main_button)
            bot.send_message(call.message.chat.id,"*⚡Ma'lumotlar yangilandi✅*")
        elif call.data=="":
            pass
        else:
            response=exchange(call.data,msg)
            bot.edit_message_text(f"{response}\n\n*@New_CurrencyBot*",call.message.chat.id,call.message.id,reply_markup=main_button)
     

bot.polling(none_stop=True)
    