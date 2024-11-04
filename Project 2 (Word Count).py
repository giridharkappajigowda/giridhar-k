# Word Counter Program

# Function to count the number of words in a given text
def count_words(text):
    """
    This function takes a string as input and returns the number of words in the string.

    Parameters:
    text (str): The input string

    Returns:
    int: The number of words in the string
    """
    # Split the text into words
    words = text.split()

    # Return the number of words
    return len(words)


# Main program
def main():
    # Prompt the user to enter a sentence or paragraph
    text = input("Please enter a sentence or paragraph: ")

    # Check if the input is empty
    if text.strip() == "":
        print("Error: Input is empty.")
    else:
        # Count the number of words in the input
        word_count = count_words(text)

        # Print the word count to the console
        print("Word count:", word_count)


# Run the main program
if __name__ == "__main__":
    main()