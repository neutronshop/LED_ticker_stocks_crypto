
def getTime(hours=None, minutes=None, show_colon=True):
    # now = time.localtime()
    matrixportal.set_background(cwd + "/systemimg/black.bmp")

    if time_mode == "ip":
        DATA_SOURCE = "http://worldtimeapi.org/api/ip"
    else:
        DATA_SOURCE = "http://worldtimeapi.org/api/timezone/" + timezone

    result = ""
    try:
        data = matrixportal.network.fetch(DATA_SOURCE)
        str_time = matrixportal.network.json_traverse(data.json(), ["datetime"])

        result = "ok"
    except Exception as error:
        result = "error"
        print(error)
        time.sleep(15)
        supervisor.reload()  # restart
    while result == "error":
        try:
            data = matrixportal.network.fetch(DATA_SOURCE)
            str_time = matrixportal.network.json_traverse(data.json(), ["datetime"])

            result = "ok"
        except Exception as error:
            result = "error"
            print(error)
            time.sleep(15)

    str_time = str_time[0:16]
    str_time = str_time[11:16]
    clock_label = str_time

    # print(clock_label)
    print(clock_label)
    matrixportal.set_text("", 0)
    matrixportal.set_text("", 1)
    matrixportal.set_text(clock_label, 2)
