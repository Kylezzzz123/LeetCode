# Given a 32-bit signed integer, reverse digits of an integer
# ex: Input  123
#     Output 321

# ex: Inut   -123
#     Output -321

# ex: Input   120
#     output  21
# note: range [-2^31 to 2^31 - 1]     exclude 0

# -214783648   to 214783647


class Solution:
    def reverse(x):                  # let's set x = 123
        num = 0
        a = abs(x)
        while (a != 0):
            temp = a % 10            #123%10 = 3
            num = num * 10 + temp    # 3--> 30+2 = 32  -> 320+1 = 321
            a = int(a/10)            # remove the last digit : 123 --> 12 
        
        if x > 0 and num < 214783547:
            return num

        elif x < 0 and num <= 214783547:
            return -num 
        else:
            return 0

'''
x = int(input("Number: "))
num = 0
a = abs(x)
while (a != 0):
    temp = a % 10            #123 % 10 = 3
    num = num * 10 + temp    # 3--> 30+2 = 32  -> 320+1 = 321
    a = int(a/10)
    if x > 0 and num < 214783547:
        print(num)

    elif x < 0 and num <= 214783547:
        print(-num)

    else:
        print(0)
        
'''



'''
123

temp =123 % 10 =3
num = 0*10+3 = 3
a = 123/10 = 12

temp = 12%10 = 2
num = 3*10 + 2 = 32
a = 12/10 =1



temp = 1%10 = 1
num = 32*10 +1 = 320
a = 1/10 = 0


'''
