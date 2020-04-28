import matplotlib.pyplot as plt

class ShearDiagram():

    def __init__(self, beam_length):
        self.__beam_length = beam_length;
        # the index of each list represents the point on the beam!
        self.__loads = [] #list of tuples (int, float)
        self.__supports = [] #list of tuples (int, float)

        for i in range(0, beam_length):
            self.__loads.append((-1, -1))
            self.__supports.append((-1, -1))

    def add_load(self):
        print("Load Types:")
        print("1. Triangular")
        print("2. Rectangular")
        print("3. Point")
        print("4. Free Moment\n")

        load_type = 0
        while (load_type > 4 or load_type < 1):
            load_type = int(input("What type of load is this? "))

        load_pos = -1
        while (load_pos > self.__beam_length or load_pos < 0):
            load_pos = int(input("What is the X position of the load? "))

        load_force = float(input("What is the force of the load (kN)? "))

        self.__loads[load_pos] = (load_type, load_force)

    def add_support(self):
        print("Support Types:")
        print("1. Pin")
        print("2. Roller")
        print("3. Fixed\n")

        support_type = 0

        while (support_type > 3 or support_type < 1):
            support_type = int(input("What type of support is this? "))

        support_pos = -1
        while (support_pos > self.__beam_length or support_pos < 0):
            support_pos = int(input("What is the X position of the support? "))

        support_force = float(input("What is the force of the support (kN)? "))

        self.__supports[support_pos] = (support_type, support_force)

    def plot(self):
        cur_x = 0
        cur_y = 0
        x_vals = []
        y_vals = []

        for i in range(0, self.__beam_length):
            x_vals.append(i)
            y_vals.append(cur_y)

            support = self.__supports[i]
            load = self.__loads[i]

            if (support[0] > -1):
                cur_y += support[1]


            if (load[0] > -1):
                cur_y -= load[1]

            x_vals.append(i)
            y_vals.append(cur_y)

        plt.plot(x_vals, y_vals)
        plt.show()

class MomentDiagram():

    def __init__(self, beam_length):
        self.__beam_length = beam_length;
        self.__loads = list() #list of tuples (int, float, float)
        self.__supports = list() #list of tuples (int, float)
        self.__moments = list() #list of floats

    def __str__(self):
        retStr = "\nBeam Length: " + str(self.__beam_length) + " meters\n\n"
        retStr += "Loads:\n"
        for load in self.__loads:
            retStr += "(Type: " + str(load[0]) + ", X: " + str(load[1]) + ", Magnitude: "+ str(load[2]) + "kN)\n"

        retStr += "\nSupports:\n"
        for sup in self.__supports:
            retStr += "(Type: " + str(sup[0]) + ", X: " + str(sup[1]) + ")\n"

        retStr += "\nMoments:\n"
        for moment in self.__moments:
            retStr += str(moment) + " kN/m\n"

        return retStr

    def add_load(self):
        print("Load Types:")
        print("1. Triangular")
        print("2. Rectangular")
        print("3. Point")
        print("4. Free Moment\n")

        load_type = 0
        while (load_type > 4 or load_type < 1):
            load_type = int(input("What type of load is this? "))

        load_pos = -1
        while (load_pos > self.__beam_length or load_pos < 0):
            load_pos = float(input("What is the X position of the load? "))

        load_force = float(input("What is the force of the load (kN)? "))

        self.__loads.append((load_type, load_pos, load_force))

    def add_support(self):
        print("Support Types:")
        print("1. Pin")
        print("2. Roller")
        print("3. Fixed\n")

        support_type = 0

        while (support_type > 3 or support_type < 1):
            support_type = int(input("What type of support is this? "))

        support_pos = -1
        while (support_pos > self.__beam_length or support_pos < 0):
            support_pos = float(input("What is the X position of the support? "))

        self.__supports.append((support_type, support_pos))

    def add_moment(self):
        moment = float(input("What is the moment you'd like to add (kN/m)? "))
        self.__moments.append(moment)
