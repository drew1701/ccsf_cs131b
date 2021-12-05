# original code creates endless loop, this has been PEP8 reformatted

def greatest_number(file):
    with open(file, 'r') as text:
        print("file opened")
        number = [line.strip().split() for line in text.readlines()]
        print("number assigned")  # this prints then hangs on return
        return max(map(int, sum(number, [])))


print(greatest_number("urantia.txt"))
