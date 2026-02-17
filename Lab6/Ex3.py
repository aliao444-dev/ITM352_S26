def test_determine_progress(progress_function):
    # Test case 1: spins = 0 (Immediate return)
    assert progress_function(0, 0) == "Get going!", "Test case 1 failed"
    
    # Test case 2: hits_spins_ratio is 0 (hits = 0)
    assert progress_function(0, 10) == "Get going!", "Test case 2 failed"
    
    # Test case 3: 0 < ratio < 0.25
    assert progress_function(1, 10) == "On your way!", "Test case 3 failed"
    
    # Test case 4: 0.25 <= ratio < 0.5
    assert progress_function(3, 10) == "Almost there!", "Test case 4 failed"
    
    # Test case 5: ratio >= 0.5 AND hits < spins
    assert progress_function(6, 10) == "You win!", "Test case 5 failed"
    
    # Test case 6: hits >= spins (Edge case for ratio >= 0.5 where "You win!" should NOT trigger)
    # Based on the code, if hits == spins, it stays "Almost there!"
    assert progress_function(10, 10) == "Almost there!", "Test case 6 failed"

    print("All tests passed!")

# Usage:
# test_determine_progress(determine_progress1)