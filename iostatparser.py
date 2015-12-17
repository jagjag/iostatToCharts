import re
import copy
import time
import datetime

#  run a  iostat  command like this:
# iostat -dNxt 60 > iostat.data
# parse the iostat.data

class iostatParser():
    def __init__(self,filepath):
        with open(filepath) as f:
            self.datadict={}
            self.datadatetime=''
            self.datatitle=[]
            pattnewline = re.compile('^$')
            pattdatetime = re.compile('^\d.*[P|A]M$')
            patttitlename = re.compile('Device:.*')

            from itertools import islice
            input_file = open(filepath,'r').readlines(400)
            #for x in open(filepath,'r'):
            for x in islice(input_file, 1, None):
                if pattnewline.findall(x):
                    continue
                elif pattdatetime.findall(x):
                    # 12/11/2015 09:30:46 AM
                    timeArray = time.strptime(x.strip(),"%m/%d/%Y %I:%M:%S %p")
                    timeStamp = float(time.mktime(timeArray))
                    self.datadatetime=datetime.datetime.utcfromtimestamp(timeStamp)
                    #print self.datadatetime
                elif patttitlename.findall(x):
                    if self.datatitle == []:
                        y = x.strip().split()
                        for y1 in y:
                            tdict={}
                            tdict.setdefault(y1,[])
                            self.datatitle.append(copy.deepcopy(tdict))
                        print self.datatitle
                    else:
                        continue
                else:
                    #
                    # real data process
                    # n=  [ name , val1 ,val2, val3 ]
                    #  for i in range(1,n):
                    #
                    #  { datatitile[i]:
                    #       { n[0]:[ [ datadattime,n[1] ],]}
                    # }

                    #  { 'r/s':
                    #       { 'sda': [ ['datetime','0.1'], ['datetime','0.2'],] }
                    #  }
                    realdata=x.strip().split()
                    print realdata

                    #for i in realdata:


    def toJSON(self):
        pass

    def Show(self):
        pass


if __name__ == '__main__':
    iostatParser('data//iostat.data')
