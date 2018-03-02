#!/usr/bin/python
## python template
import numpy as np
from numpy import arange

import cholesky as ch

class Matrix(ch.Matrix):
    '''
        variables
    '''
    n = 0

    def __init__(this, _n):  # This is the Constructor
        print "hello form constructor"
        this.n = _n
        this.val = np.zeros((this.n,this.n), dtype=float)        
    # end of __init__() constructor
    
    def __del__(this):  # This is the Destructor
        print 'bye form destructor'
    # end of __del__() destructor

    def print_size(this):
        print this.n
    # end of print_a

    def set_matrix(this):
        this.val[0,0]=  3.0
        this.val[1,0]=  1.0
        
        this.val[0,1]=  1.0
        this.val[1,1]=  3.0        
    # end of set_matrix
    
    def print_matrix(this):
        print this.val
    # end of print_matrix

    def invIter(this, x, eval):
        this.cholesky()
        for k in np.arange(0,9):
            this.solve(x)
            x=x/np.linalg.norm(x,np.inf)
            #print x
        # end for
        y=x
        this.solve(x) 
        x=x/np.linalg.norm(x,np.inf)               
        eval[0] = np.linalg.norm(y)/np.linalg.norm(x)
        return x
    # end of invIter()

# end of class MyClass    

def main():

    print ("This is main")
    n=2
    A=Matrix(n)
    
    
    eigvec =  np.zeros(n, dtype=float)
    eigval =  np.zeros(1, dtype=float)
    
    eigvec[0]=0.0
    eigvec[1]=1.0
    
    #A.print_size()
    A.set_matrix()
    A.print_matrix()
    
    eigvec = A.invIter(eigvec, eigval)
    
    print 'eigenvector: ', eigvec
    print 'eigenvalue : ', 1.0/eigval[0]
    
# end of main()    
    
if __name__ == '__main__':
    main()
# end if