import requests
from pprint import pprint
import time
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
#import matplotlib.pyplot as plt

API_URL = 'https://api.bitkub.com' #base url

endpoint = {
	'status':'/api/status',
	'timestamp':'/api/servertime',
	'symbols':'/api/market/symbols',
	'ticker':'/api/market/ticker'
}

print(API_URL + endpoint['timestamp'])

def Status():
	yrl = API_URL + endpoint['status']
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

def Ticker(COIN='THB_BTC'):
	url = API_URL + endpoint['ticker']
	r = requests.get(url, params={'sym':COIN})
	data = r.json()
	#print(data)
	print('----------------------')
	print('Last Price:', data[COIN]['last'])
	print('Change:', data[COIN]['percentChange'],'%')
	print('----------------------\n')

	#plt.plot(percentChange, color='red')
	#plt.plot(i, color='green')
	#plt.show()

Input = input("Enter Password Of 'F': ")
if Input == '70':
	try:
		Input1 = input("What Stock You want to view?: ")
		while True:
			Ticker(str(Input1))
			time.sleep(1)
	except:
		print(f"'{Input1}' Is Not Defined")
else:
	print('Password Is Not Defined')