string = input("enter a word: ")
vowel = []
consonant = []
for letters in string:
    if (letters == 'a' or letters == 'e' or letters == 'i' or letters == 'o' or letters == 'u'):
        vowel.append(letters)
    else:
        consonant.append(letters)

print("total vowel in " + string + " is", len(vowel))
print("total consonant in " + string + " is", len(consonant))