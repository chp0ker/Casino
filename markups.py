from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

buttonMain = KeyboardButton('⬅ Главное меню')

# Main Menu
buttonGame = KeyboardButton('🎰 Выбрать игру')
buttonBalance = KeyboardButton('💰 Узнать баланс')
buttonSupport = KeyboardButton('👤 Техническая поддержка')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(buttonGame, buttonBalance, buttonSupport)

# Game Menu
buttonCoin = KeyboardButton('🪙 Орел и Решка')
buttonDice = KeyboardButton('🎲 Кости')
buttonRandomBox = KeyboardButton('🎁 Рандомный Бокс')
gameMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(buttonCoin, buttonDice, buttonRandomBox, buttonMain)

# Heads And Tails
buttonHeads = KeyboardButton('🪙 Орел')
buttonTails = KeyboardButton('🪙 Решка')
coinMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(buttonHeads, buttonTails, buttonMain)

# Dice
buttonRollTheDice = KeyboardButton('🎲 Бросить Кости')
diceMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(buttonRollTheDice, buttonMain)

# Random Boxing
buttonRandomBox1 = KeyboardButton('№1 🎁')
buttonRandomBox2 = KeyboardButton('№2 🎁')
buttonRandomBox3 = KeyboardButton('№3 🎁')
buttonRandomBox4 = KeyboardButton('№4 🎁')
buttonRandomBox5 = KeyboardButton('№5 🎁')
boxMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(buttonRandomBox1, buttonRandomBox2, buttonRandomBox3, buttonRandomBox4, buttonRandomBox5, buttonMain)
