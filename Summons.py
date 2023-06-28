import random

#List of backgrounds

backgrounds = [
    "Green skies",
    "Space",
    "Heaven",
    "Broken planet",
    "Galaxy",

]

#List of special animations
special_aninmations = [
    "Vegito vs Janeba",
    "5 pods",
    "Dragon balls",
    "bardock fighting",
]

# List of available characters
characters = [
    "Ultra Legendary Super Saiyan Broly",
    "Sparking LF Super Saiyan Gohan (Youth)",
    "Sparking LF Half-Corrupted Fusion Zamasu",
    "Sparking LF Buu:Kid",
    "Sparking LF Super Saiyan Goten (Kid)",
    "Sparking Gohan ",
    "Sparking Vegeta",
    "Sparking Full Power Boujack",
    "Sparking Super Saiyan God SS Vegeta",
    "Sparking Super Saiyan God SS Goku",
    "Sparking Ultimate Gohan Absorbed Buu: Super",
    "Sparking Goku ",
    " Sparking Majin Buu",
    "Extreme Beerus",
    " Extreme Whis",
    "Extreme Android 17",
    "Extreme Android 18",
    "Extreme Jiren",
    " Extreme Toppo",
    "Extreme Hit",
    " Extreme Kale",
    " Extreme Caulifla",

]

# Probability weights for each character (adjust as desired)
character_weights = [
    0.35,  # Character A (20%)
    0.5,  # Character B (30%)
    0.5,  # Character C (15%)
    0.5,  # Character D (10%)
    0.5,  # Character E (25%)
    0.0171,  # sparking
    0.0171,  # sparking
    0.0171,  # sparking
    0.0171,  # sparking
    0.0171,  # sparking
    0.0171,  # sparking
    2.5,  # hero
    2.5,
    2.5,
    2.5,
    2.5,
    2.5,
    0.0171,
    0.0171,
    0.0171,
    0.0171,
    2.5,


]

amount = int(input("how much Chrono crystals do you have, CC "))

def rotation():
    """Simulates a gacha summon."""
    global amount
    if (amount) >= 0:
        print("Summoning...")
        background = random.choices(backgrounds)
        print(background)
        special_aninmation = random.choices(special_aninmations)
        print(special_aninmation)
        character = random.choices(characters, character_weights, k=10)
        print("Congratulations! You obtained:", character)
        (amount) -= int(1000)
        print(amount)
    else:
        print("Not enough Chrono Crystals")






# Main game loop
while True:
    print("Welcome to Gacha Summoning Game!")
    print("1. Summon a character")
    print("2. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        rotation()

    elif choice == "2":
        print("Thanks for playing! Goodbye.")
        break
    else:
        print("Invalid choice. Please try again.\n")
