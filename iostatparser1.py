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
            self.datadatetime=''
            self.data = {}
            pattnewline = re.compile('^$')
            pattdatetime = re.compile('^\d.*[P|A]M$')
            patttitlename = re.compile('Device:.*')

            from itertools import islice
            input_file = open(filepath,'r').readlines(400) # For test only
            #input_file = open(filepath,'r')
            for x in islice(input_file, 1, None):
                if pattnewline.findall(x):
                    continue
                elif pattdatetime.findall(x):
                    # 12/11/2015 09:30:46 AM
                    timeArray = time.strptime(x.strip(),"%m/%d/%Y %I:%M:%S %p")
                    timeStamp = float(time.mktime(timeArray))
                    self.datadatetime=datetime.datetime.utcfromtimestamp(timeStamp)
                    #print self.datadatetime
                    #self.datadatetime=x
                elif patttitlename.findall(x):
                    if self.data == {}:
                        y = x.strip().split()
                        for y1 in y:
                            self.data.setdefault(y1, {})
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
                    #print self.datadatetime
                    #print x
                   # realdata=x.strip().split()
                   # dataItr=1
                   # while(dataItr < len(self.datatitle)):
                   #     self.datatitle[dataItr].setdefault(self.datatitle[dataItr].keys()[0]).\
                   #         setdefault(str(realdata[0]),[]).append([str(self.datadatetime), realdata[dataItr]])
                        #if self.datatitle[dataItr][self.datatitle[dataItr].keys()[0]] == {} :
                        #    tmpdic={}
                        #  self.datatitile is a list , which is a container of iostat column
                        #  self.datatitle[dataItr] is dict .
                        #  self.datatitle[dataItr].keys()[0]) is a string , which is the key of self.datatitle[dataItr]
                   #     dataItr = dataItr + 1
                     #print self.data
                     realdata=x.strip().split()
                     dataItr=0
                     for key in self.data.keys():
                         self.data.setdefault(key).setdefault(str(realdata[0]), []).append([str(self.datadatetime), realdata[dataItr]]) ## TODO: continue
                         dataItr = dataItr + 1


#   def tojson(self):
        #jsondic={}
        #import json
        #for i in self.datatitle:
        #    return json.dumps(jsondic)

    def show(self):
        for key in self.data:
            print self.data[key]

    def get(self):
        return self.data


if __name__ == '__main__':
   import os
   aiosatp= iostatParser(os.path.realpath('data/iostat.data'))
   aiosatp.show()
   #print aiosatp.tojson()
   #print len(aiosatp.get())

