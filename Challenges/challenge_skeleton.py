"""
challenge_skeleton.py

Skeleton file for Python Challenges
Also serves as the introductory Challenge 0.

Elijah Theander
October 6, 2022


"""


def challenge(num):
    startingURL = "http://www.pythonchallenge.com/pc/def/0.html"
    print(
        "--------------------------------------------------------------------------------\n"
        f"Challenge # {num}: 2 to the power of 38.\n"
        f"Starting url: {startingURL}\n"
        "--------------------------------------------------------------------------------\n"
    )

    power2 = 2**38
    print(f"2**38: {power2}")

    nextURL = f"http://www.pythonchallenge.com/pc/def/{power2}.html\n"
    print(f"Next challenge URL: {nextURL}")


def main():
    print(
        "--------------------------------------------------------------------------------\n"
        "                               PYTHON CHALLENGE\n"
        "--------------------------------------------------------------------------------\n"
    )

    challenge(0)


if __name__ == "__main__":
    main()
