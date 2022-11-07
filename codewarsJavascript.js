// 1
// Multiply
function multiply(a, b) {
  return a * b;
}

// 2
// Square Every Digit
function squareDigits(num) {
  let newNum = String(num).split('');
  let squaredNums = [];
  for (let i of newNum) {
    squaredNums.push(Number(i) ** 2);
  }

  return Number(squaredNums.join(''));
}

// 3
// String ends with?
function solution(str, ending) {
  return str.endsWith(ending);
}

// 4
// Who likes it?
function likes(names) {
  let message;
  if (names.length > 3) {
    message = `${names[0]}, ${names[1]} and ${
      names.length - 2
    } others like this`;
  } else if (names.length > 2) {
    message = `${names[0]}, ${names[1]} and ${names[2]} like this`;
  } else if (names.length > 1) {
    message = `${names[0]} and ${names[1]} like this`;
  } else if (names.length > 0) {
    message = `${names[0]} likes this`;
  } else {
    message = 'no one likes this';
  }

  return message;
}

// 5
// Unique In Order
var uniqueInOrder = function (iterable) {
  let others = [];
  let uniqueLetters = [];
  for (let letter of iterable) {
    letter === uniqueLetters[uniqueLetters.length - 1]
      ? others.push(letter)
      : uniqueLetters.push(letter);
  }

  return uniqueLetters;
};

// 6
// Highest and Lowest
function highAndLow(numbers) {
  let newNumbers = numbers.split(' ');
  let maxMin = [];

  for (let num of newNumbers) {
    maxMin.push(Number(num));
  }

  return `${Math.max(...maxMin)} ${Math.min(...maxMin)}`;
}

// 7
// Is a number prime?
function isPrime(num) {
  for (let i = 2; i <= Math.sqrt(num); i++) {
    if (num % i === 0) {
      return false;
    }
  }

  return num > 1;
}

// 8
// Powers of 2
function powersOfTwo(n) {
  const powers = [];
  for (let i = 0; i <= n; i++) {
    console.log(i);
    powers.push(2 ** i);
  }
  return powers;
}

// 9
// Vowel Count
function getCount(str) {
  var vowelsCount = 0;

  for (let char of str) {
    if (
      char === 'a' ||
      char === 'e' ||
      char === 'i' ||
      char === 'o' ||
      char === 'u'
    ) {
      vowelsCount += 1;
    }
  }

  return vowelsCount;
}

// 10
// List Filtering
function filter_list(l) {
  return l.filter((el) => {
    return Number.isInteger(el);
  });
}

// 11
// Responsible Drinking
function hydrate(s) {
  const drinks = s.split(' ');
  const drinkAmount = drinks.filter((el) => {
    return !isNaN(el);
  });

  const water = drinkAmount.reduce((prev, current) => {
    return Number(prev) + Number(current);
  });

  if (water > 1) {
    return `${water} glasses of water`;
  } else if (water.length === 1) {
    return `${water} glass of water`;
  }
}

// 12
// Battle of the characters (Easy)
function battle(x, y) {
  const alpha = String.fromCharCode(...Array(123).keys())
    .slice(97)
    .toUpperCase()
    .split('');
  let xCount = { name: x, power: 0 };
  let yCount = { name: y, power: 0 };

  for (let char of x) {
    xCount.power += alpha.indexOf(char) + 1;
  }

  for (let char of y) {
    yCount.power += alpha.indexOf(char) + 1;
  }

  if (xCount.power > yCount.power) {
    return xCount.name;
  } else if (xCount.power === yCount.power) {
    return 'Tie!';
  } else {
    return yCount.name;
  }
}

// 13
// Dot Calculator
function dotCalculator(equation) {
  const parts = equation.split(' ');
  const operator = parts[1];
  if (operator === '+') {
    return parts[0] + parts[2];
  } else if (operator === '-') {
    const diff = parts[0].length - parts[2].length;
    return '.'.repeat(diff);
  } else if (operator === '*') {
    const diff = parts[0].length * parts[2].length;
    return '.'.repeat(diff);
  } else if (operator === '//') {
    const diff = Math.trunc(parts[0].length / parts[2].length);
    return '.'.repeat(diff);
  }
}

// 14
// CamelCase Method
String.prototype.camelCase = function (value) {
  const words = this.split(' ').filter((el) => el !== '');
  const title = words.map((el) => {
    const temp = el[0].toUpperCase() + el.slice(1);
    return temp;
  });
  return title.join('');
};

// 15
// Find the missing letter
function findMissingLetter(array) {
  const newArr = array.map((el) => el.toLowerCase());
  const alphabet = 'abcdefghijklmnopqrstuvwxyz'.split('');
  const startCheck = alphabet.indexOf(newArr[0]);
  const endCheck = alphabet.indexOf(newArr[newArr.length - 1]);
  const checkArea = alphabet.slice(startCheck, endCheck + 1);

  const missingLetter = checkArea.filter((el) => {
    if (!newArr.includes(el)) {
      return el;
    }
  });

  if (array[0] === newArr[0]) {
    return missingLetter.join('');
  } else {
    return missingLetter.join('').toUpperCase();
  }
}

// 16
// Are the numbers in order?
function inAscOrder(arr) {
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > arr[i + 1]) {
      return false;
    }
  }

  return true;
}

// 17
// Filter Long Words
function filterLongWords(sentence, n) {
  const longWords = sentence.split(' ').filter((el) => {
    return el.length > n;
  });

  return longWords;
}

// 18
// Split Strings
function solution(str) {
  const newStr = str.length % 2 === 0 ? str : str + '_';
  const splittedLetters = [];

  for (let i = 0; i < newStr.length; i += 2) {
    splittedLetters.push(newStr[i] + newStr[i + 1]);
  }

  return splittedLetters;
}

// 19
// Duplicate Encoder
String.prototype.count = function (c) {
  let result = 0;
  for (let i = 0; i < this.length; i++) {
    if (this[i] === c) {
      result++;
    }
  }
  return result;
};

function duplicateEncode(word) {
  const letters = word.toLowerCase().split('');
  return letters
    .map((char) => {
      return word.toLowerCase().count(char) > 1 ? ')' : '(';
    })
    .join('');
}

// 20
// Two to One
function longest(s1, s2) {
  const merged = (s1 + s2).split('').sort();
  return merged.filter((el, index) => merged.indexOf(el) === index).join('');
}

// 21
// Sum of two lowest positive integers
function sumTwoSmallestNumbers(numbers) {
  const sorted = numbers.sort((num1, num2) => num1 - num2);
  return sorted[0] + sorted[1];
}

// 22
// Complementary DNA
function DNAStrand(dna) {
  return dna
    .split('')
    .map((char) =>
      char === 'A'
        ? 'T'
        : char === 'T'
        ? 'A'
        : char === 'G'
        ? 'C'
        : char === 'C'
        ? 'G'
        : ''
    )
    .join('');
}

// 23
// Shortest Word
function findShort(s) {
  return s
    .split(' ')
    .reduce((prev, current) => (current.length > prev.length ? prev : current))
    .length;
}

// 24
// Exes and Ohs
function XO(str) {
  const x = str
    .toLowerCase()
    .split('')
    .filter((el) => el == 'x');
  const o = str
    .toLowerCase()
    .split('')
    .filter((el) => el == 'o');

  return x.length === o.length;
}

// 25
// Get the Middle Character
function getMiddle(s) {
  const middle = Math.floor(s.length / 2);
  return s.length % 2 == 0 ? s[middle - 1] + s[middle] : s[middle];
}

// 26
// Simple Pig Latin
function pigIt(str) {
  const alphabet = 'abcdefghijklmnopqrstuvwxyz'.split('');
  const words = str
    .split(' ')
    .map((word) => {
      return word
        .toLowerCase()
        .split('')
        .every((char) => alphabet.includes(char))
        ? word.slice(1) + word[0] + 'ay'
        : word;
    })
    .join(' ');

  return words;
}

// 27
// Reverse words
function reverseWords(str) {
  return str
    .split(' ')
    .map((word) => word.split('').reverse().join(''))
    .join(' ');
}

// 28
// Odd or Even?
function oddOrEven(array) {
  return array.reduce((prev, current) => prev + current, 0) % 2 === 0
    ? 'even'
    : 'odd';
}

// 29
// Find the divisors!
function divisors(integer) {
  const divisors = [];
  for (let i = 2; i < integer; i++) {
    if (integer % i === 0) {
      divisors.push(i);
    }
  }

  return divisors.length >= 1 ? divisors : `${integer} is prime`;
}

// 30
// Number of People in the Bus
var number = function (busStops) {
  let onBus = 0;
  let offBus = 0;
  for (let stop of busStops) {
    onBus += stop[0];
    offBus += stop[1];
  }

  return onBus - offBus;
};

// 31
// Binary Addition
function addBinary(a, b) {
  const sum = a + b;
  return sum.toString(2);
}

// 32
// Printer Errors
function printerError(s) {
  const check = 'nopqrstuvwxyz';
  const errors = s.split('').filter((char) => check.includes(char));

  return `${errors.length}/${s.length}`;
}

// 33
// Friend or Foe?
function friend(friends) {
  return friends.filter((name) => name.length === 4);
}

// 34
// Categorize New Member
function openOrSenior(data) {
  return data.map((info) => (info[0] >= 55 && info[1] > 7 ? 'Senior' : 'Open'));
}

// 35
// Case Swapping
function swap(str) {
  return str
    .split('')
    .map((char) =>
      char === char.toLowerCase() ? char.toUpperCase() : char.toLowerCase()
    )
    .join('');
}

// 36
// Bit Counting
var countBits = function (n) {
  return Number(
    n
      .toString(2)
      .split('')
      .filter((el) => el == 1)
      .reduce((a, b) => Number(a) + Number(b), 0)
  );
};

// 37
// Find the odd int
function count(arr, num) {
  let count = 0;
  for (let i = 0; i <= arr.length; i++) {
    if (arr[i] === num) {
      count += 1;
    }
  }
  return count;
}

function findOdd(A) {
  return A.filter((num) => count(A, num) % 2 !== 0)[0];
}

// 38
// Multiples of 3 or 5
function solution(number) {
  let sum = 0;
  for (let i = 0; i < number; i++) {
    i % 3 === 0 || i % 5 === 0 ? (sum += i) : (sum += 0);
  }
  return sum;
}

// 39
// Turn the Mars rover to take pictures
function turn(pos1, pos2) {
  const directions = {
    NE: 'right',
    NW: 'left',
    EN: 'left',
    ES: 'right',
    SE: 'left',
    SW: 'right',
    WS: 'left',
    WN: 'right',
  };

  const positions = pos1 + pos2;
  return directions[positions];
}

// 40
// Find the nth Digit of a Number
var findDigit = function (num, nth) {
  const nums = String(Math.abs(num)).split('').reverse();
  return nth < 0 || nth === 0
    ? -1
    : nth > nums.length
    ? 0
    : Number(nums[nth - 1]);
};

// 41
// ASCII Shift Encryption/Decryption
function asciiEncrypt(plaintext) {
  return plaintext
    .split('')
    .map((char, index) => String.fromCharCode(char.charCodeAt() + index))
    .join('');
}

function asciiDecrypt(ciphertext) {
  return ciphertext
    .split('')
    .map((char, index) => String.fromCharCode(char.charCodeAt() - index))
    .join('');
}

// 42
// How good are you really?
function betterThanAverage(classPoints, yourPoints) {
  const totalScore =
    classPoints.reduce((a, b) => a + b, 0) / classPoints.length;
  return yourPoints > totalScore;
}

// 43
// Find the vowels
function vowelIndices(word) {
  return word
    .split('')
    .map((char, index) => {
      return 'aeiouyAEIOUY'.includes(char) ? index + 1 : '';
    })
    .filter((el) => el !== '');
}

// 44
// 'x' marks the spot.
const xMarksTheSpot = (input) => {
  const xSpot = [];

  for (let i = 0; i < input.length; i++) {
    const list = input[i];
    for (let k = 0; k < list.length; k++) {
      const element = list[k];
      if (element === 'x') {
        xSpot.push([i, k]);
      }
    }
  }

  return xSpot.length > 1 || xSpot.length === 0 ? [] : xSpot[0];
};

// 45
// Filter unused digits
function unusedDigits() {
  const digits = '0123456789'.split('');
  const nums = Object.values(arguments)
    .join()
    .split('')
    .filter((el) => el !== ',');
  const waldos = digits.filter((num) => !nums.includes(num));
  return waldos.join('');
}

// 46
function dropCap(n) {
  const words = n.split(' ');
  const capitalized = words.map((el) => {
    if (el !== '' && el.length > 2) {
      return el[0].toUpperCase() + el.slice(1).toLowerCase();
    } else return el;
  });

  return capitalized.join(' ');
}

// 47
// Moving Zeros To The End
function moveZeros(arr) {
  const zeroes = arr.filter((el) => el === 0);
  const noZeroes = arr.filter((el) => el !== 0);
  return [...noZeroes, ...zeroes];
}

// 48
// First non-repeating character
Array.prototype.count = function (item) {
  let count = 0;
  this.forEach((el) => (el === item ? (count += 1) : (count += 0)));
  return count;
};

function firstNonRepeatingLetter(s) {
  const chars = s.toLowerCase().split('');
  const elementCount = chars.map((el, index) =>
    chars.count(el) === 1 ? index : ''
  );
  const filtered = elementCount.filter((el) => el !== '');
  return !s || filtered.length < 1 ? '' : s[filtered[0]];
}

// 49
// Even or Odd
const even_or_odd = (number) => (number % 2 === 0 ? 'Even' : 'Odd');

// 50
// Sum of positive
function positiveSum(arr) {
  return arr.filter((num) => num > 0).reduce((a, b) => a + b, 0);
}

// 51
// Return Negative
const makeNegative = (num) => (num < 0 ? num : -num);

// 52
// Opposite number
const opposite = (number) => (number < 0 ? Math.abs(number) : -number);

// 53
// Remove First and Last Character
const removeChar = (str) => str.slice(1, str.length - 1);

// 54
// Reversed Strings
const solution = (str) => str.split('').reverse().join('');

// 55
// Convert boolean values to strings 'Yes' or 'No'.
const boolToWord = (bool) => (bool ? 'Yes' : 'No');

// 56
// Convert a Number to a String!
const numberToString = (num) => String(num);

// 57
// String repeat
const repeatStr = (n, s) => s.repeat(n);

// 58
// Find the smallest integer in the array
class SmallestIntegerFinder {
  findSmallestInt(args) {
    return Math.min(...args);
  }
}

// 59
// Bin to Decimal
function binToDec(bin) {
  return parseInt(bin, 2);
}

// 60
// Name Shuffler
function nameShuffler(str) {
  const names = str.split(' ');
  return `${names[1]} ${names[0]}`;
}

// 60
// Square(n) Sum
function squareSum(numbers) {
  return numbers.map((num) => num ** 2).reduce((a, b) => a + b, 0);
}

// 61
// Counting sheep...
function countSheeps(arrayOfSheep) {
  return arrayOfSheep.filter((el) => el === true).length;
}

// 62
// Counting Duplicates
String.prototype.count = function (el) {
  let count = 0;
  for (let i = 0; i < this.length; i++) {
    this.toLowerCase()[i] === el ? (count += 1) : (count += 0);
  }

  return count;
};

function duplicateCount(text) {
  let elCount = [];
  for (let i = 0; i < text.length; i++) {
    if (text.count(text[i]) > 1) {
      elCount.push(text[i]);
    }
  }

  const unique = new Set(elCount);
  return [...unique].length;
}

// 63
// Keep Hydrated!
function litres(time) {
  return Math.floor(time * 0.5);
}

// 64
// Is n divisible by x and y?
function isDivisible(n, x, y) {
  return n % x === 0 && n % y === 0;
}

// 65
// Remove String Spaces
function noSpace(x) {
  return x
    .split('')
    .filter((char) => char !== ' ')
    .join('');
}

// 66
// Grasshopper - Summation
var summation = function (num) {
  let count = 0;
  for (let i = 1; i <= num; i++) {
    count += i;
  }
  return count;
};

// 67
// Century From Year
function century(year) {
  return Math.ceil(year / 100);
}

// 68
// A Needle in the Haystack
function findNeedle(haystack) {
  return `found the needle at position ${haystack.indexOf('needle')}`;
}

// 69
// Beginner - Lost Without a Map
function maps(x) {
  return x.map((num) => num + num);
}

// 70
// Convert a String to a Number!
var stringToNumber = function (str) {
  return Number(str);
};

// 71
// Returning Strings
function greet(name) {
  return `Hello, ${name} how are you doing today?`;
}

// 72
// Function 1 - hello world
const greet = () => 'hello world!';

// 73
// You only need one - Beginner
function check(a, x) {
  return a.includes(x);
}

// 74
// Reversed Words
function reverseWords(str) {
  return str.split(' ').reverse().join(' ');
}

// 75
// Do I get a bonus?
function bonusTime(salary, bonus) {
  return bonus ? `£${salary * 10}` : `£${salary}`;
}

// 76
// Sentence Smash
function smash(words) {
  return words.join(' ');
}

// 77
// WeIrD StRiNg CaSe
function toWeirdCase(string) {
  const words = string.split(' ');
  return words
    .map((word) =>
      word
        .split('')
        .map((char, i) =>
          i % 2 === 0 ? char.toUpperCase() : char.toLowerCase()
        )
        .join('')
    )
    .join(' ');
}

// 78
// Convert number to reversed array of digits
function digitize(n) {
  return String(n)
    .split('')
    .reverse()
    .map((n) => Number(n));
}

// 78
// Count the Monkeys!
function monkeyCount(n) {
  const nums = [];
  for (let num = 1; num <= n; num++) {
    nums.push(num);
  }

  return nums;
}

// 79
// Are You Playing Banjo?
function areYouPlayingBanjo(name) {
  return name.startsWith('R') || name.startsWith('r')
    ? `${name} plays banjo`
    : `${name} does not play banjo`;
}

// 80
// Sum Arrays
function sum(numbers) {
  'use strict';

  return numbers.length > 0 ? numbers.reduce((a, b) => a + b, 0) : 0;
}

// 81
// Invert values
function invert(array) {
  return array.map((num) => -Number(num));
}

// 82
// Find the capitals
var capitals = function (word) {
  const indexes = word
    .split('')
    .map((c, idx) => (c === c.toUpperCase() ? idx : null));
  return indexes.filter((el) => el !== null);
};

// 83
// Two Oldest Ages
function twoOldestAges(ages) {
  const sorted = ages.sort((a, b) => a - b, 0);
  return [sorted[sorted.length - 2], sorted[sorted.length - 1]];
}

// 84
// Sum of a sequence
const sequenceSum = (begin, end, step) => {
  let sum = 0;
  for (let i = begin; i <= end; i += step) {
    sum += i;
  }

  return sum;
};

// 85
// Anagram Detection
var isAnagram = function (test, original) {
  return (
    original.toLowerCase().split('').sort().join('') ===
    test.toLowerCase().split('').sort().join('')
  );
};

// 86
// Array plus array
function arrayPlusArray(arr1, arr2) {
  const join = arr1.concat(arr2);
  return join.reduce((a, b) => a + b, 0);
}

// 87
// Is he gonna survive?
function hero(bullets, dragons) {
  return bullets >= dragons * 2;
}

// 88
// Beginner - Reduce but Grow
function grow(x) {
  return x.reduce((a, b) => a * b, 1);
}

// 89
// MakeUpperCase
function makeUpperCase(str) {
  return str.toUpperCase();
}

// 90
// Simple multiplication
function simpleMultiplication(number) {
  return number % 2 === 0 ? 8 * number : 9 * number;
}

// 91
// Abbreviate a Two Word Name
function abbrevName(name) {
  const names = name.toUpperCase().split(' ');
  return `${names[0][0]}.${names[1][0]}`;
}

// 92
// Convert a Boolean to a String
function booleanToString(b) {
  return b ? 'true' : 'false';
}

// 93
// Fake Binary
function fakeBin(x) {
  return x
    .split('')
    .map((el) => (Number(el) < 5 ? '0' : '1'))
    .join('');
}

// 94
// Reversed sequence
const reverseSeq = (n) => {
  const nums = [];
  for (let i = n; i >= 1; i--) {
    nums.push(i);
  }

  return nums;
};

// 95
// Beginner Series #1 School Paperwork
function paperwork(n, m) {
  return n > 0 && m > 0 ? n * m : 0;
}

// 96
// Jenny's secret message
function greet(name) {
  return name === 'Johnny' ? 'Hello, my love!' : 'Hello, ' + name + '!';
}

// 97
// Calculate BMI
function bmi(weight, height) {
  const calc = weight / (height * height);
  if (calc <= 18.5) {
    return 'Underweight';
  } else if (calc <= 25.0) {
    return 'Normal';
  } else if (calc <= 30.0) {
    return 'Overweight';
  } else if (calc > 30.0) {
    return 'Obese';
  }
}

// 98
// Get the mean of an array
function getAverage(marks) {
  const sum = marks.reduce((a, b) => a + b);
  return Math.floor(sum / marks.length);
}

// 99
// Opposites Attract
function lovefunc(flower1, flower2) {
  const evens = flower1 % 2 === 0 && flower2 % 2 === 0;
  const odds = flower1 % 2 !== 0 && flower2 % 2 !== 0;

  return odds || evens ? false : true;
}

// 100
// Will you make it?
const zeroFuel = (distanceToPump, mpg, fuelLeft) => {
  return fuelLeft * mpg >= distanceToPump ? true : false;
};

// 101
// Sum without highest and lowest number
function sumArray(array) {
  if (Boolean(array) === true && array.length > 1) {
    const sorted = array.sort((a, b) => a - b).slice(1, -1);
    return sorted.reduce((a, b) => a + b, 0);
  } else {
    return 0;
  }
}

// 102
// Find Maximum and Minimum Values of a List
var min = function (list) {
  return Math.min(...list);
};

var max = function (list) {
  return Math.max(...list);
};

// 103
// Total amount of points
function points(games) {
  let points = 0;
  for (let i = 0; i < games.length; i++) {
    const game = games[i].split(':');
    game[0] > game[1]
      ? (points += 3)
      : game[0] === game[1]
      ? (points += 1)
      : (points += 0);
  }

  return points;
}

// 104
// Convert a string to an array
function stringToArray(string) {
  return string.split(' ');
}

// 105
// Count by X
function countBy(x, n) {
  let z = [];
  for (let i = 1; i <= n; i++) {
    z.push(x * i);
  }
  return z;
}

// 106
// If you can't sleep, just count sheep!!
var countSheep = function (num) {
  const sheep = [];
  for (let i = 1; i <= num; i++) {
    sheep.push(`${i} sheep...`);
  }

  return sheep.join('');
};

// 107
// Sum Mixed Array
function sumMix(x) {
  const nums = x.map((num) => Number(num));
  return nums.reduce((a, b) => a + b);
}

// 108
// Can we divide it?
function isDivideBy(number, a, b) {
  return number % a === 0 && number % b === 0;
}

// 109
// Area or Perimeter
const areaOrPerimeter = function (l, w) {
  return l === w ? l * w : l * 2 + w * 2;
};

// 110
// You Can't Code Under Pressure #1
function doubleInteger(i) {
  return i + i;
}

// 111
// Grasshopper - Personalized Message
function greet(name, owner) {
  return name === owner ? 'Hello boss' : 'Hello guest';
}

// 112
// Remove exclamation marks
function removeExclamationMarks(s) {
  return s
    .split('')
    .filter((el) => el !== '!')
    .join('');
}

// 113
// Transportation on vacation
function rentalCarCost(d) {
  if (d >= 7) {
    return d * 40 - 50;
  } else if (d >= 3) {
    return d * 40 - 20;
  } else {
    return d * 40;
  }
}

// 114
// L1: Set Alarm
function setAlarm(employed, vacation) {
  return employed && !vacation;
}

// 115
// The Feast of Many Beasts
function feast(beast, dish) {
  return (
    beast[0] === dish[0] && beast[beast.length - 1] === dish[dish.length - 1]
  );
}

// 116
// Double Char
function doubleChar(str) {
  return str
    .split('')
    .map((char) => char.repeat(2))
    .join('');
}

// 117
// Basic Mathematical Operations
const basicOp = (operation, value1, value2) => {
  if (operation === '+') {
    return value1 + value2;
  } else if (operation === '-') {
    return value1 - value2;
  } else if (operation === '*') {
    return value1 * value2;
  } else if (operation === '/') {
    return value1 / value2;
  }
};

// 118
// Beginner Series #2 Clock
function past(h, m, s) {
  const allSeconds = h * 3600 + m * 60 + s;
  return allSeconds * 1000;
}

// 119
// DNA to RNA Conversion
function DNAtoRNA(dna) {
  return dna.replace(/T/g, 'U');
}

// 120
// Removing Elements
function removeEveryOther(arr) {
  return arr.filter((el, idx) => {
    return idx % 2 === 0 ? el : null;
  });
}

// 121
// Thinkful - Logic Drills: Traffic light
function updateLight(current) {
  return current === 'yellow' ? 'red' : current === 'red' ? 'green' : 'yellow';
}

// 122
// Will there be enough space?
function enough(cap, on, wait) {
  return wait - (cap - on) < 0 ? 0 : wait - (cap - on);
}

// 123
// Beginner Series #4 Cockroach
function cockroachSpeed(s) {
  return Math.floor((s * 100000) / 3600);
}

// 124
// Get Planet Name By ID
function getPlanetName(id) {
  let name;
  switch (id) {
    case 1:
      name = 'Mercury';
      break;
    case 2:
      name = 'Venus';
      break;
    case 3:
      name = 'Earth';
      break;
    case 4:
      name = 'Mars';
      break;
    case 5:
      name = 'Jupiter';
      break;
    case 6:
      name = 'Saturn';
      break;
    case 7:
      name = 'Uranus';
    case 8:
      name = 'Neptune';
      break;
  }

  return name;
}

// 125
// Twice as old
function twiceAsOld(dadYearsOld, sonYearsOld) {
  return Math.abs(dadYearsOld - sonYearsOld * 2);
}

// 126
// Keep up the hoop
function hoopCount(n) {
  return n >= 10
    ? 'Great, now move on to tricks'
    : 'Keep at it until you get it';
}

// 127
// Correct the mistakes of the character recognition software
function correct(string) {
  let newString = string.replace(/5/g, 'S');
  newString = newString.replace(/0/g, 'O');
  newString = newString.replace(/1/g, 'I');
  return newString;
}

// 128
// Grasshopper - Check for factor
function checkForFactor(base, factor) {
  return base % factor === 0;
}

// 129
// Find numbers which are divisible by given number
function divisibleBy(numbers, divisor) {
  return numbers.filter((num) => num % divisor === 0);
}

// 130
// Parse nice int from char problem
function getAge(inputString) {
  return Number(inputString[0]);
}

// 131
// altERnaTIng cAsE <=> ALTerNAtiNG CaSe
String.prototype.toAlternatingCase = function () {
  const words = this.split(' ');
  return words
    .map((word) => {
      return word
        .split('')
        .map((char) => {
          return char === char.toUpperCase()
            ? char.toLowerCase()
            : char.toUpperCase();
        })
        .join('');
    })
    .join(' ');
};

// 132
// Switch it Up!
function switchItUp(number) {
  switch (number) {
    case 0:
      return 'Zero';
    case 1:
      return 'One';
    case 2:
      return 'Two';
    case 3:
      return 'Three';
    case 4:
      return 'Four';
    case 5:
      return 'Five';
    case 6:
      return 'Six';
    case 7:
      return 'Seven';
    case 8:
      return 'Eight';
    case 9:
      return 'Nine';
  }
}

// 133
// All Star Code Challenge #18
function strCount(str, letter) {
  let count = 0;
  str.split('').map((el) => {
    if (el === letter) count += 1;
  });
  return count;
}

// 134
// Welcome!
function greet(language) {
  const languages = {
    english: 'Welcome',
    czech: 'Vitejte',
    danish: 'Velkomst',
    dutch: 'Welkom',
    estonian: 'Tere tulemast',
    finnish: 'Tervetuloa',
    flemish: 'Welgekomen',
    french: 'Bienvenue',
    german: 'Willkommen',
    irish: 'Failte',
    italian: 'Benvenuto',
    latvian: 'Gaidits',
    lithuanian: 'Laukiamas',
    polish: 'Witamy',
    spanish: 'Bienvenido',
    swedish: 'Valkommen',
    welsh: 'Croeso',
  };

  return Object.keys(languages).includes(language)
    ? languages[language]
    : languages['english'];
}

// 135
// Volume of a Cuboid
class Kata {
  static getVolumeOfCuboid(length, width, height) {
    return length * height * width;
  }
}

// 136
// To square(root) or not to square(root)
function squareOrSquareRoot(array) {
  return array.map((num) =>
    Number.isInteger(Math.sqrt(num)) ? Math.sqrt(num) : num ** 2
  );
}

// 137
// I love you, a little , a lot, passionately ... not at all
function howMuchILoveYou(nbPetals) {
  const words = [
    'I love you',
    'a little',
    'a lot',
    'passionately',
    'madly',
    'not at all',
  ];
  return words[(nbPetals - 1) % words.length];
}

// 138
// Sort and Star
function twoSort(s) {
  return s.sort()[0].split('').join('***');
}

// 139
// Is it a palindrome?
function isPalindrome(x) {
  return x.toLowerCase() === x.toLowerCase().split('').reverse().join('');
}

// 140
// Sum The Strings
function sumStr(a, b) {
  return String(Number(a) + Number(b));
}

// 141
// Difference of Volumes of Cuboids
function findDifference(a, b) {
  return Math.abs(a.reduce((a, b) => a * b) - b.reduce((a, b) => a * b));
}

// 142
// Is it even?
function testEven(n) {
  return n % 2 === 0;
}

// 143
// Grasshopper - Messi goals function
function goals(laLigaGoals, copaDelReyGoals, championsLeagueGoals) {
  return laLigaGoals + copaDelReyGoals + championsLeagueGoals;
}

// 144
// Unfinished Loop - Bug Fixing #1
function createArray(number) {
  var newArray = [];

  for (var counter = 1; counter <= number; counter++) {
    newArray.push(counter);
  }

  return newArray;
}

// 145
// Filter out the geese
function gooseFilter(birds) {
  var geese = ['African', 'Roman Tufted', 'Toulouse', 'Pilgrim', 'Steinbacher'];
  return birds.filter((el) => !geese.includes(el));
}

// 146
// What is between?
function between(a, b) {
  const range = [];
  for (let i = a; i <= b; i++) {
    range.push(i);
  }

  return range;
}

// 147
// Well of Ideas - Easy Version
function well(x) {
  const count = x.filter((el) => el === 'good');
  if (count.length === 1 || count.length === 2) {
    return 'Publish!';
  } else if (count.length > 2) {
    return 'I smell a series!';
  } else {
    return 'Fail!';
  }
}

// 148
// N-th Power
function index(array, n) {
  return array[n] ? array[n] ** n : -1;
}

// 149
// My head is at the wrong end!
function fixTheMeerkat(arr) {
  return [arr[2], arr[1], arr[0]];
}

// 150
// Grasshopper - Terminal game move function
function move(position, roll) {
  return roll * 2 + position;
}

// 151
// Is the string uppercase?
String.prototype.isUpperCase = function () {
  return this.valueOf() === this.valueOf().toUpperCase();
};

// 152
// Grasshopper - If/else syntax debug
function checkAlive(health) {
  return health > 0;
}

// 153
// Grasshopper - Debug sayHello
function sayHello(name) {
  return `Hello, ${name}`;
}

// 154
// You're a square!
var isSquare = function (n) {
  return Number.isInteger(Math.sqrt(n));
};

// 155
// Isograms
function isIsogram(str) {
  const newStr = str.toLowerCase();
  return Array.from(new Set(newStr)).join('') === newStr;
}

// 156
// Beginner Series #3 Sum of Numbers
function getSum(...args) {
  let sum = 0;
  const sorted = args.sort((a, b) => a - b);
  if (sorted[0] === sorted[1]) {
    return sorted[0];
  } else {
    for (let i = sorted[0]; i <= sorted[1]; i++) {
      sum += i;
    }
  }

  return sum;
}

// 157
// The highest profit wins!
function minMax(arr) {
  return [Math.min(...arr), Math.max(...arr)];
}
