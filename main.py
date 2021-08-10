from web3 import Web3
import requests

w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/fd71293b54954e358ed95da002a73549'))

publicAddress = input("Input your address: ")
balance = w3.eth.get_balance(publicAddress)

print("your balance is: ", balance)

transactionCount = w3.eth.getTransactionCount(publicAddress)
print("transaction count: ", transactionCount)

r = requests.get(f'https://api.etherscan.io/api?module=account&action=txlist&address={publicAddress}&startblock=0&endblock=99999999&sort=asc&apikey=WT8AHJ71QK5V3A3A47S8JWBWM38QN95FGN')
data = r.json()
print(r.url)
print(data['result'])
