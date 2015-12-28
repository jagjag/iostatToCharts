#!/bin/bash
#  version 1.0
#  JJmomark

Interval=30
io_base=/home/gcpadmin/iostat/data
killall -u gcpadmin  iostat
cp -r ${io_base}/iostat.data  ${io_base}/iostat.data.`date +%Y%m%d`
>${io_base}/iostat.data
nohup /usr/bin/iostat -dNxt ${Interval} >> ${io_base}/iostat.data &


