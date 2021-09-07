class TextProcessing:
    def __init__(self, text):
        self.text = text

    def word_occurence(self, word):
        count = 0
        # Cleaning text as much as we can
        text = self.text.replace(",", " ")\
                        .replace(":", " ")\
                        .replace(";", " ")\
                        .replace("- ", "")\
                        .replace("...", " ")\
                        .replace(".", "")\
                        .replace("  ", " ")\
                        .replace("  ", " ")\
                        .replace("\n", "")\
                        .replace("\"", "")
        # looping on the list of word (split by space character)
        # for each e in the list of word
        for e in text.split(" "):
            # checking if the word equals our list element
            if e.lower() == word.lower():
                # adding 1 if the words are equal
                count +=1
        return count

    def paragraphs(self):
        text = self.text.replace("...", " ")
        return len(text.split(".")) - 1

    def lines(self):
        return len(self.text.split("\n")) - 1

    def words(self):
        text = self.text.replace(",", " ")\
                        .replace(":", " ")\
                        .replace(";", " ")\
                        .replace("- ", "")\
                        .replace("...", " ")\
                        .replace(".", "")\
                        .replace("  ", " ")\
                        .replace("  ", " ")\
                        .replace("\n", "")\
                        .replace("\"", "")
        return len(text.split(" "))
        
    def uniques(self):
        text = self.text.replace(",", " ")\
                        .replace(":", " ")\
                        .replace(";", " ")\
                        .replace("- ", "")\
                        .replace("...", " ")\
                        .replace(".", "")\
                        .replace("  ", " ")\
                        .replace("  ", " ")\
                        .replace("\n", "")\
                        .replace("\"", "")
        return set(text.split(" "))

    def intersection_(self, other):
        uniques_1 = self.uniques()
        uniques_2 = other.uniques()
        # set_1.intersection(set_2)
        # intersection(list_1, list_2)
        return list(uniques_1.intersection(uniques_2))


file_1 = open("obama_speech.txt", "r")
text_1 = file_1.read()

obama = TextProcessing(text_1)

# print(obama.word_occurence("it"))
# print(obama.paragraphs())
# print(obama.lines())
# print(obama.words())
# print(obama.uniques())

results = open("results.txt", "w")
results.write("Results Obama : \n")
results.write("Occurences de IT : " + str(obama.word_occurence("it")) + "\n")
results.write("Number of Paragraphs : " + str(obama.paragraphs()) + "\n")
results.write("Number of Lines : " + str(obama.lines()) + "\n")
results.write("Number of Words : " + str(obama.words()) + "\n")
results.close()

# 9 - 
file_2 = open("donald_speech.txt", "r")
text_2 = file_2.read()

donald = TextProcessing(text_2)

inter = obama.intersection_(donald)

# 10

for term in inter:
    print("Obama used : ", term, " ", obama.word_occurence(term), " times")
    print("Donal used : ", term, " ", donald.word_occurence(term), " times")
    print("===================")


nouveau = TextProcessing("In the same class : Create a function that counts the number of pharagraphs in the object TextProcessing")