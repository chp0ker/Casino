from aiogram import Bot, Dispatcher, executor, types
from asyncio import sleep
import markups
import random

bot = Bot(token = '5040783029:AAF72fiuc6SZCFwkzTyHWDGxWtG9YYWDqKU')
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
    elif message.text == '💰 Пополнить баланс':
        await bot.send_message(message.chat.id, 'Команда в разработке')

    elif message.text == '👤 Техническая поддержка':
        await bot.send_message(message.chat.id, 'Техническая поддержка и создатель кода: @chp0ker1337')

    elif message.text == '🪙 Орел и Решка':
        await bot.send_message(message.chat.id, 'Выберите Орел или Решка', reply_markup = markups.coinMenu)
    elif message.text == '🪙 Орел' or message.text == '🪙 Решка':
        heads = open('coin-heads.webp', 'rb')
        tails = open('coin-tails.webp', 'rb')
        side_tuple = ['🪙 Орел', '🪙 Решка']
        random_side = random.choice(side_tuple)
        if random_side == message.text:
            if random_side == '🪙 Орел':
                await bot.send_sticker(message.chat.id, heads)
                await sleep(0.5)
                await bot.send_message(message.chat.id, 'Поздравляю, вы выиграли! Выпала сторона: ' + str(random_side))
            else:
                await bot.send_sticker(message.chat.id, tails)
                await sleep(0.5)
                await bot.send_message(message.chat.id, 'Поздравляю, вы выиграли! Выпала сторона: ' + str(random_side))
        else:
            if random_side == '🪙 Орел':
                await bot.send_sticker(message.chat.id, heads)
                await sleep(0.5)
                await bot.send_message(message.chat.id, 'К сожалению вы проиграли! Выпала сторона: ' + str(random_side))
            else:
                await bot.send_sticker(message.chat.id, tails)
                await sleep(0.5)
                await bot.send_message(message.chat.id, 'К сожалению вы проиграли! Выпала сторона: ' + str(random_side))

    elif message.text == '🎲 Кости':
        await bot.send_message(message.chat.id, '🎲 Бросьте кости', reply_markup = markups.diceMenu)
    elif message.text == '🎲 Бросить Кости':
        await bot.send_message(message.chat.id, '🎲 Ваши кости:')
        user_data = await bot.send_dice(message.from_user.id)
        user_data = user_data['dice']['value']
        await sleep(2)
        await bot.send_message(message.chat.id, '🎲 Кости соперника:')
        bot_data = await bot.send_dice(message.from_user.id)
        bot_data = bot_data['dice']['value']
        await sleep(4)
        if user_data > bot_data:
            await bot.send_message(message.chat.id, 'Поздравляю, вы выиграли!')
        elif user_data < bot_data:
            await bot.send_message(message.chat.id, 'К сожалению вы проиграли!')
        else:
            await bot.send_message(message.chat.id, 'Произошла ничья!')

    elif message.text == '🤑 Наперстки':
        await bot.send_message(message.chat.id, 'Игра в разработке')

    else:
        await bot.send_message(message.chat.id, 'Неизвестная команда')

if __name__ == '__main__':
    executor.start_polling(dp)

