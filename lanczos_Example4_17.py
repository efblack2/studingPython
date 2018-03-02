#!/usr/bin/python
## python template
import numpy as np
from numpy import arange
import sys

from numpy import linalg as LA

import matplotlib.pyplot as plt


class Matrix():
    '''
        variables
    '''

    def __init__(this, _n):  # This is the Constructor
        print "hello form constructor"
        this.n = _n
        this.val = np.zeros((this.n,this.n), dtype=float)
        '''
        this.qold = np.zeros((this.n), dtype=float)        
        this.beta = 0.0
        this.alpha = 0.0
        '''
    # end of __init__() constructor
    
    def __del__(this):  # This is the Destructor
        print 'bye form destructor'
    # end of __del__() destructor

    def print_size(this):
        print this.n
        print this.k
    # end of print_a


    def rvs(this, dim):
         random_state = np.random
         H = np.eye(dim)
         D = np.ones((dim,))
         for n in range(1, dim):
             x = random_state.normal(size=(dim-n+1,))
             D[n-1] = np.sign(x[0])
             x[0] -= D[n-1]*np.sqrt((x*x).sum())
             # Householder transformation
             Hx = (np.eye(dim-n+1) - 2.*np.outer(x, x)/(x*x).sum())
             mat = np.eye(dim)
             mat[n-1:, n-1:] = Hx
             H = np.dot(H, mat)
             # Fix the last sign such that the determinant is 1
         D[-1] = (-1)**(1-(dim % 2))*D.prod()
         # Equivalent to np.dot(np.diag(D), H) but faster, apparently
         H = (D*H.T).T
         return H
 

    def set_matrix(this):
        q = np.zeros((this.n,this.n), dtype=float)
        temp = np.zeros((this.n,this.n), dtype=float)
        evec = np.zeros((this.n), dtype=float)
        for i in np.arange(0,this.n):
            evec[i]=i+1
        # end for
        
        q = this.rvs(this.n)
        
        for i in np.arange(0,this.n):
            temp[i,:] = evec[i]*q[i,:]
        # end for
        this.val = np.matmul(q.transpose(), temp)
    # end of set_matrix
    
    def print_matrix(this):
        print 'A:'
        print  this.val
        
        #print this.val[:,1]
    # end of print_matrix

    def lanczos(this, kk):
        alpha = np.zeros((kk), dtype=float)
        beta = np.zeros((kk), dtype=float)
        q = np.zeros((this.n,kk), dtype=float)
        q[0,0]=1.0

        print 'in lanczos'
        q[:,0]=q[:,0] / np.linalg.norm(q[:,0])
        for k in np.arange(0,kk):
            u=this.val.dot(q[:,k])
            alpha[k] = q[:,k].dot(u)
            if (k>0):
                u = u -  beta[k-1]*q[:,k-1] - alpha[k]*q[:,k]
            else:
                u = u - alpha[k]*q[:,k]
            # end if 
            if (k < kk-1):
                beta[k] = np.linalg.norm(u)
                if (beta[k] == 0.0):
                    print 'quiting'
                    #sys.exit()
                    continue
                # end if
                q[:,k+1] = u/beta[k]
            # end if
        # end for 
        
        H = np.zeros((kk,kk), dtype=float)
        for i in np.arange(0,kk):
            H[i,i]= alpha[i]
            if (i < kk-1):
                H[i+1,i]= beta[i]
                H[i,i+1]= beta[i]
            # end if
        # end for
        return H
        
        
    # end of lanczos()

# end of class MyClass    

def main():
    
    print ("This is main")
    n=29
    A=Matrix(n)
    
    plt.axis([0, n+1, 0, n+1])
    #A.print_size()
    A.set_matrix()
    #A.print_matrix()
    print "results"
    for k in np.arange(1,n+1):
        H = A.lanczos(k)
        w, v = LA.eig(H)
        
        x = np.zeros((k), dtype=float)
        for i in np.arange(0,k):
            x[i] = w[i]
        # end for
        
        y = np.zeros((k), dtype=float)
        for i in np.arange(0,k):
            y[i]=k
        # end for
        plt.plot(x, y, 'b+')
    # end if
    plt.show()
    
    
    '''    
    print H
    w, v = LA.eig(H)
    print 
    print w
    print 
    print
    w, v = LA.eig(A.val)
    print 
    print w
    '''
    
# end of main()    
    
if __name__ == '__main__':
    main()
# end if