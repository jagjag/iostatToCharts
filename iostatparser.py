import re
import copy


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
            pattdatetime = re.compile('^\d\/\d.*[P|A]M$')
            patttitlename = re.compile('Device:.*')
            for x in open(filepath,'r'):
                if pattnewline.findall(x):
                    continue
                elif pattdatetime.findall(x):
                    self.datadatetime=x.strip()   #TODO: add  convert string to datetime
                elif patttitlename.findall(x):
                    if self.datatitle.count() == 0:
                        y = x.strip().split()
                        #for i in y :
                        #    if i == 'Device':
                        #        continue
                        #    else:
                        self.datatitle=copy.deepcopy(x)
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
                    for i in realdata:




    def toJSON(self):
        pass

    def Show(self):
        for i in self.datalist:
            print i



if __name__ == '__main__':
    iostatParser('data//iostat.data').Show()
