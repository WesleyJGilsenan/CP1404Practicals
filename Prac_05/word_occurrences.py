"""
CP1404: Prac 5 Word Occurrences | Wesley Gilsenan

Estimate: 30 minutes
Actual:   50 minutes


"""

user_sentence = input("Please input your string: ")
words_to_count = {}
words = user_sentence.split()
for word in words:
    words_to_count[word] = words_to_count.get(word, 0) + 1
print(words_to_count)

words = list(words_to_count.keys())
words.sort()
print(words)

max_word_length = max((len(word) for word in words))
for word in words:
    print(f"{word:{max_word_length}} : {words_to_count[word]}")



