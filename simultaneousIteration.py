#!/usr/bin/python
## python template
import numpy as np
from numpy import arange

class Matrix():
    '''
        variables
    '''
    n = 0
    tolerance = 1.0e-3
        

    def __init__(this, _n):  # This is the Constructor
        print "hello form gms constructor"
        this.n = _n
        this.val = np.zeros((this.n,this.n), dtype=float)
        this.x = np.zeros((this.n,this.n), dtype=float)
        #this.r = np.zeros((this.n,this.n), dtype=float)
    # end of __init__() constructor
    
    def __del__(this):  # This is the Destructor
        print 'bye form destructor'
    # end of __del__() destructor

    def print_size(this):
        print this.n
    # end of print_a

    def set_matrix(this):
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

        #this.x = this.val
        this.x = np.identity(this.n)
    # end of set_matrix
    
    def print_matrix(this):
        print this.val
        print this.x
        #print this.r
    # end of print_matrix
    
    def mod_gs(this):
        for col in np.arange(0,this.n):
            rkk=np.linalg.norm(this.x[:,col])
            if (rkk != 0):
                this.x[:,col] = this.x[:,col]/rkk
                for row in np.arange(col+1,this.n):
                    rkj = np.dot( this.x[:,col],this.x[:,row] )
                    this.x[:,row]=this.x[:,row] - rkj*this.x[:,col]
                # end for 'row'
            # end if
        # end for 'col'
    # end of mod_gs()
    

    def sim_iter(this):
        X=np.zeros((this.n), dtype=float)
        eigval=np.zeros((this.n), dtype=float)
        for k in np.arange(0,10):
            this.mod_gs()
            this.x=np.matmul(this.val, this.x)
            for col in np.arange(0,this.n):
                this.x[:,col]=this.x[:,col]/np.linalg.norm(this.x[:,col]) 
            # end for
        # end for
            
        for col in np.arange(0,this.n):
            X=this.x[:,col]
            eigval[col] = X.dot(this.val.dot(X)) / X.dot(X) 
        #end for
                
        return eigval
    # end of sim_iter()

# end of class MyClass    

def main():

    print ("This is main")
    n=4
    eigval=np.zeros((n), dtype=float)
    A=Matrix(n)
    
    
    #A.print_size()
    A.set_matrix()
    print "start"
    A.print_matrix()
    eigval = A.sim_iter()
    
    print "results"
    A.print_matrix()
    print eigval
    
    
    #eigvec = A.raylQuoIter(eigvec, eigval)
    
    #print 'eigenvector: ', eigvec
    #print 'eigenvalue : ', eigval[0]
    
# end of main()    
    
if __name__ == '__main__':
    main()
# end if