# Filter out scores that do not meet the minimum threshold
scores = [60, 45, 30, 85, 10, 90]

# Iterate in reverse order to safely remove items while looping
for score in reversed(scores):
    if score < 50:
        scores.remove(score)

print(scores)