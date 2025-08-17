def count_the_words(booktext):
    # split the booktext into a list
    words = booktext.split()
    # count the list and return that.
    return len(words)

def count_letter_usage(booktext):
    # convert to lower case
    booktext = booktext.lower()
    
    letter_counts = {}
    # use a dictionary of string -> integer. If the letter has been
    # counted, add one. If the letter is not in the dictionary, add it.
    for char in booktext:
        if char in letter_counts:
            letter_counts[char] += 1
        else:
            letter_counts[char] = 1

    return letter_counts

def sort_letter_usage(letter_counts):
    # print("convert into a list of tupules")
    letter_counts_list = list(letter_counts.items())
    # print("printing list:")
    # print(letter_counts_list)
    # print("using .sort() to sort a list")
    letter_counts_list.sort(reverse=True, key=lambda x: x[1])
    # print("printing list:")
    # print(letter_counts_list)
    return letter_counts_list


# test_string = "here today gone tomororow, hello friend!"
# print(f"Test String: {test_string}")
# print("Counting letters usage function:")
# test_dict = count_letter_usage(test_string)
# print(test_dict)
# print("Testing sort_letter_usage function:")
# sort_letter_usage(test_dict)