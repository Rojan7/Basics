#7)WAP to ask for a sentence and count the number of words.

def calculate_words (sentence):
    word_count =0
   
    print(sentence)
    words = sentence.split()
    for words in enumerate(words):
        word_count +=1
    # for index,char in enumerate(sentence):
    #     if char == " ":
    #         word_count+=1
    print (word_count + 1)


    



    
#list_param = []====
sentence = input("enter a sentence")
#list_param.append(sentence)

calculate_words(sentence)
