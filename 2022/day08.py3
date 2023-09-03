#!/usr/bin/python3
# part 1 completed 2023-03-02 23:40 ET
# part 2 completed 2023-09-03 17:09 ET

import sys

tree_heights = []
grid_depth = 0
grid_width = 0

def is_visible(tree_row: int, tree_col: int) -> bool:
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
  global tree_heights, grid_width, grid_depth
  part1_trees_visible = 0
  part2_max_scenic_score = 0

  for line in sys.stdin:
    tree_heights.append([int(ch) for ch in line.rstrip()])

  grid_depth = len(tree_heights)
  grid_width = len(tree_heights[0])
  # outside trees automatically visible, subtract 4 to not count corners twice
  part1_trees_visible += (grid_width * 2 + grid_depth * 2) - 4
  print(f'{part1_trees_visible} trees automatically visible due to being at edges of grid')

  # Enumerating the rows/columns we need to check for visibility (inner trees);
  # don't need to check edge trees for part 2 either, since at least one of its
  # sides would have 0 trees visible to it, which makes the whole scenic score 0,
  # since the sides are multiplied by each other.
  min_row = 1
  min_col = 1
  # technically max values should be width/depth - 2, but -1 here since range() excludes max value
  max_row = grid_depth - 1
  max_col = grid_width - 1

  for row in range(min_row, max_row):
    for col in range(min_col, max_col):
      if is_visible(row, col):
        part1_trees_visible += 1
      if (scenic_score := count_visible(row, col)) > part2_max_scenic_score:
        part2_max_scenic_score = scenic_score

  print(f'Part 1 answer: {part1_trees_visible} total trees visible from outside the grid\n')
  print(f'Part 2 answer: {part2_max_scenic_score} is the maximum scenic score in this forest')


def count_visible(tree_row: int, tree_col: int) -> int:
  curr_height = tree_heights[tree_row][tree_col]
  curr_row = tree_heights[tree_row]
  curr_col = [row[tree_col] for row in tree_heights]
  # print(f'({tree_row}, {tree_col}) - {curr_height}')

  # Left and up are reversed so that we traverse those trees in the proper
  # order - from current tree outward to the edge of the forest
  directions = {
    'left': reversed(curr_row[0:tree_col]),
    'right': curr_row[tree_col+1:grid_width],
    'up': reversed(curr_col[0:tree_row]),
    'down': curr_col[tree_row+1:grid_depth]
  }

  # for direction, row_or_col_section in directions.items():
  #   print(f'  {direction} {row_or_col_section}')

  scenic_score = 1
  for direction, row_or_col_section in directions.items():
    direction_score = 0

    for tree_height in row_or_col_section:
      if tree_height < curr_height:
        direction_score += 1
      # Stop looking in this direction and multiply direction score into
      # overall scenic score if we reach a tree of same or greater height
      elif tree_height >= curr_height:
        direction_score += 1
        break
    scenic_score *= direction_score
    # print(f'  {direction}: {direction_score}')

  # print(f'  scenic score: {scenic_score}')
  return scenic_score


if __name__ == '__main__':
  main()
