
def changeBackgroundImage(datasource, symbol, profileid):
    print(datasource)
    img_path = ""
    if datasource == "cryptos":
        img_path = cwd + "/backgrounds/cryptos/" + symbol + ".bmp"
        img_path_generic = cwd + "/backgrounds/crypto_generic/Crypto_background_" + str(profileid) + ".bmp"
    if datasource == "stocks":
        img_path = cwd + "/backgrounds/stocks/" + symbol + ".bmp"
        img_path_generic = cwd + "/backgrounds/stock_generic/Stocks_background_" + str(profileid) + ".bmp"

    print(img_path)

    file_exists = True
    try:
        stats = os.stat(img_path)
    except Exception as error:
        file_exists = False
        print(error)

    if (file_exists):
        matrixportal.set_background(img_path)
    else:
        matrixportal.set_background(img_path_generic)
    # matrixportal.set_text("__________", 3)
    # matrixportal.set_text("__________", 4)
    # matrixportal.set_text("________", 5)
    # matrixportal.set_text("________", 6)
