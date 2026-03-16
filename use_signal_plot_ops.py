import signal_plot_ops

path = "ekg_signal.txt"

values = signal_plot_ops.load_signal_from_txt(path)

avg = signal_plot_ops.signal_avg(values)
print("Average value:", avg)

signal_plot_ops.plot_signal(values)