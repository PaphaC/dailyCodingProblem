# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
import unittest

# Original solution, for a o(n^2) answer
def adds_up_n_2(number_list, k):
    for i in range(0,len(number_list)):
        if k-number_list[i] in number_list:
            return True
    return False

# Second solution, for a o(n) anwser
def adds_up_n(number_list, k):
    # Create a tab with k values [False, False, ...k]
    seen = [False] * (k + 1)
    for number in number_list:
        # In case k is equal to 17, and number to 7
        # Magic Number is 7
        magic_number = k - number

        # Then we try to see if we already met the magic number, if so, seen[number] becomes true
        # and we return true
        if seen[number]:
            return True

        # We mark the 7th element of the array as True, for the previous line
        seen[magic_number] = True

    # If nothing match
    return False

class Test(unittest.TestCase):

    def test(self):
        liste = [10, 15, 3, 7]
        k = 17
        j = 21

        result = adds_up_n_2(liste, k)
        self.assertTrue(result)

        result = adds_up_n_2(liste, j)
        self.assertFalse(result)

        result = adds_up_n(liste, k)
        self.assertTrue(result)

        result = adds_up_n(liste, j)
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()