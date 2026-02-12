def determine_progress2(hits, spins):
    # Guard clause for division by zero
    if spins == 0:
        return "Get going!"
    
    # Default state
    progress = "Get going!"
    hits_spins_ratio = hits / spins

    if hits_spins_ratio > 0:
        progress = "On your way!"

    if hits_spins_ratio >= 0.25:
        progress = "Almost there!"

    # We use a logical 'and' to replace the nested if
    if hits_spins_ratio >= 0.5 and hits < spins:
        progress = "You win!"

    return progress