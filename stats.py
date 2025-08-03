def get_num_words(file_contents):
    words = file_contents.split()
    num = len(words)
    return num

def char_count(file_contents):
    low_cont = file_contents.lower()
    char_dict = {}
    for char in low_cont:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_dict(char_dict):
    char_list = []
    for key, value in char_dict.items():
        if key.isalpha():
            char_list.append({"char": key, "num": value})
    char_list.sort(reverse=True, key=lambda x: x["num"])
    return char_list