# Вывести последнюю букву в слове
word = 'Архангельск'
letters = []
for letter in word:
    letters += letter
print(letters[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
word = word.lower()
letters = []
for letter in word:
    letters += letter
collect = letters.count('а')
print(collect)

# Вывести количество гласных букв в слове
word = 'Архангельск'

collect = 0
word = word.lower()
vowels = ['а', 'о', 'у', 'э', 'ы', 'и', 'я', 'е', 'ё', 'ю']

for letter in word:
    if letter in vowels:
        collect += 1
 
print(collect)

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'

word = sentence.split()
for letters in word:
    print(letters[0])

# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'

collect = 0
word = sentence.split()

for letters in word:
    collect += len(letters)
print(collect/len(word))