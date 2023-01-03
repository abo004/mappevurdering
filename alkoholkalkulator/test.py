import tkinter as tk

# Create the main window
window = tk.Tk()

# Create a label
label = tk.Label(window, text="Hello, World!")

# Add the label to the window
label.pack()

# Remove the label from the window
def alkv():
    label.pack_forget()

button = tk.Button(text="Get Text", command=alkv)

button.pack()

# Run the main loop
window.mainloop()