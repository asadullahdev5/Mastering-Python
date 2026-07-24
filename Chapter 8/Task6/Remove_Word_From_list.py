# Remove word from list Function

def remove_word_from_list(word):
    Fruits.remove(word)
    return Fruits

Fruits = ['Apple', 'Banana', 'Mango', 'Grapes', 'Orange']
print("Original List:", Fruits)
word_to_remove = input("Enter the word to remove from the list: ")
Fruits = remove_word_from_list(word_to_remove)
print("List after removing the word:", Fruits)