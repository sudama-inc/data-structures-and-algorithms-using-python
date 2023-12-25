"""
40. Write a Python program to reverse words in a string.


"""


def reverse_words(st):
    lst = st.split()
    res = " ".join([lst[i] for i in range(len(lst)-1,-1,-1)])
    return res


# Method 1
def reverse_string_words(text):
    for line in text.split('\n'):
        return(' '.join(line.split()[::-1]))


print(reverse_string_words("The quick brown fox jumps over the lazy dog ."))


# Method 2
string = "geeks quiz practice code"
s = string.split()[::-1]
print(' '.join(s))


# Method 3
import re
def rev_sentence(sentence):
    words = re.findall('\w+', sentence)
    reverse_sentence = ' '.join(words[i] for i in range(len(words)-1, -1, -1))
    return reverse_sentence


if __name__ == "__main__":
    input = 'geeks quiz practice code'
    print(rev_sentence(input))