import matplotlib.animation as animation
import matplotlib.pyplot as plt


class Plotter:

    def __init__(self):
        self.ticks_and_balances = []
        self.tick = 0

    def on_data(self, tick, balances):
        self.ticks_and_balances.append((tick, balances))

    def show(self):
        # Create figure for plotting
        fig = plt.figure()

        axes = fig.add_subplot(1, 1, 1)
        xs = []
        ys = []

        # This function is called periodically from FuncAnimation
        def animate(i, xs, ys):
            new_data = self.ticks_and_balances.copy()
            self.ticks_and_balances.clear()

            # Add x and y to lists
            xs.extend([tick for tick, _ in new_data])
            ys.extend([balances for _, balances in new_data])

            # Limit x and y lists to 20 items
            xs = xs[-600:]
            ys = ys[-600:]

            # Draw x and y lists
            axes.clear()
            axes.plot(xs, ys)

            # Format plot
            plt.xticks(rotation=45, ha='right')
            plt.subplots_adjust(bottom=0.30)
            plt.title('Overall balance')
            plt.ylabel('Balance (EUR)')
            plt.xlabel('Ticks')

        # Set up plot to call animate() function periodically
        ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=200)
        plt.show()
