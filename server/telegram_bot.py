import websocket
import json
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

TOKEN = 'YOUR_BOT_TOKEN'

WEBSOCKET_URL = 'ws://localhost:8080/websocket'

def start(update: Update, context: CallbackContext):
    keyboard = [[InlineKeyboardButton("Взаимодействовать с мини-приложением", callback_data='interact_miniapp')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Нажмите на кнопку, чтобы начать взаимодействие с мини-приложением', reply_markup=reply_markup)

def button(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    if query.data == 'interact_miniapp':
        interact_with_miniapp(update, context)

def interact_with_miniapp(update: Update, context: CallbackContext):
    ws = websocket.WebSocketApp(WEBSOCKET_URL,
                               on_message=on_message,
                               on_error=on_error,
                               on_close=on_close,
                               on_open=on_open)
    ws.run_forever()

def on_message(ws, message):
    # Обработка сообщений, полученных от мини-приложения
    data = json.loads(message)
    context.bot.send_message(chat_id=update.effective_chat.id, text=data['response'])

def on_error(ws, error):
    # Обработка ошибок WebSocket-соединения
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Ошибка при взаимодействии с мини-приложением: {error}")

def on_close(ws):
    # Обработка закрытия WebSocket-соединения
    context.bot.send_message(chat_id=update.effective_chat.id, text="Соединение с мини-приложением закрыто")

def on_open(ws):
    # Обработка открытия WebSocket-соединения
    # Здесь вы можете отправить начальные данные мини-приложению
    message = {'request': 'Hello from Telegram bot!'}
    ws.send(json.dumps(message))

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()