@ -1,74 +0,0 @@
# Neutronshop's LED ticker stocks and crypto ticker

This is the code release for Neutronshop's LED ticker available at neutronshop.com (Amazon, Etsy and Ebay as well).
WARNING: This code is designed only to work with neutronshop's display, be advised that trying this code on a different LED display may result in multiple frustrations.

## Installation

Download code as zip.
Open file secrets.py and enter your Wifi credentials and API keys.

```python
secrets = {
        'ssid' : 'YOUR_WIFI_NAME',
        'password' : 'YOUR_Password',
        'FINNHUB_API_KEY': 'c0cdelf48v6u6kubpqqg', #get API key from https://finnhub.io/
        'COINMARKETCAP_API_key': 'b52382d1-007e-4a4c-b3e0-5eceaf99c1f6' #get API key from https://coinmarketcap.com/api/pricing/
    }
```

Before you make any other customizable changes it is recommended to test the display.
You can copy the entire code into the drive.
Your drive will reboot and should display default values for stocks and crypto.

## Instructions and Video tutorial:
https://neutronshop.com/tutorial_cryptoled/

## Offline testing

By setting test_mode = False you can test the display without internet.

```python
Test_mode = "False"
```

## Contributing

It is easy to add additional features (or functions).
Current functions are stored in /functions folder.
You can create your own functions or applications in the same folder.
Add your new application to NEUfunctions.py

```python
run_file(functionsdir +"currencyconvert.py");
run_file(functionsdir +"gifanimation.py");
run_file(functionsdir +"gettime.py");
run_file(functionsdir +"crypto_coinmarketcap.py");
run_file(functionsdir +"symbols_internal_storage.py");
run_file(functionsdir +"change_background.py");
run_file(functionsdir +"stocks_finnhub.py");
run_file(functionsdir +"test_mode.py");
#Add here
```
The "execution.py" file is in charge of controlling the logic to display the different features.
Here is an example of how it loops for each stock:

```python
    # cycle through each stock symbol in secrets file
    for stock in stocks:
        symbol = stock
        # print(symbol)
        # print("loop " + str(loop))
        getsymbolsfrominternal(symbol, stocks.index(symbol) + 1, "stocks")
        print("after symbols Internal")
        mem_cleaner()
        time.sleep(refresh_rate)
```
That's it!
All you need is in the functions folder, add to NEUfunctios.py and control the execution in execution.py.

Please make sure to update tests as appropriate and share with the world in this repository.

## License

[MIT](https://choosealicense.com/licenses/mit/)