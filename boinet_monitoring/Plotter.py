import matplotlib.animation as animation
import matplotlib.pyplot as plt


class Plotter:

    def __init__(self):
        self.ticks_and_balances = []
        self.tick = 0

    def on_data(self, tick, balance):
        self.ticks_and_balances.append((tick, balance))

    def show(self):
        # Create figure for plotting
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        xs = []
        ys = []

        # This function is called periodically from FuncAnimation
        def animate(i, xs, ys):
            new_data = self.ticks_and_balances.copy()
            self.ticks_and_balances.clear()

            # Add x and y to lists
            xs.extend([tick for tick, _ in new_data])
            ys.extend([balance for _, balance in new_data])

            # Limit x and y lists to 20 items
            xs = xs[-20:]
            ys = ys[-20:]

            # Draw x and y lists
            ax.clear()
            ax.plot(xs, ys)

            # Format plot
            plt.xticks(rotation=45, ha='right')
            plt.subplots_adjust(bottom=0.30)
            plt.title('TMP102 Temperature over Time')
            plt.ylabel('Temperature (deg C)')

        # Set up plot to call animate() function periodically
        ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1000)
        plt.show()
