#實際測量
sat = [1250,1000] #飽和車流(phase0,1,2,3)車/小時
maximum = [400,250 ] #最大車流(phase0,1,2,3)車/小時
lost = [2,2] #損耗時間(phase0,1,2,3)秒
##########
R=12 #全紅燈時間
lost_all = sum(lost)+R #總損耗時間
rate = [0,0] #車流比

for i in range(2):
    rate[i] = maximum[i]/sat[i]

p = ((1.5*lost_all)+5)/(1-sum(rate))#號誌周期
time_phase = [0,0]#分配的時間

for i in range(2):#車流比
    time_phase[i] = (p-R)*(maximum[i]/sum(maximum))

file = open("trafficlight.xml",'w')
file.write('<additional>\n')
file.write('  <tlLogic id="J1" programID="my_program" offset="0" type="static">\n')
file.write('     <phase duration="' + str(time_phase[0]) + '" state="rrrrrGGGgrrrrrGGGg"/>\n')   
file.write('     <phase duration="' + str(time_phase[1]) + '" state="GGGggrrrrGGGggrrrr"/>\n')                   
file.write('  </tlLogic>\n')
file.write('<additional>\n')
