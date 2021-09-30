# Author: ATN 9/30/21

magic_charge = int(input("What is your magic charge? "))
shield_charge = int(input("What is your shield charge? "))

if magic_charge >= 90 and shield_charge >= 75:
    print("You defeated the dragon! But the princess is in another castle.")
else:
    print("The dragon burns you to a crisp.")
