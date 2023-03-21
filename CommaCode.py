spam = ['apples', 'bananas', 'tofu', 'cats']

def CommaCode(somelist):
    string = ""
    for i in somelist[:-1]:
        string += str(i) + ", "
    string += "and " + str(somelist[-1]) + "."
    return string

string = CommaCode(spam)
print(f"{string}")