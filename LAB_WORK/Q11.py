#11)WAP to ask for a sentence and calculate the frequency of characters in the sentences.
sentence = input ("enter a sentence")
character = input ("enter the character whose frequency ou want")
count = 0

for index,fragments in enumerate(sentence):
    if sentence[index] == character:
        count = count +1
print(count)

