#Neutronshop.com
#Please enter your Wifi Name and Password.
#Every line starting with # is just a comment line and will be ignored by the program.

#WIFI name should be exactly as it shows up in your computer/phone
#DO NOT REMOVE THE SINGLE QUOTES
#DO NOT REMOVE THE COLON, COMMAS OR ANY PUNCTUATION MARKS
#EXAMPLE: 'ssid' : 'Anderson Home WIFI'
serialNo = 'NEU111437011'

secrets = {
        'ssid' : 'YOUR_WIFI_NAME',
        'password' : 'YOUR_Password',
        'FINNHUB_API_KEY': 'c0cdelf48v6u6kubpqqg', #get API key from https://finnhub.io/
        'COINMARKETCAP_API_key': 'b52382d1-007e-4a4c-b3e0-5eceaf99c1f6' #get API key from https://coinmarketcap.com/api/pricing/
    }

#FIRST TIME USE: Before changing anything below this line, try just updating the above values.

Base_Currency = "USD"
#You can change to other currencies like EUR, GBP, MXN, etc
Show_Currency_Symbol = "True"
#Remove or Add the $ or € sign.
#For any cryptos with over 6 digits it will hide the $ sign for space.

#stocks will use images with the name Stocks_ in the backgrounds folder
#To remove displaying stocks, leave empty like this:
#stocks = []
stocks = ["AAPL","TSLA","GME", "AMC"]
#for custom backgrounds, save a BMP image (64 x 32 pixels size) in backgrounds\stocks with the ticker name.
round_stock_price = "False"

#cryptos will use images with the name Cryptos_ in the backgrounds folder
cryptos = ["BTC", "ETH", "SHIB", "DOGE", "ADA"]
#for custom backgrounds, save a BMP image (64 x 32 pixels size) in backgrounds\cryptos with the ticker name.

round_crypto_price = "False"

crypto_API_TO_USE = "Coinmarketcap"  #Finnhub or Coinmarketcap
#Coinmarketcap supports more cryptocurrencies not listed in exchanges but price refresh rate is every 30 min
#Finnhub has a refresh rate of 5 minutes but less cryptos are supported.

#if Using Finnhub API, specify the exchange you want to use
Finnhub_crypto_exchange = "BINANCE"  #KRAKEN,HITBTC,COINBASE,POLONIEX,KUCOIN,OKEX,BITFINEX

#ETH GAS PRICE from https://ethgas.watch/
show_eth_gas_price = "False"
gas_price_type = "GWEI" #GWEI or USD: Show price in GWEI or USD. Price in USD is an average of 21000 gas
gas_price_speed = ["RAPD", "FAST", "STD", "SLOW"] #You can edit what prices you want to show
gas_price_wait_time = 5  #wait time for each price in seconds
#example:
#gas_price_speed = ["FAST"]


#Other Settings:

Test_mode = "False" #Disables online features to check play around with appeareance settings.

#color options: #white,red,yellow,blue,green,pink
Ticker_color = "yellow"
Price_color = "white"
BottomLines_color = "yellow"
TopLines_color = "red"

Symbol_Font = "Large"  #Large or Small
Price_Font = "Large"   #Large or Small

show_time = "False"
#Time is based on the location of your IP address, if you need to adjust your settings use timezone instead:
time_mode = "ip" #ip or timezone
timezone = "America/Chicago"
#timezones examples (use _ instead of spaces)
#America/New_York
#Europe/London
#America/Argentina/Salta

symbol_text_X_position = 28 #increase to move right, decrease to move left
symbol_scrolling = "True"
price_text_X_position = 15  #increase to move right, decrease to move left

refresh_rate = 12 #time in seconds. You can try lower time, but I recommend 12.
loading_image = "systemimg/loading.bmp"

show_logo = "True"
logo_image = "logo.bmp"   #Add your own logo!  (BMP file 64 x 32 pixels in size)
#Animations
#If Show_Animations is False it will just display the slides without animations.
Show_Animations = "False" #change to True
#Animations to display (located in animations folder)
animation_folders = ["gif_1", "gif_2", "gif_3"]

#note: Only 10 backgrounds for cryptos and 10 for stocks are included in the backgrounds folder.
#it is not recommended to add more for performance and memory optimization.

# Neutronshop.com
# Copyright 2021, Neutronshop, All rights reserved.

