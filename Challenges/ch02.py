"""
ch02.py

Challenge 2: Recognize Rare Characters.

Elijah Theander
October 6, 2022


"""

def challenge(num):

    startingURL = 'http://www.pythonchallenge.com/pc/def/ocr.html'
    print("--------------------------------------------------------------------------------\n"
    f"Challenge # {num}: Recognize rare characters.\n"
    f"Starting url: {startingURL}\n"
    "--------------------------------------------------------------------------------\n"
     )

    with open('ch02.txt', 'r') as data:

        charCount = {}

        for line in data:
            for character in line:
                if character in charCount:
                    charCount[character] += 1
                else:
                    charCount[character] = 1
        
    min = None

    for count in charCount.values():
        if min is None:
            min = count
        elif(count < min):
            min = count

    print(f'The fewest number of occurrances: {min}\n')

    minList = []
    for char, count in charCount.items():
        if count == min:
            minList.append(char)
        
    print(f'Characters with fewest occurrances: {minList}\n')


    next = ''.join(minList)

    nextURL = f'http://www.pythonchallenge.com/pc/def/{next}.html\n'
    print(f'Next challenge URL: {nextURL}')
    



def main():
    print("--------------------------------------------------------------------------------\n"
    "                               PYTHON CHALLENGE\n"
    "--------------------------------------------------------------------------------\n"
    )

    challenge(2)
    

if __name__ == "__main__":
    main()