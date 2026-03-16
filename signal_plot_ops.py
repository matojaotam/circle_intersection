import matplotlib.pyplot as plt

def load_signal_from_txt(path):

    values = []


    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                values.append(float(line))
    return values

def signal_min(values):
    return min(values)

def signal_max(values):
    return max(values)

def signal_avg(values):
    return sum(values) / len(values)

def plot_signal(values):
    plt.plot(values)
    plt.title("Signal plot")
    plt.xlabel("Sample")
    plt.ylabel("Value")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    path = "ekg_signal.txt"

    values = load_signal_from_txt(path)

    print("Minimum:", signal_min(values))
    print("Maximum:", signal_max(values))
    print("Average:", signal_avg(values))

    # plot_signal(values)

# import signal_plot_ops
#
# path = "ekg_signal.txt"
#
# values = signal_plot_ops.load_signal_from_txt(path)
#
# avg = signal_plot_ops.signal_avg(values)
# print("Average value:", avg)
#
# signal_plot_ops.plot_signal(values)


