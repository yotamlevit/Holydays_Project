# -*- coding: utf-8 -*-
import math

def get_tri_len(arr):
    count = 0
    side = []
    for point in arr:
        index = count
        while index < len(arr):
            print side
            print index
            if point != arr[index]:
                if point[0] == arr[index][0]:
                    if point[1] > arr[index][1]:
                        side.append(point[1] - arr[index][1])
                    else:
                        side.append(arr[index][1] - point[1])
                elif point[1] == arr[index][1]:
                    if point[0] > arr[index][0]:
                        side.append(point[0] - arr[index][0])
                    else:
                        side.append(arr[index][0] - point[0])
            index += 1
        count += 1
    side.append(math.sqrt(math.pow(side[0], 2) + math.pow(side[1], 2)))
    return side

def main():
    dot = [(100, 100), (150, 200), (300, 400), (500, 500)]
    dot1 = [(100, 100), (150, 100), (100, 200)]
    print get_tri_len(dot1)


if __name__ == '__main__':
    main()