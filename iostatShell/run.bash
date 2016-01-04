#!/bin/bash
#  version 1.0
#  JJmomark


yesterday=`date --date='a day ago' '+%Y%m%d'`
echo $yesterday
datafile="/home/gcpadmin/iostat/data/iostat.data.${yesterday}"
echo $datafile

/usr/bin/python  /home/gcpadmin/iostatToCharts/run.py ${datafile}


