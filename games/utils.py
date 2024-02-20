import requests


def send_message_to_telegram(message):
    bot_token = "6455477603:AAFrcrh4yvCOBrMLB29YQ9Oy-ZjkNYeIA7Q"
    group_id = -4123868699
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={group_id}&text={message}"

    requests.get(url)