# Given an array of integers, return a new array such that each element at index i of the new array is the product of
# all the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was
# [3, 2, 1], the expected output would be [2, 3, 6].

import unittest


# Solution using division
def generate_product_array_division(array):
    generated_array = []
    total_value_array = array[0]

    # First, we generate the product of all value of the array
    for i in range(0, len(array)):
        if array[i] == 0:
            total_value_array = total_value_array
        else:
            total_value_array = total_value_array * array[i]

    # Then we generate the new array by dividing by array[i]
    for i in range(0, len(array)):
        generated_array.append(total_value_array / array[i])

    return generated_array


# Solution without division
def generate_array_without_division(array):
    generated_array = []
    temp_value = 1
    for i in range(0, len(array)):
        for j in range(0, len(array)):
            if i == j:
                temp_value = temp_value
            else:
                temp_value = temp_value * array[j]
        generated_array.append(temp_value)
        temp_value = 1

    return generated_array

# Tests
class Test(unittest.TestCase):

    def test(self):
        liste = [1, 2, 3, 4, 5]
        expected_list = [120, 60, 40, 30, 24]

        result = generate_product_array_division(liste)
        self.assertEqual(result, expected_list)

        result = generate_array_without_division(liste)
        self.assertEqual(result, expected_list)

if __name__ == "__main__":
    unittest.main()
