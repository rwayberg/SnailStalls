from web3 import Web3
from eth_account.messages import encode_defunct
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
account = "0x8626f6940E2eb28930eFb4CeF49B2d1F2C9C1199"
private_key = "0xdf57089febbacf7ba0bc227dafbffa9fc08a93fdc68e1e42411a14efcf23656e"
print(w3.isConnected())
#print(w3.eth.getBlock("latest"))
msg = "testmessage"
en_msg = encode_defunct(text=msg)
signed = w3.eth.account.sign_message(en_msg, private_key=private_key)
print(signed)
#now to call snail api in python