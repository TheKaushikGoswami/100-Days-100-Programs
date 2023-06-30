from tkinter import *
from tkinter.ttk import Progressbar
import threading
from speedtest import Speedtest

# Creation of Function
def update_text():
    # Disable the button while the calculation is in progress
    button.config(state=DISABLED)

    # Show the loading animation
    loading_bar.grid(row=2, column=0, columnspan=2, pady=10)

    # Start a separate thread for the speed test calculation
    def perform_speed_test():
        # Start the loading animation
        loading_bar.start(10)

        speed_test = Speedtest()

        # Perform the speed test calculation
        download = speed_test.download()
        upload = speed_test.upload()

        # Update the labels with the results
        download_speed = round(download / (10 ** 6), 2)
        upload_speed = round(upload / (10 ** 6), 2)
        down_label.config(text="Download Speed - " + str(download_speed) + " Mbps")
        up_label.config(text="Upload Speed - " + str(upload_speed) + " Mbps")

        # Stop and hide the loading animation
        loading_bar.stop()
        loading_bar.grid_remove()

        # Re-enable the button after the calculation is complete
        button.config(state=NORMAL)

    # Start the speed test calculation in a separate thread
    thread = threading.Thread(target=perform_speed_test)
    thread.start()


# Creation of GUI
window = Tk()
window.title("Internet Speed Testing")
window.geometry('420x250+250+150')

# Configure grid layout
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)

button = Button(window, text="Press Here to Check Speed", width=50, command=update_text, background='#49A')
button.grid(row=0, column=0, columnspan=2, pady=10, sticky="nsew")

loading_bar = Progressbar(window, mode='indeterminate')

down_label = Label(window, text="")
down_label.grid(row=3, column=0, columnspan=2)

up_label = Label(window, text="")
up_label.grid(row=4, column=0, columnspan=2)

# Hide the loading animation initially
loading_bar.grid_remove()

# Closing the GUI
window.mainloop()

