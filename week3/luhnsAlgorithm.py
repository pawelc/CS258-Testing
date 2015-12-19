# concise definition of the Luhn checksum:
#
# "For a card with an even number of digits, double every odd numbered
# digit and subtract 9 if the product is greater than 9. Add up all
# the even digits as well as the doubled-odd digits, and the result
# must be a multiple of 10 or it's not a valid card. If the card has
# an odd number of digits, perform the same addition doubling the even
# numbered digits instead."
#
# for more details see here:
# http://www.merriampark.com/anatomycc.htm
#
# also see the Wikipedia entry, but don't do that unless you really
# want the answer, since it contains working Python code!
# 
# Implement the Luhn Checksum algorithm as described above.

# is_luhn_valid takes a credit card number as input and verifies 
# whether it is valid or not. If it is valid, it returns True, 
# otherwise it returns False.
def is_luhn_valid(n):
    n=str(n)
    if len(n) % 2 == 0:
        nums = [ int(n[i])*2 if not i%2 else int(n[i]) for i in range(len(n))]
        nums = map(lambda e: e-9 if e > 9 else e,nums)
    else:
        nums = [ int(n[i])*2 if i%2 else int(n[i]) for i in range(len(n))]
        nums = map(lambda e: e-9 if e > 9 else e,nums)
        
    print nums
        
    return True if not sum(nums)%10 else False

print is_luhn_valid(12568)


