# nested loop to print characters in a list of words
word_list = ['cat', 'dog', 'rabbit']
letter_list = []
for a_word in word_list:
    for a_letter in a_word:
        if a_letter not in letter_list:
            letter_list.append(a_letter)
print("For Loops: ")
print(letter_list)

# equivilent using list comprehensions
print("List comprehension: ")
print(list(set([word[i] for word in ['cat', 'dag', 'rabbit']
                for i in range(len(word))])))
