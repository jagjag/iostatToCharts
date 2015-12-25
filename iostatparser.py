import copy
import datetime
import re
import time


#  run a  iostat  command like this:
# iostat -dNxt 60 > iostat.data
# parse the iostat.data

class iostatParser():
    def __init__(self, filepath):
        import os
        self.filepath = ''
        if os.path.exists(filepath):
            self.filepath = filepath
        else:
            raise Exception
        self.datadatetime = []
        self.datatitle = []
        self.datadict = {}

    def process(self):
        with open(self.filepath) as f:
            from itertools import islice
            pattnewline = re.compile('^$')
            pattdatetime = re.compile('^\d.*[P|A]M$')
            patttitlename = re.compile('Device:.*')
            pattfirstline = re.compile('\(.*\)')
            #for x in islice(f.readlines(600), 0, None):
            for x in islice(f, 0, None):
                if pattnewline.findall(x):
                    continue
                elif pattfirstline.findall(x):
                    continue
                elif pattdatetime.findall(x):
                    #  12/11/2015 09:30:46 AM
                    timeArray = time.strptime(x.strip(), "%m/%d/%Y %I:%M:%S %p")
                    timeStamp = float(time.mktime(timeArray))
                    self.datadatetime.append(datetime.datetime.utcfromtimestamp(timeStamp))
                    # print self.datadatetime
                    # self.datadatetime=x
                elif patttitlename.findall(x):
                    if self.datatitle == []:
                        y = x.strip().split()
                        for y1 in y:
                            if patttitlename.findall(y1):
                                continue
                            tdict = {}
                            tdict.setdefault(str(y1).replace(r'/', '_'), {})
                            self.datatitle.append(copy.deepcopy(tdict))
                    else:
                        continue
                else:
                    #
                    # real data process
                    #  { 'r/s':
                    #       { 'sda': [ ['datetime','0.1'], ['datetime','0.2'],] }
                    #  }
                    # it is  a little complex .   and  we will rewrite later
                    # >>> abc[3]
                    # {'r/s': []}
                    # >>> abc[3].setdefault('r/s').append([1,2])
                    # >>> abc[3]
                    # {'r/s': [[1, 2]]}
                    # >>> abc[3].setdefault('r/s').append([1,2])
                    # >>> abc[3]
                    # {'r/s': [[1, 2], [1, 2]]}
                    # >>> abc[3].setdefault('r/s').append([1,2])
                    # >>> abc[3]['r/s']
                    # [[1, 2], [1, 2], [1, 2]]
                    # >>> abc[3]['r/s'][1]
                    # [1, 2]
                    # >>> abc[3]['r/s'][1][1]
                    # 2
                    # >>> abc[3]['r/s'][0][0]
                    # 1
                    #  abc[3][abc[3].keys()[0]]
                    #  [[1, 2], [1, 2], [1, 2]]
                    # print self.datadatetime

                    realdata = x.strip().split()
                    dataItr = 0
                    while (dataItr < len(self.datatitle)):
                        self.datatitle[dataItr].setdefault(self.datatitle[dataItr].keys()[0]). \
                            setdefault(str(realdata[0]), []).append(realdata[dataItr + 1])
                        #   setdefault(str(realdata[0]), []).append([str(self.datadatetime), realdata[dataItr + 1]])
                        # if self.datatitle[dataItr][self.datatitle[dataItr].keys()[0]] == {} :
                        #    tmpdic={}
                        #  self.datatitile is a list , which is a container of iostat column
                        #  self.datatitle[dataItr] is dict .
                        #  self.datatitle[dataItr].keys()[0]) is a string , which is the key of self.datatitle[dataItr]
                        dataItr = dataItr + 1
        f.close()


    def show(self):
        for i in self.datatitle:
            print i

    def tojson(self):
        import json
        return json.dumps(self.datatitle, separators=(',', ':'), sort_keys=True, indent=4)

    def get(self):
        # self.process()
        return self.datatitle

    def getdatatimelist(self):
        return self.datadatetime


if __name__ == '__main__':
    import os
    aiosatp = iostatParser(os.path.realpath('data/iostat.data.2015122212'))
    aiosatp.process()
    aiosatp.show()
    #aiosatp.show()
    # print aiosatp.tojson()
    #print len(aiosatp.get())
