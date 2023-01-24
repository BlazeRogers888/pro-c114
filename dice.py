import random

dice = "y"
while dice == "y":
    number =random.randint(1,6)

    if number == 1:
        print("[   ]")
        print("[ * ]")
        print("[   ]")
    if number == 2:

        print("[    ]")
        print("[ ** ]")
        print("[    ]")
    if number == 3:
        print("[  *]")
        print("[ * ]")
        print("[*  ]")
    if number == 4:
        print("[* *]")
        print("[   ]")
        print("[* *]")
    if number == 5:
        print("[* *]")
        print("[ * ]")
        print("[* *]")
    if number  == 6:
        print("[* *]")
        print("[* *]")
        print("[* *]")
    dice = input("press y to roll die")


