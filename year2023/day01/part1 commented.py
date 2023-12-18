def get_first_number_in_str(the_string: str) -> str:
    """
    Notion: Ascii table
    Here, we can check if a character is between two other thanks to their positions on the Ascii table. Google this.
    You should see 0 at the 30 position and 9 at the 39 position.
    We check if the letter we are looking at is between this two positions.

    You could do it in oneline if you wanted :
    return [letter in letter for the_string if "0" <= letter <= "9"][0]
    This is a list comprehension, a way of doing a for loop with conditions and all in a single line.
    It returns a list, so we have to put [0] after it to say that we want the first element it finds.

    //!\\ The double comparison (x < y < z) is not in all programming languages
    """
    for letter in the_string:
        if "0" <= letter <= "9":
            return letter


def get_sum_of_first_and_last_number_of_each_line(code: str) -> int:
    # The split allows us to work line by line rather than with the big data chunk.
    lines = code.split("\n")
    result = 0
    for line in lines:
        current = ""
        # a_list[::-1] returns the list but reversed. We use this to get the first and last number in the string.
        current += get_first_number_in_str(line) + get_first_number_in_str(line[::-1])
        if current:
            result += int(current)
    return result
