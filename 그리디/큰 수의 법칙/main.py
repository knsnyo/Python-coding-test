a, b, c = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
num1 = data[n-1] # 제일 큰 거
num2 = data[n-2] # 그 다음 거

result = 0

while True:
  for in in range(c):
    if 0 == m:
      break
    result += first
    m -= 1
  if 0 == m:
    break
  result += second
  m -= 1
  
print(result)
