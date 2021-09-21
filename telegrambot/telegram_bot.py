#Import Package
import telebot
import mysql.connector

# mydb = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     passwd='',
#     database=''
# )

#Menghubungkan Bot Telegram dengan script Python
api = '2030379612:AAEI9HSNeWg8CQYHnqgVl9I5uCW--pt8Ggs'
bot = telebot.TeleBot(api)

@bot.message_handler(commands=['start'])
def action_start(message):
    nama_awal = message.from_user.first_name
    nama_akhir = message.from_user.last_name
    bot.reply_to(message,'Halo, {} {}. Terima kasih sudah menggunakan Alarm Bot'.format(nama_awal,nama_akhir))

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message,'Command List :')

print('Bot Start Running')
bot.polling()
