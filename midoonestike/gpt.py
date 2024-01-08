from json import load
from requests import post
from telegram    import Bot
from telegram.utils.request import Request

with open(__file__[:-6]+"creds.json") as file:
    data = load(file)

request = Request(proxy_url='socks5://localhost:2080')
bot = Bot(token=data["telbottoken"], request=request)#

url = "https://api.openai.com/v1/chat/completions"
proxies = {'http': 'socks5://localhost:2080', 'https': 'socks5://localhost:2080'}
headers = {'Content-Type': 'application/json','Authorization': f'Bearer {data["gpttoken"]}'}

def ask_gpt(promt):
    try:
        payload = {
            'messages': [{'role': 'system', 'content': 'You are a helpful assistant'},
                         {'role': 'user', 'content': f'{promt}'}],
            "model" : "gpt-3.5-turbo",
            'temperature': 0.9
        }
        response = post(url, json=payload, headers=headers, proxies=proxies)#
        if response.status_code == 200:
            answer = response.json()
            answer = answer["choices"][0]["message"]["content"]
            return answer
        else:
            bot.send_message(chat_id=data["admin"], text=f"error in gpt if response handler:\n {response.json()}")
            return False
    except Exception as e:
        bot.send_message(chat_id=data["admin"], text=f"error in main gpt handler:\n {e}")
        return False