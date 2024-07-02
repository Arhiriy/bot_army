from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN
from keyboard.key_menu import set_commands
from keyboard.keyboards import get_keyboard_1, get_keyboard_2, get_keyboard_3, get_keyboard_4
from keyboard.key_inline import get_keyboard_inline, get_keyboard_inline_1, get_keyboard_inline_2, get_keyboard_inline_3, get_keyboard_inline_4, get_keyboard_inline_5, get_keboard_inline_6


bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)

#=================================================================================================#



#=================================================================================================#

@dp.message_handler(commands= 'start')
async def start(message: types.Message):
    await message.answer('Привет, я твой военный бот гит.', reply_markup= get_keyboard_1())

@dp.message_handler(commands= 'help')
async def start(message: types.Message):
    await message.answer('Я могу помочь тебе узнать больше о армии')

#=================================================================================================#
#1
@dp.message_handler(lambda message: message.text == 'Начало')
async def button_1_slick(message: types.Message):
    await message.answer('Начало работы гида', reply_markup= get_keyboard_2())

@dp.message_handler(lambda message: message.text == 'Армия')
async def button_2_slick(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://gas-kvas.com/grafic/uploads/posts/2024-01/gas-kvas-com-p-nadpis-armiya-na-prozrachnom-fone-14.jpg',
                         caption='Армия - это организованная структура, состоящая из людей, обученных и вооруженных для ведения войны или защиты своей страны.  В нее обычно входят пехота, артиллерия, бронетанковые войска,  авиация, ВМФ и т.д.',
                         reply_markup= get_keyboard_inline())

@dp.message_handler(lambda message: message.text == 'Солдаты')
async def button_2_slick(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://img.razrisyika.ru/kart/52/1200/207304-armiya-rossii-12.jpg',
                         caption='Солдаты - это люди, которые служат в армии, военно-морском флоте, ВВС или других военных силах. Они проходят специальную подготовку, чтобы быть готовыми к выполнению боевых задач или поддержанию мира.',
                         reply_markup= get_keyboard_inline_1())

@dp.message_handler(lambda message: message.text == 'Военное вооружение')
async def button_2_slick(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://popgun.ru/files/g/36/orig/11567484.jpg',
                         caption='Военное вооружение - это  совокупность средств, используемых армией для ведения войны, защиты своей территории или выполнения боевых задач.',
                         reply_markup= get_keyboard_inline_2())

@dp.message_handler(lambda message: message.text == 'Перейти на раздел с рода войск')
async def button_2_slick(message: types.Message):
    await message.answer('Тут ты можешь попросить бота показать тебе виды рада войск.', reply_markup= get_keyboard_3())


#=================================================================================================#
#2

@dp.message_handler(lambda message: message.text == 'Военно-воздушные силы')
async def button_3_slick(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://mil.ru/images/upload/2017/6.5.jpg',
                         caption='ВВС предназначены для решения следующих задач: отражения агрессии в воздушно-космической сфере и защиты от ударов с воздуха пунктов управления высших звеньев государственного и военного управления, административно-политических центров, промышленно-экономических районов, важнейших объектов экономики и инфраструктуры страны.',
                         reply_markup= get_keyboard_inline_3())

@dp.message_handler(lambda message: message.text == 'Военно-морской флот')
async def button_3_slick(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://www.sunhome.ru/i/foto/24/voenno-morskoi-parad-chast-ii-v6.orig.jpg',
                         caption='Вое́нно-морско́й флот (ВМФ), вид вооружённых сил (ВС), предназначенный для решения стратегических и оперативных задач на океанских и морских театрах военных действий (ТВД); в ряде государств – военно-морские силы (ВМС).',
                         reply_markup= get_keyboard_inline_4())

@dp.message_handler(lambda message: message.text == 'Воздушно-десантные войска')
async def button_3_slick(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://tvkrasnodar.ru/upload/iblock/e6b/e6bdad1e6a413f4140164cbf15b0fffd.jpg',
                         caption='Возду́шно-деса́нтные войска́ (ВДВ), высокомобильный род войск в составе вооружённых сил (ВС) многих государств мира. ВДВ способны быстро достигать удалённых районов театров военных действий (ТВД), наносить внезапные удары по противнику, быстро захватывать и удерживать важные районы в его глубоком тылу, нарушать государственное и военное управление, овладевать островами и тд.',
                         reply_markup= get_keyboard_inline_5())

@dp.message_handler(lambda message: message.text == 'Космические войска')
async def button_3_slick(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://otkrytky.ru/o/img/0371/otrkytky-ru-44-dXNlcmFwaS5jb20.jpg',
                         caption='Косми́ческие войска́ (КВ), род войск Воздушно-космических сил (ВКС) Вооружённых Сил Российской Федерации (ВС РФ). Предназначен для обеспечения высших органов государственного и военного управления достоверной информацией о предупреждении в отношении ракетного нападения; выявления признаков начала военных действий в космическом пространстве.',
                         reply_markup= get_keyboard_inline_6())

@dp.message_handler(lambda message: message.text == 'Вернутся к началу')
async def button_4_slick(message: types.Message):
    await message.answer('Тут ты можешь вернутся к началу', reply_markup= get_keyboard_1())

#=================================================================================================#

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

async def on_startup(dispatcher):
    await set_commands(dispatcher.bot)

#=================================================================================================#

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup= on_startup)