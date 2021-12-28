from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

buttonMain = KeyboardButton('⬅ Главное меню')

# Main Menu
buttonGame = KeyboardButton('🎰 Выбрать игру 🎰')
buttonBalance = KeyboardButton('📈 Курс валюты и криптовалюты 📈')
buttonSupport = KeyboardButton('❗ F.A.Q. ❗')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(buttonGame, buttonBalance, buttonSupport)

# Game Menu
buttonCoin = KeyboardButton('🪙 Орел и Решка 🪙')
buttonDice = KeyboardButton('🎲 Кости 🎲')
buttonRandomBox = KeyboardButton('🎁 Рандомный Бокс 🎁')
buttonRoulette = KeyboardButton('🏵 Рулетка 🏵')
gameMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(buttonRoulette, buttonDice).row(buttonCoin, buttonRandomBox).row(buttonMain)

# Choosing Currency Or Cryptocurrency
buttonCurrency = KeyboardButton('Валюта')
buttonCryptocurrency = KeyboardButton('Криптовалюта')
moneyMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(buttonCurrency, buttonCryptocurrency, buttonMain)

# Currency
buttonDollar = KeyboardButton('USD (Доллар)')
buttonEuro = KeyboardButton('EUR (Евро)')
buttonPoundSterling = KeyboardButton('GBP (Фунт стерлингов)')
currencyMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(buttonDollar, buttonEuro, buttonPoundSterling, buttonMain )

# Cryptocurrency
buttonBitcoin = KeyboardButton('BTC (Биткоин)')
buttonEthereum = KeyboardButton('ETH (Эфириум)')
buttonBinanceCoin = KeyboardButton('BNB (Бинанс Коин)')
cryptocurrency = ReplyKeyboardMarkup(resize_keyboard=True).add(buttonBitcoin, buttonEthereum, buttonBinanceCoin, buttonMain)

# Heads And Tails
buttonHeads = KeyboardButton('🪙 Орел 🪙')
buttonTails = KeyboardButton('🪙 Решка 🪙')
coinMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(buttonHeads, buttonTails, buttonMain)

# Dice
buttonRollTheDice = KeyboardButton('🎲 Бросить Кости 🎲')
diceMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(buttonRollTheDice, buttonMain)

# Random Boxing
buttonRandomBox1 = KeyboardButton('№1 🎁')
buttonRandomBox2 = KeyboardButton('№2 🎁')
buttonRandomBox3 = KeyboardButton('№3 🎁')
buttonRandomBox4 = KeyboardButton('№4 🎁')
buttonRandomBox5 = KeyboardButton('№5 🎁')
boxMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(buttonRandomBox1, buttonRandomBox2, buttonRandomBox3, buttonRandomBox4, buttonRandomBox5, buttonMain)

# Roulette
buttonRed = KeyboardButton('🔴 Красное 🔴')
buttonBlack = KeyboardButton('⚫ Черное ⚫')
buttonGreen = KeyboardButton('🟢 Зеленое 🟢')
buttonEven = KeyboardButton('Четное')
buttonOdd = KeyboardButton('Нечетеное')
button1st12 = KeyboardButton('Числа от 1 до 12')
button2st12 = KeyboardButton('Числа от 12 до 24')
button3st12 = KeyboardButton('Числа от 24 до 36')
button1_18 = KeyboardButton('Числа от 1 до 18')
button19_36 = KeyboardButton('Числа от 19 до 36')
rouletteMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(buttonRed, buttonBlack, buttonGreen).row(buttonEven, buttonOdd).row(button1st12, button2st12, button3st12).row(button1_18, button19_36, buttonMain)
