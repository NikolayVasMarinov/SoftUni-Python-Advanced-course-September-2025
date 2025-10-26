numbers_dictionary = {}

line = input()

while line != "Search":
    number_as_string = line
    number = input()

    if not number.isdigit():
        print("The variable number must be an integer")
        continue

    numbers_dictionary[number_as_string] = int(number)

    line = input()

line = input()

while line != "Remove":
    searched = line

    if not numbers_dictionary.get(searched):
        print("Number does not exist in dictionary")
        line = input()
        continue

    print(numbers_dictionary[searched])

    line = input()

line = input()

while line != "End":
    searched = line

    if not numbers_dictionary.get(searched):
        print("Number does not exist in dictionary")
        line = input()
        continue

    del numbers_dictionary[searched]

    line = input()

print(numbers_dictionary)
