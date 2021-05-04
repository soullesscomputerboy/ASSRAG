#Asset Super Spammer and Ravencoin Address Gatherer (RAGASS)
#Uses the Ravencoin RPC library to gather recent addresses
#Skips sending addresses because we assume there is a change address
from ravenrpc import Ravencoin
import time
	
rpcuser = "username"
rpcpassword = "password"

#Address Gathering
filename = "12000-may-4-2021"
number_of_wallets = 12000
scan_mode = 1 #1=Forward 0=Backwards

#Asset Stuff
spam = True
asset = 'SCAMCOIN'
number_per_address = 1

###DO NOT EDIT BELOW THIS LINE UNLESS YOU KNOW WHAT YOU ARE DOING###
address_list = []
last_block_height = -1

rvn = Ravencoin(rpcuser,rpcpassword)

def spam_assets(asset,address_list,spam=True):
	if spam:
		for i, a in enumerate(address_list):
			if asset not in [k for k,v in rvn.listassetbalancesbyaddress(a)['result'].items()]:
				tx = rvn.transfer(asset, number_per_address, a.strip())
				print(tx)
				try:
					if tx.get('error') and tx.get('error')['message'] == 'Error: The transaction was rejected! Reason given: too-long-mempool-chain':
						time.sleep(60) 
				except:
					time.sleep(60)

def saveFile(filename):
	with open(filename, 'w') as save_file:
		save_file.write('\n'.join(address_list))
	save_file.close()


block_height = rvn.getblockcount().get("result")
while len(address_list) < int(number_of_wallets):
	if scan_mode == 1:
		block_height = rvn.getblockcount().get("result")
	if block_height != last_block_height:
		last_block_height = block_height
		block_hash = rvn.getblockhash(block_height).get("result")
		txs = rvn.getblock(block_hash,1).get("result").get("tx")
		for tx in txs:
			try:
				vouts = rvn.getrawtransaction(tx,1).get("result").get("vout")
				for vout in vouts:
					addresses = vout.get("scriptPubKey").get("addresses")
					if addresses != None:
						for address in addresses:
							address_list.append(address)
			except:
				print("Some type of vout error that im too lazy to diagnose, the code works without this being fixed")
		address_list = list(set(address_list)) #Delete duplicate entries
		print("New block:",block_height)
		print("Total wallets gathered:",len(address_list),'/',str(number_of_wallets))
		if scan_mode == 0:
			block_height -= 1
	else:
		#time.sleep(1) #You can slow this down if you are dumb
		pass

saveFile(filename)
spam_assets(asset,address_list,spam)


