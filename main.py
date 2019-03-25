import matplotlib.pyplot as plt
import random

def graph_array(x_array, y_array):
    # plotting the points
    plt.scatter(x_array, y_array)

    # naming the x axis
    plt.xlabel('x - axis')
    # naming the y axis
    plt.ylabel('y - axis')

    # giving a title to my graph
    plt.title('My first graph!')

    # function to show the plot
    plt.show()


if __name__ == "__main__":
    x, y = [], []
    for i in range(10):
        x.append(random.randint(1, 101))
    for i in range(10):
        y.append(random.randint(1, 101))
    # # x axis values
    # x = [1, 2, 3]
    # # corresponding y axis values
    # y = [2, 4, 1]
    graph_array(x, y)
    print("Hello World")

