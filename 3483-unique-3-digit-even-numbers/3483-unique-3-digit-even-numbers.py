class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        numbers = set()

        freq = {}
        for digit in digits:
            freq[digit] = freq.get(digit, 0) + 1

        for digit1 in digits:
            if digit1 == 0:
                continue

            curr_freq = freq.copy()
            curr_freq[digit1] -= 1

            for digit2 in digits:
                if curr_freq.get(digit2, 0) < 1:
                    continue

                curr_freq2 = curr_freq.copy()
                curr_freq2[digit2] -= 1

                for digit3 in digits:
                    if curr_freq2.get(digit3, 0) < 1:
                        continue
                    if digit3 % 2 != 0:
                        continue

                    num = digit1 * 100 + digit2 * 10 + digit3
                    numbers.add(num)

        return len(numbers)
