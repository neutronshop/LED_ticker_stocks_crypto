
def GIFanimation(folder):
    # matrixportal.set_text("",0)

    directory_path = cwd + "/animations/" + folder
    No_of_files = len(os.listdir(directory_path))
    i = 1
    loops = 0
    while (loops <= 2):
        while (i <= No_of_files):
            # print(i)
            num = str(i)
            if i <= 9:
                num = "0" + str(i)
            matrixportal.set_background(cwd + "/animations/" + folder + "/" + num + ".bmp")
            # time.sleep(0.2)
            i += 1
        loops += 1
        i = 1
    # first image to show while the data loads.
    matrixportal.set_background(cwd + loading_image)
