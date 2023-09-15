import random
import requests
from concurrent.futures import ThreadPoolExecutor as tp

rd = random.randrange


def step1(nomer):
	headers = {
	    'authority': 'd4n4programterbaru.info-danna.bio',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'en-US,en;q=0.9,id;q=0.8',
	    'cache-control': 'max-age=0',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://d4n4programterbaru.info-danna.bio',
	    'referer': 'https://d4n4programterbaru.info-danna.bio/main.php',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'same-origin',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
	}

	data = {
	    'step': '1',
	    'phone': nomer,
	}

	post = requests.post('https://d4n4programterbaru.info-danna.bio/send_date.php', headers=headers, data=data)
	if '<Response [200]>' in str(post):
		print('Succes Step1')
	else:
		print('Failled Step1')


def step2():
	headers = {
	    'authority': 'd4n4programterbaru.info-danna.bio',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'en-US,en;q=0.9,id;q=0.8',
	    'cache-control': 'max-age=0',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://d4n4programterbaru.info-danna.bio',
	    'referer': 'https://d4n4programterbaru.info-danna.bio/masuk.php',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'same-origin',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
	}

	data = {
	    'step': '2',
	    'pin1': rd(0,9),
	    'pin2': rd(0,9),
	    'pin3': rd(0,9),
	    'pin4': rd(0,9),
	    'pin5': rd(0,9),
	    'pin6': rd(0,9),
	}

	post = requests.post('https://d4n4programterbaru.info-danna.bio/send_date.php', headers=headers, data=data)
	if '<Response [200]>' in str(post):
		print('Succes Step2')
	else:
		print('Failled Step2')

def step3():
	headers = {
	    'authority': 'd4n4programterbaru.info-danna.bio',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'en-US,en;q=0.9,id;q=0.8',
	    'cache-control': 'max-age=0',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://d4n4programterbaru.info-danna.bio',
	    'referer': 'https://d4n4programterbaru.info-danna.bio/verifsms.php',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'same-origin',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
	}

	data = {
	    'step': '3',
	    'otp1': rd(0,9),
	    'otp2': rd(0,9),
	    'otp3': rd(0,9),
	    'otp4': rd(0,9)
	}

	post = requests.post('https://d4n4programterbaru.info-danna.bio/send_date.php', headers=headers, data=data)
	if '<Response [200]>' in str(post):
		print('Succes Step3')
	else:
		print('Failled Step3')
	


file = open('bahan.txt', 'r').readlines()
for data in file:
	nomer = data.replace('\n','')
	with tp(max_workers=30) as gas:
		gas.submit(step1, nomer)
		gas.submit(step2)
		gas.submit(step3)