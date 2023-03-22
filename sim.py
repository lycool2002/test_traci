from __future__ import absolute_import
from __future__ import print_function

import os
import sys
import optparse
import random
from sumolib import checkBinary  # noqa
import traci  # noqa


def run(program):
    speed = []
    traci.trafficlight.setProgram('J1',program)
    
    while traci.simulation.getTime() < 600:
        tmp =[]
        traci.simulationStep()
        tmp.append(traci.edge.getLastStepMeanSpeed('E0'))
        tmp.append(traci.edge.getLastStepMeanSpeed('-E0'))
        tmp.append(traci.edge.getLastStepMeanSpeed('E1'))
        tmp.append(traci.edge.getLastStepMeanSpeed('-E1'))
        tmp.append(traci.edge.getLastStepMeanSpeed('E2'))
        tmp.append(traci.edge.getLastStepMeanSpeed('-E2'))
        tmp.append(traci.edge.getLastStepMeanSpeed('E3'))
        tmp.append(traci.edge.getLastStepMeanSpeed('-E3'))
        speed.append(tmp)
    

        
    traci.close()
    return speed
    # sys.stdout.flush()

def sim(program):
    traci.start([sumoBinary, "-c", "data/test.sumocfg"])
    speed = run(program)
    avg = [0,0,0,0,0,0,0,0]
    for a in range(len(speed)):
        for b in range(8):
            avg[b] += speed[a][b]

    for c in range(8):
            avg[c] /= len(speed)
    return(avg)
    

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

    avg = []
    avg.append(sim(1))
    avg.append(sim(2))
    avg.append(sim(3))
    avg.append(sim(4))

    
    file = open("speed.csv",'w')
    for n in range(len(avg)):
        for a in range(7):
            file.write(str(avg[n][a])+', ')
        file.write(str(avg[n][7])+'\n')
    file.write('\n')

    
