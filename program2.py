class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 
            'C': 100, 'D': 500, 'M': 1000
        }
        
        # Initialize the integer result
        total = 0
        
        # Traverse through the string, checking each symbol and the next one
        for i in range(len(s)):
            # If the current value is less than the next one, subtract it from the total (for cases like IV, IX, etc.)
            if i < len(s) - 1 and roman_map[s[i]] < roman_map[s[i + 1]]:
                total -= roman_map[s[i]]
            else:
                # Otherwise, just add it to the total
                total += roman_map[s[i]]
        
        return total



