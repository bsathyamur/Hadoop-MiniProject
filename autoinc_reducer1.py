#!/usr/bin/env python

import sys

vehicleinfo = {}

def flush():
    for key in vehicleinfo.keys():
        print '%s\t%s' % ((vehicleinfo[key]["make"],vehicleinfo[key]["year"]),vehicleinfo[key]["accident_count"])

for line in sys.stdin:
    line = line.strip()
    vin, values = line.split('\t')
    values_arr = [val.replace("'","") .replace("(","").replace(")","") for val in values.split(",")]

    incident_type = values_arr[0]
    vehicle_make = values_arr[1]
    vehicle_year = values_arr[2]

    # if vin is not present in the dictionary create a new entry
    if vin not in vehicleinfo:
        vehicleinfo[vin] = {"make":None,"year":None,"accident_count":0}

    # collect the vehicle make and year data from incident type = Initial sales
    if incident_type == "I":
        vehicleinfo[vin]["make"] = vehicle_make
        vehicleinfo[vin]["year"] = vehicle_year

    # increment the count for each incident type = A
    if incident_type == "A":
        vehicleinfo[vin]["accident_count"] += 1
	
# [output the reducer key values]
flush()