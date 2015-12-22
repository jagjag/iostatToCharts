import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt # import plot,savefig
from iostatparser import  *


def main():
    import os
    datalist = iostatParser(os.path.realpath('data/iostat.data')).get()

    # for i in datalist:  # {'rrqm/s'
    #     os.mkdir(i.keys()[0])   #  TODO  :
    #     for k in i:     #  'VolGroup00-LogVol03': [['2015-12-11 01:26:46', '0.00'], ['2015-12-11 01:27:46', '0.00'], ['2015-12-11 01:28:46', '0.00'], ['2015-12-11 01:29:46', '0.00'], ['2015-12-11 01:30:46', '0.00']],a
    #          txdot = []
    #          tydot = []
    #          os.mkdir()  # TODO
    #          for j in k:        #  [['2015-12-11 01:26:46', '0.00'], ['2015-12-11 01:27:46', '0.00'], ['2015-12-11 01:28:46', '0.00'], ['2015-12-11 01:29:46', '0.00'], ['2015-12-11 01:30:46', '0.00']],
    #               txdot.append([0])
    #               tydot.append([j])
    #          drawpic(txdot,tydot)
    for i in datalist:
       print "1 %s" % i
       for k in i:
           #print "2 %s" % i[k]
           print "2 %s" % k
           for j in k:
               #print "3 %s" % i[k][j]
               print "3 %s" % j




# def drawpic(xdot,ydot):
#     plt.figure(figsize=(150,20))
#     plt.plot(xxx,linewidth=0.8)
#     plt.savefig('rs.png')

if __name__ == '__main__':
    main()