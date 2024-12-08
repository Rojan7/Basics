# #11)WAP to ask for a sentence and calculate the frequency of characters in the sentences.
# sentence = input ("enter a sentence")


# for char in sentence:

#     # print (char + " : " + str(sentence.count(char)))
#     unique_chars = set(sentence)
# for char in unique_chars:
#     print(char + " : " + str(sentence.count(char)))




# Input sentence
sentence = input("Enter a sentence: ")


char_count = {}


for char in sentence:
    if char in char_count:
        char_count[char] += 1  
    else:
        char_count[char] = 1  


print(char_count)
