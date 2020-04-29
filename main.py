import graphs as Grapher

def main():
    while(1):

        print("\nMoment Diagram Grapher")
        print("----------------------")
        print("1. Generate Diagram")
        print("2. Exit\n")

        menu_selection = input("Which would you like to do? ")

        if (menu_selection == "1"):
            shear()

        else:
            break


def shear():
    beam_length = int(input("\nWhat is the beam length (whole meters)? "))
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
    graph.plot_moment()
    graph.show_plots()

main()
