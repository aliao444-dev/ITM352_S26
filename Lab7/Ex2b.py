evens = [2]

num = 2
while (evens[-1] < 50):
    num += 2
    evens.append(num)

print(evens)

    # -1 tells it to go to the last element of the list
    # doesn't work if the list is empty, so we start with 2 in the list and then add evens to it until we reach 50
    # changing num to 4 allows us to start with the next even number after 2, which is 4, and then we keep adding 2 to get the next even numbers until we reach 50.
# print(evens)

