#importing random module
import random

#introduction of the game to the user
print("Welcome to Hangman!!")
print("\t ___\n\t|. . |\n\t| ‾ |\n\t ‾|‾\n\t /|\\\n\t/ | \\\n\t  |\n\t / \\\n\t/   \\")
print("In this game, you would be given 4 chances to guess a word. Guess the word according to the hints provided.")
print("Let's Start!!")
print("-------------------------------------------------------\n-------------------------------------------------------")

#storing all the words with the hints in a python dictionary
word_store = {
    1:{'word': 'computer',
        'hint1': "It's an electronic device. It can perform various tasks based on instructions.",
        'hint2': 'It consists of hardware and software components.',
        'hint3': "You're likely using one right now to read this message.",
        'hint4': "It was invented by Charles Babbage."
        },
    2:{'word': 'book',
        'hint1': "It contains written or printed pages. It is a common source of knowledge and entertainment.",
        'hint2': 'It typically has a cover and is bound together.',
        'hint3': "People often read it for pleasure or to gain information.",
        'hint4': "It is found in libraries, bookstores, and homes."
        },
    3:{'word': 'sunflower',
        'hint1': "It's yellow-flowered plant. This flower head follows the movement of the sun.",
        'hint2': 'It produces seeds commonly eaten and used in cooking.',
        'hint3': "It is grown for its beauty in gardens and landscapes.",
        'hint4': "Oil extracted from its seeds is used in cooking and skincare."
        },
    4:{'word': 'basketball',
        'hint1': "It's a popular team sport played with a ball and hoops. Players dribble, pass, and shoot to score points.",
        'hint2': 'It is played on a rectangular court with two teams of five players each.',
        'hint3': "It was invented by Dr. James Naismith in 1891.",
        'hint4': "Professional leagues include the NBA in the United States."
        },
    5:{'word': 'chocolate',
        'hint1': "Sweet food made from cocoa beans. Eaten as a snack or used in desserts and confectionery.",
        'hint2': 'Comes in various forms such as bars, candies, and drinks.',
        'hint3': "Originated in Mesoamerica and later brought to Europe.",
        'hint4': "Contains compounds like theobromine and phenylethylamine, which can have mood-enhancing effects.",
        },
    6:{'word': 'moon',
        'hint1': "Earth's natural satellite. Fifth-largest satellite in the Solar System.",
        'hint2': 'Influences phenomena like tides on Earth.',
        'hint3': "Object of fascination and study throughout human history.",
        'hint4': "Has surface features like craters, mountains, and maria (dark plains).",
        },
    7:{'word': 'bicycle',
        'hint1': "Human-powered vehicle with two wheels. Used for transportation, recreation, and exercise.",
        'hint2': 'Operated by pedaling the pedals to turn the wheels.',
        'hint3': "Comes in various types such as road bikes, mountain bikes, and BMX bikes.",
        'hint4': "Invented in the 19th century and has undergone many technological advancements since then.",
        },
    8:{'word': 'library',
        'hint1': "Place where books and other materials are stored and made available for borrowing or reference.",
        'hint2': 'Provides services like reading rooms, computer access, and programs for the community.',
        'hint3': "Organized by subject or category for ease of finding materials.",
        'hint4': "Contains fiction, non-fiction, periodicals, and reference materials.",
        },
    9:{'word': 'butterfly',
        'hint1': "Insect with brightly colored wings. Undergoes metamorphosis, starting as a caterpillar5.",
        'hint2': 'Delicate flight and beautiful patterns on wings.',
        'hint3': "Important for pollination and maintaining ecosystem balance.",
        'hint4': "Found in various habitats worldwide, from forests to gardens.",
        },
    10:{'word': 'television',
        'hint1': "Electronic device used for viewing broadcast programs. Displays images and sound transmitted through radio waves or cables.",
        'hint2': 'Provides entertainment, news, and information to viewers.',
        'hint3': "Found in households, public places, and businesses.",
        'hint4': "Comes in various types such as CRT, LCD, LED, and plasma.",
        }
              }

#game function for the game
def game():
    py_choose_word = random.randint(1,10)
    for i in range(1,5):
        print(f"Hint {i}: {word_store[py_choose_word][f'hint{i}']}")
        guess_word = input("Your Guess:\n").lower()
        if guess_word == word_store[py_choose_word]['word']:
            print("You won!!")
            break
        else:
            if i ==1:
                print("   _________________\n    |              |\n    |              |\n    |\n    |\n    |\n    |\n    |\n    |\n    |\n    |\n    |")
            elif i ==2:
                print("   _________________\n    |              |\n    |              |\n    |            _|__\n    |            |. . |\n    |            | ‾ |\n    |             ‾‾\n    |\n    |\n    |\n    |\n    |")
            elif i ==3:
                print("   _________________\n    |              |\n    |              |\n    |            _|__\n    |            |. . |\n    |            | ‾ |\n    |             ‾|‾\n    |             /|\\\n    |            / | \\\n    |\n    |\n    |")
            elif i ==4:
                print("   _________________\n    |              |\n    |              |\n    |            _|__\n    |            |. . |\n    |            | ‾ |\n    |             ‾|‾\n    |             /|\\\n    |            / | \\\n    |              |\n    |             / \\\n    |            /   \\")        

# starting the game function
game()

#restarting the game according to the feedback of the user
main = True
while main == True:
    restart_game = input("Do you want to restart the game. (y/n)\n")
    if restart_game == 'y':
        game()
    else:
        main = False
        print("Thankyou for playing...")
