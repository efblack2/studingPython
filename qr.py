#!/usr/bin/python
## python template
import numpy as np
from numpy import arange

class Matrix:
    '''
        variables
    '''
    m = 0
    n = 0

    def __init__(this, _m, _n):  # This is the Constructor
        print "hello form constructor"
        this.m = _m
        this.n = _n
        this.val = np.zeros((this.m,this.n), dtype=float)
    # end of __init__() constructor
    
    def __del__(this):  # This is the Destructor
        print 'bye form destructor'
    # end of __del__() destructor

    def print_size(this):
        print this.m
        print this.n
    # end of print_a
    


    def set_matrix(this):
        this.val[0,0]=  1
        this.val[1,0]=  0
        this.val[2,0]=  0
        this.val[3,0]= -1
        this.val[4,0]= -1
        this.val[5,0]=  0
        
        this.val[0,1]=  0
        this.val[1,1]=  1
        this.val[2,1]=  0
        this.val[3,1]=  1
        this.val[4,1]=  0
        this.val[5,1]= -1
        
        this.val[0,2]=  0
        this.val[1,2]=  0
        this.val[2,2]=  1
        this.val[3,2]=  0
        this.val[4,2]=  1
        this.val[5,2]=  1
        
    # end of set_matrix
    
    def print_matrix(this):
        print this.val
    # end of print_matrix

    def QR(this, b):

        for col in np.arange(0,this.n):
            size=this.m-col
            e=np.zeros((size), dtype=float)
            v=np.zeros((size), dtype=float)
            e[0]=1.0
            
            ak= -np.sign(this.val[col,col])* np.linalg.norm(this.val[col:this.m,col])
            v=this.val[col:this.m,col] - ak*e
            #print "v: ", v
            tmp = np.dot(v,v)
            b[col:this.m] = b[col:this.m] - 2.0* np.dot( v,b[col:this.m] ) /tmp * v 
            
            if (tmp != 0):
                for row in np.arange(col,this.n):
                    tmp2 = np.dot( v,this.val[col:this.m,row] ) 
                    #print tmp2
                    this.val[col:this.m,row] = this.val[col:this.m,row] - 2.0*tmp2/tmp * v
                    #print "           new a: ", this.val[col:this.m,row]
                # end for 'row'
            # end if
        # end for 'col'
    # end of QR()
# end of class MyClass    



def main():

    print ("This is main")
    m=6    
    n=3
    b=np.zeros((m), dtype=float)
    b[0]= 1237
    b[1]= 1941
    b[2]= 2417
    b[3]=  711
    b[4]= 1177
    b[5]= 475
    
    A=Matrix(m,n)
    #A.print_size()
    A.set_matrix()
    A.print_matrix()
    
    
    A.QR(b)
    
    A.print_matrix()
    print b
    
    return (0)
# end of main()    
    
if __name__ == '__main__':
    main()
# end if
