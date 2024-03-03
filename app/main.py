from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import token
from enter_data import get_random_data, add_data

bot = Bot(token=token)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!ахаххахха:)")


@dp.message_handler(commands=["words"])
async def process_get_words(message: types.Message):
    data = get_random_data()
    lst_data = [f"{key} - {definition}" for key, definition in data.items()]
    await message.reply("\n".join(lst_data))


@dp.message_handler(commands=["add"])
async def add_words_to_database(message: types.Message):
    if message.reply_to_message:
        data = message.reply_to_message.text
        if add_data(data):
            await message.reply("Успешно добавлены!")
        else:
            await message.reply("Не смог расспарсить!")
    else:
        await message.reply("Сошлись на сообщение с текстом, который хочешь добавить в словарь.")


@dp.message_handler(commands=["help"])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отправлю этот текст тебе в ответ!")


# @dp.message_handler()
# async def echo_message(msg: types.Message):
#     await bot.send_message(msg.from_user.id, msg.text)

# @dp.message_handler(content_types=[types.ContentType.TEXT])
# async def text(msg: types.Message):
#     print(msg)


# @dp.message_handler(content_types=[types.ContentType.VOICE])
# async def voice(msg: types.Message):
#     file_data = await bot.get_file(file_id=msg.voice.file_id)
#     audio_file = requests.get("https://api.telegram.org/file/bot{0}/{1}".format(token, file_data.file_path))
#     print(audio_file)
#     with open("dummy", "wb") as my_file:
#         my_file.write(audio_file.content)
#     with open("dummy", "rb") as my_file:
#         transcript = await openai.Audio.transcribe("whisper-1", my_file)
#         print(transcript)

# text = voice_to_text(file.content)
# if text:
#     await bot.send_message(chat_id=msg.from_user.id, text=text, reply_to_message_id=msg.message_id)
# else:
#     await bot.send_message(chat_id=msg.from_user.id, text="Silence....", reply_to_message_id=msg.message_id)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, loop=True)
