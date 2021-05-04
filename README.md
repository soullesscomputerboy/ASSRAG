# ASSRAG
Asset Super Spammer and Ravencoin Address Gatherer

Installing/Running
----------------
You need python3, the ravencoin rpc library, and ravencoin core wallet running in daemon mode
You will also need to add the lines 
assetindex=1
addressindex=1
to your raven.conf file. This will require a reindex which can take hours. Good luck, have fun, be polite!

What does this do
----------------
The ASSRAG can search the blockchain for recent transactions, then it saves receive addresses to file. After that it can optionally send assets to those addresses.
