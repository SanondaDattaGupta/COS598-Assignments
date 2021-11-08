import numpy as np
import random as rd
import statistics as stat
import matplotlib.pyplot as plt

def predictiondata(Vector_A,Guess_W):
    predict_X=[]
    n=len(Vector_A)
    i = 0
    while i<n:
        #print(i)
        if i == 0: 
            if (Vector_A[i]==0):
                predict_X.append(0)
            if (Vector_A[i]==1):
               # result=np.random.binomial(1,0.5)
                predict_X.append(Guess_W[i])
            if (Vector_A[i]==2):
                predict_X.append(1)
        else:
            if (Vector_A[i]-Vector_A[i-1]==0):
                predict_X.append(0)
            elif (Vector_A[i]-Vector_A[i-1]==1):
                if(i<n-1 and Vector_A[i+1]-Vector_A[i]==-1):
                    predict_X.append(0)
                else:
                   # result=np.random.binomial(1,0.5)
                    predict_X.append(Guess_W[i])
            elif(Vector_A[i]-Vector_A[i-1]==2):
                predict_X.append(1)
            else:
                #result=np.random.binomial(1,0.5)
                predict_X.append(Guess_W[i])
        i=i+1
    return predict_X


def calculatestdv(Vector_A,Vector_X,Guess_W):
    fractionlist=[]
    
    for i in range (0,20):
        Predicted_X=predictiondata(Vector_A,Guess_W)
      #  print("Predicted data",Predicted_X)
        count = 0
        for i in range (len(Vector_A)):
            if (Vector_X[i]==Predicted_X[i]):
                count=count+1
        fraction=count/len(Vector_X)
        fractionlist.append(fraction)
    
       
    return np.std(fractionlist), np.mean(fractionlist)

def mainprogram(n):
    X=[]
    A=[]

   # n=100

    for i in range (0,n):
        X.append(rd.randint(0, 1))
    Vector_X= np.array(X)
    #print(Vector_X)
    Guess_W =[] 
    #probability=[]*3
    for i in range (0,n):
        #print(Vector_X[i])
        probability=[]
        for j in range (0,3):
            probability.append(rd.randint(0, 1))
        #print(probability)
        #print(sum(probability))
        if(sum(probability)>1):

            Guess_W.append(Vector_X[i])
           # print("guess with prob, vector:",Vector_X[i],"guess array",Guess_W)
        else:
            #print(1-Vector_X[i])
            Guess_W.append(np.random.binomial(1,0.67))
           # print("guess without prob, vector:",Vector_X[i], " guess array:",Guess_W)

   # print(np.array(Guess_W))

    for i in range (0,n):
        #flip_calculate = calculateflip(i+1)
        result = np.random.binomial(1,0.5)
        Counter=sum(Vector_X[0:i+1])+result 
       # print(result)

        A.append(Counter)

    Vector_A=np.array(A)
    #print("Actual data of the Counter",Vector_A)

    std,mean=calculatestdv(Vector_A,Vector_X,Guess_W)
    #print("Actual data of the Counter",Predicted_X)
   # print("Standard Deviation and Mean: ",std, mean) 
    return std, mean




n=[100,500,100,5000]
error=[]
CTEs=[]
#print(n[0])
for i in range (0,len(n)):
    std,mean = mainprogram(n[i])
    CTEs.append(mean)
    error.append(std)
print("Mean for each n",CTEs)
print("Standard Deviation for each n",error )


labels = ['n=100', 'n=500', 'n=1000', 'n=5000']

x_pos = np.arange(len(labels))


# Build the plot
fig, ax = plt.subplots()
ax.bar(x_pos, CTEs,
       yerr=error,
       align='center',
       alpha=0.5,
       ecolor='black',
       capsize=10)
ax.set_ylabel('')
ax.set_xticks(x_pos)
ax.set_xticklabels(labels)
ax.set_title('Fraction of bits of x recovered by my algorithm for n = 100, 500, 1000, 5000')
ax.yaxis.grid(True)

# Save the figure and show
plt.tight_layout()
plt.savefig('bar_plot_with_error_bars.png')
plt.show()
