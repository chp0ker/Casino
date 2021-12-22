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
buttonThimbles = KeyboardButton('🤑 Наперстки')
gameMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(buttonCoin, buttonDice, buttonThimbles, buttonMain)

# Heads And Tails
buttonHeads = KeyboardButton('🪙 Орел')
buttonTails = KeyboardButton('🪙 Решка')
coinMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(buttonHeads, buttonTails, buttonMain)

# Dice
buttonRollTheDice = KeyboardButton('🎲 Бросить Кости')
diceMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(buttonRollTheDice, buttonMain)

buttonStickerDice = KeyboardButton('🎲')
stickerDiceMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(buttonStickerDice, buttonMain)

# Balance
buttonReplenish = KeyboardButton('💰 Пополнить баланс')
balanceMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(buttonReplenish, buttonMain)