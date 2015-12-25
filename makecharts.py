import errno
import os
import socket

import matplotlib

import iostatparser

matplotlib.use('Agg')


class makecharts():
    def __init__(self, hname=socket.gethostname(), datafile='', outputpath=r'/tmp'):
        self.l_columnkey = []
        self.l_disklabel = []
        self.hname = hname
        self.dfile = os.path.realpath(datafile)
        self.opath = os.path.realpath(outputpath)

    def __output(self):
        pass

    def mkdir_p(self, path):
        try:
            os.makedirs(path)
        except OSError as exc:  # Python >2.5
            if exc.errno == errno.EEXIST and os.path.isdir(path):
                pass
            else:
                raise

    def process(self):
        print self.opath
        print self.hname
        _itcbase = self.opath + r'/ITCoutput/' + self.hname
        print _itcbase
        # os.makedirs(_itcbase)
        aiop = iostatparser.iostatParser(self.dfile)
        aiop.process()
        l_aiop = aiop.get()
        for dictitem in l_aiop:
            for columkey in dictitem:
                _dpath = _itcbase + r'/' + columkey + r'/'
                self.mkdir_p(_dpath)
                # print "2 %s" % dictitem[columkey]
                for disklabel in dictitem[columkey]:
                    # dictitem[columkey][disklabel]      #this is a list, which also is real data list
                    # print "3 %s" % disklabel
                    # print type(dictitem[columkey][disklabel])
                    # print dictitem[columkey][disklabel]

                    self.__drawcharts(dictitem[columkey][disklabel], aiop.getdatatimelist(),
                                      _dpath + r'/' + disklabel + r'.png', columkey, disklabel)

    def __drawcharts(self, data, datadatetime, outputfile, titilecol, titilerow):
        from matplotlib import pyplot as plt
        plt.figure(figsize=(50, 20))
        plt.title(titilecol + ' ' + titilerow)
        plt.xlabel("Timestamp")
        plt.ylabel(titilecol)
        plt.plot(datadatetime, data, linewidth=0.8)
        # plt.plot_date(datadatetime,data,fmt='bo', tz=None, xdate=True, ydate=False)
        plt.savefig(outputfile)

def main():
    makecharts(datafile='data/iostat.data.2015122212').process()

if __name__ == '__main__':
    main()
