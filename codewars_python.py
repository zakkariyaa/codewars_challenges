# 1
# Credit Card Mask
from math import floor
from math import ceil
from string import digits
from string import digits as d
from string import ascii_uppercase as l, ascii_lowercase as u, digits as d
from string import ascii_lowercase as alphabet
import hashlib
from math import sqrt
from string import ascii_lowercase


def maskify(cc):
    length = len(cc) - 4
    last_four = cc[-4:]
    masked = length * '#'

    return f'{masked}{last_four}'


# 2
# Replace With Alphabet Position


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
def is_pangram(s):
    return all([letter in s for letter in ascii_lowercase])


# 9
# Stop gninnipS My sdroW!
def spin_words(sentence):
    return ''.join([word + ' ' if len(word) < 5 else word[::-1] + ' ' for word in sentence.split()]).strip()


# 10
# Which are in?
def in_array(array1, array2):
    substrings = list(
        set([el for el in array1 for el2 in array2 if el in el2]))
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
def high(x):
    c = [sum([ascii_lowercase.index(char) + 1 for char in word])
         for word in x.split()]
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
    seperated = {
        char: word for word in words for char in word if char.isnumeric()}

    word_positions = list(seperated.keys())
    word_positions.sort()

    fixed_words = ' '.join([seperated[position]
                           for position in word_positions])

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
        return s[middle - 1] + s[middle]
    else:
        middle = word_length // 2
        return s[middle]


# 22
# Array.diff
def array_diff(a, b):
    return [item for item in a if item not in b]


# 23
# Is a number prime?


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
def high(x):
    c = [sum([ascii_lowercase.index(char) + 1 for char in word])
         for word in x.split()]
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
        words.append(char) if bool(
            unique) and char == unique[-1] else unique.append(char)

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


def pass_hash(str):
    return hashlib.md5(str.encode()).hexdigest()


# 35
# Exes and Ohs
def xo(s):
    return s.lower().count('o') == s.lower().count('x')


# 36
# Get the square of a number without ** or * or pow()
def square(n): return sum([n for i in range(0, n)])


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


def alphabet_position(text):
    words = text.lower().split()
    indexes = [ascii_lowercase.index(
        char) + 1 for word in words for char in word if char in ascii_lowercase]
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


# 47
# Remove All The Marked Elements of a List
class List:
    def remove_(self, integer_list, values_list):
        return [num for num in integer_list if num not in values_list]


# 48
# Find the missing letter
def find_missing_letter(chars):
    normalized_chars = [char.lower() for char in chars]
    chars_range = ascii_lowercase[ascii_lowercase.index(
        normalized_chars[0]):ascii_lowercase.index(normalized_chars[-1]) + 1]
    missing = ''.join(
        [missing_char for missing_char in chars_range if missing_char not in normalized_chars])
    return missing if chars[0] == chars[0].lower() else missing.capitalize()


# 49
# Even or Odd
def even_or_odd(number):
    return 'Even' if number % 2 == 0 else 'Odd'


# 50
# Remove First and Last Character
def remove_char(s):
    return s[1:-1]


# 51
# Return Negative
def make_negative(number):
    return number if number < 1 or number == 0 else -(number)


# 52
# Sum of positive
def positive_sum(arr):
    return sum(num for num in arr if num > 0)


# 53
# Opposite number
def opposite(number):
    return abs(number) if number < 0 else number - (number * 2)


# 54
# Change it up


def changer(s):
    step1 = ['a' if char == 'z' else alphabet[alphabet.index(
        char) + 1] if char.isalpha() and char != 'z' else char for char in s.lower()]
    step2 = [char.capitalize() if char in 'aeiou' else char for char in step1]
    return ''.join(step2)


# 55
# Which are in?
def in_array(array1, array2):
    unique = set(
        [word1 for word1 in array1 for word2 in array2 if word1 in word2])
    return sorted(list(unique))


# 56
# Find the unique number
def find_uniq(arr):
    nums = list(set(arr))
    return [num for num in nums if arr.count(num) == 1][0]


# 57
# Where my anagrams at?
def anagrams(word, words):
    return [w for w in words if sorted(w) == sorted(word)]


# 58
# Not very secure


def alphanumeric(password):
    if password:
        return all(char in l or char in u or char in d for char in password)
    else:
        return False


# 59
# Sort Numbers
def solution(nums):
    return sorted(nums) if nums else []


# 60
# Simple Pig Latin
def pig_it(text):
    return ' '.join([word[1:] + word[0] + 'ay' if word.isalpha() else word for word in text.split()])


# 61
# Moving Zeros To The End
def move_zeros(array):
    zeroes = [num for num in array if num == 0]
    return [num for num in array if not num == 0] + zeroes


# 62
# Reversed Strings
def solution(string):
    return string[::-1]


# 63
# Convert boolean values to strings 'Yes' or 'No'.
def bool_to_word(boolean):
    return 'Yes' if boolean else 'No'


# 64
# Convert a Number to a String!
def number_to_string(num):
    return str(num)


# 65
# String repeat
def repeat_str(repeat, string):
    return string * repeat


# 66
# Find the smallest integer in the array
def find_smallest_int(arr):
    return min(arr)


# 67
# Grasshopper - Summation
def summation(num):
    count = 0
    for i in range(1, num + 1):
        count += i

    return count


# 68
# ISBN-10 Validation


def valid_ISBN10(isbn):
    if (len(isbn) == 10) and (all(n in d for n in isbn[:9])) and (isbn[-1] in d or isbn[-1] == 'X'):
        nums = [int(num) if num in d else 10 for num in isbn]
        multiplied = [num * (idx + 1) for idx, num in enumerate(nums)]
        return sum(multiplied) % 11 == 0
    else:
        return False


# 69
# Remove String Spaces
def no_space(x):
    return ''.join([char for char in x if char != ' '])


# 70
# Sum of Digits / Digital Root
def digital_root(n):
    nums = n
    while len(str(nums)) != 1:
        nums = sum(int(num) for num in str(nums))

    return nums


# 71
# Who likes it?
def likes(names):
    if not names:
        return "no one likes this"
    elif len(names) == 1:
        return f'{names[0]} likes this'
    elif len(names) == 2:
        return f'{names[0]} and {names[1]} like this'
    elif len(names) == 3:
        return f'{names[0]}, {names[1]} and {names[2]} like this'
    elif len(names) > 3:
        return f'{names[0]}, {names[1]} and {len(names) - 2} others like this'


# 72
# Are they the "same"?
def comp(array1, array2):
    if array1 and array2:
        return sorted(num ** 2 for num in array1) == sorted(array2)
    elif (array1 is not None and len(array1) == 0) and (array2 is not None and len(array2) == 0):
        return True
    else:
        return False


# 73
# String cleaning
def string_clean(s):
    return ''.join(char for char in s if char not in digits)


# 74
# Convert number to reversed array of digits
def digitize(n):
    return [int(num) for num in str(n)[::-1]]


# 75
# Ones and Zeros
def binary_array_to_number(arr):
    return int(''.join(str(num) for num in arr), 2)


# 76
# Find the divisors!
def divisors(integer):
    divs = [n for n in range(2, integer) if integer % n == 0]
    return divs if divs else f'{integer} is prime'


# 77
# Convert a String to a Number!
def string_to_number(s):
    return int(s)


# 78
# Don't give me five!
def dont_give_me_five(start, end):
    return len([n for n in range(start, end + 1) if not '5' in str(n)])


# 79
# Returning Strings
def greet(name):
    return f'Hello, {name} how are you doing today?'


# 80
# Count of positives / sum of negatives
def count_positives_sum_negatives(arr):
    return [] if not arr else [sum(1 for num in arr if num > 0), sum(num for num in arr if num < 0)]


# 81
# Function 1 - hello world
def greet():
    return 'hello world!'


# 82
# You only need one - Beginner
def check(seq, elem):
    return elem in seq


# 83
# Invert values
def invert(lst):
    return [-(num) for num in lst]


# 84
# Reversed Words
def reverse_words(s):
    words = s.split(' ')
    words.reverse()
    return ' '.join(words)


# 85
# Calculate average
def find_average(numbers):
    return 0 if not numbers else sum(numbers) / len(numbers)


# 86
# Small enough? - Beginner
def small_enough(array, limit):
    return all(num < limit or num == limit for num in array)


# 87
# Remove anchor from URL
def remove_url_anchor(url):
    return url.split('#')[0]


# 88
# Disemvowel Trolls
def disemvowel(string_):
    return ''.join(char for char in string_ if char not in 'AEIOUaeiou')


# 89
# Are You Playing Banjo?
def are_you_playing_banjo(name):
    return f'{name} plays banjo' if name[0] == 'r' or name[0] == 'R' else f'{name} does not play banjo'


# 90
# Counting sheep...
def count_sheeps(sheep):
    return sheep.count(True)


# 91
# Century From Year
def century(year):
    return ceil(year / 100)


# 92
# Is n divisible by x and y?
def is_divisible(n, x, y):
    return n % x == 0 and n % y == 0


# 93
# Keep Hydrated!
def litres(time):
    return floor(0.5 * time)


# 94
# Beginner - Lost Without a Map
def maps(a):
    return [el * 2 for el in a]


# 95
# Beginner Series #2 Clock
def past(h, m, s):
    return ((h * 3600) + (m * 60) + s) * 1000


# 96
# Convert a Boolean to a String
def boolean_to_string(b):
    return 'True' if b else 'False'

# 97
# Mumbling
def accum(s):
    return '-'.join([(s[i] * (i + 1)).capitalize() for i in range(len(s))])

# 98
# You're a square!
import math

def is_square(n):
    return False if n < 0 else math.sqrt(n) == math.ceil(math.sqrt(n))

# 99
# Exes and Ohs
def xo(s):
    return s.lower().count('x') == s.lower().count('o')

# 100
# Opposites Attract
def lovefunc( flower1, flower2 ):
    return (flower1 % 2 == 0 and flower2 % 2 != 0) or (flower1 % 2 != 0 and flower2 % 2 == 0)

# 101
# Beginner Series #1 School Paperwork
def paperwork(n, m):
    return 0 if n < 0 or m < 0 else n * m

# 102
# Fake Binary
def fake_bin(x):
    return ''.join('0' if int(char) < 5 else '1' for char in x)

# 103
# How good are you really?
def better_than_average(class_points, your_points):
    return your_points > sum(class_points) / len(class_points)

# 104
# Reversed sequence
def reverse_seq(n):
    return [i for i in range(n, 0, -1)]

# 105
# Sum Arrays
def sum_array(a):
    return sum(a)

# 106
# Beginner - Reduce but Grow
def grow(arr):
    count = 1
    for n in arr:
        count *= n
    return count

# 107
# Jenny's secret message
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)

# 108
# Is he gonna survive?
def hero(bullets, dragons):
    return bullets >= dragons * 2

# 109
# Simple multiplication
def simple_multiplication(number) :
    return number * 8 if number % 2 == 0 else number * 9

# 110
# MakeUpperCase
def make_upper_case(s):
    return s.upper()

# 111
# Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return mpg * fuel_left >= distance_to_pump

# 112
# DNA to RNA Conversion
def dna_to_rna(dna):
    return dna.replace('T', 'U')

# 113
# Array plus array
def array_plus_array(arr1,arr2):
    return sum(arr1 + arr2)
