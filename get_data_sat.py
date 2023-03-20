from __future__ import absolute_import
from __future__ import print_function

import os
import sys
import optparse
import random
from sumolib import checkBinary  # noqa
import traci  # noqa


def run():
    
    """execute the TraCI control loop"""
    
    car = []
    traci.trafficlight.setProgram('J1',0)

    while traci.simulation.getTime() < 120: 

        traci.simulationStep()
        
        # traci.trafficlight.setPhase('J1',0)#設為一直綠燈
        #數車子數量
        car_WE = list(traci.inductionloop.getLastStepVehicleIDs("LWE"))

        if len(car_WE)>0:
            car.append(car_WE[0])
        else:
            car.append("0")

        
    traci.close()
    # sys.stdout.flush()
    return(car)


def get_options():
    optParser = optparse.OptionParser()
    optParser.add_option("--nogui", action="store_true",
                         default=True, help="run the commandline version of sumo")
    options, args = optParser.parse_args()
    return options

def is_red(n):
        return n < 550 



# this is the main entry point of this script
if __name__ == "__main__":
    options = get_options()

    # this script has been called from the command line. It will start sumo as a
    # server, then connect and run
    if options.nogui:
        sumoBinary = checkBinary('sumo')
    else:
        sumoBinary = checkBinary('sumo-gui')

    traci.start([sumoBinary, "-c", "data/test.sumocfg"])

    result = run()
    timer = 0
    lost = []
    lost_final = []

    for n in range(len(result)-1):
        if (result[n] != '0') & (result[n+1] == '0'):
            lost.append(timer)
        timer += 1 

    for n in range(1,len(lost)):
        tmp = lost[n] - lost[n-1]
        lost_final.append(tmp)
    
    lost_flitered = filter( is_red, lost_final)
    lost_flitered = list(lost_flitered)


    avg = max(lost_flitered,key=lost_flitered.count)
    print(avg) #飽和時 兩車時間差



