## Problem Statement
One day, Jamie noticed that many English words only use the letters A and B. Examples of such words include "AB" (short for abdominal), "BAA" (the noise a sheep makes), "AA" (a type of lava), and "ABBA" (a Swedish pop sensation).
Inspired by this observation, Jamie created a simple game. You are given two s: initial and target. The goal of the game is to find a sequence of valid moves that will change initial into target. There are two types of valid moves:
- Add the letter A to the end of the string.
- Add the letter B to the end of the string and then reverse the entire string. (After the reversal the newly-added B becomes the first character of the string).

Return "Possible" (quotes for clarity) if there is a sequence of valid moves that will change initial into target. Otherwise, return "Impossible".

### Definition
Attribute | Value
--- | ---
Class | ABBADiv1
Method | canObtain
Parameters | string, string
Returns | string
Method signature | def canObtain(self, initial, target):

### Limits
Attribute | Value
--- | ---
Time limit (s) | 2.000
Memory limit (MB) | 256
### Constraints
- The length of initial will be between 1 and 49, inclusive.
- The length of target will be between 2 and 50, inclusive.
- target will be longer than initial.
- Each character in initial and each character in target will be either 'A' or 'B'.
### Examples
#### 0.
    "A"
    "BABA"
Returns: "Possible"

Jamie can perform the following moves:
* Initially, the string is "A".
* Jamie adds a 'B' to the end of the string and then reverses the string. Now the string is "BA".
* Jamie adds a 'B' to the end of the string and then reverses the string. Now the string is "BAB".
* Jamie adds an 'A' to the end of the string. Now the string is "BABA".
* Since there is a sequence of moves which starts with "A" and creates the string "BABA", the answer is "Possible".


#### 1.
    "BAAAAABAA"
    "BAABAAAAAB"
Returns: "Possible"

Jamie can add a 'B' to the end of the string and then reverse the string.

#### 2.
    "A"
    "ABBA"
Returns: "Impossible"

#### 3.
    "AAABBAABB"
    "BAABAAABAABAABBBAAAAAABBAABBBBBBBABB"
Returns: "Possible"

#### 4.
    "AAABAAABB"
    "BAABAAABAABAABBBAAAAAABBAABBBBBBBABB"
Returns: "Impossible"
