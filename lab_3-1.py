# Author: ATN 9/29/21

points_scored = int(input("How many points are scored for the team? "))

if (points_scored <= 8):
    print("You did not earn a medal.")
else:
    if (points_scored <= 11):
        print("You earned a bronze medal.")
    else:
        if (points_scored <= 14):
            print("You earned a silver medal.")
        else:
            if (points_scored > 14):
                print("You earned a gold medal.")
