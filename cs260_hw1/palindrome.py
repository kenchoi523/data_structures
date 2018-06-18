#author: kenny choi


def palindrome(s):
    s = s.replace(" ", '')
    if str(s) == str(s)[::-1]:
        return True  # is a palindrome
    else:
        return False  # not a palindrome


if __name__ == '__main__':
    test = ['undertakes', 'impassibly', 'pop', 'misericordia', 'pup', 'dinars', 'misprisons', 'tot']
    success = 0
    for i in test:
        print(i, palindrome(i))
        if palindrome(i):
            success += 1
    print("\nPassed", success, "/", len(test), "tests.")
