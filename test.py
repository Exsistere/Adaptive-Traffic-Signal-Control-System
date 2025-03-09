fig = plt.figure()
ax = fig.add_subplot(100, 100,100)
xs = []
ys = []
def vstimeplot(values):
    global xs
    global ys
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(values)
    xs = xs[-20:]
    ys = ys[-20:]
    ax.clear()
    ax.plot(xs, ys)
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('TMP102 Temperature over Time')
    plt.ylabel('Temperature (deg C)')
    # Set up plot to call animate() function periodically

ani = animation.FuncAnimation(fig, vstimeplot(reward), fargs=(xs, ys), interval=1000)
plt.show()