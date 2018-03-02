#!/usr/bin/python
## python template
import numpy as np
from numpy import arange

import gaussLU as lu

class Matrix(lu.Matrix):
    '''
        variables
    '''
    n = 0
    tolerance = 1.0e-3

    def __init__(this, _n):  # This is the Constructor
        print "hello form RH constructor"
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

    def raylQuoIter(this, x, eval):  
        A=Matrix(this.n)                
        sigma0 = 0.0
        sigma = 1.0
        counter=0
        while abs(sigma0-sigma) > this.tolerance :
            counter=counter+1
            sigma0=sigma           
            sigma = x.dot(this.val.dot(x)) / (x.dot(x))
            A.val = this.val - sigma*np.identity(this.n)
            A.gaussLU()
            A.solve(x)
            x=x/np.linalg.norm(x,np.inf)
            #print x
        # end while
        eval[0] = sigma
        print 'number of irerations: ', counter
        return x
    # end of raylQuoIter()

# end of class MyClass    

def main():

    print ("This is main")
    n=2
    A=Matrix(n)
    
    
    eigvec =  np.zeros(n, dtype=float)
    eigval =  np.zeros(1, dtype=float)
    
    eigvec[0]=np.random.random_sample()
    eigvec[1]=np.random.random_sample()
    print 'inital vector: ',  eigvec
    
    
    #A.print_size()
    A.set_matrix()
    
    A.print_matrix()
    
    eigvec = A.raylQuoIter(eigvec, eigval)
    
    print 'eigenvector: ', eigvec
    print 'eigenvalue : ', eigval[0]
    
# end of main()    
    
if __name__ == '__main__':
    main()
# end if