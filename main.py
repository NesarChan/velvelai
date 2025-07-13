import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
from config import TELEGRAM_TOKEN
from generator import generate_nsfw_image

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_cmd(msg: Message):
    await msg.answer("👋 Привет! Напиши /gen <запрос> — сгенерирую картинку.")

@dp.message_handler(commands=["gen", "generate"])
async def cmd_gen(msg: Message):
    prompt = msg.get_args()
    if not prompt:
        return await msg.reply("❗ Укажи запрос: /gen anime girl lying in bed")
    await msg.reply("🎨 Генерирую...")
    url, used = generate_nsfw_image(prompt)
    if url:
        await bot.send_photo(msg.chat.id, url, caption=f"✅ {used}")
    else:
        await msg.reply("❌ Ошибка генерации.")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
