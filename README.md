This Hadoop Mini project is to count the number of accidents for each vehicle make and year and uses two mapper and reducers.

Step 1: The mapper1 will generate the key value pairs for vehicle VIN# as key and vehicle model, year and incident type as a tuple
Step 2: The reducer1 will capture the vehicle model and year as key and accident count as value
Step 3: The mapper2 will pass the key-value from reducer1 
Step 4: The reducer2 will combine the total accident count for the key vehicle model and year and total accident count.

The final output from reducer2 is shown as below:
(' Mercedes', ' 2016')	1
(' Toyota', ' 2017')	0
(' Nissan', ' 2003')	1
(' Mercedes', ' 2015')	2

The execution log of the hadoop mapper and reducers is captured in the file mapreduce_output.txt

To execute the Map Reduce in the oracle VM
1. create two HDFS folders /input_files and /output_files
2. copy the data.csv to a HDFS folder /input_files/
3. copy the autoinc_mapper1.py,autoinc_reducer1.py,autoinc_mapper2.py,autoinc_reducer2.py and autoinc_bash.sh to /home/cloudera/AutoMapReduce folder
4. change directory to /home/cloudera/AutoMapReduce folder
5. Run the shell script using the bash command "bash autoinc_bash.sh"
6. verify the output in HDFS /output_files/make_year_count
