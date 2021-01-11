#!/bin/bash

hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-mr1.jar \
-file /home/cloudera/AutoIncMapRed/autoinc_mapper1.py -mapper "python autoinc_mapper1.py" \
-file /home/cloudera/AutoIncMapRed/autoinc_reducer1.py -reducer "python autoinc_reducer1.py" \
-input /input_files/data.csv -output /output_files/all_accidents

hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-mr1.jar \
-file /home/cloudera/AutoIncMapRed/autoinc_mapper2.py -mapper "python autoinc_mapper2.py" \
-file /home/cloudera/AutoIncMapRed/autoinc_reducer2.py -reducer "python autoinc_reducer2.py" \
-input /output_files/all_accidents -output /output_files/make_year_count