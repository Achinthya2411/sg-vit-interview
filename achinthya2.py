string = '([])]'
arr = []
for i in string:
  
    if i == '(':
      arr.append('(')
    elif i == ')':
      arr.pop()
    elif i == '[':
      arr.append('[')
    elif i == ']':
      arr.pop()
    elif i == '{':
      arr.append('{')
    elif i == '}':
      arr.pop()
if len(arr)==0:
  print('balanced')
else:
  print('Not balanced')
