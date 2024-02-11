# lists
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# combining both lists to a dictionary
letter_to_point = {letter: point for letter, point in zip(letters, points)}

# adding whitespace to dictionary
letter_to_point[" "] = 0

# function for getting total points
def score_word(word):
    point_total = 0
    for letter in word:
        point_total += letter_to_point.get(letter, 0)
    return point_total


# variable saving the points for the score word "BROWNIE"
brownie_points = score_word("BROWNIE")

print(brownie_points)

# creating dictionary that maps players to a list of the words they have played
player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}

player_to_points = {}

for player, words in player_to_words.items():
    player_points = 0
    for word in words:
        player_points += score_word(word)
    player_to_points[player] = player_points

print(player_to_points)
