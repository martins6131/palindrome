def is_palindrome(word):
    word = ''.join(ch.lower() for ch in word if ch.isalnum())
    return word == word[::-1]

file_name = "words.txt"

with open(file_name, 'r') as file:
    for line in file:
        word = line.strip()
        if is_palindrome(word):
            print(f"{word} is a palindrome.")
        else:
            print(f"{word} is not a palindrome.")
exit()