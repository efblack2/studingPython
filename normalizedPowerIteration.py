#!/usr/bin/python
## python template
import numpy as np
from numpy import arange

class Matrix:
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

    def powIter(this, x, eval):
        y=np.zeros(this.n, dtype=float)
        for k in np.arange(0,9):
            y=this.val.dot(x)
            x=y/np.linalg.norm(y,np.inf)
            #print x
            eval[0] = x.dot(this.val.dot(x)) / x.dot(x)
            #print eval[0]
        # end for
        return x  
    # end of powIter()

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
    
    eigvec = A.powIter(eigvec, eigval)
    
    print 'eigenvector: ', eigvec
    print 'eigenvalue : ', eigval[0]
    
# end of main()    
    
if __name__ == '__main__':
    main()
# end if