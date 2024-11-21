from tonsdk.contract.wallet import Wallets, WalletVersionEnum
import requests
mnemonics = input('Seed Phrase : ').split()
pk = Wallets.from_mnemonics(mnemonics, WalletVersionEnum.v4r2, workchain=0)[1].hex()
headers = {'User-Agent': "okhttp/4.9.2",'Accept-Encoding': "gzip",'content-type': "application/json",'authorization': "Bearer AF77F5JNEUSNXPQAAAAMDXXG7RBQ3IRP6PC2HTHL4KYRWMZYOUQGDEKYFDKBETZ6FDVZJBI",'cache-control': "no-cache"}
response = requests.get(f"https://keeper.tonapi.io/v2/pubkeys/{pk}/wallets",headers=headers).json()
acc=response['accounts'][0]
add=acc['address']
ton=requests.get(f'https://keeper.tonapi.io/v2/accounts/{add}/jettons',headers=headers).json()
print(ton)
