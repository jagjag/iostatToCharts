
import matplotlib  
matplotlib.use('Agg')  
  
import matplotlib.pyplot as plt # import plot,savefig  
import time
import datetime
def main():

    realYdot= [ y.strip() for y in open('rs.log') ]
  #y= [ i for i in range(1,len(realYdot)+1) ]
   
    strTime="2015-12-10 20:00:00"
    timeArray = time.strptime(strTime, "%Y-%m-%d %H:%M:%S")
    timeStamp = float(time.mktime(timeArray)) 
    dateArray = datetime.datetime.utcfromtimestamp(timeStamp)
   
    realXdot=list()
    adjDt=dateArray
    #for i in range(1,len(realYdot+1):
    fff=[]
    i=len(realYdot)
    while(i):
        adjDt= adjDt + datetime.timedelta(seconds = 10)
        #print(adjDt)
        fff.append([adjDt,realXdot[i-1]])
        #realXdot.append(adjDt)
        i=i-1


    plt.figure(figsize=(150,15))
    #plt.plot(realXdot,realYdot,linewidth=0.8)
    plt.plot(fff,linewidth=0.8)
    plt.savefig('rs.png')

if __name__ == '__main__':
    main()

