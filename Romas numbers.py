# Roman numbers
'''
Symbol    Value
I           1
V           5
X           10
L           50
C           100
D           500
M           1000

ex: 2 = II, 27=XXVII, 4 = IV (V-I=4)
ex: LVIII = 58
ex: MCMXCIV = 1994  --> M = 1000, CM = M-C=900, XC = C-X=90 IV = V-I= 4

I can be placed before V(5) and X(10) to make 4 and 9
X can be placed before L(50) abd C(100) to make 40 and 90


'''

class Solution:
    def romanToInt(self, s):   #lets s = MCMXCIV
        numeral_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        result = 0
        for i in range(len(s)):
            if i > 0 and numeral_map[s[i]] > numeral_map[s[i-1]]:
                result += numeral_map[s[i]] -2* numeral_map[s[i-1]]     # MC = M + C = result, New_result+= M-2C = M + C + M - 2C = M + (M - C)
            else:
                result += numeral_map[s[i]]    # first result = M = 1000, second result = MC = 1000 + 100 = 1100, third result = MC = M - 2C = 1000-200 = 800, then new_result = 1100+800=1900

        return