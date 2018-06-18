from math import *


def swap(list, i, j):
    temp = list[i]
    list[i] = list[j]
    list[j] = temp


def bubblesort(list):
    compares = 0
    length = len(list)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, length):
            if list[i-1] > list[i]:
                swap(list, i-1, i)
                swapped = True
            compares += 1
    print(list)
    print("Comparisons: ", compares)
    print("Approx min: ", ceil(log(factorial(len(list)), 2)))


def insertionsort(list):
    compares = 0
    length = len(list)
    for i in range(1, length):
        j = i
        while j > 0 and list[j-1] > list[j]:
            swap(list, j-1, j)
            j = j - 1
            compares += 1
        compares += 1
    print(list)
    print("Comparisons: ", compares)
    print("Approx min: ", ceil(log(factorial(len(list)), 2)))


def merge(list, start, middle, stop):
    global merge_compares
    i = start
    j = middle + 1
    temp = []
    temp += list
    for k in range(start, stop + 1):
        if i > middle:
            list[k] = temp[j]
            j += 1
        elif j > stop:
            list[k] = temp[i]
            i += 1
        elif temp[j] > temp[i]:
            list[k] = temp[i]
            i += 1
            merge_compares += 1
        else:
            list[k] = temp[j]
            j += 1
            merge_compares += 1


def msort(list, start, stop):
    if start >= stop:
        return
    middle = start + floor((stop-start)/2)
    msort(list, start, middle)
    msort(list, middle+1, stop)
    merge(list, start, middle, stop)


def mergesort(list):
    global merge_compares
    merge_compares = 0
    msort(list, 0, len(list)-1)
    print(list)
    print("Comparisons: ", merge_compares)
    print("Approx min: ", ceil(log(factorial(len(list)), 2)))


def partition(list, start, stop):
    global quick_compares
    pivot = list[stop]
    i = start
    for j in range(start, stop):
        if not(list[j] > pivot):
            swap(list, i, j)
            i += 1
        quick_compares += 1
    swap(list, i, stop)
    return i


def qsort(list, start, stop):
    if start < stop:
        p = partition(list, start, stop)
        qsort(list, start, p-1)
        qsort(list, p+1, stop)


def quicksort(list):
    global quick_compares
    quick_compares = 0
    qsort(list, 0, len(list)-1)
    print(list)
    print("Comparisons: ", quick_compares)
    print("Approx min: ", ceil(log(factorial(len(list)), 2)))


def help():
    print("Commands: ")
    print("help - Prints this menu")
    print("exit or CTRL-D - Exits this program")
    print("sort_method int_list - Enter a sort method followed by a list of space separated integers to sort them")
    print("Possible Sort Methods: bubblesort insertion mergesort quicksort")


if __name__ == "__main__":
    print("Welcome to the sorting thunderdome")
    print("This program is used to compare sorting methods")
    help()
    while True:
        userinput = input("Command: ")
        if userinput == "help":
            help()
        elif userinput == "exit":
            print("Bye")
            break
        else:
            f = userinput.split()[0]
            list = [int(i) for i in userinput.split()[1:]]

            if f == "bubblesort":
                print("Using Bubble Sort:")
                bubblesort(list)
            elif f == "insertion":
                print("Using Insertion Sort:")
                insertionsort(list)
            elif f == "mergesort":
                print("Using Merge Sort:")
                mergesort(list)
            elif f == "quicksort":
                print("Using Quick Sort:")
                quicksort(list)
