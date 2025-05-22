# 🏛️ LTT Bot (Legal Terms Translator Bot)
**Telegram-бот для перевода юридических терминов**  
Переводчик юридических терминов с поддержкой русского и английского языков. Помогает юристам, студентам и переводчикам быстро находить точные эквиваленты правовых понятий.

This bot is a translator of legal terms with support for Russian and English languages. It helps lawyers, students, and translators quickly find exact equivalents of legal concepts. 

[Гид по установке](https://github.com/lisdonut/law-term-bot/blob/main/installation-guide.docx)

## Возможности
- Перевод юридических терминов (**EN ↔ RU**)  
- Поиск контекстных значений для сложных понятий  
- Простое управление через Telegram-команды  
- Поддержка базы из 1000+ терминов  



##  Быстрый старт
### Установка и запуск
1. **Клонируйте репозиторий**:
   ```
   git clone https://github.com/ваш-username/ltt-bot.git
   cd ltt-bot
   ```
3. **Установите зависимости**:
   ```
   pip install -r requirements.txt
   ```
3. **Настройте бота**:
  - Получите токен у @BotFather
  - Вставьте его в файл config.py:
    ```
    TOKEN = "ваш_токен"
    ```
4. **Запустите бота**:
   ```
   python bot.py
   ```
### Команды
- /start - приветственное сообщение
- /help	- справка по использованию
- /translate - перевести термин	(пример:/translate liability)

  
### Технологии 
Python 3.8+, Aiogram, Googletrans

### Как помочь проекту?

Добавьте термины в legal_terms.json (формат: {"термин": "перевод"})
Создайте Issue с предложениями по улучшению
Форкните репозиторий и отправьте Pull Request

## Разработано для упрощения работы с международным правом.
По вопросам: lisdonut@icloud.com

