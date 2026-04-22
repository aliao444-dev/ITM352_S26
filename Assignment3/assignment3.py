# assignment3.py - Flask Quiz Web Application
# ITM 352 - Assignment 3
# Converts the Assignment 1 console quiz into an interactive web app using Flask.
#
# ── REQUIRED Individual Requirements ──────────────────────────────────────────
#   IR-01  Persistent User ID & History  →  / route (login, welcome back, scores)
#   IR-02  Leaderboard                   →  /results route + results.html
#
# ── EXTRA CREDIT Individual Requirements ──────────────────────────────────────
#   IR-03  Timer (30s per question)      →  quiz.html + quiz.js
#   IR-07  Visual Feedback (green/red)   →  quiz.js showFeedback() + style.css
#   IR-08  Progress Bar                  →  quiz.html progress bar div
#
# ── Functional Requirements (search "FR-XX" to jump to each one) ─────────────
#
#   FR-01  UI Design
#          REQUIREMENT: "Design a clean and intuitive UI with HTML, CSS, and
#                        JavaScript (as needed)."
#          → templates/ + static/style.css
#
#   FR-02  Dynamic Elements
#          REQUIREMENT: "Create dynamic elements that respond to user actions,
#                        including question display, answer options, and
#                        submission feedback."
#          → quiz.js, quiz.html
#
#   FR-03  Load Questions from JSON
#          REQUIREMENT: "Load questions dynamically from a JSON file containing
#                        all questions and answer options (i.e. not 'hard-coded'
#                        into the page or program)."
#          → load_questions()
#
#   FR-04  Randomize Questions & Options
#          REQUIREMENT: "Randomize both question order and answer options for
#                        each session to ensure variety."
#          → random.shuffle() + shuffle_options()
#
#   FR-05  Real-time Feedback
#          REQUIREMENT: "Provide users with real-time feedback on their answer
#                        selections."
#          → quiz.js showFeedback()
#
#   FR-06  Score Tracking
#          REQUIREMENT: "Implement score tracking that updates based on
#                        correct/incorrect answers."
#          → session['score'] in /quiz route
#
#   FR-07  JSON Data Storage
#          REQUIREMENT: "Store questions, answer choices, and user score data in
#                        JSON format or a simple data file. Use server-side
#                        Python code to handle data storage and retrieval."
#          → scores.json, load_scores(), save_scores()
#
#   FR-08  Flask Backend
#          REQUIREMENT: "Use a framework like Flask to serve the web application."
#          → all routes below
#
#   FR-09  RESTful APIs
#          REQUIREMENT: "Implement RESTful APIs for retrieving questions and
#                        storing user scores."
#          → /api/questions and /api/scores
#
#   FR-10  Final Score & Feedback
#          REQUIREMENT: "Calculate and display the user's final score upon quiz
#                        completion. Show detailed feedback, such as the number
#                        of correct/incorrect answers, time taken, and areas for
#                        improvement."
#          → /results route + results.html
#
#   FR-11  Input Validation
#          REQUIREMENT: "Ensure input validation for text fields, login, and
#                        registration. Display user-friendly error messages when
#                        validation fails or data loading issues occur."
#          → / route username check, session guards

import json
import os
import random
from datetime import datetime
from flask import Flask, render_template, request, session, redirect, url_for, jsonify

# Create the Flask app — this is the main object that runs the web server
app = Flask(__name__)

# The secret key lets Flask encrypt the session cookie so users can't tamper with it
app.secret_key = 'itm352-quiz-secret-key'

# Build file paths based on where this script lives, so it works on any computer
_DIR           = os.path.dirname(os.path.abspath(__file__))
QUESTIONS_FILE = os.path.join(_DIR, 'questions.json')
SCORES_FILE    = os.path.join(_DIR, 'scores.json')

# IR-03: how many seconds the player gets to answer each question
QUESTION_TIME_LIMIT = 30


# ── Helper functions ──────────────────────────────────────────────────────────

# FR-03: "Load questions dynamically from a JSON file containing all questions
#          and answer options (i.e. not 'hard-coded' into the page or program)."
# questions live in a separate JSON file so we can add/edit them without
# touching the Python code
def load_questions():
    with open(QUESTIONS_FILE, 'r') as f:
        return json.load(f)


# FR-07: "Store questions, answer choices, and user score data in JSON format or
#          a simple data file. Use server-side Python code to handle data storage
#          and retrieval."
# scores are stored in a JSON file so they persist between server restarts.
# If the file doesn't exist yet (first run), return a blank starting structure.
def load_scores():
    if os.path.exists(SCORES_FILE):
        with open(SCORES_FILE, 'r') as f:
            return json.load(f)
    return {'users': {}, 'leaderboard': []}


def save_scores(data):
    with open(SCORES_FILE, 'w') as f:
        json.dump(data, f, indent=4)


# FR-04: "Randomize both question order and answer options for each session to
#          ensure variety."
# convert the options dict {a: '...', b: '...'} into a shuffled list so
# the answer choices appear in a different order every time
def shuffle_options(question):
    opts = [{'key': k, 'text': v} for k, v in question['options'].items()]
    random.shuffle(opts)
    return opts


# ── Routes ────────────────────────────────────────────────────────────────────

# FR-08, FR-11, IR-01
@app.route('/', methods=['GET', 'POST'])
def index():
    # FR-11: "Ensure input validation for text fields, login, and registration.
    #          Display user-friendly error messages when validation fails or data
    #          loading issues occur."
    # if the user already has a session open, skip the login screen
    if 'username' in session:
        return redirect(url_for('quiz'))

    if request.method == 'POST':
        username = request.form.get('username', '').strip()

        # FR-11: don't let someone log in with a blank name (input validation)
        if not username:
            return render_template('index.html', error='Please enter a username.')

        scores_data = load_scores()
        users       = scores_data['users']

        # IR-01: check if this player has visited before
        if username not in users:
            # New player — create a blank record for them
            users[username] = {'high_score': 0, 'history': []}
            save_scores(scores_data)
            session['returning'] = False
        else:
            session['returning'] = True

        # Store the username in the session so all other pages know who is playing
        session['username'] = username
        return redirect(url_for('quiz'))

    return render_template('index.html')


# FR-02, FR-05, FR-06, FR-08, IR-03, IR-07, IR-08
@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    # FR-11: only allow logged-in players
    if 'username' not in session:
        return redirect(url_for('index'))

    # If this is the very first question of a new game, set up the quiz state
    if 'questions' not in session:
        questions = load_questions()
        random.shuffle(questions)  # FR-04: randomize question order every game
        session['questions']  = questions
        session['current']    = 0          # index of the current question
        session['score']      = 0
        session['results']    = []
        session['quiz_start'] = datetime.now().isoformat()

    questions = session['questions']
    current   = session['current']
    total     = len(questions)

    # All questions done — show the results page
    if current >= total:
        return redirect(url_for('results'))

    question = questions[current]
    options  = shuffle_options(question)   # FR-04: shuffle answer options too

    if request.method == 'POST':
        chosen_key  = request.form.get('answer', '').lower()
        correct_key = question['answer'].lower()
        is_correct  = (chosen_key == correct_key)

        # FR-06: "Implement score tracking that updates based on correct/incorrect answers."
        # add 1 to score only when the answer is right
        if is_correct:
            session['score'] = session['score'] + 1

        # Move to the next question
        session['current'] = current + 1

        # FR-05: "Provide users with real-time feedback on their answer selections."
        # return JSON so JavaScript can show green/red feedback before loading the next question
        return jsonify({
            'is_correct':   is_correct,
            'correct_key':  correct_key,
            'correct_text': question['options'][correct_key],
            'next_url':     url_for('quiz'),
        })

    # IR-08: pass current/total so the template can calculate progress bar width
    # IR-03: pass time_limit so JavaScript knows how long the countdown should be
    return render_template('quiz.html',
                           question=question,
                           options=options,
                           current=current + 1,
                           total=total,
                           score=session['score'],
                           username=session['username'],
                           time_limit=QUESTION_TIME_LIMIT)


# FR-10, IR-02
@app.route('/results')
def results():
    # FR-11: make sure there's actually a finished quiz in the session
    if 'score' not in session:
        return redirect(url_for('index'))

    score    = session['score']
    total    = len(session['questions'])
    username = session['username']

    # FR-10: "Calculate and display the user's final score upon quiz completion.
    #          Show detailed feedback, such as the number of correct/incorrect
    #          answers, time taken, and areas for improvement."
    # calculate how long the quiz took so we can show it on the results page
    start   = datetime.fromisoformat(session['quiz_start'])
    elapsed = int((datetime.now() - start).total_seconds())
    mins, secs = divmod(elapsed, 60)
    time_str = f"{mins}m {secs}s" if mins else f"{secs}s"

    # FR-07: "Store questions, answer choices, and user score data in JSON format."
    # save this score to the user's history in scores.json
    scores_data = load_scores()
    user = scores_data['users'].setdefault(username, {'high_score': 0, 'history': []})
    user['history'].append({
        'score': score,
        'total': total,
        'time':  time_str,
        'date':  datetime.now().strftime('%Y-%m-%d %H:%M'),
    })
    if score > user['high_score']:
        user['high_score'] = score

    # IR-02: add this score to the leaderboard and keep only the top 10
    leaderboard = scores_data.get('leaderboard', [])
    leaderboard.append({'username': username, 'score': score, 'total': total})
    leaderboard.sort(key=lambda x: x['score'], reverse=True)
    scores_data['leaderboard'] = leaderboard[:10]

    save_scores(scores_data)

    # IR-01: pull the user's history to show on the results page
    history = user['history']

    # Clear quiz state but keep username so the player can play again
    for key in ['questions', 'current', 'score', 'results', 'quiz_start']:
        session.pop(key, None)

    return render_template('results.html',
                           username=username,
                           score=score,
                           total=total,
                           time_str=time_str,
                           history=history[-5:],
                           leaderboard=scores_data['leaderboard'])


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


# ── FR-09: REST API endpoints ──────────────────────────────────────────────────
# FR-09: "Implement RESTful APIs for retrieving questions and storing user scores."
# These return raw JSON data — useful for testing or connecting a mobile app

@app.route('/api/questions')
def api_questions():
    # Returns the full list of quiz questions as JSON
    return jsonify(load_questions())


@app.route('/api/scores')
def api_scores():
    # Returns the current leaderboard as JSON
    return jsonify(load_scores().get('leaderboard', []))


# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == '__main__':
    # debug=True means Flask will show detailed error pages and auto-reload
    # when you save changes — turn this off before putting the app online
    app.run(debug=True)
