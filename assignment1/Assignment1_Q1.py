sentence = input("Enter the sentence : ")
num_chars = len(sentence)
print("Number of Character : ",num_chars)

word = sentence.split()
num_word = len(word)
print("Number of words :", num_word)

vowels ="aeiouAEIOU"
num_vowels = 0
for ch in sentence:
    if ch in vowels:
        num_vowels += 1
print("Number of Vowels :", num_vowels)        

