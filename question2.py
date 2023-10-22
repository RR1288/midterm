def what_does_the_fox_say(func):
    saying = func()
    print("The fox says", saying)

def auuu():
    return "auuuuu"
def foxy():
    return "foxy"
def nothing():
    return "[nothing]"

def main():
    what_does_the_fox_say(auuu)
    what_does_the_fox_say(foxy)
    what_does_the_fox_say(nothing)

if __name__  == "__main__":
    main()