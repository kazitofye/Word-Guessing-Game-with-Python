import random

word_bank = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'huckleberry', 'kiwi', 'lemon', 'mango', 'nectarine', 'orange', 'papaya', 'quince', 'raspberry', 'strawberry', 'tangerine', 'ugli', 'vanilla', 'watermelon', 'xigua', 'yam', 'zucchini',
'almond', 'brazilnut', 'cashew', 'hazelnut', 'peanut', 'pistachio', 'walnut', 'apricot', 'blueberry', 'cranberry', 'dragonfruit', 'gooseberry', 'jackfruit', 'kumquat', 'lychee', 'mulberry', 'olive', 'pear', 'plum', 'pomelo', 'prune', 'soursop', 'starfruit', 'currant', 'durian', 'elderflower', 'grapefruit', 'honeydew', 'nectarine', 'persimmon', 'rambutan', 'salak', 'tamarind', 'yuzu', 'passionfruit',
'acer', 'birch', 'cedar', 'dogwood', 'elm', 'fir', 'ginkgo', 'hickory', 'larch', 'magnolia', 'oak', 'pine', 'sequoia', 'spruce', 'sycamore', 'willow', 'aspen', 'beech', 'chestnut', 'cypress', 'eucalyptus', 'juniper', 'poplar', 'redwood', 'teak',
'apple', 'banner', 'canvas', 'desk', 'envelope', 'folder', 'guitar', 'helmet', 'igloo', 'jacket', 'kettle', 'lantern', 'mirror', 'notebook', 'umbrella', 'violin', 'wagon', 'xylophone', 'yo-yo', 'zipper',
'alert', 'brave', 'calm', 'diligent', 'eager', 'faithful', 'gentle', 'heroic', 'intelligent', 'joyful', 'keen', 'loyal', 'mighty', 'nimble', 'obedient', 'patient', 'quick', 'radiant', 'strong', 'timid', 'unique', 'vigilant', 'wild', 'xenial', 'youthful', 'zealous',
'art', 'ball', 'cat', 'dog', 'egg', 'flower', 'grass', 'house', 'ice', 'jam', 'kite', 'leaf', 'moon', 'nest', 'ocean', 'paint', 'queen', 'rock', 'sun', 'tree', 'umbrella', 'vine', 'water', 'x-ray', 'yard', 'zebra',
'alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india', 'juliet', 'kilo', 'lima', 'mike', 'november', 'oscar', 'papa', 'quebec', 'romeo', 'sierra', 'tango', 'uniform', 'victor', 'whiskey', 'xray', 'yankee', 'zulu',
'red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet', 'pink', 'brown', 'black', 'white', 'silver', 'gold', 'bronze', 'copper', 'iron', 'steel', 'stone', 'clay', 'sand', 'water', 'wind', 'fire', 'earth']
word = random.choice(word_bank)  

guessedWord = ['_'] * len(word)
attempts = 10


while attempts > 0:
    print('\nCurrent word: ' + ' '.join(guessedWord))
    guess = input('Guess a letter: ').lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessedWord[i] = guess
        print('Great guess!')
    else:
        attempts -= 1
        print(f'Wrong guess! Attempts left: {attempts}')

    if '_' not in guessedWord:
        print('\nCongratulations! You guessed the word: ' + word)
        break

if '_' in guessedWord:
    print('\nYou\'ve run out of attempts! The word was: ' + word)
