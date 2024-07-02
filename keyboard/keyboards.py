from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_keyboard_1():
    keybord = ReplyKeyboardMarkup(resize_keyboard= True)
    button_1 = KeyboardButton('Начало')
    keybord.add(button_1)
    return keybord

def get_keyboard_2():
    keybord_2 = ReplyKeyboardMarkup(resize_keyboard= True)
    button_3 = KeyboardButton('Армия')
    button_4 = KeyboardButton('Солдаты')
    button_5 = KeyboardButton('Военное вооружение')
    button_6 = KeyboardButton('Перейти на раздел с рода войск')
    keybord_2.add(button_3, button_4, button_5, button_6)
    return keybord_2

def get_keyboard_3():
    keybord_3 = ReplyKeyboardMarkup(resize_keyboard= True)
    button_8 = KeyboardButton('Военно-воздушные силы')
    button_9 = KeyboardButton('Военно-морской флот')
    button_10 = KeyboardButton('Воздушно-десантные войска')
    button_11 = KeyboardButton('Космические войска')
    button_12 = KeyboardButton('Вернутся к началу')
    keybord_3.add(button_8, button_9, button_10, button_11)
    return keybord_3

def get_keyboard_4():
    keybord_4 = ReplyKeyboardMarkup(resize_keyboard= True)
    button_7 = KeyboardButton('Открыть список гарниров')
    keybord_4.add(button_7)
    return keybord_4