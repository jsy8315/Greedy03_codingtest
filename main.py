# Greedy 03

#001 내 풀이
n, k = map(int, input().split())

result = 0

# 일단 if문을 써야될것같음
while True:
  if n % k == 0:
    n = n // k
    result += 1
    if n == 1:
      break
  else:
    n -= 1
    result += 1
    if n == 1:
      break

print(result)

#002 단순하게 풀기
n, k = map(int, input().split())
result = 0

# N이 K 이상이라면 K로 계속 나누기
while n >= k:
  # N이 K로 나누어 떨어지지 않는다면 N에서 1씩 빼기
  while n % k != 0:
    n -= 1
    result += 1
    #k로 나누기
    n //= k
    result += 1

while n > 1:
  n -= 1
  result += 1

print(result)

#003 답안예시

# N,K를 공백으로 구분하여 입력받기
n, k = map(int, input().split())
result = 0

while True:
  # (N==K로 나누어 떨어지는 수)가 될때까지 1씩 빼기
  target = (n // k) * k
  result += (n - target)
  n = target
  # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
  if n < k:
    break
  result += 1
  n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)
