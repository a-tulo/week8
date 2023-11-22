import matplotlib.pyplot as plt

def display_line(x,y):
    plt.plot(x, y)
    plt.show()

def run_task1():
    x_values = [1,2,3,4,5]
    y_values = [1,4,9,16,25]
    display_line(x_values,y_values)

def run_task2():
    small()
    medium()
    large()
    plt.show()

def run_task3():
    values = path()
    plt.plot(values[0], values[1], 'ro--')
    plt.show()

def small():
    x = [3,3,4,4,3]
    y = [3,4,4,3,3]
    plt.plot(x,y,'r:o')

def medium():
    x = [2,2,5,5,2]
    y = [2,5,5,2,2]
    plt.plot(x,y,'g--s')

def large():
    x = [1, 1, 6, 6, 1]
    y = [1, 6, 6, 1, 1]
    plt.plot(x,y,'bp-')

def coordinate():
    x = int(input("Enter x value:\n"))
    y = int(input("Enter y Value:\n"))
    return(x,y)

def path():
    print("Retrieving path..")
    x_values = []
    y_values = []

    for count in range(4):
        data = coordinate()
        x_values.append(data[0])
        y_values.append(data[1])

    return [x_values, y_values]

if __name__ == "__main__":
    # run_task1()
    # run_task2()
    run_task3()


# # marker styles can be specified using single characters
# # these include o for circles, s for squares, ^ for triangle up, v for triangle down

# plt.plot(x, y, 'o')   # will display circle markers
# plt.plot(x, y, 's')   # will display square markers

# # similarly, we can control the line styles
# # these include - for solid lines, -- for dashed lines, -. for dash-dot lines, : for dotted lines

# plt.plot(x, y, 'o-')  # will display circle markers with a solid line
# plt.plot(x, y, 'o--') # will display circle markers with a dashed line
# plt.plot(x, y, 'o:')  # will display circle markers with a dotted line

# # colors can be specified using single characters where r is red, b is blue, g is green, etc.
# # supported colours include red, blue, green, cyan, magenta, yellow, black and white.

# plt.plot(x, y, 'yo')   # will display yellow markers
# plt.plot(x, y, 'ro--') # will display a red dashed line