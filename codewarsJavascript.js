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
function solution(str, ending){
    return str.endsWith(ending);
}


// 4
// Who likes it?
function likes(names) {
    let message;
    if (names.length > 3) {
      message = `${names[0]}, ${names[1]} and ${names.length - 2} others like this`;
    } else if (names.length > 2) {
      message = `${names[0]}, ${names[1]} and ${names[2]} like this`;
    } else if (names.length > 1) {
      message = `${names[0]} and ${names[1]} like this`;
    } else if (names.length > 0) {
      message = `${names[0]} likes this`;
    } else {
      message = "no one likes this";
    }
    
    return message;
}


// 5
// Unique In Order
var uniqueInOrder=function(iterable){
    let others = [];
    let uniqueLetters = [];
    for (let letter of iterable) {
      letter === uniqueLetters[uniqueLetters.length -1] ? others.push(letter) : uniqueLetters.push(letter);
    }
    
    return uniqueLetters;
}


// 6
// Highest and Lowest
function highAndLow(numbers){
    let newNumbers = numbers.split(' ');
    let maxMin = [];
    
    for (let num of newNumbers) {
      maxMin.push(Number(num))
    }
    
    return `${Math.max(...maxMin)} ${Math.min(...maxMin)}`
}


// 7
// Is a number prime?
function isPrime(num) {
    for (let i = 2; i <= Math.sqrt(num); i++) {
      if (num % i === 0) {
        return false;
      }
    }
    
    return num > 1
}


// 8
// Powers of 2
function powersOfTwo(n){
    const powers = [];
    for (let i = 0; i <= n; i++) {
      console.log(i)
      powers.push(2 ** i)
    }
    return powers
}


// 9
// Vowel Count
function getCount(str) {
    var vowelsCount = 0;
    
    for (let char of str) {
      if (char === 'a' || char === 'e' || char === 'i' || char === 'o' || char === 'u') {
        vowelsCount += 1;
      }
    }
    
    return vowelsCount;
}


// 10
// List Filtering
function filter_list(l) {
    return l.filter(el => {
      return (Number.isInteger(el))
    })
}


// 11
// Responsible Drinking
function hydrate(s) {
  const drinks = s.split(' ');
  const drinkAmount = drinks.filter(el => {
    return !isNaN(el);
  })
  
  const water = drinkAmount.reduce((prev, current) => {
    return Number(prev) + Number(current);
  })
  
  if (water > 1) {
    return `${water} glasses of water`
  } else if (water.length === 1) {
    return `${water} glass of water`
  }
}


// 12
// Battle of the characters (Easy)
function battle(x, y) {
  const alpha = String.fromCharCode(...Array(123).keys()).slice(97).toUpperCase().split('');
  let xCount = {name: x, power: 0};
  let yCount = {name: y, power: 0};
  
  for (let char of x) {
    xCount.power += alpha.indexOf(char) + 1
  }
  
  for (let char of y) {
    yCount.power += alpha.indexOf(char) + 1
  }
  
  if (xCount.power > yCount.power) {
    return xCount.name
  } else if (xCount.power === yCount.power) {
    return 'Tie!'
  } else {
    return yCount.name;
  }
}


// 13
// Dot Calculator
function dotCalculator (equation) {
  const parts = equation.split(' ');
  const operator = parts[1];
  if (operator === '+') {
    return parts[0] + parts[2];
  } else if (operator === '-') {
    const diff = parts[0].length - parts[2].length
    return '.'.repeat(diff)
  } else if (operator === '*') {
    const diff = parts[0].length * parts[2].length
    return '.'.repeat(diff)
  } else if (operator === '//') {
    const diff = Math.trunc(parts[0].length / parts[2].length)
    return '.'.repeat(diff)
  }
}


// 14
// CamelCase Method
String.prototype.camelCase=function(value){
  const words = this.split(' ').filter(el => el !== '');
  const title = words.map(el => {
    const temp = el[0].toUpperCase() + el.slice(1);
    return temp;
  })
  return title.join('');
}


// 15
// Find the missing letter
function findMissingLetter(array) {
  const newArr = array.map(el => el.toLowerCase())
  const alphabet = 'abcdefghijklmnopqrstuvwxyz'.split('');
  const startCheck = alphabet.indexOf(newArr[0]);
  const endCheck = alphabet.indexOf(newArr[newArr.length-1]);
  const checkArea = alphabet.slice(startCheck, endCheck + 1);
  
  const missingLetter = checkArea.filter(el => {
    if (!newArr.includes(el)) {
      return el;
    }
  })
  
  if (array[0] === newArr[0]) {
    return missingLetter.join('')
  } else {
    return missingLetter.join('').toUpperCase()
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
  const longWords = sentence.split(' ').filter(el => {
    return el.length > n;
  })
  
  return longWords;
}
