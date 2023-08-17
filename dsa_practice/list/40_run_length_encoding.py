
"""
***
75. Write a Python program to create a list reflecting the run-length encoding
from a given list of integers or a given list of characters.

Original list: [1, 1, 2, 3, 4, 4.3, 5, 1]

List reflecting the run-length encoding from the said list:
[[2, 1], [1, 2], [1, 3], [1, 4], [1, 4.3], [1, 5], [1, 1]]

Original String: automatically
List reflecting the run-length encoding from the said string:
[[1, 'a'], [1, 'u'], [1, 't'], [1, 'o'], [1, 'm'], [1, 'a'], [1, 't'], [1, 'i'], [1, 'c'], [1, 'a'], [2, 'l'], [1, 'y']]

"""


from itertools import groupby


def encode(message):
    encoded_message = ""
    i = 0

    while (i <= len(message)-1):
        count = 1
        ch = message[i]
        j = i
        while (j < len(message)-1):
            if (message[j] == message[j+1]):
                count = count+1
                j = j+1
            else:
                break
        encoded_message = encoded_message+str(count)+ch
        i = j+1
    return encoded_message


# Provide different values for message and test your program
encoded_message = encode("ABBBBCCCCCCCCAB")
print(encoded_message)


def runLengthEncode(plainText):
    res = []

    for k, i in groupby(plainText):
        run = list(i)
        if(len(run) > 4):
            res.append("/{:02}{}".format(len(run), k))
        else:
            res.extend(run)

    return "".join(res)


Split = (list(input("Enter string: ")))
Split.append("")
a = 0
for i in range(len(Split)):
    try:
        if (Split[i] in Split) > 0:
            a = a + 1
        if Split[i] != Split[i+1]:
            print(Split[i], a)
            a = 0
    except IndexError:
        print()


text = input("Please enter the string to encode")
encoded = []
index = 0
amount = 1
while index <= (len(text)-1):
    if index == (len(text)-1) or text[index] != text[(index+1)]:
        encoded.append([text[index], amount])
        amount = 1
    else:
        amount = amount+1
    index = index+1
print(encoded)


def printRLE(st):
    n = len(st)
    i = 0
    while i < n - 1:
        # Count occurrences of current character
        count = 1
        while (i < n - 1 and
               st[i] == st[i + 1]):
            count += 1
            i += 1
        i += 1

        # Print character and its count
        print(st[i - 1] +
              str(count),
              end="")


# Driver code
if __name__ == "__main__":

    st = "wwwwaaadexxxxxxywww"
    printRLE(st)


"""
76. Write a Python program to create a list reflecting the modified run-length encoding
from a given list of integers or a given list of characters.

Original list: [1, 1, 2, 3, 4, 4, 5, 1]

List reflecting the modified run-length encoding from the said list:
[[2, 1], 2, 3, [2, 4], 5, 1] 

Original String: aabcddddadnss

List reflecting the modified run-length encoding from the said string:
[[2, 'a'], 'b', 'c', [4, 'd'], 'a', 'd', 'n', [2, 's']]
"""


def modified_encode(alist):
    def ctr_ele(el):
        if len(el) > 1:
            return [len(el), el[0]]
        else:
            return el[0]
    return [ctr_ele(list(group)) for key, group in groupby(alist)]


n_list = [1, 1, 2, 3, 4, 4, 5, 1]

print(modified_encode(n_list))
