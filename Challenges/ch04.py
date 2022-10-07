"""
ch04.py

Challenge 4: Grabbing information from webpages. And traversing links

Elijah Theander
October 7, 2022


"""
from urllib.request import urlopen
import re

def traverse(startLink,substring):
    print("Traversing Links, this will take a while...")
    data = urlopen(startLink).read().decode('utf-8')
    result = substring.search(data)
    next = result.group(1)
    nextLink =f'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={next}'

    while True:
        data = urlopen(nextLink).read().decode('utf-8')
        result = substring.search(data)
        output = [data,next,nextLink]

        if result is None:
            print('Link traversal finished!\n')
            return output
            break
        
        next = result.group(1)
        nextLink = f'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={next}'




def challenge(num):
    startingURL = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
    print("--------------------------------------------------------------------------------\n"
    f"Challenge # {num}: 4 Grab information from webpages.\n"
    f"Starting url: {startingURL}\n"
    "--------------------------------------------------------------------------------\n"
     )

    firstLink = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345'
    substring = re.compile('and the next nothing is (\d+)')

    result = traverse(firstLink,substring)

    print(f'Output from first traversal:\n{result[0]}\n{result[1]}\n{result[2]}\n')

    #so, we have to divide by two and run again.

    next = int( int(result[1])/2)
    nextLink = f'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={next}'

    print(f"The next starting link for traversal:\n{nextLink}\n")

    result = traverse(nextLink,substring)

    print(f"Results of second traversal:\n{result[0]}\n{result[1]}\n{result[2]}\n")



    next = result[0]
    nextURL = f'http://www.pythonchallenge.com/pc/def/{next}\n'
    print(f'Next challenge URL: {nextURL}')
    



def main():
    print("--------------------------------------------------------------------------------\n"
    "                               PYTHON CHALLENGE\n"
    "--------------------------------------------------------------------------------\n"
    )

    challenge(4)
    

if __name__ == "__main__":
    main()