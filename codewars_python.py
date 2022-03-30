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


# 24
# Split Strings
def solution(s):
    new_str = s if len(s) % 2 == 0 else s + '_'
    splitted_letters = []
    
    for i in range(0, len(new_str), 2):
        splitted_letters.append(new_str[i] + new_str[i + 1])
        
    return splitted_letters


# 25
# Highest Scoring Word
from string import ascii_lowercase

def high(x):
    c = [sum([ascii_lowercase.index(char) + 1 for char in word]) for word in x.split()]
    return x.split()[c.index(max(c))]



# 26
# Take a Ten Minute Walk
def is_valid_walk(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')



# 27
# Unique In Order
def unique_in_order(iterable):
    words = []
    unique = []

    for char in iterable:
        words.append(char) if bool(unique) and char == unique[-1] else unique.append(char)

    return unique



# 28
# Bit Counting
def count_bits(n):
    return str(bin(n)[2:]).count('1')


# 29
# max diff - easy
def max_diff(lst):
    return max(lst) - min(lst) if len(lst) > 1 else 0


# 30
# Character Counter
def validate_word(word):
    return len(list(set([word.lower().count(char) for char in word.lower()]))) == 1


# 31
# Spacify
def spacify(string):
    return ' '.join([char for char in string])


# 32
# Merge two sorted arrays into one
def merge_arrays(arr1, arr2):
    return sorted(list(set(arr1 + arr2)))


# 33
# Case swapping
def swap(string_):
    return string_.swapcase()


# 34
# Password Hashes
import hashlib

def pass_hash(str):
    return hashlib.md5(str.encode()).hexdigest()


# 35
# Exes and Ohs
def xo(s):
    return s.lower().count('o') == s.lower().count('x')


# 36
# Get the square of a number without ** or * or pow()
def square(n):return sum([n for i in range(0,n)])


# 37
# Shortest Word
def find_short(s):
    words = s.split()
    word_lengths = {word: len(word) for word in words}
    return min(list(word_lengths.values()))


# 38
# Isograms
def is_isogram(string):
    return len(set(string.lower())) == len(string)


# 39
# Descending Order
def descending_order(num):
    sorted_nums = sorted([int(num) for num in str(num)])
    sorted_nums.reverse()
    return int(''.join([str(num) for num in sorted_nums]))


# 40
# Highest and Lowest
def high_and_low(numbers):
    nums = [int(num) for num in numbers.split()]
    return f'{str(max(nums))} {str(min(nums))}'


# 41
# Square Every Digit
def square_digits(num):
    nums = [num for num in str(num)]
    squared = [int(num) ** 2 for num in nums]
    return int(''.join([str(num) for num in squared]))


# 42
# Vowel Count
def get_count(sentence):
    return len([char for char in sentence if char in 'aeiou'])


# 43
# Replace With Alphabet Position
from string import ascii_lowercase

def alphabet_position(text):
    words = text.lower().split()
    indexes = [ascii_lowercase.index(char) + 1 for word in words for char in word if char in ascii_lowercase]
    return ' '.join([str(num) for num in indexes])



# 44
# Stop gninnipS My sdroW!
def spin_words(sentence):
    return ' '.join([word[::-1] if len(word) >= 5 else word for word in sentence.split()])


# 45
# Find the odd int
def find_it(seq):
    return sum([key for key, value in {num: seq.count(num) for num in seq}.items() if value % 2 != 0])


# 46
# Multiples of 3 or 5
def solution(number):
    return 0 if number < 0 else sum([num for num in range(1, number) if num % 3 == 0 or num % 5 == 0])

