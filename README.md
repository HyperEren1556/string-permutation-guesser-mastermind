````markdown
# String Permutation Guesser

A Python program that tries to guess a secret string using a combination of random initial guesses and backtracking with constraint pruning.  

It supports both **player-provided secrets** and **automatically generated random strings**, and provides feedback on each guess similar to Mastermind-style games.

---

## Features

- Generate random strings from a subset of the alphabet or a custom charset.
- Interactive mode where the user provides a secret.
- Calculates exact character matches in each guess.
- Uses backtracking with early pruning to efficiently generate valid permutations.
- Orders guesses intelligently based on feedback using a custom insertion function.
- Estimates the number of permutations and expected computation time.
- Fully interactive loop for multiple rounds of play.

---

## Requirements

- Python 3.7+
- Standard libraries only: `random`, `math`, `string`, `bisect`, `time`, `collections`

No additional packages are required.

---

## Installation

Clone this repository:

```bash
git clone https://github.com/yourusername/string-permutation-guesser.git
cd string-permutation-guesser
````

Run the program:

```bash
python main.py
```

---

## Usage

When you run the program:

1. You will be asked if you want to play interactively (`y`) or let the computer generate a secret (`n`).
2. Input the length of the secret string.
3. If playing interactively, type your secret string of the specified length.
4. If generating randomly, input how many letters from the alphabet (A-Z) to use.
5. The program will make initial guesses to identify correct characters.
6. It will then generate permutations and attempt to guess the secret using feedback.
7. The program prints each guess, feedback, total attempts, and execution time.
8. Optionally, you can play again in a loop.

---

### Example

```
Would you like to play? (y/n): n
How long do you want the string to be? 14
How many letters to use (1-26)? 13
(Secret generated: DMMFKLGCGMDJBD)
ABCDEFGHIJKLM
Player1_guess: IIIIIIIIIIIIII Player2_feedback: 0
Player1_guess: BBBBBBBBBBBBBB Player2_feedback: 1
Player1_guess: DDDDDDDDDDDDDD Player2_feedback: 3
Player1_guess: KKKKKKKKKKKKKK Player2_feedback: 1
Player1_guess: GGGGGGGGGGGGGG Player2_feedback: 2
Player1_guess: CCCCCCCCCCCCCC Player2_feedback: 1
Player1_guess: JJJJJJJJJJJJJJ Player2_feedback: 1
Player1_guess: HHHHHHHHHHHHHH Player2_feedback: 0
Player1_guess: MMMMMMMMMMMMMM Player2_feedback: 3
Player1_guess: FFFFFFFFFFFFFF Player2_feedback: 1
Player1_guess: EEEEEEEEEEEEEE Player2_feedback: 0
Player1_guess: LLLLLLLLLLLLLL Player2_feedback: 1
Attempts: 12
Permutation candidates: ['B', 'D', 'D', 'D', 'K', 'G', 'G', 'C', 'J', 'M', 'M', 'M', 'F', 'L']
Permutations to generate: 1210809600
Estimated time: xxxxxx
Player1_guess: BDDDKGGCJMMMFL Player2_feedback: 4
Player1_guess: BDDDGKCGMJFLMM Player2_feedback: 0
Player1_guess: DBKGDDGJCMMMLF Player2_feedback: 3
Player1_guess: DBKCMGMMJDDGFL Player2_feedback: 2
Player1_guess: DKBJFMDCDGMMGL Player2_feedback: 2
Player1_guess: DGGMKBJDLMCMFD Player2_feedback: 4
Player1_guess: DGMBKCFLJMMDDG Player2_feedback: 4
Player1_guess: DJMMBGGCKMLFDD Player2_feedback: 6
Player1_guess: DMCMKGGBFLMJDD Player2_feedback: 6
Player1_guess: DMJMKGGFDMLDBC Player2_feedback: 6
Player1_guess: DMMFKGGDBCLMDJ Player2_feedback: 6
Player1_guess: DMMFKLGCGMDJBD Player2_feedback: 14
I've guessed your number DMMFKLGCGMDJBD correctly in 24 attempts!
Execution time: 26.411342 seconds
Do you want to play again? (y/n):
```

---

## Functions

* `generate_random_string(length, nletter=None, custom_charset=None)`: Generate a random string from a charset.
* `get_feedback(secret, guess)`: Count exact matches between secret and guess.
* `count_unique_permutations(data)`: Compute number of unique permutations considering duplicates.
* `insert_custom(lst, item)`: Insert a guess into a list sorted by feedback, with custom rules.
* `unique_permutations(iterable, parameters, secret, attempts)`: Backtracking generator to produce valid permutations efficiently.
* `Dump_code(secret, length, nletter, playing=False)`: Main driver for initial guesses and permutation search.
* `main()`: Interactive CLI loop.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Author

* [HyperEren1556] - Original implementation

---

### Notes

* The program is designed for small to moderate string lengths. For very long strings, the number of permutations grows factorially, and computation may become infeasible.
* The feedback system is exact-match based (like Mastermind), not partial matches.

```
