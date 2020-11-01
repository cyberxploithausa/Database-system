
############################################################
#####                   CYBERXPLOIT                    #####
##### PROJECT NAME: DATABASE SYSTEM                    #####
##### PROJECT ID: CYBX006                             #####
#####                                                  #####
############################################################



from tkinter import *
import TkinterDB


def get_selected_row(event):
     global selected_tuple
     #Can add a for loop in order to keep id in ascending order.
     
     index = list1.curselection()[0]
     selected_tuple = list1.get(index)
     nameEntry.delete(0, END)
     nameEntry.insert(END, selected_tuple[1])
     
     addressEntry.delete(0, END)
     addressEntry.insert(END, selected_tuple[2])
     
     phoneNumberEntry.delete(0, END)
     phoneNumberEntry.insert(END, selected_tuple[3])
     
     genderEntry.delete(0, END)
     genderEntry.insert(END, selected_tuple[4])
     
def view_command():
     list1.delete(0, END)
     for row in TkinterDB.view():
          list1.insert(END, row)
     
     
def search_command():
     list1.delete(0, END)
     for row in TkinterDB.search(name_text.get(), address_text.get(), phone_number_text.get(), gender_text.get()):
          list1.insert(END, row)
     
def add_command():
     TkinterDB.insert(name_text.get(), address_text.get(), phone_number_text.get(), gender_text.get())
     list1.delete(0, END)
     list1.insert(END, name_text.get(), address_text.get(), phone_number_text.get(), gender_text.get())
     
     
def delete_command():
      TkinterDB.delete(selected_tuple[0])
      
      
def update_command():
      TkinterDB.update(selected_tuple[0], name_text.get(), address_text.get(), phone_number_text.get(), gender_text.get())
      
      

     
window = Tk()
window.title("ALH. AHMED ALARAMMA")
window.configure(background = 'light green')

Title = Label(window, text = "AAACNL")
Title.grid(row = 0, column = 1)

name = Label(window, text = "NAME:")
name.grid(row = 2, column = 0)

address = Label(window, text = "ADDRESS:")
address.grid(row = 3, column = 0)

phone_number = Label(window, text = "PHONE NUMBER:")
phone_number.grid(row = 4, column = 0)

gender = Label(window, text = "GENDER:")
gender.grid(row = 5, column = 0)

name_text = StringVar()
nameEntry = Entry(window, textvariable = name_text)
nameEntry.grid(row = 2, column = 1)

address_text = StringVar()
addressEntry = Entry(window, textvariable = address_text)
addressEntry.grid(row = 3, column = 1)

phone_number_text = StringVar()
phoneNumberEntry = Entry(window, textvariable = phone_number_text)
phoneNumberEntry.grid(row = 4, column = 1)

gender_text = StringVar()
genderEntry = Entry(window, textvariable = gender_text)
genderEntry.grid(row = 5, column = 1)

list1 = Listbox(window, height = 10, width = 29)
list1.grid(row = 1, column = 3, rowspan = 6, columnspan = 2)

scrollbar = Scrollbar(window)
scrollbar.grid(row = 1, column = 2, sticky = 'ns', rowspan = 6)

list1.configure(yscrollcommand = scrollbar.set)
scrollbar.configure(command = list1.yview)

list1.bind("<<ListboxSelect>>", get_selected_row)

b1 = Button(window, text = "View all", bg = "grey", fg = "red",width = 12, command = view_command)
b1.grid(row = 7, column = 0)

b2 = Button(window, text = "Add Entry", bg = "grey", fg = "red", width = 12, command = add_command)
b2.grid(row = 8, column = 0)

b3 = Button(window, text = "Delete Entry", bg = "red", fg = "grey", width = 12, command = delete_command)
b3.grid(row = 9, column = 0)

b4 = Button(window, text = "Search Entry", bg = "grey", fg = "red", width = 12, command = search_command)
b4.grid(row = 7, column = 1)

b5 = Button(window, text = "Update Entry", bg = "grey", fg = "red", width = 12, command = update_command)
b5.grid(row = 8, column = 1)



window.mainloop()
