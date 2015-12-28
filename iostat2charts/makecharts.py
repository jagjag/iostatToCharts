#!/usr/bin/env python
# -*- coding: utf-8 -*-
import errno
import os
import socket

import matplotlib

from iostat2charts import iostatparser

matplotlib.use('Agg')


class MakeCharts:
    """
    draw charts into certain path
    """

    def __init__(self, hname=socket.gethostname(), datafile='', outputpath=r'/tmp'):
        """
        init make
        :param hname: hostname , default is hostname of current runner
        :param datafile: a real path of datafile
        :param outputpath:  a real path to output , default is /tmp
        :return:  None
        """
        self.__hname = hname
        self.__dfile = os.path.realpath(datafile)
        self.__opath = os.path.realpath(outputpath)

    def mkdir_p(self, path):
        """
        a util method like  mkdir -p in linux system when create dirs
        :param path: path string
        :return: None  or raise
        """
        try:
            os.makedirs(path)
        except OSError as exc:  # Python >2.5
            if exc.errno == errno.EEXIST and os.path.isdir(path):
                pass
            else:
                raise

    def draw(self):
        """
        put datafile into iostatparser class and make output directory structure , it invokes __drawchars() to draw
        :return:  None
        """
        import datetime
        today = datetime.datetime.now()
        print self.__opath
        print self.__hname
        _itcbase = self.__opath + r'/iostat2charts/' + self.__hname
        print _itcbase
        # os.makedirs(_itcbase)
        aiop = iostatparser.IostatParser(self.__dfile)

        aiop.process()
        l_aiop = aiop.get()
        for dictitem in l_aiop:
            for columkey in dictitem:
                _dpath = _itcbase + r'/' + str(today) + r'/' + columkey + r'/'
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
        """
        draw charts ,  data as y  datadatetime as x
        :param data: list of  x dot , which is data
        :param datadatetime:  list of y dot, which is datetime
        :param outputfile:  output file path and name
        :param titilecol:  titile text of data
        :param titilerow:  certain disk volume name (row name of istat output)
        :return: None
        """
        from matplotlib import pyplot as plt
        plt.figure(figsize=(25.6, 14.4))
        plt.title(titilecol + ' ' + titilerow)
        plt.text(0.05, 0.95, titilecol + '' + titilerow, verticalalignment="top", fontsize=18)
        plt.xlabel("Timestamp")
        plt.ylabel(titilecol)
        # plt.plot(datadatetime, data, linewidth=0.8)
        plt.plot_date(datadatetime, data, fmt='bo', tz=None, xdate=True, ydate=False)
        plt.savefig(outputfile)


def main():
    MakeCharts(datafile='data/iostat.data.2015122312').draw()

# if __name__ == '__main__':
# main()
