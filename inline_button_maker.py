from telebot import types
def make_button(button):
    if button=="mbutton":
        button=types.InlineKeyboardMarkup(row_width=2)
        button1=types.InlineKeyboardButton(text="🇺🇿UZS➙🇺🇸USD",callback_data="UZS-USD")
        button2=types.InlineKeyboardButton(text="🇺🇸USD➙🇺🇿UZS",callback_data="USD-UZS")
        button3=types.InlineKeyboardButton(text="🇺🇿UZS➙🇷🇺RUB",callback_data="UZS-RUB")
        button4=types.InlineKeyboardButton(text="🇷🇺RUB➙🇺🇿UZS",callback_data="RUB-UZS")
        button5=types.InlineKeyboardButton(text="🇺🇸USD➙🇷🇺RUB",callback_data="USD-RUB")
        button6=types.InlineKeyboardButton(text="🇷🇺RUB➙🇺🇸USD",callback_data="RUB-USD")
        button7=types.InlineKeyboardButton(text="🇹🇷TRY➙🇺🇸USD",callback_data="TRY-USD")
        button8=types.InlineKeyboardButton(text="🇺🇸USD➙🇹🇷TRY",callback_data="USD-TRY")
        button9=types.InlineKeyboardButton(text="🇹🇷TRY➙🇷🇺RUB",callback_data="TRY-RUB")
        button10=types.InlineKeyboardButton(text="🇷🇺RUB➙🇹🇷TRY",callback_data="RUB-TRY")
        button11=types.InlineKeyboardButton(text="Yangilash🚀",callback_data="update")
        button12=types.InlineKeyboardButton(text="❌",callback_data="delete")
        button.add(button1,button2,button3,button4,button5,button6,button7,button8,button9,button10,button11,button12)
        return button
        
        