"""
ch04.py

Challenge 4: Grabbing information from webpages. And traversing links

Elijah Theander
October 7, 2022


"""
from urllib.request import urlopen
import re


def traverse(start_link, substring):
    """Traverses webpages for linkedlist python challenge."""

    print("Traversing Links, this will take a while...")
    data = urlopen(start_link).read().decode("utf-8")
    result = substring.search(data)
    next_number = result.group(1)
    next_link = (
        f"http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={next_number}"
    )

    while True:
        data = urlopen(next_link).read().decode("utf-8")
        result = substring.search(data)
        output = [data, next, next_link]

        if result is None:
            print("Link traversal finished!\n")
            return output

        next_number = result.group(1)
        next_link = f"http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={next_number}"


def challenge(num):
    """Implementation of challenge 4."""

    starting_url = "http://www.pythonchallenge.com/pc/def/linkedlist.php"
    print(
        "--------------------------------------------------------------------------------\n"
        f"Challenge # {num}: 4 Grab information from webpages.\n"
        f"Starting url: {starting_url}\n"
        "--------------------------------------------------------------------------------\n"
    )

    first_link = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345"
    substring = re.compile("and the next nothing is (\d+)")

    result = traverse(first_link, substring)

    print(f"Output from first traversal:\n{result[0]}\n{result[1]}\n{result[2]}\n")

    # so, we have to divide by two and run again.

    next_number = int(int(result[1]) / 2)
    next_link = (
        f"http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={next_number}"
    )

    print(f"The next starting link for traversal:\n{next_link}\n")

    result = traverse(next_link, substring)

    print(f"Results of second traversal:\n{result[0]}\n{result[1]}\n{result[2]}\n")

    next_path = result[0]
    next_url = f"http://www.pythonchallenge.com/pc/def/{next_path}\n"
    print(f"Next challenge URL: {next_url}")


def main():
    """Main Function"""
    print(
        "--------------------------------------------------------------------------------\n"
        "                               PYTHON CHALLENGE\n"
        "--------------------------------------------------------------------------------\n"
    )

    challenge(4)


if __name__ == "__main__":
    main()
