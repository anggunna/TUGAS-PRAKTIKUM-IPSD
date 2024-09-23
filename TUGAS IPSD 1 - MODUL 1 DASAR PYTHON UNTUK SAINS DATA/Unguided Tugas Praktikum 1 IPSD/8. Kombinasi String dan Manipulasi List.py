def reverse_words(sentence):
    words = sentence.split()
    reversed_words = [word[::-1] for word in words]
    return reversed_words

# Contoh penggunaan
input_sentence = "Kata Kata Hari Ini Paham?!"
output_list = reverse_words(input_sentence)
print(output_list)