# Iterate through 1 to 10, skipping 5 and stopping at 8
for x in range(1, 11):
    # Check if the number is 8 to terminate the loop
    if x == 8:
        print("done!")
        break
    
    # Check if the number is 5 to skip printing
    if x == 5:
        continue
        
    print(x)