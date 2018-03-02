#!/usr/bin/python
## python template
import numpy as np
from numpy import arange
import sys

from numpy import linalg as LA

class Matrix():
    '''
        variables
    '''

    def __init__(this, _n, _k):  # This is the Constructor
        print "hello form constructor"
        this.n = _n
        this.k = _k
        this.val = np.zeros((this.n,this.n), dtype=float)
        this.alpha = np.zeros((this.k), dtype=float)
        this.beta = np.zeros((this.k), dtype=float)
        this.q = np.zeros((this.n,this.k), dtype=float)
        this.q[0,0]=1.0
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

    def set_matrix(this):
        '''
        for i in np.arange(0,this.n):
            this.val[i,i]=i+1
        # end for     
        '''
        this.val[0,0]=  2.9766
        this.val[1,0]=  0.3945
        this.val[2,0]=  0.4198
        this.val[3,0]=  1.1159
        
        this.val[0,1]= this.val[1,0]
        this.val[1,1]=  2.7328
        this.val[2,1]= -0.3097
        this.val[3,1]=  0.1129

        this.val[0,2]=  this.val[2,0]
        this.val[1,2]=  this.val[2,1] 
        this.val[2,2]=  2.5675
        this.val[3,2]=  0.6079

        this.val[0,3]= this.val[3,0]  
        this.val[1,3]= this.val[3,1]  
        this.val[2,3]= this.val[3,2]  
        this.val[3,3]=  1.7231

        
    # end of set_matrix
    
    def print_matrix(this):
        print 'A:'
        print  this.val
        
        #print this.val[:,1]
    # end of print_matrix

    def lanczos(this):
        print 'in lanczos'
        this.q[:,0]=this.q[:,0] / np.linalg.norm(this.q[:,0])
        for k in np.arange(0,this.k):
            u=this.val.dot(this.q[:,k])
            this.alpha[k] = this.q[:,k].dot(u)
            if (k>0):
                u = u -  this.beta[k-1]*this.q[:,k-1] - this.alpha[k]*this.q[:,k]
            else:
                u = u - this.alpha[k]*this.q[:,k]
            # end if 
            
            if (k < this.k-1):
                this.beta[k] = np.linalg.norm(u)
                if (this.beta[k] == 0.0):
                    sys.exit()
                # end if
                this.q[:,k+1] = u/this.beta[k]
            # end if
        # end for 
    # end of lanczos()

# end of class MyClass    

def main():

    print ("This is main")
    n=4
    k=2
    A=Matrix(n,k)
    
    
    #A.print_size()
    A.set_matrix()
    A.print_matrix()
    
    A.lanczos()
    
    print "results"
    print 
    print A.alpha
    print A.beta
    H = np.zeros((k,k), dtype=float)
    
    for i in np.arange(0,k):
        H[i,i]= A.alpha[i]
        if (i < k-1):
            H[i+1,i]= A.beta[i]
            H[i,i+1]= A.beta[i]
        # end if
    # end for
    
    
    #A.print_matrix()
    
    w, v = LA.eig(H)
    print 
    print w
    w, v = LA.eig(A.val)
    print 
    print w
    
    
# end of main()    
    
if __name__ == '__main__':
    main()
# end if