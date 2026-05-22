def longest_palindromic_substring(s):
    """
    Given a string s, return the longest palindromic substring.
    """

    n = len(s)

    # If the string is empty or only one character,
    # it is already a palindrome
    if n < 2:
        return s

    start = 0
    max_len = 1

    # Helper function
    def expand_around_center(left, right):

        # Keep expanding while characters match
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1

        # Return palindrome length
        return right - left - 1

    # Loop through every character
    for i in range(n):

        # Odd length palindrome
        len1 = expand_around_center(i, i)

        # Even length palindrome
        len2 = expand_around_center(i, i + 1)

        # Get larger palindrome
        current_max = max(len1, len2)

        # Update longest palindrome if needed
        if current_max > max_len:
            max_len = current_max
            start = i - (max_len - 1) // 2

    return s[start:start + max_len]