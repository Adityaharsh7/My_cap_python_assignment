def most_frequent(string):
    freq_dict = {}
    for char in string:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1

    sorted_dict = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)
    for item in sorted_dict:
        print(item[0], item[1])
