def num_of_words(b):
    contents = b.split()
    num_words = len(contents)
    print(f"Found {num_words} total words")
    return num_words

def character_count(c):
    char_counts = {}
    for char in c:
        char_lower = char.lower()
        if char_lower.isalpha():    
            char_counts[char_lower] = char_counts.get(char_lower,0) + 1
    return char_counts



def sort_dictionary(s):
    counts = []
    for key, value in s.items():
        counts.append({"char": key, "num": value})
    counts.sort(reverse = True, key = sort_on)
    return counts
    
def sort_on(item):
    return item["num"]


    

    