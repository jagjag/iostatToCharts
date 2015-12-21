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
            #input_file = open(filepath,'r')
            for x in islice(input_file, 1, None):
                if pattnewline.findall(x):
                    print 'newline'
                    continue
                elif pattdatetime.findall(x):   ## TODO: have problem here
                    # 12/11/2015 09:30:46 AM
                    #timeArray = time.strptime(x.strip(),"%m/%d/%Y %I:%M:%S %p")
                    #timeStamp = float(time.mktime(timeArray))
                    #self.datadatetime=datetime.datetime.utcfromtimestamp(timeStamp)
                    #print self.datadatetime
                    self.datadatetime=x
                elif patttitlename.findall(x):
                    if self.datatitle == []:
                        y = x.strip().split()
                        for y1 in y:
                            tdict={}
                            tdict.setdefault(y1,[])
                            self.datatitle.append(copy.deepcopy(tdict))
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
                    # it is  a little complex .   and  we will rewrite later
                    #>>> abc[3]
                    #{'r/s': []}
                    #>>> abc[3].setdefault('r/s').append([1,2])
                    #>>> abc[3]
                    #{'r/s': [[1, 2]]}
                    #>>> abc[3].setdefault('r/s').append([1,2])
                    #>>> abc[3]
                    #{'r/s': [[1, 2], [1, 2]]}
                    #>>> abc[3].setdefault('r/s').append([1,2])
                    #>>> abc[3]['r/s']
                    #[[1, 2], [1, 2], [1, 2]]
                    #>>> abc[3]['r/s'][1]
                    #[1, 2]
                    #>>> abc[3]['r/s'][1][1]
                    #2
                    #>>> abc[3]['r/s'][0][0]
                    #1
                    #  abc[3][abc[3].keys()[0]]
                    #  [[1, 2], [1, 2], [1, 2]]
                    print self.datadatetime
                    print x
                    realdata=x.strip().split()
                    dataItr=1
                    while(dataItr < len(self.datatitle)):
                        tmpdic.setdefault(realdata[0],)
                             .append([str(self.datadatetime), realdata[dataItr]])
                         #  self.datatitile is a list , which is a container of iostat column
                         #  self.datatitle[dataItr] is dict .
                         #  self.datatitle[dataItr].keys()[0]) is a string , which is the key of self.datatitle[dataItr]
                         dataItr = dataItr + 1

                    self.datatitle[dataItr].setdefault(self.datatitle[dataItr].keys()[0]) \
                             .append([str(self.datadatetime), realdata[dataItr]])
                    #print realdata
                    #for i in realdata:
    def tojson(self):
        pass

    def show(self):
        for i in self.datatitle:
            print i

    def get(self):
        return self.datatitle


if __name__ == '__main__':
   aiosatp= iostatParser('data//iostat.data')
   aiosatp.show()
   print len(aiosatp.get())

