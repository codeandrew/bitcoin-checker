#!/usr/bin/env python
import config
import bitcoin_fetcher
import email_server

def main(): 
	config.main()

	bc = bitcoin_fetcher.request()
	#print type(bc)
	buy = bc.get('buy')
	sell = bc.get('sell')
	#print buy, sell

	message = "test message" 
	
	email_server.main(message, buy, sell)	
	print "Final Line!" 


