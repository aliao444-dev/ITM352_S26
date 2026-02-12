def determine_progress_branchless(hits, spins):
    if spins == 0:
        return "Get going!"

    messages = [
        "Get going!",      # Index 0: No thresholds met
        "On your way!",    # Index 1: Ratio > 0
        "Almost there!",   # Index 2: Ratio >= 0.25
        "You win!"         # Index 3: Ratio >= 0.5 AND hits < spins
    ]

    ratio = hits / spins

    # Each True condition adds 1 to the index
    # We "stack" them to move further down the list
    index = (
        (ratio > 0) + 
        (ratio >= 0.25) + 
        (ratio >= 0.5 and hits < spins)
    )

    return messages[index]