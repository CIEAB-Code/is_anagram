first = input("Enter a word or phrase: ")
second = input("Enter another word or phrase: ")

init_first, init_second = first, second

first, second = first.strip(), second.strip()
first, second = first.replace(' ', ''), second.replace(' ', '')
first, second = first.lower(), second.lower()

isAnagram = True

for char in first:
    if char in second:
        continue
    else:
        isAnagram = False

if isAnagram:
    message = "Is an ANAGRAM:"
else:
    message = "Is NOT an anagram:"

print(message, init_first, "--", init_second)
