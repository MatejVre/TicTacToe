import customtkinter

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        self.title("Tic Tac Toe")
        self.geometry("700x700")
        customtkinter.set_appearance_mode("light")

        #configure grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

        #create font
        self.font = customtkinter.CTkFont(family="helvetica", size=70)

        #create grid
        self.create_grid()
        

    def create_grid(self):
        for i in range(3):
            for u in range(3):
                self.button = customtkinter.CTkButton(self,
                                                      text="X",
                                                      fg_color="transparent",
                                                      hover_color="gray",
                                                      border_color="black",
                                                      border_width=1,
                                                      corner_radius=0,
                                                      font=self.font,
                                                      command= lambda row=i, column=u : self.place_symbol(row, column))
                self.button.grid(row=i, column=u, padx=0, pady=0,sticky="nesw")
    
    def place_symbol(self, row, column):
        print(row, column)



app = App()
app.mainloop()