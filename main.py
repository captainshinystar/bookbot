def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
    print("--- Begin report of books/frankenstein.txt ---")
    print(str(word_count(file_contents)) + " words found in the document")
    print()
    characters = char_count(file_contents)
    char_list = list(characters.items())   
    char_list.sort(key=lambda item: item[1], reverse=True)
    for letter, count in char_list:
        if letter.isalpha():
            print(f"The {letter} character was found {count} times")
    print("--- End Report ---")
def word_count(book):
    words = book.split()
    return len(words)

def char_count(book):
    lowered_book = book.lower()
    characters = {
    }
    for char in lowered_book:
        if char not in characters:
            characters[char] = 1
        else:
            characters[char] += 1
    return characters

main()