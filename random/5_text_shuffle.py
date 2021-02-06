import random

#sentence = input("Enter a sentence to transform: ")
sentence = ["По результатам исследований одного английского университета, не имеет значения, в каком порядке расположена буквы в слове. Главное, чтобы первая и последняя буквы были на месте. Остальные буквы могут следовать в полном беспорядке, всё-равно текст читается без проблем. Причиной этого  является то, что мы не читаем каждую букву по отдельности, а всё слово целиком."]

input_list_of_words = sentence.split()
output_list_of_words = []

for word in input_list_of_words:
    if len(word) > 3:
        letters = list(word)
        first_letter = letters[0]
        last_letter = letters[-1]
        remaining_letters = letters[1: -1]
        random.shuffle(remaining_letters)
        transformed_letters = []
        transformed_letters.extend(first_letter)
        transformed_letters.extend(remaining_letters)
        transformed_letters.extend(last_letter)

        transformed_word = ''.join(transformed_letters)
        output_list_of_words.append(transformed_word)
    else:
        output_list_of_words.append(word)

print(' '.join(output_list_of_words))