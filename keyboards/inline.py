from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from data.config import payout, admin, pays, chatbot, chan1, chan2, manualdep, viewsch, game_cube_price, game_slot_price, botname
from utils.qiwi import get_qiwi_url
from loader import data

class ProfileMenu(object):
      def profile_main(self):
        keyboard = InlineKeyboardMarkup()
        k1 = InlineKeyboardButton(text = '💳 Пополнить', callback_data = 'dep')
        k2 = InlineKeyboardButton(text = '💸 Вывести', callback_data = 'payout')
        k3 = InlineKeyboardButton(text = '♻️ Обменять', callback_data = 'exchange')
        if payout:
          keyboard.add(k1, k2)
          keyboard.add(k3)
        else:
          keyboard.add(k1)
          keyboard.add(k3)
        return keyboard
	
      def profile_deposit(self):
         keyboard = InlineKeyboardMarkup()
         k1 = InlineKeyboardButton(text = '💳Карта', callback_data = 'qiwi_method')
         k2 = InlineKeyboardButton(text = '🙎‍♂️ Через поддержку', callback_data = 'manual_dep')
         keyboard.add(k1)
         if manualdep:
           keyboard.add(k2)
         return keyboard
	 
      def deposit_qiwi(self, comment):
         keyboard = InlineKeyboardMarkup(row_width=2)
         k1 = InlineKeyboardButton(text = '💸Оплатить💸', url = get_qiwi_url(comment))
         k2 = InlineKeyboardButton(text = '🔁Проверить платёж', callback_data = 'check_qiwi')
         k3 = InlineKeyboardButton(text = '❌Отменить', callback_data = 'del_deposit')
         k4 = InlineKeyboardButton(text = '🗂История пополнений', callback_data = 'history_dep')
         keyboard.add(k1)
         keyboard.add(k2, k3)
         keyboard.add(k4)
         return keyboard
		 
      def payout_menu_main(self):
         keyboard = InlineKeyboardMarkup()
         k1 = InlineKeyboardButton(text = '📤 Вывести средства', callback_data = 'payoutq')
         k2 = InlineKeyboardButton(text = '🗂 История выводов', callback_data = 'payoutshistory')
         keyboard.add(k1)
         keyboard.add(k2)
         return keyboard
		 
class ReferalMenu(object):
      def referal_main(self):
         keyboard = InlineKeyboardMarkup()
         k1 = InlineKeyboardButton(text = '✉️ Приветственное сообщение', callback_data = 'hellomsg')
         k2 = InlineKeyboardButton(text = '🏆 Топ рефоводов', callback_data = 'reftop')
         keyboard.add(k1)
         keyboard.add(k2)
         return keyboard
		 
      def ref_msg_bt(self, status):
         keyboard = InlineKeyboardMarkup()
         if status:
           kb = InlineKeyboardButton(text = '📝 Изменить текст', callback_data = 'edit_hello_msg')
         else:
           kb = InlineKeyboardButton(text = '💳 Купить функцию', callback_data = 'buy_hello_msg')
         keyboard.add(kb)
         return keyboard

class InfoMenu(object):
      def info_main(self):
         keyboard = InlineKeyboardMarkup()
         for x in data['data']:
          eval(x)
         return keyboard
		 
class EarnMenu(object):
      def chanel_main(self):
         keyboard = InlineKeyboardMarkup()
         k1 = InlineKeyboardButton(text = '🗣️ Подписаться', url = 'https://t.me/' + chan1.split('@')[1])
         k2 = InlineKeyboardButton(text = '🗣️ Подписаться', url = 'https://t.me/' + chan2.split('@')[1])
         keyboard.add(k1)
         keyboard.add(k2)
         return keyboard
		 
      def chanel_chk(self, name, num):
         keyboard = InlineKeyboardMarkup()
         k1 = InlineKeyboardButton(text = 'Перейти к каналу', url = 'tg://resolve?domain=' + name)
         k2 = InlineKeyboardButton(text = 'Проверить подписку', callback_data = 'chchk_' + num)
         keyboard.add(k1)
         keyboard.add(k2)
         return keyboard
		 
      def group_chk(self, name, num):
         keyboard = InlineKeyboardMarkup()
         k1 = InlineKeyboardButton(text = 'Перейти в группу', url = 'tg://resolve?domain=' + name)
         k2 = InlineKeyboardButton(text = 'Проверить подписку', callback_data = 'grchk_' + num)
         keyboard.add(k1)
         keyboard.add(k2)
         return keyboard
		 
      def bots(self, name):
         keyboard = InlineKeyboardMarkup()
         k1 = InlineKeyboardButton(text = 'Перейти в бот', url = name)
         keyboard.add(k1)
         return keyboard
		 
      def views_ch(self):
         keyboard = InlineKeyboardMarkup()
         k1 = InlineKeyboardButton(text = 'Перейти к постам', url = 'tg://resolve?domain=' + viewsch)
         keyboard.add(k1)
         return keyboard
		 
class PromoMenu(object):
      def get_money(self):
         keyboard = InlineKeyboardMarkup()
         k1 = InlineKeyboardButton(text = '💳 Пополнить', callback_data = 'dep')
         k2 = InlineKeyboardButton(text = '♻️ Обменять', callback_data = 'exchange')
         keyboard.add(k1)
         keyboard.add(k2)
         return keyboard
		 
      def views_main(self):
         keyboard = InlineKeyboardMarkup()
         k1 = InlineKeyboardButton(text = '👁 Добавить пост', callback_data = 'addview')
         k2 = InlineKeyboardButton(text = '⏱ Активные заказы', callback_data = 'myviews')
         k3 = InlineKeyboardButton(text = '❌ Отмена', callback_data = 'cancel')
         keyboard.add(k1)
         keyboard.add(k2)
         keyboard.add(k3)
         return keyboard
		 
      def views_bt(self, num):
         keyboard = InlineKeyboardMarkup()
         k1 = InlineKeyboardButton(text = '👁', callback_data = 'chkview_' + num)
         keyboard.add(k1)
         return keyboard
		 
      def channels_main(self):
         keyboard = InlineKeyboardMarkup()
         k1 = InlineKeyboardButton(text = '📢 Добавить канал', callback_data = 'addch')
         k2 = InlineKeyboardButton(text = '⏱ Активные заказы', callback_data = 'mych')
         k3 = InlineKeyboardButton(text = '❌ Отмена', callback_data = 'cancel')
         keyboard.add(k1)
         keyboard.add(k2)
         keyboard.add(k3)
         return keyboard
		 
      def channel_del(self, num):
         keyboard = InlineKeyboardMarkup()
         k1 = InlineKeyboardButton(text = '❌ Удалить задание', callback_data = 'chdel:' + num)
         k2 = InlineKeyboardButton(text = '❌ Отмена', callback_data = 'cancel')
         keyboard.add(k1)
         keyboard.add(k2)
         return keyboard
		 
      def groups_main(self):
         keyboard = InlineKeyboardMarkup()
         k1 = InlineKeyboardButton(text = '📢 Добавить канал', callback_data = 'addgr')
         k2 = InlineKeyboardButton(text = '⏱ Активные заказы', callback_data = 'mygr')
         k3 = InlineKeyboardButton(text = '❌ Отмена', callback_data = 'cancel')
         keyboard.add(k1)
         keyboard.add(k2)
         keyboard.add(k3)
         return keyboard
		 
      def group_del(self, num):
         keyboard = InlineKeyboardMarkup()
         k1 = InlineKeyboardButton(text = '❌ Удалить задание', callback_data = 'grdel:' + num)
         k2 = InlineKeyboardButton(text = '❌ Отмена', callback_data = 'cancel')
         keyboard.add(k1)
         keyboard.add(k2)
         return keyboard
		 
      def bots_main(self):
         keyboard = InlineKeyboardMarkup()
         k1 = InlineKeyboardButton(text = '🤖 Добавить бот', callback_data = 'addbot')
         k2 = InlineKeyboardButton(text = '⏱ Активные заказы', callback_data = 'mybot')
         k3 = InlineKeyboardButton(text = '❌ Отмена', callback_data = 'cancel')
         keyboard.add(k1)
         keyboard.add(k2)
         keyboard.add(k3)
         return keyboard
		 
      def bot_del(self, num):
         keyboard = InlineKeyboardMarkup()
         k1 = InlineKeyboardButton(text = '❌ Удалить задание', callback_data = 'botdel:' + num)
         k2 = InlineKeyboardButton(text = '❌ Отмена', callback_data = 'cancel')
         keyboard.add(k1)
         keyboard.add(k2)
         return keyboard
		 
class GameMenu(object):
      def game_menu(self):
         keyboard = InlineKeyboardMarkup()
         k1 = InlineKeyboardButton(text = f'🎲 Кубики {game_cube_price} SC', callback_data = 'game_cube')
         k2 = InlineKeyboardButton(text = f'🎰 Автомат {game_slot_price} SC', callback_data = 'game_slot')
         k3 = InlineKeyboardButton(text = f'🎁 Ежедневный бонус', callback_data = 'bonus')
         keyboard.add(k1)
         keyboard.add(k2)
         keyboard.add(k3)
         return keyboard
		 
class AdminMenu(object):
      def admin_main(self):
         keyboard = InlineKeyboardMarkup()
         k1 = InlineKeyboardButton(text = '📤 Выплаты', callback_data = 'payslist_adm')
         k2 = InlineKeyboardButton(text = '📥 Пополнения', callback_data = 'dep_adm')
         k3 = InlineKeyboardButton(text = '📃 Создать чек', callback_data = 'vaucher_adm')
         k4 = InlineKeyboardButton(text = '✉️ Рассылка', callback_data = 'masmailing')
         k5 = InlineKeyboardButton(text = '🔎 Инфа', callback_data = 'info_adm')
         k6 = InlineKeyboardButton(text = '🍀 Задания', callback_data = 'task_mgr')
         k7 = InlineKeyboardButton(text = '📬 Заявки на вывод средств', callback_data = 'payouts')
         k8 = InlineKeyboardButton(text = '❌ Отмена', callback_data = 'cancel')
         keyboard.add(k1, k2)
         keyboard.add(k3, k4)
         keyboard.add(k5, k6)
         keyboard.add(k7, k8)
         return keyboard
		 
      def voucher_kb(self, id):
         keyboard = InlineKeyboardMarkup()
         k1 = InlineKeyboardButton(text = 'Активировать чек', url = 'https://t.me/' + botname + '?start=' + id)
         keyboard.add(k1)
         return keyboard
		 
      def selectpay_kb(self, num):
         keyboard = InlineKeyboardMarkup()
         k1 = InlineKeyboardButton(text = '✅ Подтвердить', callback_data = 'accpay_' + num)
         k2 = InlineKeyboardButton(text = '🛑 Отклонить', callback_data = 'cancpay_' + num)
         k3 = InlineKeyboardButton(text = '↪️ Вернуть', callback_data = 'backpay_' + num)
         k4 = InlineKeyboardButton(text = '❌ Отмена', callback_data = 'cancel')
         keyboard.add(k1)
         keyboard.add(k2)
         keyboard.add(k3)
         keyboard.add(k4)
         return keyboard
		 
      def info_kb(self, id, ban):
         keyboard = InlineKeyboardMarkup()
         k1 = InlineKeyboardButton(text = '➕ Добавить', callback_data = 'selectbaladd_' + id)
         k2 = InlineKeyboardButton(text = '💸 Изменить', callback_data = 'selectbalch_' + id)
         k3 = InlineKeyboardButton(text = 'Забанить', callback_data = 'ban_' + id)
         k4 = InlineKeyboardButton(text = 'Разбанить', callback_data = 'unban_' + id)
         k5 = InlineKeyboardButton(text = '❌ Отмена', callback_data = 'cancel')
         keyboard.add(k1, k2)
         if ban:
           keyboard.add(k4)
         else:
           keyboard.add(k3)
         keyboard.add(k5)
         return keyboard
		 
      def selectbal_kb(self, num):
         keyboard = InlineKeyboardMarkup()
         k1 = InlineKeyboardButton(text = '💰 Основной', callback_data = 'addbal_' + num)
         k2 = InlineKeyboardButton(text = '💳 Рекламный', callback_data = 'addadv_' + num)
         k3 = InlineKeyboardButton(text = '❌ Отмена', callback_data = 'cancel')
         keyboard.add(k1)
         keyboard.add(k2)
         keyboard.add(k3)
         return keyboard
		 
      def selectchbal_kb(self, num):
         keyboard = InlineKeyboardMarkup()
         k1 = InlineKeyboardButton(text = '💰 Основной', callback_data = 'chbal_' + num)
         k2 = InlineKeyboardButton(text = '💳 Рекламный', callback_data = 'chadv_' + num)
         k3 = InlineKeyboardButton(text = '❌ Отмена', callback_data = 'cancel')
         keyboard.add(k1)
         keyboard.add(k2)
         keyboard.add(k3)
         return keyboard
		 
      def task_mgr_menu(self):
         keyboard = InlineKeyboardMarkup()
         k1 = InlineKeyboardButton(text = '🗣️ Каналы', callback_data = 'cahnnels_adm')
         k2 = InlineKeyboardButton(text = '👥 Группы', callback_data = 'groups_adm')
         k3 = InlineKeyboardButton(text = '👁 Просмотры', callback_data = 'views_adm')
         k4 = InlineKeyboardButton(text = '🤖 Боты', callback_data = 'bots_adm')
         k5 = InlineKeyboardButton(text = '❌ Отмена', callback_data = 'cancel')
         keyboard.add(k1, k2)
         keyboard.add(k3, k4)
         keyboard.add(k5)
         return keyboard
		 
      def channel_del_adm(self, num):
         keyboard = InlineKeyboardMarkup()
         k1 = InlineKeyboardButton(text = '💣 Убить задание', callback_data = 'chdel_adm_' + num)
         k2 = InlineKeyboardButton(text = '❌ Отмена', callback_data = 'cancel')
         keyboard.add(k1)
         keyboard.add(k2)
         return keyboard
		 
      def group_del_adm(self, num):
         keyboard = InlineKeyboardMarkup()
         k1 = InlineKeyboardButton(text = '💣 Убить задание', callback_data = 'grdel_adm_' + num)
         k2 = InlineKeyboardButton(text = '❌ Отмена', callback_data = 'cancel')
         keyboard.add(k1)
         keyboard.add(k2)
         return keyboard
		 
      def bot_del_adm(self, num):
         keyboard = InlineKeyboardMarkup()
         k1 = InlineKeyboardButton(text = '💣 Убить задание', callback_data = 'botdel_adm_' + num)
         k2 = InlineKeyboardButton(text = '❌ Отмена', callback_data = 'cancel')
         keyboard.add(k1)
         keyboard.add(k2)
         return keyboard
		 
      def chat_ban_kb(self, id, ban):
         keyboard = InlineKeyboardMarkup()
         k1 = InlineKeyboardButton(text = 'Заблокать', callback_data = 'ban_' + id)
         k2 = InlineKeyboardButton(text = 'Разблокать', callback_data = 'unban_' + id)
         k3 = InlineKeyboardButton(text = '❌ Отмена', callback_data = 'cancel_chat')
         if ban:
           keyboard.add(k2)
         else:
           keyboard.add(k1)
         keyboard.add(k3)
         return keyboard
		 
