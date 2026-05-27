from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import BETS_LINK, ADMINS, OWNER_LINK
import sqlite3


conn = sqlite3.connect("db.db")
cursor = conn.cursor()
def menu(userid):
    kb = InlineKeyboardMarkup(row_width=2)
    btn1 = InlineKeyboardButton("💠 Профиль", callback_data='profile')
    btn2 = InlineKeyboardButton("Статистика 💠", callback_data='stats')
    btn3 = InlineKeyboardButton("🎲 Сделать ставку 🎲", url=BETS_LINK)
    btn4 = InlineKeyboardButton("💫 Админ-Панель 💫", callback_data='admin')
    kb.add(btn1, btn2)
    kb.add(btn3)
    if userid in ADMINS:
        kb.add(btn4)
    return kb

def profile():
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(InlineKeyboardButton("💠 Реф. Панель", callback_data='ref_panel'), InlineKeyboardButton("Кэшбек система 💠", callback_data='cashback'))
    kb.add(InlineKeyboardButton("◀️ Назад", callback_data='menu'))
    return kb

def back(call):
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(InlineKeyboardButton("◀️ Назад", callback_data=call))
    return kb

def ref():
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(InlineKeyboardButton("💠 Рефералы", callback_data='refs'), InlineKeyboardButton("Ссылки 💠", callback_data='links'))
    kb.add(InlineKeyboardButton("◀️ Назад", callback_data='profile'))
    return kb

def cashback():
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(InlineKeyboardButton("💠 Вывести", url=OWNER_LINK))
    kb.add(InlineKeyboardButton("◀️ Назад", callback_data='profile'))
    return kb

def admin():
    status = cursor.execute("SELECT stop FROM settings").fetchone()[0]

    if status == 1:
        status = '🟢'
        call = '0'
    else:
        status = '🔴'
        call = '1'

    status1 = cursor.execute("SELECT ex FROM settings").fetchone()[0]

    if status1 == 1:
        status1 = '🟢'
        call1 = '0'
    else:
        status1 = '🔴'
        call1 = '1'

    kb = InlineKeyboardMarkup(row_width=2)
    btn1 = InlineKeyboardButton("💠 Рассылка", callback_data='broadcast')
    btn2 = InlineKeyboardButton("💠 Попол. Казну", callback_data='popol')
    btn3 = InlineKeyboardButton("💠 Изм. Счёт", callback_data='change_invoice')
    btn4 = InlineKeyboardButton("💠 Упр. Пользователем", callback_data='control_user')
    btn5 = InlineKeyboardButton("💠 Изм. Макс. Сумму", callback_data='change_max')
    btn6 = InlineKeyboardButton("💠 Вывод казны", callback_data='withdraw')
    btn7 = InlineKeyboardButton("💠 Упр. Чеками", callback_data='checks')
    btn8 = InlineKeyboardButton(f"{status} Стоп ставки", callback_data=f'set_stop:{call}')
    btn9 = InlineKeyboardButton("💠 Отправить туториал", callback_data='send_tutorial')
    btn10 = InlineKeyboardButton(f"{status1} 1.1x", callback_data=f'set_x:{call1}')
    btn11 = InlineKeyboardButton("◀️ Назад", callback_data='menu')
    kb.add(btn1, btn2)
    kb.add(btn3, btn4)
    kb.add(btn5, btn6)
    kb.add(btn7, btn8)
    kb.add(btn9, btn10)
    kb.add(btn11)
    return kb

def control(userid):
    kb = InlineKeyboardMarkup(row_width=1)
    btn1 = InlineKeyboardButton("💠 Отправить сообщение", callback_data=f'send_message:{userid}')
    btn2 = InlineKeyboardButton("💠 Анулировать реф-баланс", callback_data=f'empty_ref:{userid}')
    btn3 = InlineKeyboardButton("💠 Анулировать кэшбек-счет", callback_data=f'empty_cashback:{userid}')
    btn4 = InlineKeyboardButton("◀️ Назад", callback_data='control_user')
    kb.add(btn1, btn2, btn3, btn4)
    return kb