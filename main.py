array = [4, 5, 6, 1, 2, 23, 9]
target = 25
length = len(array)

for i in range(length - 1):
    for j in range(i + 1, length):  # Start j from i + 1
        if array[i] + array[j] == target:
            print(f"index {i} and index {j}")
