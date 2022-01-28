import pyautogui
# import pillow
# from numpy import array, asarray
import time
from PIL import Image, ImageGrab


# def takeScreenshot():
#     image = ImageGrab.grab().convert('L')
#     image.show()
#     return image


# def draw():
#     for i in range(34, 45):
#         for j in range(45, 67):
#             data

def isCollide(data):
 # find the cactus
    for i in range(750, 800):
        for j in range(500, 520):
            if data[i, j] < 100:
                hit('up')
                return
# find the birds
    for i in range(680, 730):
        for j in range(400, 470):
            if data[i, j] < 100:
                hit('down')
                return
    return

def hit(key):
    pyautogui.keyDown(key)
    return


if __name__ == '__main__':
    time.sleep(5)
    #hit('up')

    while True:
        image = ImageGrab.grab().convert('L')
        # image = takeScreenshot()
        data = image.load()
        isCollide(data)

        # #print(asarray(image)
        # for i in range(710, 740):
        #     for j in range(490, 530):
        #          data[i, j] = 0
        #
        #
        # for i in range(690, 740):
        #     for j in range(400, 460):
        #          data[i, j] = 171
        #
        # image.show()
        # break



