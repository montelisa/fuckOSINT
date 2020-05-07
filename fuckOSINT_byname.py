import requests, libs.logo, libs.users_agents


sites=['https://instagram.com/', 'https://twitter.com/', 'https://steamcommunity.com/id/', 'https://ok.ru/', 'https://www.youtube.com/user/', 'https://freelance.ru/']


def check(header, target, proxy=0):
	for i in sites:
		try:
			g=requests.get(i+target, headers=header)
			if g.status_code==200:
				print(f'found {i+target}')
			else:
				print(f'{i} not found')
		except:
			print(f"Возможно сайт не доступен в вашем регионе {i}")



def main():
	libs.logo.logo()
	header=libs.users_agents.initHeaders()
	target=input('target: ')
	check(header, target)
	


if __name__ == '__main__':
	main()
