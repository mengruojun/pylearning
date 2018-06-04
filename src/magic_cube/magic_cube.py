"""
File magic_cube.py
Author: Ruojun Meng

"""
class MagicCube(object) :
    """
    F: green  ['', 'y', 'r', 'g', 'g', 'g',' g', 'g','b','b']   === F[5] must be 'g'
    L: orange
    U: white
    R: red
    B: blue
    D: yellow


    """

    front = [
        [],
    ]

    def __init__(self, state):
        """
        :param state:
        state={
        'F' : ['y', 'r', 'g', 'g', 'g',' g', 'g','b','b']
        ....
        ....
        }
        """
        self.state = state
        self.U = state['U']
        self.F = state['F']
        self.L = state['L']
        self.R = state['R']
        self.B = state['B']
        self.D = state['D']

    """
    Turn Operations
    
    F,L,U,R,B,D  they are clockwise
    Fa,La,Ua,Ra,Ba,Da  they are anti-clockwise
    Fa=3*F and etc.
    
    """

    def f(self):
        self.clock_wise(self.F)
        temp1, temp2, temp3 = self.U[7], self.U[8], self.U[9]
        self.U[7], self.U[8], self.U[9] = self.L[9], self.L[6], self.L[3]
        self.L[9], self.L[6], self.L[3] = self.D[3], self.D[2], self.D[1]
        self.D[1], self.D[2], self.D[3] = self.R[7], self.R[4], self.R[1]
        self.R[7], self.R[4], self.R[1] = temp3, temp2, temp1

    def f_a(self):
        self.f()
        self.f()
        self.f()

    def clock_wise(self, arry):
        temp1, temp2, temp3 = arry[1], arry[2], arry[3]
        arry[1], arry[2], arry[3] = arry[7], arry[4], arry[1]
        arry[7], arry[4], arry[1] = arry[9], arry[8], arry[7]
        arry[9], arry[8], arry[7] = arry[3], arry[6], arry[9]
        arry[3], arry[6], arry[9] = temp1, temp2, temp3

    def print_state(self):
        for side in self.state:
            print(side + ":" + str(self.state[side]))

    """
    evaluate the value of the state
    """
    def value(self):
        pass


if __name__ == '__main__':
    test = MagicCube({
        'F': [' ', 'y', 'r', 'g', 'g', 'g', 'g', 'g', 'b', 'b'],
        'U': [' ','b', 'g', 'r', 'r', 'w', 'y', 'o', 'w', 'w'],
        'L': [' ','w', 'b', 'b', 'r', 'o', 'y', 'y', 'o', 'w'],
        'R': [' ','r', 'o', 'y', 'o', 'r', 'y', 'r', 'b', 'r'],
        'B': [' ','b', 'w', 'o', 'b', 'b', 'y', 'y', 'g', 'g'],
        'D': [' ','o', 'o', 'w', 'w', 'y', 'w', 'o', 'r', 'g']
    })

    test.print_state()

    test.f()
    print("f()1")

    test.print_state()

    print("f()2")
    test.f()
    test.print_state()

    print("f()3")
    test.f()
    test.print_state()


    print("f()4")
    test.f()
    test.print_state()

