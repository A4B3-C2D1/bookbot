def count_words(input_string):
    words = input_string.split()
    return len(words)

def count_char(input_string):
    words = input_string.split()
    count=[]
    for i in range(0,26):
        count.append(0)
    for word in words:
        word=word.lower()
        for i in range(0,len(word)):
            character=word[i]
            if(ord(character)>=97):
                count[(ord(character)-97)]+=1
    return count


def main():
    with open("books/frankenstein.txt") as f:
        file_contents=f.read()
        words=count_words(file_contents)
        count=count_char(file_contents)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{words} words found in the document")
        new_dict={}
        for i in range(0,len(count)):
            print(f"The character '{chr(i+97)}' was found {count[i]} times")
        print("--- End Report ---")
main()    