import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):

        self.main_window = tkinter.Tk()
        
        self.main_window.title('Building Bridges Admin')
        self.main_window.geometry('500x100')

        self.top_frame = tkinter.Frame(self.main_window)
        self.mid1_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        
    
        self.prompt_label = tkinter.Label(self.top_frame, \
                                          text = "Last Name:")
        self.lastName = tkinter.Entry(self.top_frame, \
                                      width = 15)
        self.prompt_label2 = tkinter.Label(self.top_frame, \
                                          text = "First Name:")
        self.firstName = tkinter.Entry(self.top_frame, \
                                       width = 15)
        self.prompt_label3 = tkinter.Label(self.top_frame, \
                                           text = "Middle Initial:")
        self.middleInitial = tkinter.Entry(self.top_frame, \
                                           width = 5)

        self.prompt_label.pack(side='left')
        self.lastName.pack(side='left')
        self.prompt_label2.pack(side='left')
        self.firstName.pack(side='left')
        self.prompt_label3.pack(side='left')
        self.middleInitial.pack(side='left')

        self.prompt_label4 = tkinter.Label(self.mid1_frame, \
                                           text = "Street Address:")
        self.address = tkinter.Entry(self.mid1_frame, \
                                     width = 57)

        self.prompt_label4.pack(side='left')
        self.address.pack(side='left')



        

        self.saveButton = tkinter.Button(self.bottom_frame, \
                                         text = 'Save', \
                                         command = self.save)
        self.quitButton = tkinter.Button(self.bottom_frame, \
                                         text = 'Quit', \
                                         command = self.main_window.destroy)

        self.saveButton.pack(side='left')
        self.quitButton.pack(side='left')

        self.top_frame.pack()
        self.mid1_frame.pack()
        self.bottom_frame.pack()
        
        tkinter.mainloop()

    def save(self):
        tkinter.messagebox.showinfo('Last Name Saved')

my_gui = MyGUI()


