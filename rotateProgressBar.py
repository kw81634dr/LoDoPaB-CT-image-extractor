import sys
import time


def animated_loading():
    chars = "/—\|"
    for char in chars:
        sys.stdout.write('\r'+'loading...'+char)
        time.sleep(.4)
        sys.stdout.flush()


if __name__ == '__main__':
    while 1:
        animated_loading()
