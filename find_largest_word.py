
def find_larg():
    sentence = input("Enter sentence: ")


    longest = max(sentence.split(), key=len)

    # Displaying longest word
    print("Longest word is: ", longest)
    print("And its length is: ", len(longest))


find_larg()
