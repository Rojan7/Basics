#11)WAP to ask for a sentence and calculate the frequency of characters in the sentences.
sentence = input ("enter a sentence")
character = input ("enter the character whose frequency ou want")
count = 0

for index,hgjh in enumerate(sentence):
    print(hgjh)
    print(index)
    if sentence[index] == character:
        count = count +1
print(count)

