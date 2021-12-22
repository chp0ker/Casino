from aiogram import Bot, Dispatcher, executor, types
import markups
import random

bot = Bot(token = 'ВАШ ТОКЕН')
dp = Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    sticker = open('AnimatedSticker.tgs', 'rb')
    await bot.send_sticker(message.chat.id, sticker)
    await bot.send_message(message.chat.id, 'Добро пожаловать, {0.first_name} ({0.username})!\n'
                                            'Я бот созданный для веселого времяпровождения.\n'
                                            'Ваш ID: {0.id}'.format(message.from_user), reply_markup = markups.mainMenu)

@dp.message_handler(state = None)
async def main(message: types.Message):
    if message.chat.type != 'private':
        return

    elif message.text == '⬅ Главное меню':
        await bot.send_message(message.chat.id, 'Добро пожаловать, {0.first_name} ({0.username})!\n'
                                                'Вы находитесь в главном меню.\n'
                                                'Ваш ID: {0.id}'.format(message.from_user), reply_markup = markups.mainMenu)

    elif message.text == '🎰 Выбрать игру':
        await bot.send_message(message.chat.id, '🎰 Выберите игру', reply_markup = markups.gameMenu)

    elif message.text == '💰 Узнать баланс':
        await bot.send_message(message.chat.id, 'Ваш баланс: 0', reply_markup = markups.balanceMenu)


    elif message.text == '👤 Техническая поддержка':
        await bot.send_message(message.chat.id, 'Техническая поддержка: @Vboost')

    elif message.text == '🤑 Орел и Решка':
        await bot.send_message(message.chat.id, 'Выберите Орел или Решка', reply_markup = markups.coinMenu)

    elif message.text == '🪙 Орел' or message.text == '🪙 Решка':
        heads = open('coin-heads.webp', 'rb')
        tails = open('coin-tails.webp', 'rb')
        side_tuple = ['Орел', 'Решка']
        random_side = random.choice(side_tuple)
        if random_side == message.text:
            if random_side == 'Орел':
                await bot.send_sticker(message.chat.id, heads)
                await bot.send_message(message.chat.id, 'Поздравляю, вы выиграли! Выпала сторона: ' + str(random_side))
            else:
                await bot.send_sticker(message.chat.id, tails)
                await bot.send_message(message.chat.id, 'Поздравляю, вы выиграли! Выпала сторона: ' + str(random_side))
        else:
            if random_side == 'Орел':
                await bot.send_sticker(message.chat.id, heads)
                await bot.send_message(message.chat.id, 'К сожалению вы проиграли! Выпала сторона: ' + str(random_side))
            else:
                await bot.send_sticker(message.chat.id, tails)
                await bot.send_message(message.chat.id, 'К сожалению вы проиграли! Выпала сторона: ' + str(random_side))

    elif message.text == '🤑 Наперстки':
        await bot.send_message(message.chat.id, 'Игра в разработке')

    else:
        await bot.send_message(message.chat.id, 'Неизвестная команда')

if __name__ == '__main__':
    executor.start_polling(dp)

