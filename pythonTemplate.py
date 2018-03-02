#!/usr/bin/python
## python template

class MyClass:

    def __init__(this):  # This is the Constructor
        print "hello form constructor"
        this.a = 1.0
        this.b = 2.0
    # end of __init__() constructor

    def __del__(this):  # This is the Destructor
        print 'bye form destructor'
    # end of __del__() destructor

    def print_a(this):
        print this.a
    # end of print_a

    def print_b(this):
        print this.b
    # end of print_b

# end of class MyClass

def main():
    print ("This is main")
    edgar=MyClass()
    edgar.print_a()
    edgar.print_b()
# end of main()

if __name__ == '__main__':
    main()
# end if
