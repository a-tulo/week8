import matplotlib.pyplot as plt
import random as rnd

def data():
    paths = {}
    paths["lineStyle"] = input("What line type? : -- or -\n")
    paths["colour"] = input("What color? r g or b\n")
    paths["markerStyle"] = input("What marker style? o s or ^\n")
    return paths

def generate():
    linesToDisplay = int(input("How many lines would you like to display?"))
    for count in range(linesToDisplay):
        values = data()
        x = rnd.sample(range(1, 10), 5)
        y = rnd.sample(range(1, 10), 5)
        format = f"{values['colour']}{values['lineStyle']}{values['markerStyle']}"
        plt.plot(x,y,format)
    plt.show()

def run():
    print("Running")
    generate()
    print("Done!")

if __name__ == "__main__":
    run()