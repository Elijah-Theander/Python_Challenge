"""
ch01.py

Python Challenge 1:  Translate String using a map

Elijah Theander
October 6, 2022


"""

import string

def challenge(num):
    startingURL = 'http://www.pythonchallenge.com/pc/def/map.html'
    print("--------------------------------------------------------------------------------\n"
    f"Challenge # {num}: Translate a String by using a map.\n"
    f"Starting url: {startingURL}\n"
    "The image on this page shows a map of letters.\n"
    "K->M, O-Q, E->G\n"
    "So it would appear that the map for each letter is the letter two spaces to the\n"
    "right of it, alphabetically. I am going to assume Y and Z will wrap around and\n"
    " map to A and B."
    "--------------------------------------------------------------------------------\n"
     )

    with open('ch01.txt', 'r') as data:

        clue = ''.join(data.read())

        alphabet = list(string.ascii_lowercase)
        map = {}

        for i in range(len(alphabet)):
            if(i == 25): #Z
                map[alphabet[i]] = 'b'
            elif(i == 24): #Y
                map[alphabet[i]] = 'a'
            else:
                map[alphabet[i]] = alphabet[i + 2]
        
        print('Created Map.\n')
        
        trans = clue.maketrans(map)
        newClue = clue.translate(trans)

        print(f'Translated Clue: {newClue}\n')

        transURL = startingURL.translate(trans)

        print(f'Translated URL: {transURL}\n')
        #I think I only need to change the portion of the URL after 'def', because otherwise this is total nonsense.
    next = 'ocr'
    nextURL = f'http://www.pythonchallenge.com/pc/def/{next}.html\n'
    print(f'Next challenge URL: {nextURL}')
    



def main():
    print("--------------------------------------------------------------------------------\n"
    "                               PYTHON CHALLENGE\n"
    "--------------------------------------------------------------------------------\n"
    )

    challenge(1)
    

if __name__ == "__main__":
    main()