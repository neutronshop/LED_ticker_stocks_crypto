def getsymbolsfrominternal(symbol, profileid, datasource):
    matrixportal.set_text("", 2)
    symbol_price = symbols_Dict[symbol]
    matrixportal.set_text(symbol_price)
    changeBackgroundImage(datasource, symbol, profileid)
    matrixportal.set_text(symbol, 1)
