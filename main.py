#!/usr/bin/env python
import config
import bitcoin_fetcher
import email_server
import datetime

time = datetime.datetime.now()

def mailManager(time, buy, sell):
    buyBreakpoint = buy % 100000 == 0
    sellBreakpoint = sell % 100000 == 0

    if buyBreakpoint:
        subject = "[Buy] Bitcoin price at %s " % ( buy )
        message = "%s \r\nYou can now buy bitcoins at %s." % ( time , buy )

    if sellBreakpoint:
        subject = "[Sell] Bitcoin price at %s " % ( sell )
        message = "%s \r\nYou can now sell bitcoins at %s." % ( time , sell )


    data = {
        'subject' : subject,
        'message' : message,
    }


def main():
    print time
    config.execute()

    bc = bitcoin_fetcher.request()
    buy = bc.get('buy')
    sell = bc.get('sell')

    message = "%s \r\nBuy Bitcoins at %s. \r\nSell Bitcoins at %s " % (time, buy, sell )

    email_server.main(message, buy, sell)
    print "[*] Program finished."

main()
