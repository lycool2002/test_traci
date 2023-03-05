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
    


    #飽和流率是假設在連續不斷的車流抵達情況下，且有100％綠燈通行時間，每小時可通過路口的車輛數(輛/小時)
    while traci.simulation.getTime() < 600:
        
        traci.simulationStep()
        
        traci.trafficlight.setProgram('J1',0)#設為一直綠燈
    

        
    traci.close()
    # sys.stdout.flush()


def get_options():
    optParser = optparse.OptionParser()
    optParser.add_option("--nogui", action="store_true",
                         default=False, help="run the commandline version of sumo")
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

    run()
    
