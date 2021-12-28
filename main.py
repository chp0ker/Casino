from aiogram import Bot, Dispatcher, executor, types
from pprint import pprint
from asyncio import sleep
import requests
import markups
import random

bot = Bot(token='ВАШ ТОКЕН', parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'], chat_type='private')
async def start(message: types.Message):
    sticker = open('assets\HelloSticker.tgs', 'rb')
    await message.answer_sticker(sticker)
    await message.answer('Добро пожаловать, <b>{0.first_name} ({0.username})!</b>\n'
                         'Я бот созданный для веселого времяпровождения.\n'
                         'Ваш ID: <b>{0.id}</b>'.format(message.from_user), reply_markup=markups.mainMenu)

@dp.message_handler(text='⬅ Главное меню', chat_type='private')
async def MainMenu(message: types.Message):
    await message.answer('Добро пожаловать, <b>{0.first_name} ({0.username})!</b>\n'
                         'Вы находитесь в главном меню.\n'
                         'Ваш ID: <b>{0.id}</b>'.format(message.from_user), reply_markup=markups.mainMenu)

@dp.message_handler(text='🎰 Выбрать игру 🎰', chat_type='private')
async def GameSelection(message: types.Message):
    await message.answer('🎰 Выберите игру', reply_markup=markups.gameMenu)

@dp.message_handler(text='📈 Курс валюты и криптовалюты 📈', chat_type='private')
async def CourseSelection(message: types.Message):
    await message.answer('Выберите курс чего смотреть', reply_markup=markups.moneyMenu)

@dp.message_handler(text='Валюта', chat_type='private')
async def CurrencyCourse(message: types.Message):
    await message.answer('Выберите курс какого типа валюты смотреть', reply_markup=markups.currencyMenu)
    # if message.text == 'USD (Доллар)':

    #elif message.text == 'EUR (Евро)':

    #elif message.text == 'GBP (Фунт стерлингов)':

@dp.message_handler(text='Криптовалюта', chat_type='private')
async def CryptocurrencyCourse(message: types.Message):
    await message.answer('Выберите курс чего смотреть', reply_markup=markups.cryptocurrency)
    #if message.text == 'BTC (Биткоин)':

    #elif message.text == 'ETH (Эфириум)':

    #elif message.text == 'BNB (Бинанс Коин)':

@dp.message_handler(text='❗ F.A.Q. ❗', chat_type='private')
async def FAQ(message: types.Message):
    await message.answer('Техническая поддержка и создатель кода: <b>@chp0ker1337</b>')

@dp.message_handler(text='🪙 Орел и Решка 🪙', chat_type='private')
async def HeadsAndTails(message: types.Message):
    await message.answer('Выберите Орел или Решка', reply_markup=markups.coinMenu)
@dp.message_handler(lambda message: message.text == '🪙 Орел 🪙' or message.text == '🪙 Решка 🪙', chat_type='private')
async def HeadsAndTailsStart(message: types.Message):
    heads = open('assets/HeadsAndTails/coin-heads.webp', 'rb')
    tails = open('assets/HeadsAndTails/coin-tails.webp', 'rb')
    side_tuple = ['🪙 Орел 🪙', '🪙 Решка 🪙']
    random_side = random.choice(side_tuple)
    if random_side == message.text:
        if random_side == '🪙 Орел 🪙':
            await message.answer_sticker(heads)
            await sleep(0.5)
            await message.answer('<b> 🟩 Поздравляю, вы выиграли 🟩 </b>\n\n'
                                 'Выпала сторона: ' + str(random_side))
        elif random_side == '🪙 Решка 🪙':
            await message.answer_sticker(tails)
            await sleep(0.5)
            await message.answer('<b> 🟩 Поздравляю, вы выиграли 🟩 </b>\n\n'
                                 'Выпала сторона: ' + str(random_side))
    elif random_side != message.text:
        if random_side == '🪙 Орел 🪙':
            await message.answer_sticker(heads)
            await sleep(0.5)
            await message.answer('<b> 🟥 К сожалению вы проиграли 🟥 </b>\n\n'
                                 'Выпала сторона: ' + str(random_side))
        elif random_side == '🪙 Решка 🪙':
            await message.answer_sticker(tails)
            await sleep(0.5)
            await message.answer('<b> 🟥 К сожалению вы проиграли 🟥 </b>\n\n'
                                 'Выпала сторона: ' + str(random_side))

@dp.message_handler(text='🎲 Кости 🎲', chat_type='private')
async def Dice(message: types.Message):
    await message.answer('🎲 Бросьте кости', reply_markup=markups.diceMenu)
@dp.message_handler(text='🎲 Бросить Кости 🎲', chat_type='private')
async def DiceStart(message: types.Message):
    await message.answer('🎲 Ваши кости:')
    user_data = await bot.send_dice(message.from_user.id)
    user_data = user_data['dice']['value']
    await sleep(2)
    await message.answer('🎲 Кости соперника:')
    bot_data = await bot.send_dice(message.from_user.id)
    bot_data = bot_data['dice']['value']
    await sleep(4)
    if user_data > bot_data:
        await message.answer('<b> 🟩 Поздравляю, вы выиграли 🟩 </b>')
    elif user_data < bot_data:
        await message.answer('<b> 🟥 К сожалению вы проиграли 🟥 </b>')
    elif user_data == bot_data:
        await message.answer('<b> 🟧 Произошла ничья 🟧 </b>')

@dp.message_handler(text='🎁 Рандомный Бокс 🎁', chat_type='private')
async def RandomBox(message: types.Message):
    await message.answer('Выберите любой бокс', reply_markup=markups.boxMenu)
@dp.message_handler(lambda message: message.text == '№1 🎁' or message.text == '№2 🎁' or message.text == '№3 🎁'
                    or message.text == '№4 🎁' or message.text == '№5 🎁', chat_type='private')
async def RandomBoxStart(message: types.Message):
    box_tuple = ['№1 🎁', '№2 🎁', '№3 🎁', '№4 🎁', '№5 🎁']
    BoxRandom = random.sample(box_tuple, 2)
    BoxRandom.sort()
    if BoxRandom[0] == message.text or BoxRandom[1] == message.text:
        await message.answer('<b> 🟩 Поздравляю, вы выиграли 🟩 </b>\n\n'
                             'Выигрышные боксы: ' + str(BoxRandom[0]) + ' и ' + str(BoxRandom[1]))
    else:
        await message.answer('<b> 🟥 К сожалению, вы проиграли 🟥 </b>\n\n'
                             'Выигрышные боксы: ' + str(BoxRandom[0]) + ' и ' + str(BoxRandom[1]))

@dp.message_handler(text='🏵 Рулетка 🏵', chat_type='private')
async def Roulette(message: types.Message):
    await message.answer('Выберите на что вы будете ставить', reply_markup=markups.rouletteMenu)
Red = '🔴 Красное 🔴'
Black = '⚫ Черное ⚫'
Green = '🟢 Зеленое 🟢'
Even = 'Четное'
Odd = 'Нечетеное'
First_12 = 'Числа от 1 до 12'
Second_12 = 'Числа от 12 до 24'
Third_12 = 'Числа от 24 до 36'
From_1_to_18 = 'Числа от 1 до 18'
From_19_to_36 = 'Числа от 19 до 36'
@dp.message_handler(lambda message: message.text == Red or message.text == Black or message.text == Green
                    or message.text == Even or message.text == Odd
                    or message.text == First_12 or message.text == Second_12 or message.text == Third_12
                    or message.text == From_1_to_18 or message.text == From_19_to_36, chat_type='private')
async def RouletteStart(message: types.Message):
    BollRouletteRandom = random.randint(0, 36)
    red_tuple = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    black_tuple = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
    green_tuple = [0]
    even_tuple = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
    odd_tuple = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
    number1st12_tuple = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    number2st12_tuple = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
    number3st12_tuple = [24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
    number1to18_tuple = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    number19to36_tuple = [19, 20, 21, 22, 23, 24, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
    await sleep(0.5)
    async def RedWin(sub_message: types.Message):
        await sub_message.answer('<b> 🟩 Поздравляю, вы выиграли 🟩 </b>\n\n'
                                 'Выпало число: ' + str(BollRouletteRandom) + ' (Красное)')

    async def BlackWin(sub_message: types.Message):
        await sub_message.answer('<b> 🟩 Поздравляю, вы выиграли 🟩 </b>\n\n'
                                 'Выпало число: ' + str(BollRouletteRandom) + ' (Черное)')

    async def GreenWin(sub_message: types.Message):
        await sub_message.answer('<b> 🟩 Поздравляю, вы выиграли 🟩 </b>\n\n'
                                 'Выпало число: 0 (Зеленое)')

    async def RedLose(sub_message: types.Message):
        await sub_message.answer('<b> 🟥 К сожалению, вы проиграли 🟥 </b>\n\n'
                                 'Выпало число: ' + str(BollRouletteRandom) + ' (Красное)')

    async def BlackLose(sub_message: types.Message):
        await sub_message.answer('<b> 🟥 К сожалению, вы проиграли 🟥 </b>\n\n'
                                 'Выпало число: ' + str(BollRouletteRandom) + ' (Черное)')

    async def GreenLose(sub_message: types.Message):
        await sub_message.answer('<b> 🟥 К сожалению, вы проиграли 🟥 </b>\n\n'
                                 'Выпало число: 0 (Зеленое)')

    async def Win(sub_message: types.Message):
        if BollRouletteRandom in red_tuple:
            await RedWin(sub_message)
        elif BollRouletteRandom in black_tuple:
            await BlackWin(sub_message)

    async def Lose(sub_message: types.Message):
        if BollRouletteRandom in red_tuple:
            await RedLose(sub_message)
        elif BollRouletteRandom in black_tuple:
            await GreenLose(sub_message)
        elif BollRouletteRandom in green_tuple:
            await GreenLose(sub_message)

    if message.text == Red:
        if BollRouletteRandom in red_tuple:
            await RedWin(message)
        else:
            if BollRouletteRandom in black_tuple:
                await BlackLose(message)
            elif BollRouletteRandom in green_tuple:
                await GreenLose(message)

    elif message.text == Black:
        if BollRouletteRandom in black_tuple:
            await BlackWin(message)
        else:
            if BollRouletteRandom in red_tuple:
                await RedLose(message)
            elif BollRouletteRandom in green_tuple:
                await GreenLose(message)

    elif message.text == Green:
        if BollRouletteRandom in green_tuple:
            await GreenWin(message)
        else:
            if BollRouletteRandom in red_tuple:
                await RedLose(message)
            elif BollRouletteRandom in black_tuple:
                await BlackLose(message)

    elif message.text == Even:
        if BollRouletteRandom in even_tuple:
            if BollRouletteRandom in red_tuple:
                await RedWin(message)
            elif BollRouletteRandom in black_tuple:
                await BlackWin(message)
        else:
            await Lose(message)

    elif message.text == Odd:
        if BollRouletteRandom in odd_tuple:
            await Win(message)
        else:
            await Lose(message)

    elif message.text == First_12:
        if BollRouletteRandom in number1st12_tuple:
            await Win(message)
        else:
            await Lose(message)

    elif message.text == Second_12:
        if BollRouletteRandom in number2st12_tuple:
            await Win(message)
        else:
            await Lose(message)

    elif message.text == Third_12:
        if BollRouletteRandom in number3st12_tuple:
            await Win(message)
        else:
            await Lose(message)

    elif message.text == From_1_to_18:
        if BollRouletteRandom in number1to18_tuple:
            await Win(message)
        else:
            await Lose(message)

    elif message.text == From_19_to_36:
        if BollRouletteRandom in number19to36_tuple:
            await Win(message)
        else:
            await Lose(message)

    else:
        await message.answer('Неизвестная ставка')

if __name__ == '__main__':
    executor.start_polling(dp)
