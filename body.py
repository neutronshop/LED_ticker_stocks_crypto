# Neutronshop.com
# Copyright 2023, Neutronshop, All rights reserved.
import time
import board
import terminalio
import supervisor
import gc
import os
import time

from adafruit_matrixportal.matrixportal import MatrixPortal

# CURRENCY = "USD"
cwd = ("/" + __file__).rsplit("/", 1)[0]
Currency_APIKEY = "7654ebddd42acb2625e520bbc2268a4d"
symbols_Dict = {}
currency_Dict = {}
LicenseCheck = ""
LicenseCheck_only1time = ""

try:
    from secrets import secrets
except ImportError:
    print("WiFi secrets are kept in secrets.py, please add them there!")
    raise

from secrets import serialNo, Test_mode, Symbol_Font, Price_Font, BottomLines_color, TopLines_color, \
    symbol_text_X_position, crypto_API_TO_USE, Show_Currency_Symbol, show_time, time_mode, timezone, show_logo, \
    show_eth_gas_price, gas_price_type, gas_price_speed, gas_price_wait_time, show_time, stocks, cryptos, \
    Finnhub_crypto_exchange, price_text_X_position, refresh_rate, Show_Animations, animation_folders, loading_image, \
    round_stock_price, round_crypto_price, Price_color, Ticker_color, logo_image, Base_Currency

matrixportal = MatrixPortal(
    default_bg=cwd + loading_image,
    status_neopixel=board.NEOPIXEL,
    debug=True
)

Curr_Symbol = "$"
BLINK = True

if Base_Currency == "EUR":
    Curr_Symbol = "€"
if Base_Currency == "GBP":
    Curr_Symbol = "£"

if Show_Currency_Symbol.lower() == "false":
    Curr_Symbol = ""


# colors
def switch_colors(txt_color):
    txt_color = txt_color.lower()
    switcher = {
        "black": 0x000000,
        "white": 0xffffff,
        "red": 0xff0000,
        "yellow": 0xffcc00,
        "blue": 0x0066ff,
        "green": 0x00cc00,
        "pink": 0xff00ff
    }
    return switcher.get(txt_color, "Invalid color")


def text_transform(val):
    if Base_Currency == "USD":
        return "$%d" % val
    #    if Base_Currency == "EUR":
    #        return "‎€%d" % val
    #    if Base_Currency == "GBP":
    #        return "£%d" % val
    return "%d" % val


if Symbol_Font == "Large":
    # symb_Font =  terminalio.FONT
    symb_Font = cwd + "/fonts/cherry-13-b.bdf"
    # top_line_Y = 8
    symbol_text_Y_position = 7
else:
    symb_Font = cwd + "/fonts/Tamzen5x9r.bdf"
    # top_line_Y = 5
    symbol_text_Y_position = 7

if Price_Font == "Large":
    Pr_Font = terminalio.FONT
    # Pr_Font = cwd + "/fonts/cherry-10-r.bdf"
    # btm_line_Y = 20
    price_text_Y_position = 22

else:
    Pr_Font = cwd + "/fonts/spleen-5x8.bdf"
    # btm_line_Y = 21
    price_text_Y_position = 23

# Text 0 Price
matrixportal.add_text(
    # text_font=terminalio.FONT,
    text_font=Pr_Font,
    text_position=(price_text_X_position, price_text_Y_position),
    text_color=switch_colors(Price_color.lower()),
    text_transform=text_transform
)

# Text 1 Symbol
matrixportal.add_text(
    text_font=symb_Font,
    text_position=(symbol_text_X_position, symbol_text_Y_position),
    text_color=switch_colors(Ticker_color.lower()),
    text_transform=text_transform
    # scrolling = True
)

# Text 2 Time & message 1
matrixportal.add_text(
    text_font=terminalio.FONT,
    text_position=(20, 12),  # 19, 23
    text_color=0xffffff
)

# Text 3  Hashtags text
matrixportal.add_text(
    text_font=terminalio.FONT,
    text_position=(19, 22),
    text_color=0xffffff,
    scrolling=True
)


matrixportal.preload_font(b"$€£012345789")
matrixportal.preload_font((0x00A3, 0x20AC))

time.sleep(1)  # show first image
LicenseCheck == ""


def ValidLicense(serialNo):
    print("Validating License...")
    DATA_SOURCE = "https://neutronshoplic.herokuapp.com/NLicenses/" + serialNo
    print(DATA_SOURCE)
    DATA_LOCATION = ["nLicense", "nStatus"]  # for this API c means current price
    # Safe_Offline serial NEU1000123000
    if (serialNo == "NEU1000123000"):
        print("License status: SAFE ACTIVE")
        LicenseCheck = "Active"
    else:
        try:
            lic_data = matrixportal.network.fetch(DATA_SOURCE)
            License = matrixportal.network.json_traverse(lic_data.json(), DATA_LOCATION)
            if (License == "Active"):
                print("License status: " + License)
                LicenseCheck = "Active"
                NetworkStatus = "Ok"
            else:
                print("License status: " + License)
                matrixportal.set_background(cwd + "/systemimg/lic.bmp")
                LicenseCheck = "InActive"
                time.sleep(10)


        except Exception as error:
            print(error)
            matrixportal.set_background(cwd + "/systemimg/error_Wifi.bmp")
            NetworkStatus = "Error"
            time.sleep(15)
            if NetworkStatus == "Error":
                supervisor.reload()  # restart

    return LicenseCheck


def run_file(path):
    return exec(open(path).read());

run_file("NEUfunctions.py");

def mem_cleaner():
    free_mem = gc.mem_free()
    print("Current memory:" + str(free_mem))
    if free_mem <= 40000 and free_mem >= 10000:
        gc.collect()
        print("Garbage collected.")
        free_mem = gc.mem_free()
        print("Free mem:" + str(free_mem))
    if free_mem < 8000:
        supervisor.reload()  # restart to clean memory


if crypto_API_TO_USE.lower == "finnhub":
    cycleTimes = 5
else:
    cycleTimes = 15
    # coinmarketcap is more restricted for free plan


loop = 0

while True:
    if (Test_mode.lower() == "true"):
        matrixportal.set_background(cwd + "/systemimg/black.bmp")
        matrixportal.set_text("", 1)
        matrixportal.set_text("TEST MODE")
        time.sleep(3)
        for stock in stocks:
            symbol = stock
            TestModefeature("stocks", symbol, stocks.index(symbol) + 1)

        for crypto in cryptos:
            symbol = crypto
            TestModefeature("cryptos", symbol, cryptos.index(symbol) + 1)
    else:

        if (LicenseCheck_only1time == ""):
            LicenseCheck = ValidLicense(serialNo)
            LicenseCheck_only1time = LicenseCheck
        if (LicenseCheck == "Active"):
            run_file("execution.py");
        else:
            print("Invalid license")
            LicenseCheck = ValidLicense(serialNo)
