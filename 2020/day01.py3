#!/usr/bin/python3
#
# completed 2020-12-01 11:--pm EST

import sys
from typing import Tuple, Set

def expense_report(expenses: Set[int]) -> Tuple[int, int]:
  diff_2020 = 0

  for expense in expenses:
    diff_2020 = 2020 - expense

    if diff_2020 in expenses:
      return (expense, diff_2020)

  return ()

def main():
  nums = set()

  for line in sys.stdin:
    nums.add(int(line))

  sum_2020 = expense_report(nums)
  prod = sum_2020[0] * sum_2020[1]
  print(f"The two expense entries that add up to 2020 are {sum_2020[0]} and {sum_2020[1]}" \
    f" and their product is {prod}")

if __name__ == '__main__':
  main()