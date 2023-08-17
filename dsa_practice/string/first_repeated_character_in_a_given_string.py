"""
***
53. Write a Python program to find the first repeated character in a given string.
54. Write a Python program to find the first repeated character in a given string
where the index of the first occurrence is smallest. 


55. Write a Python program to find the first repeated word in a given string.
56. Write a Python program to find the second most repeated word in a given string.

Write a Python program to find the ALL repeated character in a given string.
Write a Python program to find the ALL repeated WORD in a given string.

https://www.geeksforgeeks.org/find-the-first-repeated-character-in-a-string/
https://stackoverflow.com/questions/50976511/code-to-output-the-first-repeated-character-in-given-string

***
https://www.geeksforgeeks.org/find-first-repeated-word-string-python-using-dictionary/
https://www.geeksforgeeks.org/find-first-repeated-word-string/
"""


# Method 1
st = 'geeks'

for i in range(0, len(st)-1):
    if st[i] == st[i+1]:
        print(st[i])
        break


# Method 2
st = 'geeks'
found_dict = {}
for i in st:
    if i in found_dict:
        print(i)
        break
    else:
        found_dict[i] = 1


# Method 3
def firstRepeatedChar(str):
    h = {}  # Create empty hash
    # Traverse each characters in string in lower case order
    for ch in str:
        # If character is already present in hash, return char
        if ch in h:
            return ch
        else:
            h[ch] = 0
    return ''


# Driver code
print(firstRepeatedChar("geeksforgeeks"))


# Method 4
def findChar(inputString):
    list = []
    for c in inputString:
        if c in list:
            return c
        else:
            list.append(c)
    return 'None'


print(findChar('gotgogle'))


# Method 1
# Python program to find first repeated word in a string
def solve(s):

    mp = {}  # to store occurrences of word
    t = ""
    ans = ""

    # traversing from back makes sure that we get the word which repeats first as ans
    for i in range(len(s) - 1, -1, -1):
        # if char present , then add that in temp word string t
        if (s[i] != ' '):
            t += s[i]
        # if space is there then this word t needs to stored in map
        else:
            # if that string t has occurred previously then it is a possible ans
            if (t in mp):
                ans = t
            else:
                mp[t] = 1

            # set t as empty for again new word
            t = ""

    # first word like "he" needs to be mapped
    if (t in mp):
        ans = t
    if (ans != ""):
        # reverse ans string as it has characters in reverse order
        ans = ans[::-1]
        print(ans)
    else:
        print("No Repetition")


# driver code
u = "Ravi had been saying that he had been there"
solve(u)


# Method 2
def find_first_repeated_word(input_string):
    word_freq = {}
    words = input_string.split()
    for word in words:
        if word not in word_freq:
            word_freq[word] = 1
        else:
            word_freq[word] += 1

        if word_freq[word] > 1:
            return word
    return "No Repetition"


input_string = 'Ravi had been saying that he had been there'
print(find_first_repeated_word(input_string))
