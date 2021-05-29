# Golf Game

# Welcome to Golf Game!

# This function plays a hole of golf. The length of the hole is randomly selected. The user
# is then provided a club based on the distance left to the hole. The user can decide to hit the
# ball softly, medium, or hard, to try and get it closer to the hole.

import random

def main():
    # WELCOME
    print("Welcome to python golf. A hole will be randomly selected and you must choose how to shoot the club provided until the ball is in the hole.")
    print("")

    # SET UP HOLE - shots, distance covered, length of hole, distance left, par
    shot_number = 0
    distance_covered = 0
    hole_length = get_hole()
    par = set_par(hole_length)
    distance_left = hole_length - distance_covered
    print("The Hole is a par", par, "and is", hole_length, "yards long.")

    # PLAY GOLF
    # This function runs the input functions until the distance left gets to 0, ie the
    # ball has reached the hole
    while distance_left > 0:
        # GET SHOT
        print("Shots so far:", shot_number)
        print("")
        get_shot = determine_club(distance_left)
        print("You shot:", get_shot, "yards!")
        distance_covered += get_shot

        # if the user shoots beyond the hole length (ie over shoots), then this function
        # turns the distance left into the remaining distance from the hole
        if distance_covered > hole_length:
            distance_left = ((hole_length - distance_covered) * - 1)

            # Resets the function of playing golf until the user gets the ball in the hole
            while distance_left > 0:
                print("")
                # This function terminates the game. Once they reach within 1-3 yards, they put out, or
                # else they continue playing
                if distance_left > 0 and distance_left <= 3:
                    put_out(distance_left)
                    shot_number += 1
                    distance_left = 0
                else:
                    get_shot = determine_club(distance_left)
                    print("You shot:", get_shot, "yards!")
                    distance_left -= get_shot
                    shot_number += 1

        else:
            distance_left = hole_length - distance_covered

        shot_number += 1

    print("")
    print("You finished the hole with", shot_number, "shots!")

    # FINAL Score
    if shot_number == 1:
        print("Wow! You got a hole in one!")

    final_score(shot_number, par)

def final_score(shots, par):
    # This function calculates final score relative to par
    total = shots - par
    if total == 0:
        return print("You shot par!")
    elif total > 0:
        return print("You shot", final_score, "over par")
    elif total == -1:
        return print("Congrats! You shot a birdie!")
    elif total == -2:
        return print("Congrats! You shot an eagle!")

def put_out(distance):
    # This function terminates the game by making the shot distance equal to the distance left
    shoot_putter(distance)
    return print("You putted out!")

def determine_club(distance):
    # This function decides which club will be used dependent on the distance left on the hole.
    if distance > 239:
        shot_length = shoot_driver(distance)
        return shot_length
    if distance > 189 and distance < 241:
        shot_length = shoot_three(distance)
        return shot_length
    if distance > 129 and distance < 191:
        shot_length = shoot_five(distance)
        return shot_length
    if distance > 69 and distance < 126:
        shot_length = shoot_seven(distance)
        return shot_length
    if distance > 11 and distance < 71:
        shot_length = shoot_wedge(distance)
        return shot_length
    if distance > 0 and distance < 11:
        shot_length = shoot_putter(distance)
        return shot_length

def shoot_driver(distance):
    # This function picks the driver and gets user input in how hard they'd like to shoot. Each
    # intensity of shot corresponds to a range of yards.
    print("You are", distance, "yards from the pin. Your club choice is Driver. Range: 240-295 yards.")
    power = input("How hard would you like to shoot? Enter: Soft, Medium, or Hard: ")
    if power == 'Soft':
        return random.randint(240, 255)
    if power == 'Medium':
        return random.randint(255, 270)
    if power == 'Hard':
        return random.randint(270, 295)

def shoot_three(distance):
    print("You are", distance, "yards from the pin. Your club choice is 3 Wood. Range: 190 - 240 yards.")
    power = input("How hard would you like to shoot? Enter: Soft, Medium, or Hard: ")
    if power == 'Soft':
        return random.randint(190, 205)
    if power == 'Medium':
        return random.randint(205, 225)
    if power == 'Hard':
        return random.randint(225, 240)

def shoot_five(distance):
    print("You are", distance, "yards from the pin. Your club choice is 5 Iron. Range: 130 - 190 yards.")
    power = input("How hard would you like to shoot? Enter: Soft, Medium, or Hard: ")
    if power == 'Soft':
        return random.randint(130, 145)
    if power == 'Medium':
        return random.randint(145, 165)
    if power == 'Hard':
        return random.randint(165, 190)

def shoot_seven(distance):
    print("You are", distance, "yards from the pin. Your club choice is 7 Iron. Range: 70 - 125 yards.")
    power = input("How hard would you like to shoot? Enter: Soft, Medium, or Hard: ")
    if power == 'Soft':
        return random.randint(70, 90)
    if power == 'Medium':
        return random.randint(90, 110)
    if power == 'Hard':
        return random.randint(100, 125)

def shoot_wedge(distance):
    print("You are", distance, "yards from the pin. Your club choice is Pitching Wedge. Range: 12 - 70 yards.")
    power = input("How hard would you like to shoot? Enter: Soft, Medium, or Hard: ")
    if power == 'Soft':
        return random.randint(12, 20)
    if power == 'Medium':
        return random.randint(20, 45)
    if power == 'Hard':
        return random.randint(45, 70)

def shoot_putter(distance):
    print("You are", distance, "yards from the pin. Your club choice is Putter. Range: 1 - 10 yards. ")
    power = input("How hard would you like to shoot? Enter: Soft, Medium, or Hard: ")
    if power == 'Soft':
        return random.randint(1, 3)
    if power == 'Medium':
        return random.randint(4, 7)
    if power == 'Hard':
        return random.randint(8, 10)



def get_hole():
    # Determines hole length
    length = random.randint(120, 420)
    return length


def set_par(length):
    # Sets the par of the hole depending on length
    if length > 119 and length < 180:
        par = 3
    elif length > 179 and length < 320:
        par = 4
    elif length > 319 and length < 420:
        par = 5
    return par


if __name__ == '__main__':
    main()
