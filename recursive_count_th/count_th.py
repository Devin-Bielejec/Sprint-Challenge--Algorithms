'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

def count_th(word):
    count = 0

    def helper(word):
        nonlocal count
        if word is "":
            return count
        elif word[-2:] == "th":
            count += 1
        return helper(word[:-1])

    return helper(word)

print(count_th("abcthxyzth"))
