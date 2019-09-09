import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sps


def exo1():

    n=10

    if n==1:
        print(0)
    else:
        tas_de_cartes=[k for k in range(n)]
    
        while len(tas_de_cartes)>2:
            print (tas_de_cartes[0])
            tas_de_cartes.append(tas_de_cartes[1])
            tas_de_cartes=tas_de_cartes[2:]
        
        print(tas_de_cartes[0])
        print(tas_de_cartes[1])


def exo2():
    
    a=20*np.pi
    n=int(1e3)
    x1=np.linspace(0,a,n)[1:]
    x=list(-x1[::-1])+[0]+list(x1)

    y1=np.sin(x1)/x1
    y=list(y1[::-1])+[1]+list(y1)
    
    plt.plot(x,y,color="r",label="y=sinc(x)")
    plt.axis([-a,a,-.25,1.1])
    plt.xlabel("x")
    plt.ylabel("sin(x)/x")
    plt.legend(loc='best')
    plt.title("Courbe de la fonction sinus cardinal")
    plt.show()


def exo3():

    n=int(1e3)
    X=2*np.random.rand(n)-1
    S=np.cumsum(X)/np.arange(1,n+1)
    plt.plot(range(1,n+1),S,'r',label="S_n")
    plt.plot((1,n),(0,0),"b--",label="Esperance")
    plt.xlabel("n")
    plt.legend(loc='best')
    plt.title("LGN")
    plt.show()


def exo4():


    n=int(1e3)
    Y=np.tan(np.pi*.5*(2*np.random.rand(n)-1))
    S=np.cumsum(Y)/np.arange(1,n+1)
    plt.plot(range(1,int(n)+1),S,'r',label="S_n")
    plt.plot((1,n),(0,0),"b--",label="y=0")
    plt.xlabel("n")
    plt.legend(loc='best')
    plt.title("LGN pour v.a. de Cauchy ?")
    plt.show()



def exo5():

    n,m=int(1e3),int(1e4)
    sigma=3**(-.5)
    X=2*np.random.rand(m,n)-1
    S=np.sum(X,axis=1)/(np.sqrt(n)*sigma)
    M=max(np.abs(S))
    x=np.linspace(-M,M,1000)
    y=sps.norm.pdf(x)
    plt.plot(x,y,'r',label="Densite")
    plt.hist(S,bins=int(round(m**(1./3)*M*.5)),density=1,histtype='step',label="Histogramme")
    plt.legend(loc='best'),plt.title("TCL")
    plt.show()


def exo6():

    n=int(1e5)
    x=np.linspace(-2,2,1000)
    y=.25*(2-np.abs(x))
    plt.plot(x,y,"r",label="Densite")
    
    X=2*np.random.rand(2,n)-1
    plt.hist(X[0,:]+X[1,:],bins=round(n**(1./3)),density=1,histtype='step',label="Histogramme")
    plt.legend(loc='best')
    plt.show()


def exo7():

    n=int(1e5)
    X=np.random.exponential(size=(2,n))
    S=X[0,:]+X[1,:]
    M=max(S)
    plt.hist(S,bins=round(n**(1./3)),density=1,histtype='step',label="Histogramme")
    x=np.linspace(0,M,1000)
    y=x*np.exp(-x)
    plt.plot(x,y,"r",label="Densite")
    plt.legend(loc='best')
    plt.show()



def exo8():

    t = 10.
    shape = 1.
    scale = 4.
    n = int(1e5)
    
    X = np.random.gamma(shape, scale, size=n)
    X_c = X[X > t] - t
    x = np.linspace(0., max(X_c), 1000)
    f_x = sps.gamma.pdf(x, a=shape, scale=scale)
    
    plt.hist(X_c, density=True, bins=round(2*len(X_c)**(1./3)),histtype='step',label="Histogramme" )
    plt.plot(x, f_x, "r")
    plt.title("Loi empirique de (X | X > t) - t pour X de loi exponentielle d'intensite " + str(1./scale))
    plt.show()


def exo9():
    
    n = 1000
    p = 0.005
    mu = p * n
    print 
    print("n * p^2 =", n*p*p)
    
    
    x = np.arange(0, 7*mu)
    distrib_poisson = sps.poisson.pmf(x, mu)
    distrib_binom = sps.binom.pmf(x, n, p) 
    
    plt.stem(x, distrib_poisson, label="Poisson",markerfmt='b.', basefmt="b")
    plt.stem(x + 0.3, distrib_binom, "r", markerfmt='r.',  label="binomiale")
    plt.legend()
    plt.show()

