def palindrome(word):
    word = str(word)  # Ensure input is a string
    return word == word[::-1]  # Compare with its reverse

while True:
    text = input("Give word: ")

    if text.lower() == "leave":  # Check before calling the function
        break

    if palindrome(text):
        print("Yes, a palindrome!")
    else:
        print("Not a palindrome")
