# ASSRAG
Asset Super Spammer and Ravencoin Address Gatherer

Installing/Running
----------------
You need python3, the ravencoin rpc library, and ravencoin core wallet running in daemon mode
You will also need to add the lines 
assetindex=1
addressindex=1
to your raven.conf file. This will require a reindex which can take hours. Good luck, have fun, be polite!

Windows Installation
----------------
A few people have asked for a windows guide on how to use this tool. This is going to be a quick extremely basic 'guide' on how to install dependencies. If you need more help than what is listed here, I urge you to google your questions. This should be fairly easy.

Install the latest version of Python from here: https://www.python.org/downloads/

During installation make sure you check the box that says add to PATH, also install pip if that is an option.

After installing python click the start button, type cmd and hit enter. This should open a command prompt.

Type 'python3 pip install ravenrpc' without quotes into the command prompt.

Click start type %appdata% and hit enter. Find the folder named 'Raven'. Create a file in that folder called raven.conf. Add these lines to the file (change the user and password):

rpcuser=alice
rpcpassword=DONT_USE_THIS_YOU_WILL_GET_ROBBED_8ak1gI25KFTvjovL3gAM967mies3E=
assetindex=1
addressindex=1

You will have to start ravencoin in daemon mode and probably reindex, that will take hours.

Download ASSRAG and save it as ASSRAG.py edit the file in notepad to change the asset name that you want to spam., also make sure rpcuser and password match the raven.conf file. Ensure you have enough RVN to pay for transaction fees.



What does this do
----------------
The ASSRAG can search the blockchain for recent transactions, then it saves receive addresses to file. After that it can optionally send assets to those addresses.


Donate RVN here: RCghrkNAZWYoYZY3ZeSaRePYdDYcKXVWq9
