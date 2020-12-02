# Question: https://adventofcode.com/2020/day/1
# Find the two entries that sum to 2020 and then multiply those two numbers together.
#
# For example, suppose your expense report contained the following:
#
# 1721
# 979
# 366
# 299
# 675
# 1456
# In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

def get_inputs(filepath):
    """

    Args:
        filepath (string): path to file containing input strings

    Returns:
        inputs (list): all inputs saved as ints.

    """
    with open(filepath, 'r') as file:
        inputs = [int(input) for input in file.readlines()]
    return inputs



def save_output(answer):
    """

    Args:
        answer (int): Ad

    Returns:

    """
    print("Multiplied answer is: ", answer)
    with open('output.txt', 'w') as file:
        file.write(str(answer))
    print("Saved to file")




def find_2020_values(inputs):
    """
    O(n^2)
    Args:
        inputs (list): Integer inputs

    Returns:
        Value1 (int): The first value to sum for 2020
        Value2 (int): The second value to sum for 2020

    """
    for value1 in inputs:
        for value2 in inputs:
            if (value1 + value2) == 2020:
                return value1, value2
    raise



if __name__ =="__main__":
    # 1. Get inputs
    inputs = get_inputs('input.txt')

    # 2. Compare values to find two values which add for 2020
    value1, value2 = find_2020_values(inputs)
    print("Value1: ", value1)
    print("Value2: ", value2)

    # 3. Write out multiplied number
    multiplied_value = value1 * value2
    save_output(multiplied_value)
