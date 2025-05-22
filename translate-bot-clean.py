from aiogram import Bot, Dispatcher, types, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from googletrans import Translator
import asyncio

TOKEN = ""
bot = Bot(token=TOKEN)
dp = Dispatcher()
router = Router()
translator = Translator()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        "👋 Привет! Я бот-переводчик юридических терминов.\n"
        "Я перевожу термины с английского на русский и наоборот.\n"
        "Используйте /translate <термин> для перевода.\n"
        "Для справки используйте /help"
    )

@dp.message(Command("help"))
async def cmd_help(message: Message):
    help_text = (
        "📚 Доступные команды:\n"
        "/start - начать работу с ботом\n"
        "/translate <термин> - перевести юридический термин\n"
        "/help - показать эту справку\n\n"
        "Примеры использования:\n"
        "/translate liability - перевести термин 'liability' на русский\n"
        "/translate иск - перевести термин 'иск' на английский"
    )
    await message.answer(help_text)

@dp.message(Command("translate"))
async def cmd_translate(message: Message):
    parts = message.text.split()
    
    if len(parts) == 1:
        await message.answer("❌ Пожалуйста, укажите юридический термин для перевода после команды /translate")
        return
    elif len(parts) > 2:
        await message.answer("❌ Пожалуйста, укажите только один термин для перевода")
        return
        
    term = parts[1]
    
    try:
        detected = translator.detect(term)
        
        if detected.lang == 'ru':
            translation = translator.translate(term, src='ru', dest='en')
            await message.answer(f"🔄 Перевод термина: {translation.text}")
        else:
            translation = translator.translate(term, src='en', dest='ru')
            await message.answer(f"🔄 Перевод термина: {translation.text}")
            
    except Exception as e:
        await message.answer("❌ Произошла ошибка при переводе. Пожалуйста, попробуйте снова.")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())