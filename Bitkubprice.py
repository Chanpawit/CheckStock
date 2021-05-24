import requests
from pprint import pprint
import time
import songline
import datetime
#import matplotlib.pyplot as plt

API_URL = 'https://api.bitkub.com' #base url

endpoint = {
	'status':'/api/status',
	'timestamp':'/api/servertime',
	'symbols':'/api/market/symbols',
	'ticker':'/api/market/ticker',
	'trade':'/api/market/trades'
}

print(API_URL + endpoint['timestamp'])

def Status():
	url = API_URL + endpoint['status']
	if r.status_code == 200:
		print('Server Working Normally'+'\n')
		print(r.status_code)
	return r.status_code

def ServerTime():
	url = API_URL + endpoint['timestamp']
	comtime = time.time()
	print('Com:', comtime)
	print(time.ctime(comtime))
	# print(time.localtime(comtime))

	r = requests.get(url)
	data = r.json()
	
	print('Server:', data)
	print(time.ctime(data))

def Allsymbol():
	url = API_URL + endpoint['symbols']
	r = requests.get(url)
	data = r.json()
	# pprint(r.json())
	count = len(data['result'])
	print('COUNT:', count)
	print(data['result'])

def Ticker(COIN='THB_BTC', ALL=False):
	list1 = []
	global data
	url = API_URL + endpoint['ticker']

	if ALL == True:
		r = requests.get(url)
		data = r.json()
		pprint(data)
		return data
	else:
		r = requests.get(url, params={'sym':COIN})
		data = r.json()
	#print(data)
	Now = datetime.datetime.now()
	#token = 'n8RkQWX0gFlD3Ibu0HG5U6G5RS2xKNImFZE6KQqDGYM'
	#messenger = songline.Sendline(token)
	#messenger.sendtext('== Bot Is Ready Now! ==')
	#messenger.sendtext(f"{COIN} 💰\nLast Price: {data[COIN]['last']} 📊\nChange: {data[COIN]['percentChange']}% 💥")
	#time.sleep(30)
	list1.append(float(data[COIN]['last']))
	list1.append(float(data[COIN]['percentChange']))
	print(list1)

	if data[COIN]['last'] != list1[0]:
		print(data[COIN]['last'])
	
	return data
	return COIN

	#plt.plot(percentChange, color='red')
	#plt.plot(i, color='green')
	#plt.show()

def Trades(COIN='THB_BTC'):
	url = API_URL + endpoint['ticker']
	r = requests.get(url, params={'sym':COIN})
	data = r.json()
	print(data)

while True:
	Ticker()
	


#Trades('THB_DOGE')
'''
#while True:
	#Ticker()
	#time.sleep(1)
	# Allsymbol()
'''
# Trades()