"""Restaurant rating lister."""

# put your code here

# create dictionary
rating_dict = {}

# read file lines into new variable
with open('scores.txt') as f:
    lines = f.readlines()

# loop through lines and add to dictionary
for line in lines:
    key, value = line[:-1].split(':')
    rating_dict[key] = value

# print out ratings in alphabetical order


def print_ratings():
    print("\nHere's the ratings:")
    for key, value in sorted(rating_dict.items()):
        print(f'{key} is rated at {value}.')

# add a restauraunt and rating to the dictionary


def add_rating():
    print("\n\nAdd a new restaurant rating:")
    new_rest = input("What restauraunt are you rating?\n")
    new_rating = input("What do you rate this restaurant?\n")
    rating_dict[new_rest] = new_rating
    print_ratings()


# run functions
print_ratings()
add_rating()
