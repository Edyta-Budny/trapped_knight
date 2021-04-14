from math import inf

from matrix import Matrix, add_tuples
from utils import draw_end, draw_line, draw_start, show_fig

SIZE = 100
board = Matrix(SIZE)
board.fill()

ALLOWED_MOVES = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2),
                 (2, -1)]


def draw_graph():
    next_move = (0, 0)
    location = (0, 0)
    step_no = 1

    draw_start(location, step_no)
    while True:
        last_move_value = inf
        for move in ALLOWED_MOVES:
            candidate = add_tuples(location, move)
            if board.get(candidate) < last_move_value:
                last_move_value = board.get(candidate)
                next_move = candidate
        if last_move_value == inf:
            break
        draw_line(location, next_move, step_no)
        step_no += 1
        board.set(location, inf)
        location = next_move
    draw_end(next_move, step_no)
    show_fig()


draw_graph()
