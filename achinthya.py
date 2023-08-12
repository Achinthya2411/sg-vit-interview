arr = []
test1 = 1
test2=1
for i in range(len(arr)-1):
  if arr[i]!=arr[i+1]:
    test1 = 0
  if arr[i]!=arr[i+1]-2:
    test2=0
if test1==1:
  print('is equal')
elif test2==1:
  print('is sequence')
else:
  print('other')
