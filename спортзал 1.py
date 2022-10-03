import  telebot#
from telebot import types#
bot=telebot.TeleBot('5399551940:AAFUuXm8TwMVpB_dhz8Rz9Dyurkg2hb8HbY')#


day='';
time='';
colich=0
cena=10
@bot.message_handler(content_types=['text'])
def start(message):
    if message.text=='Привет':
        bot.send_message(message.from_user.id,'выберите день для посещения спортзала')
        bot.register_next_step_handler(message,get_day);
    else:
        bot.send_message(message.from_user.id,'Напиши Привет')

def get_day(message):
    global day;
    name=message.text;
    bot.send_message(message.from_user.id,'выбери время ')
    bot.register_next_step_handler(message,get_time);

def get_time(message):
    global time;
    time=message.text;
    bot.send_message(message.from_user.id, 'выбери количество посещений')
    bot.register_next_step_handler(message, get_colich);

def get_colich(message):
    global colich;
    while colich==0:#
        try:
            colich=int(message.text)#
            ctoimost=cena*colich
        except Exception:
            bot.send_message(message.from_user.id, 'цифрами пожалуйста');
        keyboard = types.InlineKeyboardMarkup()  #
        key_yes = types.InlineKeyboardButton(text='да', callback_data='yes');  #
        keyboard.add(key_yes);  #
        key_no = types.InlineKeyboardButton(text='нет', callback_data='no');
        keyboard.add(key_no);
        itog = ' Ты ' + str(
            colich) + ' раз прийдешь в спортзал ' + day + 'в  ' + time + ' часов, стоимость абонемента=' + str(ctoimost)
        bot.send_message(message.from_user.id, text=itog, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'yes':  #
        bot.send_message(call.message.chat.id, 'Записал, ис нетерпением буду ждать! :)');
    elif call.data == 'no':
        bot.send_message(call.message.chat.id, 'выберите день для посещения спортзала')

bot.polling(none_stop=True, interval=0)
