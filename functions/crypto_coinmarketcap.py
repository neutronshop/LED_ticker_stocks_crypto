
def getfromcoinmarketcap(symbol, profileid, APIKEY):
    matrixportal.set_text("", 2)
    print("Coinmarketcap start")
    #APIKEY = secrets["COINMARKETCAP_API_key"]
    symbolUpper = symbol.upper()
    DATA_SOURCE = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol=" + symbolUpper + "&convert=" + Base_Currency + "&CMC_PRO_API_KEY=" + APIKEY
    DATA_LOCATION = ["data", symbolUpper, "quote", Base_Currency, "price"]
    DATA_PercentChange = ["data", symbolUpper, "quote", Base_Currency, "percent_change_24h"]


    try:
        symbols_data = matrixportal.network.fetch(DATA_SOURCE)
    except Exception as error:
        matrixportal.set_background(cwd + "/systemimg/error_Wifi.bmp")
        time.sleep(5)
        supervisor.reload()

    try:
        symbol_price = matrixportal.network.json_traverse(symbols_data.json(), DATA_LOCATION)
        percent_change = matrixportal.network.json_traverse(symbols_data.json(), DATA_PercentChange)
        if (percent_change > 0):
            Strpercent_change = "    " + str(round(percent_change)) + "%"

        elif (round(percent_change) == 0):
            Strpercent_change = "    " + str(round(percent_change)) + "%"
        else:
            Strpercent_change = "    " + str(round(percent_change)) + "%"

        # symbol_price = round(symbol_price, 12)
        symbol_price = str(symbol_price)
        print(symbol_price)
        if "e" in symbol_price:
            print("price e")
            multi = symbol_price.split("e", 1)[-1]
            multi = multi.replace("-", "")
            multi = int(multi)
            print(multi)
            zeros = "0."
            i = 0
            while i < multi - 1:
                zeros = zeros + "0"
                i = i + 1

            symbol_price = symbol_price[:3]
            symbol_price = zeros + symbol_price.replace(".", "")

            # if (scroll_large_prices.lower() == "true"):
            #   matrixportal.scroll_text(SCROLL_DELAY)

        if (Show_Currency_Symbol.lower() == "true"):
            symbol_price = Curr_Symbol + " " + symbol_price[:11]
        else:
            symbol_price = symbol_price[:12]
        symbols_Dict[symbol] = symbol_price
        print(symbol_price)
    except Exception as error:
        result = "error"
        print(error)
        matrixportal.set_text("")
        matrixportal.set_text("", 1)
        matrixportal.set_text("", 2)
        matrixportal.set_background(cwd + "/systemimg/error_API.bmp")
        time.sleep(15)

    changeBackgroundImage("cryptos", symbol, profileid)
    matrixportal.set_text(symbol_price)
    matrixportal.set_text(symbol, 1)
    time.sleep(5)
    matrixportal.set_text(Strpercent_change)
    if (round(percent_change) >= 0):
        matrixportal.set_background(cwd + "/systemimg/up.bmp")
    else:
        matrixportal.set_background(cwd + "/systemimg/down.bmp")

