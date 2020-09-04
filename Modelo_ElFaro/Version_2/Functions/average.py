import os
import matplotlib.pyplot as plt

def average_score(base_file_name, n_files, ROUNDS):
    cur_path = 'Modelo_ElFaro/Version_2/Functions'
    base_path = os.getcwd()[:-len(cur_path)-1]
    file_path = base_path+"Modelo_ElFaro/Version_2/results/"
    
    data = [0 for i in range(ROUNDS)]
    n_agents = 0
    for i in range(n_files):
        file_name = file_path+base_file_name+"_"+str(i)+".csv"
        #print(file_name)
        data_f = open(file_name,"r")
        data_f.readline()
        index = 0
        for line in data_f:
            v = list(map(int, line.split(",")[1:-1]))
            data[index] += sum(v)
            n_agents = len(v)
            index += 1
        data_f.close()
        
    for i in range(len(data)):
        data[i] = float(data[i]) / (n_files*n_agents)
    
    Out = open("av_score.dat", "w")
    for i in range(len(data)):
        Out.write("{0} {1}\n".format(i,data[i]))
    Out.close()
        

def plot_av():
    data = [[],[]]
    In = open("av_score.dat", "r")
    for line in In:
        v = list(map(float,line.split()))
        data[0].append(v[0])
        data[1].append(v[1])
    In.close()

    #Plot-----------------------------
    fig = plt.figure(figsize=(25,20), dpi=30)
    ax = fig.add_subplot(111)

    ax.plot(data[0],data[1])

    plt.show()
