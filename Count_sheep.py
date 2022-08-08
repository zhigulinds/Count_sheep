import time


def count_sheep():
    for i in range (0,6):
        print(i, end="Sheep....")
        time.sleep(2)

count_sheep()