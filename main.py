from aiogram import Bot, Dispatcher, executor, types
from asyncio import sleep
import markups
import random

bot = Bot(token = 'ВАШ ТОКЕН')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'], chat_type = 'private')
async def start(message: types.Message):
    sticker = open('AnimatedSticker.tgs', 'rb')
    await message.answer_sticker(sticker)
    await message.answer('Добро пожаловать, {0.first_name} ({0.username})!\n'
                        'Я бот созданный для веселого времяпровождения.\n'
                        'Ваш ID: {0.id}'.format(message.from_user), reply_markup = markups.mainMenu)

@dp.message_handler(text = '⬅ Главное меню', chat_type = 'private')
async def MainMenu(message: types.Message):
    await message.answer('Добро пожаловать, {0.first_name} ({0.username})!\n'
                        'Вы находитесь в главном меню.\n'
                        'Ваш ID: {0.id}'.format(message.from_user), reply_markup = markups.mainMenu)

@dp.message_handler(text = '🎰 Выбрать игру', chat_type = 'private')
async def GameSelection(message: types.Message):
    await message.answer('🎰 Выберите игру', reply_markup = markups.gameMenu)

@dp.message_handler(text = '💰 Узнать баланс', chat_type = 'private')
async def Balance(message: types.Message):
    await message.answer('Ваш баланс: 0', reply_markup = markups.balanceMenu)

@dp.message_handler(text = '💰 Пополнить баланс', chat_type = 'private')
async def TopUpBalance(message: types.Message):
    await message.answer('Команда в разработке')

@dp.message_handler(text = '👤 Техническая поддержка', chat_type = 'private')
async def Support(message: types.Message):
    await message.answer('Техническая поддержка и создатель кода: @chp0ker1337')

@dp.message_handler(text = '🪙 Орел и Решка', chat_type = 'private')
async def HeadsAndTails(message: types.Message):
    await message.answer('Выберите Орел или Решка', reply_markup = markups.coinMenu)
@dp.message_handler(lambda message: message.text == '🪙 Орел' or message.text == '🪙 Решка', chat_type = 'private')
async def ChoosingSide(message: types.Message):
    heads = open('coin-heads.webp', 'rb')
    tails = open('coin-tails.webp', 'rb')
    side_tuple = ['🪙 Орел', '🪙 Решка']
    random_side = random.choice(side_tuple)
    if random_side == message.text:
        if random_side == '🪙 Орел':
            await message.answer_sticker(heads)
            await sleep(0.5)
            await message.answer('Поздравляю, вы выиграли! Выпала сторона: ' + str(random_side))
        elif random_side == '🪙 Решка':
            await message.answer_sticker(tails)
            await sleep(0.5)
            await message.answer('Поздравляю, вы выиграли! Выпала сторона: ' + str(random_side))
    elif random_side != message.text:
        if random_side == '🪙 Орел':
            await message.answer_sticker(heads)
            await sleep(0.5)
            await message.answer('К сожалению вы проиграли! Выпала сторона: ' + str(random_side))
        elif random_side == '🪙 Решка':
            await message.answer_sticker(tails)
            await sleep(0.5)
            await message.answer('К сожалению вы проиграли! Выпала сторона: ' + str(random_side))

@dp.message_handler(text = '🎲 Кости', chat_type = 'private')
async def Dice(message: types.Message):
    await message.answer('🎲 Бросьте кости', reply_markup = markups.diceMenu)
@dp.message_handler(text = '🎲 Бросить Кости', chat_type = 'private')
async def Dice(message: types.Message):
    await message.answer('🎲 Ваши кости:')
    user_data = await bot.send_dice(message.from_user.id)
    user_data = user_data['dice']['value']
    await sleep(2)
    await message.answer ('🎲 Кости соперника:')
    bot_data = await bot.send_dice(message.from_user.id)
    bot_data = bot_data['dice']['value']
    await sleep(4)
    if user_data > bot_data:
        await message.answer('Поздравляю, вы выиграли!')
    elif user_data < bot_data:
        await message.answer('К сожалению вы проиграли!')
    elif user_data == bot_data:
        await message.answer('Произошла ничья!')

@dp.message_handler(text = '🤑 Наперстки', chat_type = 'private')
async def Thimbles(message: types.Message):
    await message.answer('Игра в разработке')

if __name__ == '__main__':
    executor.start_polling(dp)
