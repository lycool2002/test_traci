#實際測量
sat = [2400,2400] #飽和車流(phase0,1,2,3)車/小時
maximum = [1200,800 ] #最大車流(phase0,1,2,3)車/小時
lost = [2,2] #損耗時間(phase0,1,2,3)秒
##########
#飽和車流大概3600/1.5=2400 (時速50以下) 2.5(車流過大時)
R=4 #全紅燈時間
lost_all = sum(lost)+R #總損耗時間
rate = [0,0] #車流比

for i in range(2):
    rate[i] = maximum[i]/sat[i]


p = ((1.5*lost_all)+5)/(1-sum(rate))#號誌周期
time_phase = [0,0]#分配的時間

for i in range(2):#車流比
    time_phase[i] = (p-R)*(maximum[i]/sum(maximum))

file = open("trafficlight.xml",'w')
file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
file.write('<additional>\n')
file.write('    <tlLogic id="J1" type="static" programID="1" offset="0">\n')
file.write('         <phase duration="' + str(int(time_phase[0])) + '" state="rrrrrGGGgrrrrrGGGg"/>\n')  
file.write('         <phase duration="' + str(int(R/2)) + '" state="rrrrryyyyrrrrryyyy"/>\n')   
file.write('         <phase duration="' + str(int(time_phase[1])) + '" state="GGGggrrrrGGGggrrrr"/>\n')  
file.write('         <phase duration="' + str(int(R/2)) + '" state="yyyyyrrrryyyyyrrrr"/>\n')   
file.write('     </tlLogic>\n')
file.write('</additional>\n')
