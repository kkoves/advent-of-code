#!/usr/bin/python3
# part 1 completed 2023-03-02 23:40 ET
# part 2 completed 2023-03-__ __:__ ET

import sys

tree_heights = []
trees_visible = 0
grid_depth = 0
grid_width = 0

def is_visible(tree_row: int, tree_col: int) -> bool:
  global tree_heights, grid_width, grid_depth

  visible = False
  curr_height = tree_heights[tree_row][tree_col]
  curr_row = tree_heights[tree_row]
  curr_col = [row[tree_col] for row in tree_heights]
  # print(f'{tree_col = }, {curr_col = }')
  
  left_visible = not any(height >= curr_height for height in curr_row[0:tree_col])
  right_visible = not any(height >= curr_height for height in curr_row[tree_col+1:grid_width])
  up_visible = not any(height >= curr_height for height in curr_col[0:tree_row])
  down_visible = not any(height >= curr_height for height in curr_col[tree_row+1:grid_depth])

  is_visible = left_visible or right_visible or up_visible or down_visible
  # print(f'{tree_row}, {tree_col} {"is" if is_visible else "NOT"} visible - '
  #      f'left {left_visible}, right {right_visible}, up {up_visible}, down {down_visible}')
  return is_visible


def main():
  global tree_heights, trees_visible, grid_width, grid_depth

  for line in sys.stdin:
    tree_heights.append([int(ch) for ch in line.rstrip()])

  grid_depth = len(tree_heights)
  grid_width = len(tree_heights[0])
  # outside trees automatically visible, subtract 4 to not count corners twice
  trees_visible += (grid_width * 2 + grid_depth * 2) - 4
  print(f'{trees_visible} trees automatically visible due to being at edges of grid')

  # enumerating the rows/columns we need to check for visibility (inner trees)
  min_row = 1
  min_col = 1
  # technically max values should be width/depth - 2, but -1 here since range() excludes max value
  max_row = grid_depth - 1
  max_col = grid_width - 1

  for row in range(min_row, max_row):
    for col in range(min_col, max_col):
      if is_visible(row, col):
        trees_visible += 1

  print(f'Part 1 answer: {trees_visible} total trees visible from outside the grid')

if __name__ == '__main__':
  main()
