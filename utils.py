import matplotlib.pyplot as plt
from matplotlib import cm

colormap = cm.get_cmap('viridis', 2015)
fig, move = plt.subplots()
fig.suptitle('The Trapped Knight')


def draw_start(spot, step_no):
    return move.scatter(spot[0], spot[1], linewidth=0.6, edgecolor='r',
                        facecolors='none', zorder=3,
                        label='move={}'.format(step_no))


def draw_line(spotA, spotB, step_no):
    return move.plot([spotA[0], spotB[0]], [spotA[1], spotB[1]],
                     c=colormap(step_no), linewidth=0.6)


def draw_end(spot, step_no):
    return move.scatter(spot[0], spot[1], c='r', marker='x', linewidth=0.6,
                        label='move={}'.format(step_no))


def show_fig():
    move.legend(loc='lower right', frameon=False)
    plt.show()
