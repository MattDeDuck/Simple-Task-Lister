from tkinter import *
from tkinter import messagebox
import os.path

root = Tk()
root.title = "Simple Task Lister"
root.resizable(0, 0)


def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        # Saves the list upon exit
        with open('data.txt', 'w+') as b:
            b.truncate(0)
            b.write(",".join(items))
            # Debug
            print("On quit: " + ",".join(items))
            root.destroy()


def updatebox():
    # Delete the tasks from the listbox
    itemsList.delete(0, END)
    # Display the updated list by inserting the updated list
    for item in items:
        itemsList.insert(END, item)


def additem():
    if e.get() == "":
        # If nothing in the box...display info box
        messagebox.showinfo("Oops!", "You need to enter an item")
    else:
        # Add the item to the list
        items.append(e.get())
        # Clear the input box
        e.delete(0, 'end')
        # Update the listbox
        updatebox()
        # Debug
        print("On Adding: " + str(items))


def deleteitem():
    # Remove the item from the list
    items.remove(itemsList.get(ANCHOR))
    # Update the listbox
    updatebox()
    # Debug
    print("On Delete: " + str(items))


root.protocol("WM_DELETE_WINDOW", on_closing)

# Define the list of tasks
items = []

# Check if the data file exists
itemfile = os.path.isfile('data.txt')

if itemfile:
    # The file is there...proceed
    with open('data.txt', 'r') as g:
        # Grab the contents of the file
        contents = g.read()
        if contents:
            items = contents.split(",")
            # Debug
            print("On startup: " + str(contents))
else:
    # File isn't there
    with open('data.txt', 'w'):
        pass


# Make the user input box
e = Entry(root, width=20, font=('Helvetica', 30))
e.pack()
# Make the add item button
addtheitem = Button(root, text="Add Item", command=additem)
addtheitem.pack(padx=10)
# Make the listbox
itemsList = Listbox(root, width=50)
itemsList.pack()
# Make the delete button
deltheitem = Button(root, text="Delete Item", command=deleteitem)
deltheitem.pack()
# Update the listbox
updatebox()

root.mainloop()