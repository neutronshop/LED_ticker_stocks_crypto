def currency_convert(val, curr):
    curr_pair = "USD" + Base_Currency
    # if dictinary is empty
    if len(currency_Dict) == 0:
        print("Retrieving Currency Prices...")
        DATA_SOURCE = "http://api.currencylayer.com/live?format=1&currencies=" + Base_Currency + "&access_key=" + Currency_APIKEY
        DATA_LOCATION = ["quotes", curr_pair]  # for this API c means current price
        curr_data = matrixportal.network.fetch(DATA_SOURCE)
        curr_price = matrixportal.network.json_traverse(curr_data.json(), DATA_LOCATION)
        # add to DICT
        currency_Dict[curr] = curr_price
    return val * currency_Dict[curr]