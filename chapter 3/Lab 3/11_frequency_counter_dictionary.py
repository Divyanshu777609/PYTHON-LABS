text = input("Enter a sentence: ")

frequency = {}

for character in text:
    if character != " ":
        frequency[character] = frequency.get(character, 0) + 1

print("Character frequencies:")

for character, count in frequency.items():
    print(character, ":", count)