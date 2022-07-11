def remove_letters(letters_list: list, word: str) -> list:
    letters_remove = []
    for letter in letters_list:
        if (letter in word):
            veces_letter_list = letters_list.count(letter)
            veces_letter_word = word.count(letter)
            total = abs(veces_letter_word - veces_letter_list)
            if (total != 0):
                letters_list.remove(letter)
                letters_remove.append(letter)
        else:
            letters_remove.append(letter)
    
    print("Letter removed", letters_remove)

if __name__ == '__main__':
    letters = input('Enter letters Ex.(a,b,f,w): ')
    letter_user = letters.split(',')
    word_user = input('Enter word: ')
    remove_letters(letter_user, word_user)