print("++++++++++++++++++++++ SNAKE WATER GUN THE GAME+++++++++++++++++++++\n\n")


while 1:

    def comp(name):

        print(f"################## WELCOME {name} ################\n\n")
        print(f"{name} VS computer")

        import random

        moveList = ["Snake", "Water", "Gun"]

        cScore = 0
        pScore = 0

        i = 0

        while i < 10:

            cMove = random.choice(moveList)

            print("Choose your move:\n[1] Snake\n[2] Water\n[3] Gun\n[q] Go to menu")
            pMove = input(">>>")

            if (pMove == "1" and cMove == "Snake") or (pMove == "2" and cMove == "Water") or (pMove == "3" and cMove == "Gun"):
                print(f"You Both Chose {cMove}, so:\nIts a Tie")
                continue

            elif (pMove == "1" and cMove == "Water") or (pMove == "2" and cMove == "Gun") or (pMove == "3" and cMove == "Snake"):
                pScore += 1
                i += 1    
                print(f"Computer chose {cMove}, so:\nYou won a point, Now:\n{name} = {pScore} & computer = {cScore}")

            elif (pMove == "1" and cMove == "Gun") or (pMove == "2" and cMove == "Snake") or (pMove == "3" and cMove == "Water"):
                cScore += 1
                i += 1
                print(f"Computer chose {cMove}, so:\nComputer won a point, Now:\n{name} = {pScore} & computer = {cScore}")

            elif pMove == "q":
                return 0

            else: 
                print("Invalid Input")

        import datetime

        now = datetime.datetime.now()

        if cScore > pScore:
            print(f"\n\nComputer's Score => {cScore} and {name}'s Score => {pScore}\n YOU LOST !!! Better Luck Next time\n\n")

            with open("snakeWaterGun.txt", "a") as f:
                f.write(f"\n on => [{now}] {name} LOST")

        elif pScore > cScore:
            print(f"\n\nComputer's Score => {cScore} and {name}'s Score => {pScore}\n YOU WON !!! Congratulations\n\n")

            with open("snakeWaterGun.txt", "a") as f:
                f.write(f"\n on => [{now}] {name} WON")
        
        else:
            print(f"\n\nComputer's Score => {cScore} and {name}'s Score => {pScore}\n THIS MATCH IS TIE !!!\n\n")

            with open("snakeWaterGun.txt", "a") as f:
                f.write(f"\n on => [{now}] {name} and Computer had a Tie")


        with open("snakeWaterGun.txt") as l:
            rd = l.read()
            print("\n\n",rd,"\n\n")
        

    print("Play:\n[1] Start\n[2] Quit Game")
    play = input(">>>")

    if play == "1":
        a = input("Enter Your Name >>>")
        val = comp(a)
        if val == 0:
            continue
    elif play == "2":
        print(f"Thanks for playing:)")
        break
    else: 
        print("Invalid input")
        continue

