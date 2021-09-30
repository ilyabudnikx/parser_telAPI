import telebot
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager

chromedriver = "/home/ilyabudnikxs/Documents/chromedriver/chromedriver"
driver = webdriver.Chrome(chromedriver)

token = ''
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Напишите команду /search для начала поиска.")


@bot.message_handler(commands=['search'])
def search_videos(message):
    msg = bot.send_message(message.chat.id, 'Введите название видео которые вы хотите найти.')
    bot.register_next_step_handler(msg, search)


@bot.message_handler(commands=['text'])
def text(message):
    bot.send_message(message.chat.id,'Ты дятел? Не видел что у тебя при старете написало?')
    photo = open('1.jpeg', 'rb')
    bot.send_photo(message.chat.id, photo)


def search(message):
    bot.send_message(message.chat.id, 'Начинаю парсинг')
    video = f"https://www.youtube.com/results?search_query={message.text}"
    driver.get(video)
    video = driver.find_elements_by_id("video-title")

    for i in range(len(video)):
        time.sleep(1)
        bot.send_message(message.chat.id, video[i].get_attribute('href'))
        if i == 5:
            break
bot.infinity_polling()
