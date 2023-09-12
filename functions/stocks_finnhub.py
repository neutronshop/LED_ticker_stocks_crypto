
def getsymbolsdata(symbol, profileid, datasource):
    matrixportal.set_text("", 2)
    print("getsymbolsdata start")
    print("profile id:", profileid)
    APIKEY = secrets["FINNHUB_API_KEY"]
    # Set up where we'll be fetching data from
    symbolUpper = symbol.upper()
    if (datasource == "stocks"):
        DATA_SOURCE = "https://finnhub.io/api/v1/quote?symbol=" + symbolUpper + "&token=" + APIKEY
        DATA_LOCATION = ["c"]  # for this API c means current price

    elif (datasource == "cryptos"):
        DATA_SOURCE = "https://finnhub.io/api/v1/quote?symbol=" + Finnhub_crypto_exchange + ":" + symbolUpper + "USDT&resolution=D&token=" + APIKEY
        DATA_LOCATION = ["c"]  # for this API c means current price

    result = ""

    try:
        symbols_data = matrixportal.network.fetch(DATA_SOURCE)
    except Exception as error:
        result = "error"
        print(error)
        matrixportal.set_background(cwd + "/systemimg/error_Wifi.bmp")
        time.sleep(10)
        supervisor.reload()

    try:
        symbol_price = matrixportal.network.json_traverse(symbols_data.json(), DATA_LOCATION)

        if Base_Currency != "USD":
            print("Converting Currency to " + Base_Currency)
            symbol_price = currency_convert(symbol_price, Base_Currency)
        # add to DICT
        symbols_Dict[symbol] = symbol_price

    # pylint: disable=broad-except
    except Exception as error:
        result = "error"
        print(error)
        matrixportal.set_background(cwd + "/systemimg/error_API.bmp")
        time.sleep(5)

    while result == "error":
        try:
            symbols_data = matrixportal.network.fetch(DATA_SOURCE)
            symbol_price = matrixportal.network.json_traverse(symbols_data.json(), DATA_LOCATION)
            # add to DICT
            symbols_Dict[symbol] = symbol_price
            result = "ok"
            time.sleep(1 * 15)
            tries = tries + 1
            print(result)
            print(tries)

        # pylint: disable=broad-except
        except Exception as error:
            result = "error"
            print(error)
    # symbol_price = text_transform(symbol_price)

    # add to DICT
    if (datasource == "stocks"):
        if (round_stock_price.lower() == "true"):
            symbol_price = Curr_Symbol + " " + str(round(symbol_price, 2))
        else:
            symbol_price = Curr_Symbol + str(symbol_price)
    else:
        if (round_crypto_price.lower() == "true"):
            if len(str(symbol_price)) < 7:
                symbol_price = Curr_Symbol + " " + str(round(symbol_price))
            else:
                symbol_price = str(round(symbol_price))
        else:
            if len(str(symbol_price)) < 7:
                symbol_price = Curr_Symbol + str(round(symbol_price, 8))
            else:
                symbol_price = str(round(symbol_price, 8))
    print(symbol_price)
    symbols_Dict[symbol] = symbol_price
    matrixportal.set_text(symbol_price)
    changeBackgroundImage(datasource, symbol, profileid)
    matrixportal.set_text(symbol, 1)
