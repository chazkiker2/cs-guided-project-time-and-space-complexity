def cs_first_unique_char_1(input_str):
    hit = ""
    unique = {
        "index": -1,
        "character": None
    }
    # unique = (-1, "1")
    for i, letter in enumerate(input_str):
        if letter not in hit:
            # print(letter)
            hit += letter
            # unique = (i, letter)
            unique["index"] = i
            unique["character"] = letter
        elif letter == unique["character"]:
            unique["index"] = -1
            unique["character"] = None

    # if unique[0] >= 0:
    if unique["character"] is not None:
        return unique["index"]
        # return len(input_str) - 1 - unique["index"]

    return -1


def cs_first_unique_char(input_str):
    unique = {}

    for i, letter in enumerate(input_str):
        if unique.get(letter) is not None:
            unique[letter] = -1

        else:
            unique[letter] = i

    first = -1
    for x in unique:
        i = unique[x]
        if first >= 0 and 0 <= i < first:
            first = i

        elif first < 0:
            first = i

    return first if first is not None else -1


print(cs_first_unique_char("ilovelambdaschool"))  # expect 0
print(cs_first_unique_char("vvv"))  # expect -1
