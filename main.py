from web3 import Web3
import requests
import json
from datetime import datetime
from decimal import Decimal

mainnetURL = 'https://mainnet.infura.io/v3/fd71293b54954e358ed95da002a73549'
def transactionUrl(publicAddress):
    return 'https://api.etherscan.io/api?module=account&action=txlist&address={publicAddress}&startblock=0&endblock=99999999&sort=asc&apikey=WT8AHJ71QK5V3A3A47S8JWBWM38QN95FGN'

w3 = Web3(Web3.HTTPProvider(mainnetURL))

publicAddress = input("Input your address: ")
balance = w3.eth.get_balance(publicAddress)

print("your balance is: ", balance)

transactionCount = w3.eth.getTransactionCount(publicAddress)
print("transaction count: ", transactionCount)

r = requests.get(transactionUrl(publicAddress))
data = r.json()

def gweiToEth(gwei):
    eth = w3.fromWei(gwei, 'ether')
    return eth
def timeCreated(time):
    date = datetime.fromtimestamp(time)
    return date

for transaction in data['result']:
    print('from: ', transaction['from'])
    print('to: ', transaction['to'])
    gweiAmount = gweiToEth(float(transaction['value']))
    print('amount: ', gweiAmount, ' ETH')
    print('at: ', timeCreated(int(transaction['timeStamp'])))
    print('\n\n')


