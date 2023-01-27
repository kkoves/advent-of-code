#!/usr/bin/python3
# part 1 completed 2023-01-21 19:03 ET
# part 2 completed 2023-01-26 23:29 ET

import sys, re, copy

class AdventOfCodeDay5:
  def __init__(self):
    self.stack_numbers = []
    self.stack_strings = []
    self.stacks_cratemover9000 = {}
    self.stacks_cratemover9001 = {}


  # This function is called by re.sub later to help turn stack input lines into simpler strings
  # For example: "    [A] [B]" --> "_AB"
  def simplify_column(self, match_obj):
    crate_col = match_obj.group(1)

    # three spaces - empty column
    if crate_col == '   ':
      return '_'
    # '[A]' -> 'A'
    elif crate_col[0] == '[':
      return crate_col[1]
    else:
      return crate_col


  # Input lines are in a different orientation to final stacks, essentially we make the input
  # "sideways" in final stack representation, swapping row and column, so:
  #    [B] [D]
  #    [A] [C]
  #     1   2
  # becomes:
  # {
  #   1: ['A', 'B']
  #   2: ['C', 'D']
  # }
  # Function is named as such since this is basically a matrix transposition
  def list_transpose(self):
    # last element of stack_numbers is the total number of crate stacks
    num_stacks = self.stack_numbers[-1]
    self.stack_strings.reverse()

    curr_stack = 0
    for i in range(num_stacks):
      curr_stack = self.stack_numbers[i]
      # after list of strings is reversed before loop, we just have to get the i-th
      # element of each string to get each crate label for the stacks, ignoring blanks ('_')
      self.stacks_cratemover9000[curr_stack] = [s[i] for s in self.stack_strings if s[i] != '_']

    # make a copy of the finalized stacks to work with independently for day 5 part 2
    self.stacks_cratemover9001 = copy.deepcopy(self.stacks_cratemover9000)


  # CrateMover 9000 can only move one crate at a time from the top of each stack
  def move_crates_cratemover9000(self, how_many, source, dest):
    for _ in range(how_many):
      source_stack_val = self.stacks_cratemover9000[source].pop()
      self.stacks_cratemover9000[dest].append(source_stack_val)


  # CrateMover 9001 can move several (no limit specified in prompt) crates at once
  # from the top of each stack, thus keeping them in the same order on the new stack
  def move_crates_cratemover9001(self, how_many, source, dest):
    # go backward from top of source stack by how_many to grab those crates, then remove them
    crates_moving = self.stacks_cratemover9001[source][-how_many:]
    del self.stacks_cratemover9001[source][-how_many:]

    # add crates we're moving to top of destination stack
    self.stacks_cratemover9001[dest].extend(crates_moving)


  # Returns the result we need for part 1 and part 2, the labels of the crates on top of each stack
  # Takes CrateMover model number (9000 or 9001) as an argument to determine which result stack
  # to pull from
  def top_of_stacks(self, cratemover_model):
    if cratemover_model == 9000:
      stack = self.stacks_cratemover9000
    elif cratemover_model == 9001:
      stack = self.stacks_cratemover9001

    top_string = ''
    for i in self.stack_numbers:
      top_string += stack[i][-1]

    return top_string


  def main(self):
    stack_regex = r'(\[\w\]|\s{3})\s?'
    # move_template = {'count': 0, 'move_from': 0, 'move_to': 0}

    # array indexes for processed move input lines
    HOW_MANY = 0
    FROM_STACK = 1
    TO_STACK = 2

    for line in sys.stdin:
      line = line.rstrip('\n')

      # crates - '   [A] [B]   ' etc. lines of input
      if '[' in line:
        self.stack_strings += [re.sub(stack_regex, self.simplify_column, line)]

      # stack numbers - ' 1 2 3 4 5 [...]' line of input; always has a space as line[0], so check line[1]
      elif len(line) > 1 and line[1].isnumeric():
        self.stack_numbers = [int(s) for s in line.split()]
        # since stack numbers are after stack lines, we can now finalize our data structure representation
        self.list_transpose()

      # get every other element of split-by-words move line, which works out to
      # just the numbers from "move 1 from 2 to 3", so [1, 2, 3]
      elif line.startswith('move'):
        move = [int(num_str) for num_str in line.split()[1::2]]
        self.move_crates_cratemover9000(move[HOW_MANY], move[FROM_STACK], move[TO_STACK])
        self.move_crates_cratemover9001(move[HOW_MANY], move[FROM_STACK], move[TO_STACK])

    print(f'-----\nPart 1 answer: {self.top_of_stacks(9000)}')
    print(f'-----\nPart 2 answer: {self.top_of_stacks(9001)}')


if __name__ == '__main__':
  day5 = AdventOfCodeDay5()
  day5.main()
