#!/usr/bin/env python
import config
import bitcoin_fetcher
import email_server

def main():
    config.execute()

    bc = bitcoin_fetcher.request()
    buy = bc.get('buy')
    sell = bc.get('sell')

    message = "Buy Bitcoins at %s. \r\nSell Bitcoins at %s " % ( buy, sell )

    email_server.main(message, buy, sell)
    print "[*] Program finished."

main()
