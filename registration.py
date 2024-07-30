import tkinter as Tk
from tkinter import messagebox
class SchoolRegistrationApp:
    def __init__(self, root):
        self.root=root
        self.root.title("StudentRegistration")
        #Labels and Entries
        self.create_widgets()
      #List to store students
        self.students=[]
    def create_widgets(self):
        #Name
            Tk.Label(self.root,text="Name:").grid(row=0, column=0, padx=10, pady=10)
            self.name_entry= Tk.Entry(self.root)
            self.name_entry.grid(row=1, column=0, padx=10, pady=10)
            #Date of registration
            Tk.Label(self.root, text="Date of Registration").grid(row=1, column=1, padx=10, pady=10)
            #Gender
            Tk.Label(self.root, text="Gender:").grid(row=2, column=0, padx=10, pady=10)
            self.gender_var= Tk.StringVar()
            self.gender_combobox=Tk.Combobox(self.root,textvariable=self.gender_var)
            self.gender_combobox['values']=("Male","Female","Other")
            self.gender_combobox.grid(row=2,column=1,padx=10,pady=10)
            Tk.Label(self.root, text="Price:").grid(row=3, column=0, padx=10, pady=10)
            self.price_entry = Tk.Entry(self.root)
            self.price_entry.grid(row=3, column=1, padx=10, pady=10)

                # Buttons
            Tk.Button(self.root, text="Add Student", command=self.add_student).grid(row=4, column=0, padx=10, pady=10)
            Tk.Button(self.root, text="Remove Student", command=self.remove_student).grid(row=4, column=1, padx=10, pady=10)

                # Listbox to display students
            self.student_listbox = Tk.Listbox(self.root, width=50)
            self.student_listbox.grid(row=5, columnspan=2, padx=10, pady=10)

    def add_student(self):
                name = self.name_entry.get()
                date = self.date_entry.get()
                gender = self.gender_var.get()
                price = self.price_entry.get()

                if name and date and gender and price:
                    student = f"Name: {name}, Date: {date}, Gender: {gender}, Price: {price}"
                    self.students.append(student)
                    self.student_listbox.insert(Tk.END, student)
                    self.clear_entries()
                else:
                    messagebox.showwarning("Input Error", "Please fill in all fields.")

    def remove_student(self):
                selected_index = self.student_listbox.curselection()
                if selected_index:
                    self.student_listbox.delete(selected_index)
                    del self.students[selected_index[0]]
                else:
                    messagebox.showwarning("Selection Error", "Please select a student to remove.")

    def clear_entries(self):
                self.name_entry.delete(0, Tk.END)
                self.date_entry.delete(0, Tk.END)
                self.gender_combobox.set('')
                self.price_entry.delete(0, Tk.END)

if '_name_' == "_init_":
    root = Tk()
    app = SchoolRegistrationApp(root)
    root.mainloop()