# 1
# Credit Card Mask
def maskify(cc):
    length = len(cc) - 4
    last_four = cc[-4:]
    masked = length * '#'

    return f'{masked}{last_four}'


# 2
# Replace With Alphabet Position
from string import ascii_lowercase
def alphabet_position(text):
    fixed_str = ''
    text = text.lower()
    for word in text:
        for char in word:
            if char in ascii_lowercase:
                fixed_str += str(ascii_lowercase.index(char) + 1) + ' '

    return fixed_str.strip()


# 3
# Is this a triangle?
def is_triangle(a, b, c):
    if a > 0 and b > 0 and c > 0:
        a_check = a + b >= c or a + c >= b
        b_check = b + a >= c or b + c >= a
        c_check = c + a >= b or c + b >= a
        return any(a_check, b_check, c_check)
    else:
        return False

# 4
# Is this a triangle?
def is_triangle(a, b, c):
    if a > 0 and b > 0 and c > 0:
        nums = [a, b, c]
        nums.sort()
        return nums[0] + nums[1] > nums[2]
    else:
        return False

# 5
# Mumbling
def accum(s):
    new_s = ''
    s = s.lower()

    for index, item in enumerate(s, 1):
        new_s += item.capitalize()
        for i in range(index - 1):
            new_s += item
        new_s += '-'

    return new_s.strip('-')


# 6
# Disemvowel Trolls
def disemvowel(string_):
    return ''.join(['' if char.lower() in 'aeiou' else char for char in string_])


# 7
# Jaden Casing Strings
def to_jaden_case(string):
    words = string.lower().split()
    return ' '.join([word.capitalize() for word in words])


# 8
# Detect Pangram
from string import ascii_lowercase

def is_pangram(s):
    return all([letter in s for letter in ascii_lowercase])


# 9
# Stop gninnipS My sdroW!
def spin_words(sentence):
    return ''.join([word + ' ' if len(word) < 5 else word[::-1] + ' ' for word in sentence.split()]).strip()



# 10
# Which are in?
def in_array(array1, array2):
    substrings = list(set([el for el in array1 for el2 in array2 if el in el2]))
    substrings.sort()
    return substrings


# 11
# Array.diff
def array_diff(a, b):
    return [el for el in a if el not in b]


# 12
# Create Phone Number
def create_phone_number(n):
	return f'({n[0]}{n[1]}{n[2]}) {n[3]}{n[4]}{n[5]}-{n[6]}{n[7]}{n[8]}{n[9]}'


# 13
# Does my number look big in this?
def narcissistic(value):
	return sum([pow(int(num), len(str(value))) for num in str(value)]) == value


# 14
# Count characters in your string
def count(string):
    if string:
    	return {char: string.count(char) for char in string}
    return {}


# 15
# Highest Scoring Word
from string import ascii_lowercase

def high(x):
	c = [sum([ascii_lowercase.index(char) + 1 for char in word]) for word in x.split()]
	return x.split()[c.index(max(c))]


# 16
# Where my anagrams at?
def anagrams(word, words):
	return [w for w in words if ''.join(sorted(w)) == ''.join(sorted(word))]


# 17
# Find The Parity Outlier
def find_outlier(integers):
    odds = [num for num in integers if num % 2 != 0]
    if len(odds) > 1:
        even = [i for i in integers if i % 2 == 0]
        return even[0]
    else:
        return odds[0]


# 18
# Your order, please
def order(sentence):
  words = sentence.split()
  seperated = {char: word for word in words for char in word if char.isnumeric()}

  word_positions = list(seperated.keys())
  word_positions.sort()

  fixed_words = ' '.join([seperated[position] for position in word_positions])

  return fixed_words


# 19
# Counting Duplicates
def duplicate_count(text):
    letters = {}

    for letter in text.lower():
        if letters.get(letter) is not None:
            letters[letter] += 1
        else:
            letters[letter] = 1


    duplicates = [key for key, value in letters.items() if letters[key] > 1]

    return len(duplicates)



# 20
# Two to One
def longest(a1, a2):
    strings = list(set(a1 + a2))
    strings.sort()

    return ''.join(strings)



# 21
# Get the Middle Character
def get_middle(s):
    word_length = len(s)

    if word_length % 2 == 0:
        middle = word_length // 2
        return s[middle -1 ] + s[middle]
    else:
        middle = word_length // 2
        return s[middle]


# 22
# Array.diff
def array_diff(a, b):
    return [item for item in a if item not in b]



# 23
# Is a number prime?
from math import sqrt

def is_prime(num):
    if num <= 1:
        return False
    
    i = 2
    
    while i <= sqrt(num):    
        if num % i == 0:
            return False
        i += 1
        
    return True 
