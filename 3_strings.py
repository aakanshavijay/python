name = "Python"
message = 'Hello, world!'
paragraph = """This is
a multiline string."""

#strings are immutable.
# Operations such as replacing characters produce new strings rather than modifying the original string in place.

#indexing
#Positive indices start at zero; negative indices count backward from the end.

word = "Python"

print(word[0])    # P
print(word[-1])   # n
print(word[0:3])  # Pyt
print(word[2:])   # thon
print(word[::-1]) # nohtyP

#slicing uses the general form
#sequence[start:stop:step]
#stop position is optional, if not provided, it will go to the end of the string.

#methods
#Python provides a rich set of built-in methods for string manipulation.

#change case
print(name.upper())  # PYTHON
print(name.lower())  # python
print(name.capitalize())  # Python
print(name.title())  # Python

#search
# .find() returns the index of the first occurrence of a substring, or -1 if not found.
# .count() returns the number of occurrences of a substring.
text = "Python is a powerful programming language. Python is also easy to learn."
print(text.find("Python"))  # 0
print(text.count("Python"))  # 2

#check content
# .startswith(), .endswith(), .isdigit(), .isalpha(), .isalnum()
text = "Hello, World!"
print(text.startswith("Hello"))  # True
print(text.endswith("World!"))  # True
print("123".isdigit())  # True
print("abc".isalpha())  # True
print("abc123".isalnum())  # True

#whitespace removal
text = "   Hello, World!   "
print(text.strip())  # "Hello, World!"

#replacement
greeting = "Hello, World!"
new_greeting = greeting.replace("World", "Python")
print(new_greeting)  # "Hello, Python!"

#splitting and joining
sentence = "Python is a powerful programming language."
words = sentence.split()  # Splits the sentence into a list of words
print(words)  # ['Python', 'is', 'a', 'powerful', 'programming', 'language.']
joined_sentence = " ".join(words)  # Joins the list of words back into a single string
print(joined_sentence)  # "Python is a powerful programming language."

#string formatting
name = "Rahul"
score = 87.456

print(f"{name} scored {score:.2f} marks.")

#less readable formatting
print("{} scored {:.2f} marks.".format(name, score))
print(name + " scored " + str(score) + " marks.")

#text processing example
text = "The quick brown fox jumps over the lazy dog."
print(text.upper())  # "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG."
print(text.lower())  # "the quick brown fox jumps over the lazy dog."
print(text.title())  # "The Quick Brown Fox Jumps Over The Lazy Dog."
print(text.capitalize())  # "The quick brown fox jumps over the lazy dog."

text = input("Enter a sentence: ")

text = text.strip()
words = text.split()

print("Cleaned text:", " ".join(words))
print("Word count:", len(words))
print("Character count:", len(text))

#also include 
# number of words, characters, excluding surrounding whitespace.
# number of occurences of a specific word or character.
# reversed string

