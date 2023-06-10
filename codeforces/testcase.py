import re
print(int(input()) - len(re.sub(r'(.)\1+', r'\1', input())))