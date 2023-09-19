# Neutronshop.com
# Copyright 2023, Neutronshop, All rights reserved.
# This file controls the execution and sequence of all the device
# custom functions.
#
#if device is online, it will pull values from the internet
if loop == 0 or loop % cycleTimes == 0:
    loop = 0
    # display preloaded GIFs animation
    if Show_Animations.lower() == "true":
        for folder in animation_folders:
            GIFanimation(folder)
    # cycle through each stock symbol in secrets file
    for stock in stocks:
        symbol = stock
        # print(symbol)
        if (symbol != ""):
            try:
                getsymbolsdata(symbol, stocks.index(symbol) + 1, "stocks", FinnHub_APIkey)
                mem_cleaner()
                time.sleep(refresh_rate)


            except (ValueError, RuntimeError) as e:
                print("Some error occured, retrying! -", e)

    # cycle through each crypto symbol in secrets file
    for crypto in cryptos:
        symbol = crypto
        # print(symbol)
        if (symbol != ""):
            try:
                if (crypto_API_TO_USE == "Finnhub"):
                    getsymbolsdata(symbol, cryptos.index(symbol) + 1, "cryptos", FinnHub_APIkey)
                else:
                    getfromcoinmarketcap(symbol, cryptos.index(symbol) + 1, CoinMarketcap_APIkey)
                mem_cleaner()
                time.sleep(refresh_rate)

            except (ValueError, RuntimeError) as e:
                print("Some error occured, retrying! -", e)

    matrixportal.set_text("", 0)
    matrixportal.set_text("", 1)

    # show logo
    if show_logo == "True":
        matrixportal.set_background(cwd + "/logo.bmp")
        time.sleep(5)

#if device is not online, it will pull last values from internal memory
#this avoids crashes with intermittent internet
else:
    if show_time == "True":
        getTime()
        time.sleep(5)

    #display preloaded GIFs animation
    if Show_Animations.lower() == "true":
        for folder in animation_folders:
            GIFanimation(folder)

    # cycle through each stock symbol in secrets file
    for stock in stocks:
        symbol = stock
        # print(symbol)
        # print("loop " + str(loop))
        getsymbolsfrominternal(symbol, stocks.index(symbol) + 1, "stocks")
        print("after symbols Internal")
        mem_cleaner()
        time.sleep(refresh_rate)

    #cycle through each crypto symbol in secrets file
    for crypto in cryptos:
        symbol = crypto
        # print(symbol)
        # print("loop " + str(loop))
        getsymbolsfrominternal(symbol, cryptos.index(symbol) + 1, "cryptos")
        print("after symbols Internal")
        mem_cleaner()
        time.sleep(refresh_rate)

    matrixportal.set_text("", 0)
    matrixportal.set_text("", 1)

    # show custom logo
    if show_logo == "True":
        matrixportal.set_background(cwd + "/logo.bmp")
        time.sleep(5)

loop += 1