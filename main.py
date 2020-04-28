import graphs as Grapher

def main():
    while(1):

        print("\nMoment Diagram Grapher")
        print("----------------------")
        print("1. Shear Force Diagram")
        print("2. Bending Moment Diagram")
        print("3. Exit\n")

        menu_selection = input("Which would you like to do? ")

        if (menu_selection == "1"):
            shear()

        elif(menu_selection == "2"):
            bending()

        else:
            break


def shear():
    beam_length = int(input("What is the beam length (whole meters)? "))
    graph = Grapher.ShearDiagram(beam_length)

    while(1):
        print("Enter Graph Data:")
        print("1. Add Load")
        print("2. Add Support")
        print("3. Draw Graph\n")

        selection = input("Which would you like to do? ")

        if (selection == "1"):
            graph.add_load()

        elif (selection == "2"):
            graph.add_support()

        else:
            break

    graph.plot_shear()


def bending():
    beam_length = int(input("What is the beam length (whole meters)? "))
    graph = Grapher.MomentDiagram(beam_length)

    while(1):
        print("Enter Graph Data:")
        print("1. Add Load")
        print("2. Add Support")
        print("3. Add Moment")
        print("4. Draw Graph\n")

        selection = input("Which would you like to do? ")

        if (selection == "1"):
            graph.add_load()

        elif (selection == "2"):
            graph.add_support()

        elif (selection == "3"):
            graph.add_moment()

        else:
            break

    print(str(graph))


main()
