"""
ch03.py

Challenge 3: Find a substring in a large file.

Elijah Theander
October 6, 2022


"""
import re

def challenge(num):
    startingURL = 'http://www.pythonchallenge.com/pc/def/equality.html'
    print("--------------------------------------------------------------------------------\n"
    f"Challenge # {num}: Find a substring in a large file.\n"
    f"Starting url: {startingURL}\n"
    "--------------------------------------------------------------------------------\n"
     )

    with open('ch03.txt', 'r') as data:
        dataList = []

        for line in data:
            for character in line:
                if(character != '\n'):
                    dataList.append(character)

        clue = ''.join(dataList)


    substring = re.compile("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+")
    result = substring.findall(clue)

    print(f"Result: {result}\n")

    next = ''.join(result)
    nextURL = f'http://www.pythonchallenge.com/pc/def/{next}.html\n'
    print(f'Next challenge URL: {nextURL}')
    



def main():
    print("--------------------------------------------------------------------------------\n"
    "                               PYTHON CHALLENGE\n"
    "--------------------------------------------------------------------------------\n"
    )

    challenge(0)
    

if __name__ == "__main__":
    main()