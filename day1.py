import sys, math

def part1(numbers):
  sum = 0
  for n in numbers:
    sum_n = math.floor(int(n) / 3) - 2
    sum += sum_n
  return sum

def part2(numbers):
  sum = 0
  for n in numbers:
    sum_n = math.floor(int(n) / 3) - 2
    sum += sum_n
    while sum_n > 0:
      sum_n = math.floor(int(sum_n) / 3) - 2
      if sum_n > 0:
        sum += sum_n
  return sum

assert len(sys.argv) == 2
numbers = open(sys.argv[1]).read().splitlines()

print(f'Part 1: {part1(numbers)} - Part 2: {part2(numbers)}')