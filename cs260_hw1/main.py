from palindrome import palindrome


def main():
    print("Welcome to Palindrome Checker!")
    print("Enter a word. The program will tell you if it is a palindrome.")
    print("To quit enter a blank line.")
    while True:
        s = input("Enter a word to check: ")
        if s == "":
            break
        print("The word is a palindrome:", palindrome(s))


if __name__ == '__main__':
    main()