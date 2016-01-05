#!/usr/bin/env python
# -*- coding: utf-8 -*-
import copy
import datetime
import re


class IostatParser:
    """
    This module parse  iostat output file into a list of dict structure(get()) and a time series list( getdatetimelist())
    """

    def __init__(self, filepath):
        import os
        self.filepath = ''
        if os.path.exists(filepath):
            self.filepath = filepath
        else:
            raise Exception
        self.datadatetime = []  # list of datetime ,which is actual timestamp of collect
        self.datalist = []  # a list of  dict , which is a structure of real data

    def process(self):
        with open(self.filepath) as f:
            from itertools import islice
            pattnewline = re.compile('^$')
            pattdatetime12 = re.compile('^\d.*[P|A]M$')
            pattdatetime = re.compile('^[01][0-9]\/[0-3][0-9]\/[0-9][0-9]\s[012][0-9]\:[0-9][0-9]\:[0-9[0-9]')
            patttitlename = re.compile('Device:.*')
            pattfirstline = re.compile('\(.*\)')
            # for x in islice(f.readlines(600), 0, None):
            for x in islice(f, 0, None):
                if pattnewline.findall(x):  # ignore  \n  and other lines
                    continue
                elif pattfirstline.findall(x):
                    continue
                elif pattdatetime12.findall(
                        x):  # get datetime for every iostat table . and convert it to 24 Hour format
                    #  12/11/2015 09:30:46 AM
                    timearray = datetime.datetime.strptime(x.strip(), "%m/%d/%Y %I:%M:%S %p")
                    self.datadatetime.append(timearray)
                elif pattdatetime.findall(x):
                    #  12/11/2015 09:30:46 AM
                    timearray = datetime.datetime.strptime(x.strip(), "%m/%d/%y %H:%M:%S")
                    self.datadatetime.append(timearray)
                elif patttitlename.findall(x):  # get column of iostat tables
                    if self.datalist == []:
                        y = x.strip().split()
                        for y1 in y:
                            if patttitlename.findall(y1):
                                continue
                            tdict = {}
                            tdict.setdefault(str(y1).replace(r'/', '_'), {})
                            self.datalist.append(copy.deepcopy(tdict))  # a dict to fill data
                    else:
                        continue
                else:
                    #
                    # real data process
                    #
                    realdata = x.strip().split()
                    dataitr = 0
                    while dataitr < len(self.datalist):
                        self.datalist[dataitr].setdefault(self.datalist[dataitr].keys()[0]). \
                            setdefault(str(realdata[0]), []).append(realdata[dataitr + 1])
                        # print self.datalist[dataitr].keys()[0]
                        # print str(realdata[0])
                        # print realdata[dataitr + 1]
                        #  self.datalist is a list , which is a container of iostat column
                        #  self.datalist[dataitr] is dict .
                        #  self.datalist[dataitr].keys()[0]) is a string , which is the key of self.datalist[dataitr]
                        dataitr += 1
        f.close()

    def show(self):
        """
        print all data
        :return:  None
        """
        for i in self.datalist:
            print i

    def tojson(self):
        """
        dump to json format , and also for human read
        :return:  json format of data
        """
        import json
        return json.dumps(self.datalist, separators=(',', ':'), sort_keys=True, indent=4)

    def get(self):
        """
        get self.datalist
        :return:  list of data
        """
        # self.process()
        return self.datalist

    def getdatatimelist(self):
        """
        get self.datadattime
        :return: self.datadatetime
        """
        return self.datadatetime


if __name__ == '__main__':
    import os

    aiosatp = IostatParser(os.path.realpath('data/iostat.data.2015122212'))
    aiosatp.process()
    aiosatp.show()
    # aiosatp.show()
    # print aiosatp.tojson()
    # print len(aiosatp.get())
