# fun_hub_20.py
# Python Fun Hub 2.0 — 20 Console Games/Utilities
# Copy this whole file, save as fun_hub_20.py, then run: python fun_hub_20.py

import random
import string
import time
import datetime
import sys

# ---------------- Utility Helpers ----------------
def safe_int(prompt, min_val=None, max_val=None):
    while True:
        s = input(prompt).strip()
        if s.lower() in ('q','quit','exit'):
            return None
        try:
            v = int(s)
            if (min_val is not None and v < min_val) or (max_val is not None and v > max_val):
                print(f"Enter a number between {min_val} and {max_val}.")
                continue
            return v
        except:
            print("Please enter a valid integer or type 'q' to cancel.")

def press_enter():
    input("\nPress Enter to return to menu...")

# ---------------- 1. Guess the Number ----------------
def guess_the_number():
    print("\n--- Guess the Number ---")
    low, high = 1, 100
    secret = random.randint(low, high)
    attempts = 0
    while True:
        v = safe_int(f"Guess a number ({low}-{high}) or 'q' to quit: ", low, high)
        if v is None:
            print("Exiting Guess the Number.")
            break
        attempts += 1
        if v < secret:
            print("Too low.")
        elif v > secret:
            print("Too high.")
        else:
            print(f"Correct! You guessed it in {attempts} attempts.")
            break
    press_enter()

# ---------------- 2. Rock Paper Scissors ----------------
def rock_paper_scissors():
    print("\n--- Rock Paper Scissors ---")
    choices = ['rock','paper','scissors']
    while True:
        user = input("Enter rock/paper/scissors (or 'q' to quit): ").strip().lower()
        if user in ('q','quit','exit'): break
        if user not in choices:
            print("Invalid. Try again.")
            continue
        comp = random.choice(choices)
        print("Computer chose:", comp)
        if user == comp:
            print("Draw.")
        elif (user=='rock' and comp=='scissors') or (user=='paper' and comp=='rock') or (user=='scissors' and comp=='paper'):
            print("You win!")
        else:
            print("Computer wins!")
    press_enter()

# ---------------- 3. Tic Tac Toe (2-player) ----------------
def tic_tac_toe():
    print("\n--- Tic Tac Toe (2-player) ---")
    board = [' ']*9
    def show():
        print("\n", board[0],'|',board[1],'|',board[2])
        print("-----------")
        print(board[3],'|',board[4],'|',board[5])
        print("-----------")
        print(board[6],'|',board[7],'|',board[8],"\n")
    def check_winner(b):
        wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
        for a,b,c in wins:
            if b[a]==b[b]==b[c] and b[a] != ' ':
                return b[a]
        return None
    turn = 'X'
    moves = 0
    while True:
        show()
        pos = safe_int(f"Player {turn} - choose cell 1-9 or 'q' to quit: ",1,9)
        if pos is None: break
        idx = pos-1
        if board[idx] != ' ':
            print("Cell taken. Choose another.")
            continue
        board[idx] = turn
        moves += 1
        # check
        wins = [
            (0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)
        ]
        winner = None
        for a,b,c in wins:
            if board[a]==board[b]==board[c] and board[a] != ' ':
                winner = board[a]
                break
        if winner:
            show()
            print(f"Player {winner} wins! 🎉")
            break
        if moves == 9:
            show()
            print("It's a draw.")
            break
        turn = 'O' if turn == 'X' else 'X'
    press_enter()

# ---------------- 4. Dice Roll Simulator ----------------
def dice_roll():
    print("\n--- Dice Roll Simulator ---")
    while True:
        n = safe_int("How many dice to roll (1-10) or 'q' to quit: ",1,10)
        if n is None: break
        rolls = [random.randint(1,6) for _ in range(n)]
        print("Rolls:", rolls, "Sum =", sum(rolls))
    press_enter()

# ---------------- 5. Coin Toss ----------------
def coin_toss():
    print("\n--- Coin Toss ---")
    while True:
        t = input("Type 'toss' to flip or 'q' to quit: ").strip().lower()
        if t in ('q','quit','exit'): break
        if t != 'toss':
            print("Type 'toss' to flip.")
            continue
        res = random.choice(['Heads','Tails'])
        print("Result:", res)
    press_enter()

# ---------------- 6. Quiz Game (MCQ) ----------------
def quiz_game():
    print("\n--- Quiz Game (MCQ) ---")
    questions = [
        ("What is the capital of India?", ["Mumbai","New Delhi","Kolkata","Chennai"], 2),
        ("Which language is this program written in?", ["Java","C++","Python","Ruby"], 3),
        ("2 + 3 * 4 = ?", ["20","14","10","24"], 2)
    ]
    score = 0
    for i,(q,opts,ans) in enumerate(questions,1):
        print(f"\nQ{i}: {q}")
        for idx,opt in enumerate(opts,1):
            print(f" {idx}. {opt}")
        choice = safe_int("Your answer (1-4) or 'q' to quit: ",1,len(opts))
        if choice is None: break
        if choice == ans:
            print("Correct!")
            score += 1
        else:
            print("Wrong. Correct:", opts[ans-1])
    print(f"\nYour score: {score}/{len(questions)}")
    press_enter()

# ---------------- 7. Math Quiz (random ops) ----------------
def math_quiz():
    print("\n--- Math Quiz ---")
    ops = ['+','-','*']
    score = 0
    rounds = safe_int("How many questions? (1-20) or 'q' to quit: ",1,20)
    if rounds is None:
        press_enter(); return
    for i in range(rounds):
        a = random.randint(1,20)
        b = random.randint(1,20)
        op = random.choice(ops)
        if op == '+': ans = a + b
        elif op == '-': ans = a - b
        else: ans = a * b
        user = safe_int(f"Q{i+1}: {a} {op} {b} = ")
        if user is None:
            print("Quiz cancelled.")
            break
        if user == ans:
            print("Correct.")
            score += 1
        else:
            print("Wrong. Answer:", ans)
    print(f"Score: {score}/{rounds}")
    press_enter()

# ---------------- 8. Hangman ----------------
def hangman():
    print("\n--- Hangman (Word Guess) ---")
    words = ["PYTHON","HANGMAN","COMPUTER","PROGRAM","ALGORITHM","VARIABLE","FUNCTION"]
    secret = random.choice(words)
    display = ['_'] * len(secret)
    wrongs = set()
    tries = 6
    while True:
        print("\nWord:", ' '.join(display))
        print("Wrong guesses:", ' '.join(sorted(wrongs)), f"({len(wrongs)}/{tries})")
        if '_' not in display:
            print("You won! The word was", secret)
            break
        if len(wrongs) >= tries:
            print("You lost. The word was", secret)
            break
        ch = input("Enter a letter or 'q' to quit: ").strip().upper()
        if ch in ('Q','QUIT','EXIT'): break
        if len(ch) != 1 or not ch.isalpha():
            print("Enter a single letter.")
            continue
        if ch in wrongs or ch in display:
            print("Already guessed.")
            continue
        if ch in secret:
            for i,c in enumerate(secret):
                if c == ch: display[i] = ch
            print("Good guess!")
        else:
            wrongs.add(ch)
            print("Wrong guess.")
    press_enter()

# ---------------- 9. Number Guess Race (user vs computer) ----------------
def number_guess_race():
    print("\n--- Number Guess Race (You vs Computer) ---")
    secret = random.randint(1,50)
    user_attempts = 0
    comp_attempts = 0
    comp_low, comp_high = 1, 50
    while True:
        # user's turn
        v = safe_int("Your guess 1-50 or 'q' to quit: ",1,50)
        if v is None:
            print("You quit.")
            break
        user_attempts += 1
        if v == secret:
            print(f"You found it in {user_attempts} attempts! You win!")
            break
        elif v < secret:
            print("Too low.")
        else:
            print("Too high.")
        # computer's turn (binary-ish)
        comp_guess = random.randint(comp_low, comp_high)
        comp_attempts += 1
        print(f"Computer guesses: {comp_guess}")
        if comp_guess == secret:
            print(f"Computer found it in {comp_attempts} attempts! Computer wins.")
            break
        elif comp_guess < secret:
            comp_low = max(comp_low, comp_guess+1)
            print("Computer guessed too low.")
        else:
            comp_high = min(comp_high, comp_guess-1)
            print("Computer guessed too high.")
    press_enter()

# ---------------- 10. Memory Game (number sequence repeat) ----------------
def memory_game():
    print("\n--- Memory Game ---")
    level = safe_int("How many numbers to remember (3-10)? ",3,10)
    if level is None:
        press_enter(); return
    sequence = [random.randint(0,9) for _ in range(level)]
    print("Memorize this sequence:")
    print(' '.join(str(x) for x in sequence))
    time.sleep(max(2, level))  # show for some seconds
    print("\n" * 50)
    ans = input("Enter the sequence separated by spaces: ").strip().split()
    try:
        ans = [int(x) for x in ans]
    except:
        print("Invalid input.")
        press_enter(); return
    if ans == sequence:
        print("Correct! Well done.")
    else:
        print("Wrong. Correct sequence was:", ' '.join(str(x) for x in sequence))
    press_enter()

# ---------------- 11. Password Generator ----------------
def password_generator():
    print("\n--- Password Generator ---")
    length = safe_int("Enter desired length (6-32): ",6,32)
    if length is None:
        press_enter(); return
    chars = string.ascii_letters + string.digits + string.punctuation
    pwd = ''.join(random.choice(chars) for _ in range(length))
    print("Generated password:", pwd)
    press_enter()

# ---------------- 12. Calculator ----------------
def calculator():
    print("\n--- Calculator ---")
    while True:
        a = input("Enter expression (e.g. 2+3*4) or 'q' to quit: ").strip()
        if a.lower() in ('q','quit','exit'): break
        try:
            # safe-ish eval: restrict builtins
            result = eval(a, {"__builtins__": None}, {})
            print("Result:", result)
        except Exception as e:
            print("Error:", e)
    press_enter()

# ---------------- 13. Age Calculator ----------------
def age_calculator():
    print("\n--- Age Calculator ---")
    print("Enter your birth date.")
    y = safe_int("Year (e.g. 2005) or 'q' to quit: ")
    if y is None: press_enter(); return
    m = safe_int("Month (1-12): ",1,12)
    if m is None: press_enter(); return
    d = safe_int("Day (1-31): ",1,31)
    if d is None: press_enter(); return
    try:
        dob = datetime.date(y,m,d)
        today = datetime.date.today()
        age_years = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        print(f"You are {age_years} years old.")
    except Exception as e:
        print("Invalid date:", e)
    press_enter()

# ---------------- 14. Random Joke Generator ----------------
def joke_generator():
    print("\n--- Random Joke Generator ---")
    jokes = [
        "Why did the programmer quit his job? Because he didn't get arrays.",
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "What do you call 8 hobbits? A hobbyte.",
        "Why was the JavaScript developer sad? Because he didn't Node how to Express himself."
    ]
    while True:
        cmd = input("Type 'joke' for a joke or 'q' to quit: ").strip().lower()
        if cmd in ('q','quit','exit'): break
        if cmd == 'joke':
            print(random.choice(jokes))
        else:
            print("Type 'joke' or 'q'.")
    press_enter()

# ---------------- 15. Random Name Picker ----------------
def name_picker():
    print("\n--- Random Name Picker ---")
    print("Enter names separated by commas (or type 'q' to cancel).")
    s = input("Names: ").strip()
    if s.lower() in ('q','quit','exit') or not s:
        press_enter(); return
    names = [n.strip() for n in s.split(',') if n.strip()]
    if not names:
        print("No valid names.")
        press_enter(); return
    print("Picked:", random.choice(names))
    press_enter()

# ---------------- 16. Color Guess Game (text) ----------------
def color_guess():
    print("\n--- Color Guess Game ---")
    colors = ['red','blue','green','yellow','purple','orange','black','white']
    secret = random.choice(colors)
    attempts = 3
    while attempts > 0:
        guess = input(f"Guess the color ({attempts} attempts left) or 'q' to quit: ").strip().lower()
        if guess in ('q','quit','exit'): break
        if guess == secret:
            print("Correct!")
            break
        else:
            print("Nope.")
            attempts -= 1
    else:
        print("Out of attempts. The color was", secret)
    press_enter()

# ---------------- 17. Typing Speed Test ----------------
def typing_test():
    print("\n--- Typing Speed Test ---")
    sentence = "The quick brown fox jumps over the lazy dog."
    print("Type the following sentence exactly and press Enter:\n")
    print(sentence)
    input("Ready? Press Enter to start...")
    start = time.time()
    typed = input()
    end = time.time()
    time_taken = end - start
    correct = typed.strip() == sentence
    words = len(sentence.split())
    wpm = round((words / time_taken)*60,2) if time_taken>0 else 0
    print(f"\nTime: {time_taken:.2f}s  WPM: {wpm}")
    print("Exact match:" , "Yes" if correct else "No")
    press_enter()

# ---------------- 18. Dice Guess Game ----------------
def dice_guess():
    print("\n--- Dice Guess Game ---")
    while True:
        guess = safe_int("Guess the dice roll (1-6) or 'q' to quit: ",1,6)
        if guess is None: break
        roll = random.randint(1,6)
        print("Rolled:", roll)
        if guess == roll:
            print("You guessed it!")
        else:
            print("Wrong guess.")
    press_enter()

# ---------------- 19. Slot Machine (text) ----------------
def slot_machine():
    print("\n--- Slot Machine ---")
    symbols = ['7','BAR','🍒','★','$']
    while True:
        cmd = input("Type 'spin' to play or 'q' to quit: ").strip().lower()
        if cmd in ('q','quit','exit'): break
        if cmd != 'spin':
            print("Type 'spin' or 'q'."); continue
        r = [random.choice(symbols) for _ in range(3)]
        print(" | ".join(r))
        if r[0]==r[1]==r[2]:
            print("Jackpot! 🎉")
        elif r[0]==r[1] or r[1]==r[2] or r[0]==r[2]:
            print("Nice! You matched two.")
        else:
            print("No match. Try again.")
    press_enter()

# ---------------- 20. Simple To-Do List (in-memory) ----------------
def todo_list():
    print("\n--- To-Do List ---")
    todos = []
    while True:
        print("\n1. Add task\n2. View tasks\n3. Remove task\n4. Clear tasks\n5. Back to main menu")
        c = input("Choice: ").strip()
        if c == '1':
            t = input("Enter task (or blank to cancel): ").strip()
            if t: todos.append(t); print("Added.")
        elif c == '2':
            if not todos: print("No tasks.")
            else:
                print("Tasks:")
                for i,t in enumerate(todos,1): print(i, t)
        elif c == '3':
            if not todos:
                print("No tasks.")
            else:
                idx = safe_int("Enter task number to remove: ",1,len(todos))
                if idx is not None:
                    removed = todos.pop(idx-1)
                    print("Removed:", removed)
        elif c == '4':
            todos.clear(); print("Cleared.")
        elif c == '5' or c.lower() in ('q','quit','exit'):
            break
        else:
            print("Invalid choice.")
    press_enter()

# ---------------- Main Menu ----------------
def main():
    MENU = {
        '1': ("Guess the Number", guess_the_number),
        '2': ("Rock Paper Scissors", rock_paper_scissors),
        '3': ("Tic Tac Toe (2-player)", tic_tac_toe),
        '4': ("Dice Roll Simulator", dice_roll),
        '5': ("Coin Toss", coin_toss),
        '6': ("Quiz Game (MCQ)", quiz_game),
        '7': ("Math Quiz", math_quiz),
        '8': ("Hangman", hangman),
        '9': ("Number Guess Race (You vs Computer)", number_guess_race),
        '10':("Memory Game", memory_game),
        '11':("Password Generator", password_generator),
        '12':("Calculator", calculator),
        '13':("Age Calculator", age_calculator),
        '14':("Random Joke Generator", joke_generator),
        '15':("Random Name Picker", name_picker),
        '16':("Color Guess Game", color_guess),
        '17':("Typing Speed Test", typing_test),
        '18':("Dice Guess Game", dice_guess),
        '19':("Slot Machine", slot_machine),
        '20':("To-Do List", todo_list),
        '0':("Exit", None)
    }

    while True:
        print("\n" + "="*36)
        print("   🎮 PYTHON FUN HUB 2.0 — 20 GAMES & TOOLS")
        print("="*36)
        for k in sorted(MENU, key=lambda x: (int(x) if x.isdigit() else x)):
            if k == '0':
                print(f"  {k}. Exit")
            else:
                print(f"  {k}. {MENU[k][0]}")
        choice = input("\nEnter choice number (e.g. 1) and Enter: ").strip()
        if choice == '0' or choice.lower() in ('q','quit','exit'):
            print("Thanks for using Python Fun Hub — Goodbye!")
            break
        action = MENU.get(choice)
        if action:
            func = action[1]
            try:
                func()
            except KeyboardInterrupt:
                print("\nInterrupted. Returning to menu.")
            except Exception as e:
                print("An error occurred:", e)
                press_enter()
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting. Bye!")
        sys.exit(0)
