#!/usr/bin/python3
# part 2 completed 2023-01-14 22:08 ET

import sys

# scissors < rock < paper
# paper < scissors
rps_codes = {
  'A': 'rock',
  'B': 'paper',
  'C': 'scissors',
  'X': 'rock',
  'Y': 'paper',
  'Z': 'scissors'
}

rps_scores = {
  'rock': 1,
  'paper': 2,
  'scissors': 3,
  'win': 6,
  'draw': 3,
}

beats_what = {
  'rock': 'scissors',
  'paper': 'rock',
  'scissors': 'paper'
}


def main():
  part1_score = 0
  part2_score = 0

  for line in sys.stdin:
    hands = line.split()
    opponent_shape = hands[0]
    my_shape_or_strategy = hands[1]
    part1_score += eval_rps_part1(my_shape_or_strategy, opponent_shape)
    part2_score += eval_rps_part2(my_shape_or_strategy, opponent_shape)

  print("Part 1 - total score:", part1_score)
  print("Part 2 - total score:", part2_score)


def eval_rps_part1(my_shape, opponent_shape):
  my_shape = rps_codes[my_shape]
  opponent_shape = rps_codes[opponent_shape]

  score = rps_scores[my_shape]
  if opponent_shape == my_shape:
     score += rps_scores['draw']
  elif opponent_shape == beats_what[my_shape]:
    score += rps_scores['win']
  # no if needed for lose, since lose = 0

  return score


def eval_rps_part2(my_strategy, opponent_shape):
  rps_strategies = {
    'X': 'lose',
    'Y': 'draw',
    'Z': 'win'
  }

  is_beaten_by = {
    'rock': 'paper',
    'paper': 'scissors',
    'scissors': 'rock'
  }

  my_strategy = rps_strategies[my_strategy]
  opponent_shape = rps_codes[opponent_shape]
  score = 0

  if my_strategy == 'draw':
    score += rps_scores['draw'] + rps_scores[opponent_shape] # make same shape as opponent
  elif my_strategy == 'win':
    my_shape = is_beaten_by[opponent_shape]
    score += rps_scores['win'] + rps_scores[my_shape]
  else: # my_strategy == 'lose'
    my_shape = beats_what[opponent_shape]
    score += rps_scores[my_shape] # no extra points for losing (duh)

  return score


if __name__ == '__main__':
  main()