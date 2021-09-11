from playsound import playsound

class Alphabets:
    '''This class contains patterns of all English Alphabets '''
    @staticmethod
    def a(self):

        Alphabets.playSound(self)

        for i in range(1):
            print(" " + (3) * "*" + " ", end="")
            print()
            for j in range(2):
                print("*" + (3) * " " + "*")
            for k in range(5):
                print("*", end="")
            print()
            for l in range(3):
                print("*" + 3 * " " + "*")
            print("A For Apple")

        Alphabets.mainmenu()

    @staticmethod
    def b(self):

        Alphabets.playSound(self)
        for i in range(4):
            print("*", end=" ")
        print()
        for j in range(2):
            print("*" + 7 * " " + "*")
        for i in range(4):
            print("*", end=" ")
        print()
        for j in range(2):
            print("*" + 7 * " " + "*")
        for i in range(4):
            print("*", end=" ")
        print("\nB For Ball")
        Alphabets.mainmenu()
    @staticmethod
    def c(self):

        Alphabets.playSound(self)
        for i in range(1):
            print(3 * " " + 4 * " *", end="")
            print()
            print(" " + "*")
        for j in range(3):
            print("*")
        for k in range(1):
            print(" " + "*")
            print(3 * " " + 4 * " *", end="")
        print("\nC For cat")
        Alphabets.mainmenu()
    @staticmethod
    def d(self):

        Alphabets.playSound(self)
        for i in range(5):
            print("*", end="")
        print()
        for j in range(6):
            print("*" + (5 - 1) * " " + "*")
        for k in range(5):
            print("*", end="")
        print("\nD For Doctor")
        Alphabets.mainmenu()
    @staticmethod
    def e(self):

        Alphabets.playSound(self)
        for i in range(5):
            print("*", end="")
        print()
        for j in range(2):
            print("*")
        for k in range(4):
            print("*", end="")
        print()
        for m in range(2):
            print("*")
        for l in range(5):
            print("*", end="")
        print("\nE For Elephant")
        Alphabets.mainmenu()

    @staticmethod
    def f(self):

        Alphabets.playSound(self)
        for i in range(5):
            print("*", end=" ")
        print()
        for j in range(2):
            print("*")
        for i in range(4):
            print("*", end=" ")
        print()
        for j in range(3):
            print("*")
        print("\nF For Frog")
        Alphabets.mainmenu()

    @staticmethod
    def g(self):

        Alphabets.playSound(self)
        for i in range(1):
            print(" " + (3) * "*" + " ", end="")
        print()
        for j in range(1):
            print("*" + (3) * " " + "*")
            print("*")
        for k in range(1):
            print("*" + " " + (3) * "*")
        for l in range(2):
            print("*" + (3) * " " + "*")
        for m in range(1):
            print(" " + (3) * "*" + " ", end="")
        print("\nG For Goat")
        Alphabets.mainmenu()

    @staticmethod
    def h(self):

        Alphabets.playSound(self)
        for i in range(3):
            print("*" + 7 * " " + "*")
        for j in range(5):
            print("*", end=" ")
        print()
        for i in range(3):
            print("*" + 7 * " " + "*")
        print("\nH For Horse")
        Alphabets.mainmenu()

    @staticmethod
    def i(self):

        Alphabets.playSound(self)
        for i in range(5):
            print("*", end=" ")
        print()
        for j in range(5):
            print(4 * " " + "*")
        for i in range(5):
            print("*", end=" ")
        print("\nI For Iron")
        Alphabets.mainmenu()

    @staticmethod
    def j(self):

        Alphabets.playSound(self)
        for i in range(5):
            print("*", end=" ")
        print()
        for j in range(2):
            print(4 * " " + "*")
        for i in range(2):
            print("*" + 3 * " " + "*")
        for i in range(5):
            print("*", end="")
        print("\nJ For Joker")
        Alphabets.mainmenu()

    @staticmethod
    def k(self):

        Alphabets.playSound(self)
        n = 4
        for i in range(4):
            print("*" + n * " " + "*")
            n -= 1
        n = 1
        for i in range(4):
            print("*" + n * " " + "*")
            n += 1
        print("\nK For King")
        Alphabets.mainmenu()

    @staticmethod
    def l(self):

        Alphabets.playSound(self)
        for i in range(6):
            print("*")
        for j in range(5):
            print("*", end="")
        print("\nL For Lion")
        Alphabets.mainmenu()
    @staticmethod
    def m(self):

        Alphabets.playSound(self)
        for i in range(2):
            print("*", 7 * " " + "*")
        for j in range(1):
            print("*" + " " + "*" + 4 * " " + "*" + " " + "*")
            print("*" + 3 * " " + "*" + 4 * " " + "*")
        for i in range(3):
            print("*", 7 * " " + "*")
        print("\nM For Mango")
        Alphabets.mainmenu()

    @staticmethod
    def n(self):

        Alphabets.playSound(self)
        v = 6
        n = 1
        for i in range(6):
            print("*" + n * " " + "*" + v * " " + "*")
            n += 1
            v -= 1
        print("\nN For Nose")
        Alphabets.mainmenu()

    @staticmethod
    def o(self):

        Alphabets.playSound(self)
        for i in range(1):
            print(" " + (3) * "*" + " ")
        for j in range(5):
            print("*" + (3) * " " + "*")
        for k in range(1):
            print(" " + (3) * "*" + " ")
        print("\nO For Onion")
        Alphabets.mainmenu()

    @staticmethod
    def p(self):

        Alphabets.playSound(self)
        for i in range(4):
            print("*", end="")
        print()
        for i in range(2):
            print("*" + 3 * " " + "*")
        for i in range(4):
            print("*", end="")
        print()
        for l in range(3):
            print("*")
        print("\nP For Pencil")
        Alphabets.mainmenu()

    @staticmethod
    def q(self):

        Alphabets.playSound(self)
        for i in range(1):
            print(4 * " *", end=" ")
        print()
        n = 0
        c = 7
        for j in range(6):
            print("*" + n * " " + "*" + c * " " + "*")
            n += 1
            c -= 1
        for k in range(5):
            print(" *", end="")
        print()
        for l in range(1):
            print(9 * " " + "*")
            print(10 * " " + "*")
        print("\nQ For Queen")
        Alphabets.mainmenu()

    @staticmethod
    def r(self):

        Alphabets.playSound(self)
        for i in range(4):
            print("*", end="")
        print()
        for i in range(2):
            print("*" + 3 * " " + "*")
        for i in range(4):
            print("*", end="")
        print()
        for l in range(1):
            print("*" + " " + "*")
            print("*" + 2 * " " + "*")
            print("*" + 3 * " " + "*")
        print("\nR For Rat")
        Alphabets.mainmenu()

    @staticmethod
    def s(self):

        Alphabets.playSound(self)
        for i in range(1):
            print(" " + 4 * "*", end="")
        print()
        for i in range(2):
            print("*")
        for i in range(1):
            print(" " + 3 * "*", end="")
        print()
        for i in range(2):
            print(4 * " " + "*")
        for i in range(4):
            print("*", end="")
        print("\nS For Super")
        Alphabets.mainmenu()
    @staticmethod
    def t(self):

        Alphabets.playSound(self)
        for i in range(5):
            print("*", end="")
        print()
        for i in range(6):
            print(2 * " " + "*")
        print("\nT For Tornado")
        Alphabets.mainmenu()
    @staticmethod
    def u(self):

        Alphabets.playSound(self)
        for i in range(6):
            print("*" + 3 * " " + "*")
        for i in range(1):
            print(" " + 3 * "*")
        print("\nU For Umbrella")
        Alphabets.mainmenu()

    @staticmethod
    def v(self):

        Alphabets.playSound(self)
        n = 5
        v = 1
        for i in range(5):
            print(v * " " + "*" + n * "  " + "*")
            n -= 1
            v += 1
        for i in range(1):
            print(6 * " " + 2 * "*", end="")
        print("\nV For Violin")
        Alphabets.mainmenu()

    @staticmethod
    def w(self):

        Alphabets.playSound(self)
        for i in range(1):
            print("*" + 10 * " " + 4 * "*" + 10 * " " + "*")
        v = 1
        c = 4
        m = 2
        for j in range(5):
            print(v * " " + "*" + c * "  " + "*" + m * "  " + "*" + c * "  " + "*")
            v += 1
            c -= 1
            m += 1
        print("\nW For World")
        Alphabets.mainmenu()
    @staticmethod
    def x(self):

        Alphabets.playSound(self)
        for i in range(2):
            print("*" + 3 * " " + "*")
        for i in range(1):
            print(" " + "*" + " " + "*")
            print(2 * " " + "*")
        for i in range(1):
            print(" " + "*" + " " + "*")
        for i in range(2):
            print("*" + 3 * " " + "*")
        print("\nX For X-Ray")
        Alphabets.mainmenu()

    @staticmethod
    def y(self):

        Alphabets.playSound(self)
        n = 5
        v = 1
        for i in range(5):
            print(v * " " + "*" + n * "  " + "*")
            n -= 1
            v += 1
        for i in range(5):
            print(6 * " " + 2 * "*")
        print("\nY For Yoga")
        Alphabets.mainmenu()

    @staticmethod
    def z(self):

        Alphabets.playSound(self)
        for i in range(7):
            print("*", end="")
        print()
        n = 5
        for j in range(5):
            print(n * " " + "*")
            n -= 1
        for i in range(7):
            print("*", end="")
        print("\nZ For Zebra")
        Alphabets.mainmenu()

    @staticmethod
    def playSound(alphabetName):
        try:
            playsound('E:/University Material/2nd Semester Material/Sounds/' + alphabetName + '.wav')
        except BaseException:
            pass

    @staticmethod
    def mainmenu():
        self = input("Write Any Alphabet to show it's Pattern:")

        if self.upper() == "A":
            Alphabets.a("A")

        elif self.upper() == "B":
            Alphabets.b("B")

        elif self.upper() == "C":
            Alphabets.c("C")

        elif self.upper() == "D":
            Alphabets.d("D")

        elif self.upper() == "E":
            Alphabets.e("E")

        elif self.upper() == "F":
            Alphabets.f("F")

        elif self.upper() == "G":
            Alphabets.g("G")

        elif self.upper() == "H":
            Alphabets.h("H")

        elif self.upper() == "I":
            Alphabets.i("I")

        elif self.upper() == "J":
            Alphabets.j("J")

        elif self.upper() == "K":
            Alphabets.k("K")

        elif self.upper() == "L":
            Alphabets.l("L")

        elif self.upper() == "M":
            Alphabets.m("M")

        elif self.upper() == "N":
            Alphabets.n("N")

        elif self.upper() == "O":
            Alphabets.o("O")

        elif self.upper() == "P":
            Alphabets.p("P")

        elif self.upper() == "Q":
            Alphabets.q("Q")

        elif self.upper() == "R":
            Alphabets.r("R")

        elif self.upper() == "S":
            Alphabets.s("S")

        elif self.upper() == "T":
            Alphabets.t("T")

        elif self.upper() == "U":
            Alphabets.u("U")

        elif self.upper() == "V":
            Alphabets.v("V")

        elif self.upper() == "W":
            Alphabets.w("W")

        elif self.upper() == "X":
            Alphabets.x("X")

        elif self.upper() == "Y":
            Alphabets.y("Y")

        elif self.upper() == "Z":
            Alphabets.z("Z")
c=Alphabets
c.mainmenu()





