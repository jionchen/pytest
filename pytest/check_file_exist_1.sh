#!/bin/bash

#check file exists or not and check the statenments
#version 1.1

function usage(){
echo "Usage:$0 file time
      file is just name not contain time
      time is the number of hour and minute"
}

function check(){

  if [ $current_time -lt $time ];then
         echo "OK,current time the file ${filename}_001.log is not create yet"
         continue
         
  fi
  if [ $filenum -ge 1 ];then
        echo "OK,file $file exist"
  else
        echo "WARNING,file ${filename}_001.log is not exist,please check"
  fi
}

#function main(){
#  
#  if [ $# -ne 2 ];then
#        usage
#        exit 2;
#  fi
#  time=$2
#  dir=$(cd $(dirname $1);pwd)
#  current_time=$(date +%H%M)
#  y_day=$(date -d"yesterday" +%Y%m%d)
#  filename=$(basename $1)_$y_day
#  file=`cd $dir;ls|grep $filename`
#  filenum=`find $dir -iname "$filename*" -mtime -1|wc -l`
#  check
#}
#
#main $@

function main(){
if [ $# -lt 1 ];then
    usage
fi

 for i in `echo $@|awk -F'_' '{$1=$1;print}'`
 do
   path=$(echo $i|awk -F':' '{print $1}')
   time=$(echo $i|awk -F':' '{print $2}')
   dir=$(cd $(dirname $path);pwd)
  current_time=$(date +%H%M)
  y_day=$(date -d"yesterday" +%Y%m%d)
  filename=$(basename $path)_$y_day
  file=`cd $dir;ls|grep $filename`
  filenum=`find $dir -iname "$filename*" -mtime -1|wc -l`
  check
 done


}

main $@



