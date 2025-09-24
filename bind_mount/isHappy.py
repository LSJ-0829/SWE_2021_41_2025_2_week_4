def isHappy(n):
  loop = [n]
  while n != 1:
    sum = 0
    while n >= 1:
      sum += (n % 10) * (n % 10)
      n /= 10
      n = int(n)
    n = sum
    i = 0
    while i < len(loop):
      if loop[i] == n:
        return False
      i += 1
    loop.append(n)
  return True


if __name__ == "__main__":
    sample0_output = isHappy(19)
    sample1_output = isHappy(2)
    
    with open("/app/bind_mount/output.txt", "w") as f:
        f.write(f"19: {sample0_output}\n")
        f.write(f"2: {sample1_output}\n")
        
    print("Results saved to /app/bind_mount/output.txt")