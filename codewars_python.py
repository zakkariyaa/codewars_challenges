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

# 114
# If you can't sleep, just count sheep!!
def count_sheep(n):
    return ''.join(f'{i + 1} sheep...' for i in range(0, n))

# 115
# Get the mean of an array
import math

def get_average(marks):
    return math.floor(sum(marks) / len(marks))

# 116
# Find Maximum and Minimum Values of a List
def minimum(arr):
    min = arr[0]
    for num in arr:
        if num < min:
            min = num
    return min

def maximum(arr):
    max = arr[0]
    for num in arr:
        if num > max:
            max = num
    return max

# 117
# Count by X
def count_by(x, n):
    return [x * i for i in range(1, n + 1)]

# 118
# Sentence Smash
def smash(words):
    return " ".join(words)

# 119
# Sum without highest and lowest number
def sum_array(arr):
    return sum(sorted(arr)[1:len(arr) - 1]) if arr else 0

# 120
# Count the Monkeys!
def monkey_count(n):
    return [i for i in range(1, n + 1)]

# 121
# Do I get a bonus?
def bonus_time(salary, bonus):
    return f'${salary * 10}' if bonus else f'${salary}'

# 122
# Total amount of points
def points(games):
    p = 0

    for game in games:
        scores = game.split(':')
        if scores[0] > scores[1]:
            p += 3
        elif scores[0] < scores[1]:
            p += 0
        else:
            p += 1

    return p

# 123
# Convert a string to an array
def string_to_array(s):
    return s.split(' ')

# 124
# Calculate BMI
def bmi(weight, height):
    result = weight / (height ** 2)
    if result <= 18.5:
        return "Underweight"
    elif result <= 25.0:
        return "Normal"
    elif result <= 30.0:
        return "Overweight"
    elif result > 30:
        return "Obese"

# 125
# You Can't Code Under Pressure #1
def double_integer(i):
    return i * 2

# 126
# Sum Mixed Array
def sum_mix(arr):
    return sum(int(num) for num in arr)

# 127
# Area or Perimeter
def area_or_perimeter(l, w):
    return l ** 2 if l == w else 2 * (l + w)

# 128
# Grasshopper - Personalized Message
def greet(name, owner):
    return 'Hello boss' if name == owner else 'Hello guest'

# 129
# The Feast of Many Beasts
def feast(beast, dish):
    return beast[0] == dish[0] and beast[-1] == dish[-1]

# 130
# Rock Paper Scissors!
def rps(p1, p2):
    beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if beats[p1] == p2:
        return "Player 1 won!"
    if beats[p2] == p1:
        return "Player 2 won!"
    return "Draw!"

# 131
# Transportation on vacation
def rental_car_cost(d):
    if d >= 7:
        return (d * 40) - 50
    elif d > 3:
        return (d * 40) - 20
    else:
        return d * 40

# 132
# Remove exclamation marks
def remove_exclamation_marks(s):
    return s.replace('!', '')

# 133
# L1: Set Alarm
def set_alarm(employed, vacation):
    return True if employed and not vacation else False

# 134
# Thinkful - Logic Drills: Traffic light
def update_light(current):
    states = ['green', 'yellow', 'red']
    return states[(states.index(current) + 1) % len(states)]

# 135
# Double Char
def double_char(s):
    return ''.join(char * 2 for char in list(s))

# 136
# Twice as old
def twice_as_old(dad_years_old, son_years_old):
    return abs(dad_years_old - (son_years_old * 2))

# 137
# Removing Elements
def remove_every_other(my_list):
    return [my_list[i] for i in range(len(my_list)) if i % 2 == 0]

# 138
# Get Planet Name By ID
def get_planet_name(id):
    planets = {
        1: "Mercury",
        2: "Venus",
        3: "Earth",
        4: "Mars",
        5: "Jupiter",
        6: "Saturn",
        7: "Uranus",
        8: "Neptune",
    }
    return planets[id]

# 139
# Will there be enough space?
def enough(cap, on, wait):
    return 0 if cap - on >= wait else abs(cap - on - wait)

# 140
# Beginner Series #4 Cockroach
from math import floor

def cockroach_speed(s):
    return floor(s / 0.036)

# 141
# Keep up the hoop
def hoop_count(n):
    return "Great, now move on to tricks" if n >= 10 else "Keep at it until you get it"

# 142
# Correct the mistakes of the character recognition software
def correct(s):
    return s.replace('5', 'S').replace('0', 'O').replace('1', 'I')

# 143
# Third Angle of a Triangle
def other_angle(a, b):
    return 180 - (a + b)

# 144
# Grasshopper - Check for factor
def check_for_factor(base, factor):
    return base % factor == 0

# 145
# Count Odd Numbers below n
import math

def odd_count(n):
    return math.floor(n / 2)

# 146
# Find numbers which are divisible by given number
def divisible_by(numbers, divisor):
    return [num for num in numbers if num % divisor == 0]

# 147
# Parse nice int from char problem
def get_age(age):
    return int(age[0])

# 148
# All Star Code Challenge #18
def str_count(strng, letter):
    return strng.count(letter)

# 149
# altERnaTIng cAsE <=> ALTerNAtiNG CaSe
def to_alternating_case(string):
    return ''.join(char.upper() if char == char.lower() else char.lower() for char in list(string))

# 150
# Welcome!
def greet(language):
    languages = {
        'english': 'Welcome',
        'czech': 'Vitejte',
        'danish': 'Velkomst',
        'dutch': 'Welkom',
        'estonian': 'Tere tulemast',
        'finnish': 'Tervetuloa',
        'flemish': 'Welgekomen',
        'french': 'Bienvenue',
        'german': 'Willkommen',
        'irish': 'Failte',
        'italian': 'Benvenuto',
        'latvian': 'Gaidits',
        'lithuanian': 'Laukiamas',
        'polish': 'Witamy',
        'spanish': 'Bienvenido',
        'swedish': 'Valkommen',
        'welsh': 'Croeso'
        }
    return languages[language] if language in languages.keys() else languages['english']

# 151
# Volume of a Cuboid
def get_volume_of_cuboid(length, width, height):
    return length * width * height

# 152
# To square(root) or not to square(root)
import math

def square_or_square_root(arr):
    return [math.sqrt(num) if math.sqrt(num).is_integer() else num ** 2 for num in arr]

# 153
# Powers of 2
def powers_of_two(n):
    return [2 ** i for i in range(0, n + 1)]

# 154
# I love you, a little , a lot, passionately ... not at all
def how_much_i_love_you(nb_petals):
    words = [
    'I love you',
    'a little',
    'a lot',
    'passionately',
    'madly',
    'not at all',
    ];

    return words[(nb_petals - 1) % len(words)]

# 155
# Sort and Star
def two_sort(array):
    return '***'.join(list(sorted(array)[0]))

# 156
# Is it a palindrome?
def is_palindrome(s):
    return s.lower() == s.lower()[::-1]

# 157
# Sum The Strings
def sum_str(a, b):
    num1 = int(a) if a else 0
    num2 = int(b) if b else 0
    return str(num1 + num2)

# 158
# Difference of Volumes of Cuboids
def find_difference(a, b):
    num1 = 1
    num2 = 1
    for num in a: num1 *= num
    for num in b: num2 *= num

    return abs(num1 - num2)

# 159
# Is it even?
def is_even(n):
    return n % 2 == 0

# 160
# Grasshopper - Messi goals function
def goals(laLiga, copaDelRey, championsLeague):
    return laLiga + copaDelRey + championsLeague

# 161
# Unfinished Loop - Bug Fixing #1
def create_array(n):
    res=[]
    i=1
    while i<=n:
        res+=[i]
        i += 1
    return res

# 162
# Filter out the geese
geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    return [el for el in birds if el not in geese]

# 163
# Reverse List Order
def reverse_list(l):
    l.reverse()
    return l

# 164
# Generate range of integers
def generate_range(min, max, step):
    return [i for i in range(min, max + 1, step)]

# 165
# Lario and Muigi Pipe Problem
def pipe_fix(nums):
    return [i for i in range(nums[0], nums[-1] + 1)]

# 166
# Capitalization and Mutability
def capitalize_word(word):
    return word.capitalize()

# 167
# 101 Dalmatians - squash the bugs, not the dogs!
def how_many_dalmatians(n):
    dogs = ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"];
    if n <= 10:
        return dogs[0]
    elif n <= 50:
        return dogs[1]
    elif n == 101:
        return dogs[3]
    else:
        return dogs[2]

# 168
# Grasshopper - Terminal game combat function
def combat(health, damage):
    return health - damage if health - damage > 0 else 0

# 169
# Exclamation marks series #1: Remove an exclamation mark from the end of string
def remove(s):
    return s[:-1] if s and s[-1] == '!' else s

# 170
# Basic variable assignment
a = "code"
b = "wa.rs"
name = a + b

# 171
# The Wide-Mouthed frog!
def mouth_size(animal):
    return 'small' if animal.lower() == 'alligator' else 'wide'

# 172
# Vowel remover
def shortcut(s):
    return ''.join(char for char in list(s) if char not in 'aeiou')


# 173
# Jaden Casing Strings
def to_jaden_case(string):
    return ' '.join(word.capitalize() for word in string.split(' '))


# 174
# Complementary DNA
def DNA_strand(dna):
    return dna.translate(dna.maketrans('ATCG', 'TAGC'))

# 175
# Credit Card Mask
def maskify(cc):
    return f"{len(cc[:-4]) * '#'}{cc[-4:]}"

# 176
# Sum of two lowest positive integers
def sum_two_smallest_numbers(numbers):
    return sorted(numbers)[0] + sorted(numbers)[1]

# 177
# Beginner Series #3 Sum of Numbers
def get_sum(a,b):
    nums = sorted([a, b])
    return sum(i for i in range(nums[0], nums[1] + 1))

# 178
# Friend or Foe?
def friend(x):
    return [name for name in x if len(name) == 4]

# 179
# Categorize New Member
def open_or_senior(data):
    return ['Senior' if p[0] >= 55 and p[1] > 7 else 'Open' for p in data]

# 180
# Printer Errors
def printer_error(s):
    errors = 'nopqrstuvwxyz'
    return f'{len([char for char in s if char in errors])}/{len(s)}'

# 181
# Regex validate PIN code
def validate_pin(pin):
    check_length = len(pin) == 4 or len(pin) == 6
    digits = [char for char in pin if char.isnumeric()]
    check_digits = len(digits) == 4 or len(digits) == 6

    return check_length and check_digits

# 182
# Binary Addition
def add_binary(a,b):
    return bin(a + b)[2:]

# 183
# String ends with?
def solution(string, ending):
    return string.endswith(ending)

# 184
# Sum of odd numbers
def row_sum_odd_numbers(n):
    current_row = (n * n) - (n - 1)
    prev_row = ((n - 1) * (n - 1)) - (n - 2)
    end_loop = (current_row - prev_row) + current_row

    result = 0
    for i in range(current_row, end_loop + 1):
        if i % 2 != 0:
            result += i

    return result

# 185
# Odd or Even?
def odd_or_even(arr):
    return 'even' if sum(arr) % 2 == 0 else 'odd'

# 186
# Reverse words
def reverse_words(text):
    words = text.split(' ')
    reversed = [word[::-1] for word in words]

    return ' '.join(reversed)

# 187
# Testing 1-2-3
def number(lines):
    return [f'{i+1}: {lines[i]}' for i in range(len(lines))]

# 188
# The highest profit wins!
def min_max(lst):
    return [min(lst), max(lst)]

# 189
# Remove the minimum
def remove_smallest(numbers):
    new_arr = [num for num in numbers]

    if numbers:
        new_arr.pop(new_arr.index(min(new_arr)))
        return new_arr
    else:
        return []

# 190
# Anagram Detection
def is_anagram(test, original):
    return sorted(test.lower()) == sorted(original.lower())

# 191
# Find the stray number
def stray(arr):
    new_arr = sorted(arr)
    return new_arr[-1] if new_arr[0] == new_arr[1] else new_arr[0]

# 192
# Number of People in the Bus
def number(bus_stops):
    in_people = sum([arr[0] for arr in bus_stops])
    out_people = sum([arr[1] for arr in bus_stops])

    return in_people - out_people


# 193
# Count the divisors of a number
def divisors(n):
    return len([i + 1 for i in range(n) if n % (i + 1) == 0])

# 194
# Count the Digit
def nb_dig(n, d):
    k = [i ** 2 for i in range(n + 1)]
    return sum(str(num).count(str(d)) for num in k if str(d) in str(num))
