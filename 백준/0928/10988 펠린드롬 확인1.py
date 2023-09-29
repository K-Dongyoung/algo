string = list(input())
L = len(string)
mid = L//2
if L%2:
    if string[:mid] == list(reversed(string[mid+1:])):
        print(1)
    else:
        print(0)
else:
    if string[:mid] == list(reversed(string[mid:])):
        print(1)
    else:
        print(0)