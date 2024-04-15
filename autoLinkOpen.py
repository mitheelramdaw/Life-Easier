from tkinter import *
import time
import webbrowser

# Define root as Tkinter instance
root: Tk = Tk()

# Function to open the link
def open_link():
    link = "https://cv2jobsryanchitatemitheelramdawlaeekaadamsmikhaarramdaw.streamlit.app/"
    webbrowser.open(link)

# Function to schedule the link opening
def schedule_link_open():
    current_time = time.strftime("%H:%M:%S")
    if current_time == "09:00:00":  # Change the time to 9:00 AM
        open_link()
    else:
        root.after(1000, schedule_link_open)  # Check every second

# CustomTkinter setup
root.title("Auto Link Opener")
root.geometry("300x100")

# Button to manually open the link
open_button = Button(root, text="Open Link Now", command=open_link)
open_button.pack(pady=10)

# Schedule the link opening
schedule_link_open()

# Run the Tkinter event loop
root.mainloop()
