#!/bin/bash
#  version 1.0
#  JJmomark

Interval=30  # modify it
io_base=/some/path//data   #modify it

killall -u yourusername  iostat  # modify it
cp -r ${io_base}/iostat.data  ${io_base}/iostat.data.`date +%Y%m%d`
>${io_base}/iostat.data
nohup /usr/bin/iostat -dkNxt ${Interval} >> ${io_base}/iostat.data &


