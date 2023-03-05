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
    
    LSN1_car = []
    LSN2_car = []
    LNS1_car = []
    LNS2_car = []
    LWE_car = []
    LEW_car = []

    #飽和流率是假設在連續不斷的車流抵達情況下，且有100％綠燈通行時間，每小時可通過路口的車輛數(輛/小時)
    while traci.simulation.getTime() < 600:
        
        traci.simulationStep()
        
        traci.trafficlight.setPhase('J1',0)#設為一直綠燈
        #數車子數量
        car = []
        for n in car:
            LSN1_car.append(n)
        car = list(traci.inductionloop.getLastStepVehicleIDs("LSN2"))
        for n in car:
            LSN2_car.append(n)
        car = list(traci.inductionloop.getLastStepVehicleIDs("LNS1"))
        for n in car:
            LNS1_car.append(n)
        car = list(traci.inductionloop.getLastStepVehicleIDs("LNS2"))
        for n in car:
            LNS2_car.append(n)
        car = list(traci.inductionloop.getLastStepVehicleIDs("LWE"))
        for n in car:
            LEW_car.append(n)
        car = list(traci.inductionloop.getLastStepVehicleIDs("LEW"))
        for n in car:
            LWE_car.append(n)
        #瞬時最大車流
        
    LSN1_num = len(list(set(LSN1_car)))
    LSN2_num = len(list(set(LSN2_car)))
    LNS1_num = len(list(set(LNS1_car)))
    LNS2_num = len(list(set(LNS2_car)))
    LWE_num = len(list(set(LWE_car)))
    LEW_num = len(list(set(LEW_car)))
    

        
    traci.close()
    # sys.stdout.flush()
    return([LSN1_num,LSN2_num,LNS1_num,LNS2_num,LWE_num,LEW_num])


def get_options():
    optParser = optparse.OptionParser()
    optParser.add_option("--nogui", action="store_true",
                         default=True, help="run the commandline version of sumo")
    options, args = optParser.parse_args()
    return options


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
    file = open("result.csv",'w')
    for n in result:
        file.write(str(n))
        file.write('\n')
    
