// quiz.js — handles the countdown timer, answer submission, and visual feedback
// This file only does anything on the quiz page (where TIME_LIMIT is defined).

// IR-03: tracks whether the player has already answered so we ignore extra clicks
let answered = false;

// IR-03: holds the setInterval reference so we can stop the timer after answering
let timerInterval = null;

// Only run the timer if we're on the quiz page
// (TIME_LIMIT is defined in a <script> block in quiz.html)
if (typeof TIME_LIMIT !== 'undefined') {
    startTimer(TIME_LIMIT);
}

// IR-03: counts down from `seconds` and auto-submits when it hits zero
function startTimer(seconds) {
    const timerEl = document.getElementById('timer');
    if (!timerEl) return;

    let remaining = seconds;

    // setInterval calls the function inside every 1000ms (1 second)
    timerInterval = setInterval(function () {
        remaining = remaining - 1;
        timerEl.textContent = remaining;

        // Change the timer color as time gets low so the player notices
        timerEl.className = 'timer';
        if (remaining <= 5)       timerEl.classList.add('danger');
        else if (remaining <= 10) timerEl.classList.add('warning');

        // Time ran out — submit a blank answer so the quiz can move on
        if (remaining <= 0) {
            clearInterval(timerInterval);
            if (!answered) {
                submitAnswer('');
            }
        }
    }, 1000);
}

// IR-07: called when the player clicks an answer button
function selectAnswer(key) {
    // Ignore clicks if we've already answered this question
    if (answered) return;
    answered = true;

    // Stop the countdown since the player answered in time
    clearInterval(timerInterval);

    // Put the chosen key into the hidden form field
    document.getElementById('answer-input').value = key;

    submitAnswer(key);
}

// Sends the answer to the server and waits for feedback
function submitAnswer(key) {
    // Disable all option buttons so the player can't change their answer
    document.querySelectorAll('.option-btn').forEach(function (btn) {
        btn.disabled = true;
    });

    // Build form data to POST — same as a regular HTML form submission
    var formData = new FormData();
    formData.set('answer', key);

    // FR-05: "Provide users with real-time feedback on their answer selections."
    // use fetch() to send the answer without reloading the page.
    // The server returns JSON telling us if the answer was right or wrong.
    fetch(QUIZ_URL, { method: 'POST', body: formData })
        .then(function (response) { return response.json(); })
        .then(function (data) { showFeedback(data); });
}

// IR-07: highlight the correct answer green, wrong choice red, show a message
function showFeedback(data) {
    var feedback = document.getElementById('feedback');
    feedback.classList.remove('hidden', 'correct-msg', 'wrong-msg');

    // Go through each button and colour it based on whether it was correct
    document.querySelectorAll('.option-btn').forEach(function (btn) {
        var key = btn.dataset.key;

        if (key === data.correct_key) {
            // Always highlight the right answer green
            btn.classList.add('correct');
        } else if (key === document.getElementById('answer-input').value && !data.is_correct) {
            // Highlight what the player picked in red if it was wrong
            btn.classList.add('wrong');
        }
    });

    // Show a text message below the options
    if (data.is_correct) {
        feedback.textContent = '✅ Correct!';
        feedback.classList.add('correct-msg');
    } else {
        // If answer is blank the timer ran out, otherwise they picked wrong
        var msg = (data.correct_key)
            ? '❌ Wrong. Correct: ' + data.correct_key.toUpperCase() + ') ' + data.correct_text
            : "⏱ Time's up!";
        feedback.textContent = msg;
        feedback.classList.add('wrong-msg');
    }

    // Wait 1.5 seconds so the player can read the feedback, then load next question
    setTimeout(function () {
        window.location.href = data.next_url;
    }, 1500);
}
