import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt # import plot,savefig
from iostatparser import  *


def main():
    import os
    datalist = iostatParser(os.path.realpath('data/iostat.data'))




def drawpic(xdot,ydot):

    plt.figure(figsize=(150,20))
    plt.plot(xxx,linewidth=0.8)
    plt.savefig('rs.png')

if __name__ == '__main__':
    main()