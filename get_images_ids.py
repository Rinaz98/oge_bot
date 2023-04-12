from aiogram import types, Dispatcher
from create_bot import bot


async def get_image_id(message: types.Message):
    image_id = message.photo[0].file_id
    print(image_id)
    print(message.from_user.id)
    await message.answer('Done')


async def get_sticker_id(message: types.Message):
    sticker_id = message.sticker.file_id
    print(sticker_id)


async def get_audio_id(message: types.Message):
    audio_id = message.voice.file_id
    print(audio_id)


def register_handlers_admin_main(dp: Dispatcher):
    dp.register_message_handler(get_image_id, content_types=['photo'])
    dp.register_message_handler(get_sticker_id, content_types=['sticker'])
    dp.register_message_handler(get_audio_id, content_types=['voice'])
