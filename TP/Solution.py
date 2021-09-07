class TextProcessing:
    def __init__(self, text):
        self.text = text

    def word_occurences(self, word):
        count = 0
        text = self.text.replace("...", " ")\
                        .replace(".", "")\
                        .replace(",", "")\
                        .replace(":", "")\
                        .replace(";", "")\
                        .replace("- ", "")\
                        .replace("\n", " ")\
                        .replace("\"", "")
        for e in text.split(" "):
            if e.lower() == word.lower():
                count += 1
        return count
    
    def paragraphs(self):
        return len(self.text.split(".")) - 1
    
    def lines(self):
        return len(self.text.split("\n")) - 1

    def words(self):
        text = self.text.replace("...", " ")\
                        .replace(".", "")\
                        .replace(",", "")\
                        .replace(":", "")\
                        .replace(";", "")\
                        .replace("- ", "")\
                        .replace("\n", " ")\
                        .replace("\"", "")
        return len(text.split(" "))
    
    def uniques(self):
        text = self.text.replace("...", " ")\
                        .replace(".", "")\
                        .replace(",", "")\
                        .replace(":", "")\
                        .replace(";", "")\
                        .replace("- ", "")\
                        .replace("\n", " ")\
                        .replace("\"", "")
        return set(text.split(" "))

    def intersection(self, other):
        uniques_1 = self.uniques()
        uniques_2 = other.uniques()
        return list(uniques_1.intersection(uniques_2))
                        

file_1 = open("obama_speech.txt", "r")
text_1 = file_1.read()

obama = TextProcessing(text_1)

print(obama.paragraphs())
print(obama.lines())
print(obama.word_occurences("america"))
print(obama.words())
# print(obama.uniques())
print(len(obama.uniques()))

result_text = "Resultats :\nNombre de paragraphes : " + str(obama.paragraphs()) + "\nNombre de lignes : " + str(obama.lines()) + "\nNombre de mots : " + str(obama.words())

results = open("results.txt", "w")
results.write(result_text)
results.close()

file_2 = open("donald_speech.txt", "r")
text_2 = file_2.read()

donald = TextProcessing(text_2)

print(len(donald.uniques()))
print(len(obama.intersection(donald)))


inter = obama.intersection(donald)
for term in inter[5:10]:
    print("Obama used : ", term, " ", obama.word_occurences(term), " times.")
    print("Obama used : ", term, " ", donald.word_occurences(term), " times.")