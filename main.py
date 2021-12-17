import telebot
import random
from telebot import types
bot = telebot.TeleBot('ВВЕДИТЕ ВАШ ТОКЕН')
@bot.message_handler(commands=['start'])
def start(message):
    sticker = open('AnimatedSticker.tgs', 'rb')
    bot.send_sticker(message.chat.id, sticker)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('🎰 Выбрать игру')
    button2 = types.KeyboardButton('💰 Узнать баланс')
    button3 = types.KeyboardButton('👤 Техническая поддержка')
    markup.add(button1, button2, button3)
    bot.send_message(message.chat.id, 'Добро пожаловать, {0.first_name}!\n'
                                      'Я - {1.first_name}, бот созданный для веселого проведения времени.\n'
                                      'Ваш ID: {0.id}'.format(message.from_user, bot.get_me()),reply_markup=markup)

@bot.message_handler(content_types=['text'])
def game(message):
    if message.chat.type == 'private':
        if message.text == '🎰 Выбрать игру':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton('🤑 Орел и Решка')
            button2 = types.KeyboardButton('🤑 Наперстки')
            back = types.KeyboardButton('⬅ Назад')
            markup.add(button1, button2, back)
            bot.send_message(message.chat.id, '🎰 Выберите игру', reply_markup=markup)

        elif message.text == '🤑 Орел и Решка':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton('Орел')
            button2 = types.KeyboardButton('Решка')
            back = types.KeyboardButton('⬅ Назад')
            markup.add(button1, button2, back)
            bot.send_message(message.chat.id, 'Выберите Орел или Решка', reply_markup=markup)
        elif message.text == 'Орел' or message.text == 'Решка':
            side_list = ['Орел', 'Решка']
            random_side = random.choice(side_list)
            if random_side == message.text:
                if random_side == 'Орел':
                    heads = open('coin-heads-1.webp', 'rb')
                    bot.send_sticker(message.chat.id, heads)
                    bot.send_message(message.chat.id, 'Поздравляю, вы выиграли! Выпала сторона: ' + str(random_side))
                else:
                    tails = open('coin-tails-1.webp', 'rb')
                    bot.send_sticker(message.chat.id, tails)
                    bot.send_message(message.chat.id, 'Поздравляю, вы выиграли! Выпала сторона: ' + str(random_side))
            else:
                if random_side == 'Орел':
                    heads = open('coin-heads-1.webp', 'rb')
                    bot.send_sticker(message.chat.id, heads)
                    bot.send_message(message.chat.id, 'К сожалению вы проиграли! Выпала сторона: ' + str(random_side))
                else:
                    tails = open('coin-tails-1.webp', 'rb')
                    bot.send_sticker(message.chat.id, tails)
                    bot.send_message(message.chat.id, 'К сожалению вы проиграли! Выпала сторона: ' + str(random_side))

        elif message.text == '🤑 Наперстки':
            bot.send_message(message.chat.id, 'Игра в разработке')

        elif message.text == '💰 Узнать баланс':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton('💰 Пополнить баланс')
            back = types.KeyboardButton('⬅ Назад')
            markup.add(button1, back)
            bot.send_message(message.chat.id, 'Ваш баланс: 0', reply_markup=markup)
        if message.text == '💰 Пополнить баланс':
            bot.send_message(message.chat.id, 'Пополнение баланс происходит через администрацию @Vboost')

        elif message.text == '👤 Техническая поддержка':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('⬅ Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Техническая поддержка: @Vboost', reply_markup=markup)

        elif message.text == '⬅ Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton('🎰 Выбрать игру')
            button2 = types.KeyboardButton('💰 Узнать баланс')
            button3 = types.KeyboardButton('👤 Техническая поддержка')
            markup.add(button1, button2, button3)
            bot.send_message(message.chat.id, 'Добро пожаловать, {0.first_name}.\n'
                                              'Вы находитесь в основном меню\n'                             
                                              'Ваш ID: {0.id}'.format(message.from_user, bot.get_me()), reply_markup=markup)

bot.polling(none_stop = True)