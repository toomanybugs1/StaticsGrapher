import matplotlib.pyplot as plt

class ShearDiagram():

    def __init__(self, beam_length):
        self.__beam_length = beam_length;
        # the index of each list represents the point on the beam!
        self.__loads = [] #list of tuples (int, float)
        self.__supports = [] #list of tuples (int, float)

        for i in range(0, beam_length + 1):
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

        # Point, most simple
        if (load_type == 3):
            self.__loads[load_pos] = (load_type, load_force)
            return

        # Rectangular, distributes by creating multiple points
        if (load_type == 2):
            base = int(input("What is the base length of this rectangular load? "))
            for i in range(load_pos, load_pos + base):
                self.__loads[i] = (2, load_force)
            return

        # Triangular has two cases: right loading and left loading
        if (load_type == 1):
            base = int(input("What is the base length of this Triangular load? "))
            left_right = 0
            while (left_right != "1" and left_right != "2"):
                print("Is the larger force on the: ")
                print("1. Left Side")
                print("2. Right Side")
                left_right = input("Enter your selection: ")

            if (left_right == "1"):
                x_val = 0
                for i in range(load_pos, load_pos + base):
                    new_y = -((load_force / base) * x_val) + load_force
                    print("Left " + str(new_y))
                    self.__loads[i] = (1, new_y)
                    x_val += 1
                return

            else:
                x_val = 0
                for i in range(load_pos, load_pos + base):
                    new_y = (load_force / base) * x_val
                    print("Right " + str(new_y))
                    self.__loads[i] = (1, new_y)
                    x_val += 1
                return


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

    # SHEAR GRAPH PLOTTER
    def plot_shear(self):
        plt.subplot(1, 2, 1)

        cur_x = 0
        cur_y = 0
        x_vals = []
        y_vals = []

        x_vals.append(-2)
        y_vals.append(0)

        for i in range(0, self.__beam_length):
            support = self.__supports[i]
            load = self.__loads[i]

            if (load[0] != 2 and load[0] != 1):
                x_vals.append(i)
                y_vals.append(cur_y)

            cur_y = self.process_shear_support(support, cur_y)
            cur_y = self.process_shear_load(load, cur_y)

            x_vals.append(i)
            y_vals.append(cur_y)


        x_vals.append(self.__beam_length)
        y_vals.append(cur_y)
        x_vals.append(self.__beam_length)
        y_vals.append(0)
        x_vals.append(self.__beam_length + 2)
        y_vals.append(0)

        plt.plot(x_vals, y_vals)

    def process_shear_load(self, load, cur_y):
        if (load[0] > -1):
            cur_y -= load[1]

        return cur_y

    def process_shear_support(self, support, cur_y):
        if (support[0] > -1 and support[0] != 4):
            cur_y += support[1]

        return cur_y

    # MOMENT GRAPH PLOTTER
    def plot_moment(self):
        plt.subplot(1, 2, 2)

        cur_x = 0
        cur_y = 0
        x_vals = []
        y_vals = []

        # empty object to keep track of the last force
        last_force = [-1, 0]
        was_load = False

        x_vals.append(0)
        y_vals.append(0)

        for i in range(0, self.__beam_length + 1):
            support = self.__supports[i]
            load = self.__loads[i]

            if last_force[0] != -1:
                if was_load:
                    cur_y += last_force[1]
                else:
                    cur_y += last_force[1]

                x_vals.append(i)
                y_vals.append(cur_y)

            if support[0] != -1:
                last_force[0] = support[0]
                last_force[1] += support[1]
                was_load = False
            elif load[0] != -1:
                last_force[0] = load[0]
                last_force[1] -= load[1]
                was_load = True

        plt.plot(x_vals, y_vals)

    def show_plots(self):
        plt.show()
