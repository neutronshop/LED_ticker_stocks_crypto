
def TestModefeature(datasource, symbol, profileid):
    print("Test Mode enabled")

    matrixportal.set_text("")
    changeBackgroundImage(datasource, symbol, profileid)
    matrixportal.set_text("0.123456789123")
    matrixportal.set_text(symbol, 1)
    time.sleep(5)
    # matrixportal.set_text("__________", 3)
    # matrixportal.set_text("__________", 4)
    # matrixportal.set_text("________", 5)
    # matrixportal.set_text("________", 6)
    if show_logo == "True":
        matrixportal.set_text("")
        matrixportal.set_text("", 1)
        matrixportal.set_background(cwd + "/logo.bmp")
        time.sleep(5)

    if Show_Animations.lower() == "true":
        matrixportal.set_text("")
        matrixportal.set_text("", 1)
        for folder in animation_folders:
            GIFanimation(folder)

    time.sleep(5)
    # matrixportal.set_background(cwd + "/systemimg/black.bmp")
