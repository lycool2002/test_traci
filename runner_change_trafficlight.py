from __future__ import absolute_import
from __future__ import print_function

import os
import sys
import optparse
import random
from sumolib import checkBinary  # noqa
import traci  # noqa


def run():
    
    while traci.simulation.getTime() < 600:
        
        traci.simulationStep()
        
        traci.trafficlight.setProgram('J1',0)#改週期
    

        
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
    
