import re


str_user = '225424272163254474441338664823'
pattern = "([2,4,6,8][1,3,5,7,9])"
matches = re.sub(pattern,"",str_user)

print(matches)