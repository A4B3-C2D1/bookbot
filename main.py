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
        for charac in range(0,len(count)):
            if(chr(charac+97) in new_dict):
                new_dict[chr(charac+97)]+=count[charac]
            else:
                new_dict[chr(charac+97)]=count[charac]
        newer_dict=dict(sorted(new_dict.items(),reverse=True,key=lambda item:item[1]))
        for key, value in newer_dict.items():
            print(f"The character '{key}' was found {value} times")
        print("--- End Report ---")
main()    