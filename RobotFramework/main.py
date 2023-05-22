def are_anagrams(str1, str2):
    # Remove whitespace and convert strings to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if lengths are different
    if len(str1) != len(str2):
        return False

    # Convert strings to lists and sort them
    str1_sorted = sorted(list(str1))
    str2_sorted = sorted(list(str2))

    # Compare sorted strings
    if str1_sorted == str2_sorted:
        return True
    else:
        return False

# Test the function
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if are_anagrams(string1, string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
