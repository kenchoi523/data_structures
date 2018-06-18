from queue import *
import sys

if len(sys.argv) == 1:
    print("Usage: python josephus NumPeople MthPerson")
    sys.exit(1)
elif len(sys.argv) == 3:
    numPeople = int(sys.argv[1])
    mthPerson = int(sys.argv[2])

    people = list(range(numPeople))
    counter = 1
    pointer = 0

    josephus = Queue()

    while people.count(None) != len(people):
        if counter == mthPerson:
            josephus.enqueue(people[pointer])
            people[pointer] = None
            counter = 0
        pointer += 1
        pointer = pointer % numPeople
        if people[pointer] is not None:
            counter += 1
    print(str(josephus))









