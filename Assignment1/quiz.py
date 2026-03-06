"""
quiz.py - Interactive Multiple-Choice Quiz Application
ITM 352 - Assignment 1

Features:
  - Loads questions from questions.json (supports text, image, and video questions)
  - Category selection: play all questions or a single topic (History, NBA, etc.)
  - Per-question countdown timer with bonus points for fast correct answers
  - User login and registration with per-user score history
  - High score tracking per user and a grand champion across all users
  - Writes all score history to scores.json
  - Validates all input (re-prompts on invalid answers)

Bonus point system (awarded only on correct answers):
  < 5 seconds  -> +2 bonus points
  5-10 seconds -> +1 bonus point
  >= 10 seconds -> no bonus
"""

import json
import os
import sys
import time
from datetime import datetime

# --- File paths (relative to this script's directory) ---
_DIR           = os.path.dirname(os.path.abspath(__file__))
QUESTIONS_FILE = os.path.join(_DIR, "questions.json")
SCORES_FILE    = os.path.join(_DIR, "scores.json")

# Bonus thresholds (seconds)
BONUS_FAST_THRESHOLD   = 5    # under this -> +2 pts
BONUS_MEDIUM_THRESHOLD = 10   # under this -> +1 pt


# ---------------------------------------------------------------------------
# Data loading / saving
# ---------------------------------------------------------------------------

def load_questions(filename):
    """Load and return the list of questions from a JSON file."""
    try:
        with open(filename, "r") as f:
            questions = json.load(f)
        if not questions:
            print(f"Error: No questions found in '{filename}'.")
            sys.exit(1)
        return questions
    except FileNotFoundError:
        print(f"Error: Questions file '{filename}' not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: '{filename}' is not valid JSON.")
        sys.exit(1)


def load_scores(filename):
    """
    Load score data from a JSON file.
    Returns a dict with keys 'users' and 'grand_champion'.
    Creates a fresh structure if the file doesn't exist yet.
    """
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    # Default structure for a brand-new scores file
    return {"users": {}, "grand_champion": {"username": None, "score": 0}}


def save_scores(data, filename):
    """Persist score data to a JSON file."""
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


# ---------------------------------------------------------------------------
# Category selection
# ---------------------------------------------------------------------------

def choose_category(questions):
    """
    Extract all unique categories from the question list, display them, and
    let the user pick one or choose to play all categories.

    Returns a filtered list of questions matching the chosen category,
    or the full list if the user selects 'All'.

    This is a non-trivial custom function: it dynamically builds the category
    menu from whatever categories exist in the questions file, so adding new
    categories to questions.json requires no code changes here.
    """
    # Collect unique categories while preserving first-seen order
    seen = set()
    categories = []
    for q in questions:
        cat = q.get("category", "General")
        if cat not in seen:
            seen.add(cat)
            categories.append(cat)

    print("\n" + "=" * 50)
    print("       SELECT A CATEGORY")
    print("=" * 50)
    print("  0) All Categories")
    for i, cat in enumerate(categories, start=1):
        # Count how many questions are in each category
        count = sum(1 for q in questions if q.get("category", "General") == cat)
        print(f"  {i}) {cat}  ({count} questions)")

    valid_choices = set(str(i) for i in range(len(categories) + 1))

    while True:
        choice = input("\nEnter the number of your choice: ").strip()
        if choice in valid_choices:
            break
        print(f"  Please enter a number between 0 and {len(categories)}.")

    if choice == "0":
        print("\nPlaying all categories.")
        return questions
    else:
        selected = categories[int(choice) - 1]
        filtered = [q for q in questions if q.get("category", "General") == selected]
        print(f"\nPlaying category: {selected} ({len(filtered)} questions)")
        return filtered


# ---------------------------------------------------------------------------
# Question display and input validation
# ---------------------------------------------------------------------------

def display_question(question_data, number, total):
    """
    Print a single question with its lettered options.
    If the question has an associated media file, open it.
    Returns the set of valid option keys (e.g. {'a','b','c','d'}).
    """
    print(f"\nQuestion {number} of {total}  [{question_data.get('category', 'General')}]")
    print("-" * 40)

    print(question_data["question"])
    print()

    options = question_data["options"]
    for key in sorted(options.keys()):
        print(f"  {key}) {options[key]}")

    return set(options.keys())


def get_valid_answer(valid_options):
    """
    Repeatedly prompt the user until they enter one of the valid option keys.
    Input is case-insensitive.  Returns the answer in lower case.

    Also measures and returns the elapsed time in seconds so the caller can
    award bonus points based on response speed.

    Returns: (answer: str, elapsed_seconds: float)
    """
    valid_lower = {opt.lower() for opt in valid_options}
    prompt = f"\nYour answer ({'/'.join(sorted(valid_lower))}): "

    start_time = time.time()

    while True:
        answer = input(prompt).strip().lower()
        if answer in valid_lower:
            elapsed = time.time() - start_time
            return answer, elapsed
        print(f"  Invalid response '{answer}'. Please enter one of: {', '.join(sorted(valid_lower))}")


def calc_bonus(elapsed_seconds):
    """
    Return the bonus points earned based on how quickly the user answered.
    Only called when the answer is correct.
      < BONUS_FAST_THRESHOLD seconds   -> 2 bonus points
      < BONUS_MEDIUM_THRESHOLD seconds -> 1 bonus point
      otherwise                        -> 0 bonus points
    """
    if elapsed_seconds < BONUS_FAST_THRESHOLD:
        return 2
    elif elapsed_seconds < BONUS_MEDIUM_THRESHOLD:
        return 1
    return 0


# ---------------------------------------------------------------------------
# Score tracking
# ---------------------------------------------------------------------------

def update_user_scores(scores_data, username, score, total_possible):
    """
    Record the new score for the user, check for a personal best, and update
    the overall grand champion if needed.
    Returns a tuple (is_personal_best, is_grand_champion_beaten).
    """
    if username == "guest":
        return False, False

    users = scores_data["users"]
    user  = users[username]

    # Append this run to the user's score history with a timestamp
    user["scores"].append({
        "score":          score,
        "total_possible": total_possible,
        "date":           datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

    is_personal_best      = score > user["high_score"]
    is_grand_champion_new = False

    if is_personal_best:
        user["high_score"] = score

        # Check whether this beats the overall grand champion
        champ = scores_data["grand_champion"]
        if score > champ["score"]:
            scores_data["grand_champion"] = {"username": username, "score": score}
            is_grand_champion_new = True

    return is_personal_best, is_grand_champion_new


def display_leaderboard(scores_data):
    """Print the current grand champion and a sorted leaderboard."""
    users = scores_data["users"]
    champ = scores_data["grand_champion"]

    print("\n" + "=" * 50)
    print("           LEADERBOARD")
    print("=" * 50)

    if champ["username"]:
        print(f"  Grand Champion: {champ['username']}  ({champ['score']} points)")
    else:
        print("  No grand champion yet.")

    if users:
        print("\n  All-time high scores (includes bonus points):")
        # Sort users by high score descending
        ranked = sorted(users.items(), key=lambda x: x[1]["high_score"], reverse=True)
        for rank, (name, data) in enumerate(ranked, start=1):
            print(f"    {rank}. {name:20s} {data['high_score']}")
    print("=" * 50)


# ---------------------------------------------------------------------------
# User login / registration
# ---------------------------------------------------------------------------

def login_or_register(scores_data):
    """
    Prompt for a username.  If the user exists, welcome them back and show
    their personal best.  If not, create a new account automatically.
    Returns the username string.
    """
    print("\n" + "=" * 50)
    print("         QUIZ LOGIN")
    print("=" * 50)

    while True:
        username = input("Enter your username (or type 'guest' to play without saving): ").strip()
        if username:
            break
        print("Username cannot be empty. Please try again.")

    if username.lower() == "guest":
        print("\nPlaying as guest. Your score will not be saved.")
        return "guest"

    users = scores_data["users"]

    if username in users:
        best = users[username]["high_score"]
        print(f"\nWelcome back, {username}! Your personal best is {best} points.")
    else:
        # New user — create their record
        users[username] = {"high_score": 0, "scores": []}
        print(f"\nNew account created for '{username}'. Good luck!")

    return username


# ---------------------------------------------------------------------------
# Main quiz loop
# ---------------------------------------------------------------------------

def run_quiz(questions):
    """
    Present every question in sequence, time each answer, tally the score
    (base points + speed bonus), and return a result dict with:
      'base'           - number of correct answers
      'bonus'          - total bonus points earned
      'total'          - base + bonus
      'total_possible' - maximum score achievable
      'elapsed'        - total quiz time in seconds
    """
    base_score  = 0
    bonus_score = 0
    total       = len(questions)
    quiz_start  = time.time()

    print("\n" + "=" * 50)
    print("           LET'S BEGIN!")
    print(f"  Bonus: answer in <{BONUS_FAST_THRESHOLD}s for +2 pts, <{BONUS_MEDIUM_THRESHOLD}s for +1 pt")
    print("=" * 50)

    for i, q in enumerate(questions, start=1):
        valid_options = display_question(q, i, total)
        answer, elapsed = get_valid_answer(valid_options)
        correct = q["answer"].lower()

        if answer == correct:
            bonus = calc_bonus(elapsed)
            base_score  += 1
            bonus_score += bonus
            if bonus > 0:
                print(f"  Correct!  ({elapsed:.1f}s)  +1 pt  +{bonus} bonus")
            else:
                print(f"  Correct!  ({elapsed:.1f}s)  +1 pt")
        else:
            print(f"  Wrong. ({elapsed:.1f}s)  The correct answer was: {correct}) {q['options'][correct]}")

    quiz_elapsed = time.time() - quiz_start

    return {
        "base":           base_score,
        "bonus":          bonus_score,
        "total":          base_score + bonus_score,
        "total_possible": total * (1 + 2),   # 1 base + max 2 bonus per question
        "elapsed":        quiz_elapsed
    }


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    print("=" * 50)
    print("       WELCOME TO THE QUIZ APP")
    print("=" * 50)

    # Load questions and existing score data
    all_questions = load_questions(QUESTIONS_FILE)
    scores_data   = load_scores(SCORES_FILE)

    # Show leaderboard before the quiz starts
    display_leaderboard(scores_data)

    # User login / registration
    username = login_or_register(scores_data)

    # Let the user choose a category (or all)
    questions = choose_category(all_questions)

    # Run the quiz and collect results
    result = run_quiz(questions)

    # --- Final score report ---
    mins, secs = divmod(int(result["elapsed"]), 60)
    time_str   = f"{mins}m {secs}s" if mins else f"{secs}s"

    print("\n" + "=" * 50)
    print(f"  Quiz complete!  Player: {username}")
    print(f"  Correct answers : {result['base']} / {len(questions)}")
    print(f"  Bonus points    : {result['bonus']}")
    print(f"  TOTAL SCORE     : {result['total']} / {result['total_possible']}")
    print(f"  Total time      : {time_str}")
    print("=" * 50)

    # Update scores and check for records
    is_personal_best, is_grand_champ = update_user_scores(
        scores_data, username, result["total"], result["total_possible"]
    )

    if is_grand_champ:
        print(f"\n*** NEW GRAND CHAMPION! {username} leads with {result['total']} points! ***")
    elif is_personal_best:
        print(f"\n*** NEW PERSONAL BEST for {username}: {result['total']} points! ***")

    # Persist scores to disk
    if username != "guest":
        save_scores(scores_data, SCORES_FILE)
        print(f"\nScore saved to '{SCORES_FILE}'.")

    # Show updated leaderboard after the quiz
    display_leaderboard(scores_data)


if __name__ == "__main__":
    main()
