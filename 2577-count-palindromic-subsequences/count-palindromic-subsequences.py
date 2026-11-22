class Solution:
    def memoisation(self, ind, selected, first, second, s, dp):
        if selected == 5:
            return 1

        if ind == len(s):
            return 0

        if dp[ind][selected][first][second] != -1:
            return dp[ind][selected][first][second]

        # Skip the current character.
        nottake = self.memoisation(
            ind + 1, selected, first, second, s, dp
        )

        digit = int(s[ind])
        take = 0

        if selected == 0:
            # Choose and remember the first digit.
            take = self.memoisation(
                ind + 1, 1, digit, second, s, dp
            )

        elif selected == 1:
            # Choose and remember the second digit.
            take = self.memoisation(
                ind + 1, 2, first, digit, s, dp
            )

        elif selected == 2:
            # Any digit can be the middle character.
            take = self.memoisation(
                ind + 1, 3, first, second, s, dp
            )

        elif selected == 3 and digit == second:
            # Fourth digit must match the second.
            take = self.memoisation(
                ind + 1, 4, first, second, s, dp
            )

        elif selected == 4 and digit == first:
            # Fifth digit must match the first.
            take = self.memoisation(
                ind + 1, 5, first, second, s, dp
            )

        dp[ind][selected][first][second] = (
            take + nottake
        ) % (10**9 + 7)

        return dp[ind][selected][first][second]

    def countPalindromes(self, s: str) -> int:
        n = len(s)

        if n < 5:
            return 0

        dp = [
            [
                [[-1] * 11 for _ in range(11)]
                for _ in range(5)
            ]
            for _ in range(n)
        ]

        # 10 means the digit has not been selected yet.
        return self.memoisation(0, 0, 10, 10, s, dp)