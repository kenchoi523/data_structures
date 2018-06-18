from heap import *

def help():
    print("help - Prints this list")
    print("makenull - Clears the heap")
    print("insert <integer> - Inserts the number into the heap")
    print("min - Prints the current min on the heap")
    print("inorder - Prints heap in inorder")
    print("preorder - Prints heap in preorder")
    print("postorder - Prints heap in postorder")
    print("deletemin - Removes min from the heap")
    print("sort - Calls deletemin repeatedly to print out sorted numbers")
    print("exit - Exits the program (also Ctrl-D exits)")

if __name__ == "__main__":
    heap = Heap()


    print("Welcome to the Heap")
    print("The List of Commands is below, type help to see them again.")
    help()
    while True:
        rawinput = input(">")
        userinput = rawinput.split(" ")
        command = userinput[0]
        if len(userinput) >= 2:
            value = userinput[1]
        if command == "help":
            help()
        elif command == "makenull":
            heap.makenull()
        elif command == "insert":
            heap.insert(int(value))
        elif command == "min":
            print(heap.min())
        elif command == "inorder":
            heap.inorder(0)
            print()
        elif command == "preorder":
            heap.preorder(0)
            print()
        elif command == "postorder":
            heap.postorder(0)
            print()
        elif command == "deletemin":
            heap.deletemin()
        elif command == "sort":
            for i in range(0, heap.last):
                print(heap.min())
                heap.deletemin()
        elif command == "exit":
            break
        else:
            print("Invalid input")