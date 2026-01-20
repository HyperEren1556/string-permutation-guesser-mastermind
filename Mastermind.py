import random
import math
import string
import bisect
import time
from collections import Counter
import itertools

# -------------------------------------------
# Generate a random string from a given charset
# If custom_charset is provided, use it
# Otherwise, use the first `nletter` letters of the alphabet
# -------------------------------------------
def generate_random_string(length, nletter=None, custom_charset=None):
    if custom_charset is not None:
        charset = custom_charset
    else:
        if nletter is None:
            raise ValueError("nletter must be provided when custom_charset is None")
        charset = string.ascii_uppercase[:nletter]

    return ''.join(random.choice(charset) for _ in range(length))

def generate_string_without_duplicates(nletter=10):
    charset = string.ascii_uppercase[:nletter]
    return random.shuffle(charset)

# -------------------------------------------
# Feedback function: counts exact matches in position
# -------------------------------------------
def get_feedback(secret, guess):
    secret = str(secret)
    guess = str(guess)
    correct_place = sum(s == g for s, g in zip(secret, guess))
    return correct_place



# Alias using list comprehension for clarity
def get_feedback_list(secret, guess):
    return sum(s == g for s, g in zip(secret, guess))


# -------------------------------------------
# Count number of unique permutations considering duplicate elements
# -------------------------------------------
def count_unique_permutations(data):
    n = len(data)
    denom = 1
    for c in Counter(data).values():
        denom *= math.factorial(c)
    return math.factorial(n) // denom


# -------------------------------------------
# Insert an item into a list in descending order of second value
# Special rule: if second value == 0, always insert at the beginning
# -------------------------------------------
def insert_custom(lst, item):
    # Generate keys for bisect: 0 → -inf to be always first, others negative for descending sort
    keys = [float('-inf') if v == 0 else -v for _, v in lst]
    k = float('-inf') if item[1] == 0 else -item[1]

    i = bisect.bisect_left(keys, k)
    lst.insert(i, item)
    return lst

def eliminate_possibilities(possibilities, guess, feedback):
    remaining_possibilities = []
    for num in possibilities:
        if get_feedback(num, guess) == feedback:
            remaining_possibilities.append(num)
    return remaining_possibilities

import random
import itertools

def guess_string(secret, charset, length, nletter, playing):
    """
    Guess a secret string composed of characters from `charset`.

    secret: str, the string to guess
    charset: iterable of characters to use
    length: int, length of the secret
    """
    # Generate all possible strings of given length from charset
    possibilities = [''.join(p) for p in itertools.product(charset, repeat=length)]
    attempts = 1

    while possibilities:
        # Random guess from remaining possibilities
        Player1_guess = random.choice(possibilities)
        Player2_feedback = get_feedback(secret, Player1_guess)

        print(f"Player1_guess: {Player1_guess} Player2_feedback: {Player2_feedback}")

        # Success check
        if Player2_feedback == length:
            print(f"I've guessed your string '{Player1_guess}' correctly in {attempts} attempts!")
            return True

        # Eliminate impossible candidates based on feedback
        possibilities = [p for p in possibilities if get_feedback(p, Player1_guess) == Player2_feedback]

        attempts += 1

    # Should not reach here if secret is in charset^length
    print("Failed to guess the secret.")
    return False


# -------------------------------------------
# Generate all unique permutations with backtracking and early pruning
# -------------------------------------------
def unique_permutations(iterable, parameters, secret, attempts):
    counter = Counter(iterable)  # Count available characters
    n = len(iterable)
    perm = [None] * n  # Current permutation being built

    # ---------------------------------------
    # Check if a partial permutation is valid
    # Early pruning: discard if it cannot possibly satisfy feedback constraints
    # ---------------------------------------
    def is_partial_valid(pos):
        for guess, expected in parameters:
            matches = sum(perm[i] == guess[i] for i in range(pos + 1))
            if matches > expected:
                return False
            if matches + (n - pos - 1) < expected:
                return False
        return True

    # ---------------------------------------
    # Recursive backtracking
    # ---------------------------------------
    def backtrack(pos):
        if pos == n:
            # Full permutation: check against all feedbacks
            for guess, expected in parameters:
                if guess == tuple(perm):
                    return False
                if get_feedback_list(guess, perm) != expected:
                    return False

            Player1_guess = ''.join(str(d) for d in perm)
            Player2_feedback = get_feedback(secret, Player1_guess)

            print(f"Player1_guess: {Player1_guess} Player2_feedback: {Player2_feedback}")
            insert_custom(parameters, [tuple(perm), Player2_feedback])

            if Player2_feedback == n:
                total_attempts = attempts + len(parameters)
                print(f"I've guessed your number {Player1_guess} correctly in {total_attempts} attempts!")
                return True

            return False

        # Try each available character
        for value in counter:
            if counter[value] > 0:
                perm[pos] = value
                counter[value] -= 1

                if is_partial_valid(pos):  # Early pruning
                    if backtrack(pos + 1):
                        return True

                counter[value] += 1  # Backtrack

        return False

    backtrack(0)


# -------------------------------------------
# Main logic to generate initial guesses, correct characters, and run permutation search
# -------------------------------------------
def Dump_code(secret, charset, length=10, nletter=10, playing=False):
    parameters = []
    attempts = 0
    correct_chars = []



    # Initial guesses to identify correct characters
    charset_list = list(charset)
    random.shuffle(charset_list)
    for c in charset_list:
        Player1_guess = c * length
        Player2_feedback = get_feedback(secret, Player1_guess)
        print(f"Player1_guess: {Player1_guess} Player2_feedback: {Player2_feedback}")
        correct_chars.extend([c] * Player2_feedback)
        attempts += 1
        if len(correct_chars) == length:
            break
        if len(correct_chars) < length and c == charset_list[-2]:
            correct_chars.extend([charset_list[-1]] * (length - len(correct_chars)))
            break
    print("Attempts:", attempts)
    print("Permutation candidates:", correct_chars)

        

    # Estimate number of permutations and processing time
    permutations_count = count_unique_permutations(correct_chars)
    print("Permutations to generate:", permutations_count)
    avg_time_per_permutation = 0.000001
    estimated_time = math.floor(permutations_count * avg_time_per_permutation)

    # Nicely format estimated time
    if estimated_time >= 31536000:
        print(f"Estimated time: {estimated_time // 31536000} years")
    elif estimated_time >= 86400:
        print(f"Estimated time: {estimated_time // 86400} days")
    elif estimated_time >= 3600:
        print(f"Estimated time: {estimated_time // 3600} hours")
    elif estimated_time >= 60:
        print(f"Estimated time: {estimated_time // 60} minutes")
    else:
        print(f"Estimated time: {estimated_time} seconds")

    Player1_guess = ''.join(str(d) for d in correct_chars)
    Player2_feedback = get_feedback(secret, Player1_guess)
    print(f"Player1_guess: {Player1_guess} Player2_feedback: {Player2_feedback}")
    parameters.append([correct_chars, Player2_feedback])

    # Run full backtracking search
    start = time.perf_counter()
    unique_permutations(correct_chars, parameters, secret, attempts)
    end = time.perf_counter()
    print(f"Execution time: {end - start:.6f} seconds")


# -------------------------------------------
# Interactive main program
# -------------------------------------------
def main():
    while True:
        # Ask if user wants to play
        while True:
            playing = input("Would you like to play? (y/n): ").strip().lower()
            if playing in ["yes", "y"]:
                playing = True
                break
            elif playing in ["no", "n"]:
                playing = False
                break
            print("Please enter 'yes' or 'no'.")

        # Ask for string length
        while True:
            try:
                length = int(input("How long do you want the string to be? "))
                if length >= 1:
                    break
            except ValueError:
                print("Value error: must enter an integer.")

        # Player-provided secret
        if playing:
            while True:
                secret = input(f"Type your secret ({length} characters): ").strip()
                if len(secret) == length:
                    nletter = len(secret)
                    # Determine charset
                    charset = "".join(dict.fromkeys(secret))  # Remove duplicates from secret
                    break
                print(f"Secret must be exactly {length} characters long.")

        # Random secret
        else:
            while True:
                try:
                    nletter = int(input("How many letters to use (1-26)? "))
                    # Determine charset
                    charset = string.ascii_uppercase[:nletter]
                    if 1 <= nletter <= 26:
                        break
                except ValueError:
                    print("Value error")
            while True:
                allow_duplicates = input("allow duplicates? (y/n): ").strip().lower()
                if allow_duplicates in ["yes", "y"]:
                    secret = generate_random_string(length, nletter)
                    break
                elif allow_duplicates in ["no", "n"]:
                    secret = generate_random_string(length, nletter)
                    break
                else:
                    print("Please enter 'yes' or 'no'.")

            
    


        print(f"(Secret generated: {secret})")  # Optional reveal
        if length > 7:
            Dump_code(secret, charset, length, nletter, playing)
        else:
            start = time.perf_counter()
            guess_string(secret, charset, length, nletter, playing)
            end = time.perf_counter()
            print(f"Execution time: {end - start:.6f} seconds")
        # Ask to play again
        while True:
            again = input("Do you want to play again? (y/n): ").strip().lower()
            if again in ["yes", "y"]:
                break
            elif again in ["no", "n"]:
                return
            else:
                print("Please enter 'yes' or 'no'.")


if __name__ == "__main__":
    main()
