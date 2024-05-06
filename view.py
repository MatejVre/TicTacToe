import customtkinter


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        self.title("Tic Tac Toe")
        self.geometry("700x700")
        customtkinter.set_appearance_mode("light")

        #initialize other stuff
        self.current_player = "X"

        #configure grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=2)
        self.grid_rowconfigure(2, weight=2)
        self.grid_rowconfigure(3, weight=2)

        #create font
        self.font = customtkinter.CTkFont(family="helvetica", size=70)

        #create player label
        self.player_label = customtkinter.CTkLabel(self, text=f"{self.current_player}'s turn")
        self.player_label.grid(row=0, column=1)

        #create grid
        self.create_grid()

        
#testing contributions again
    def create_grid(self):
        for i in range(3):
            for u in range(3):
                self.button = customtkinter.CTkButton(self,
                                                      text=" ",
                                                      fg_color="transparent",
                                                      hover_color="gray",
                                                      border_color="black",
                                                      text_color="black",
                                                      border_width=1,
                                                      corner_radius=0,
                                                      font=self.font,
                                                      command= lambda row=i, column=u : self.place_symbol(row, column))
                self.button.grid(row=i+1, column=u, padx=0, pady=0,sticky="nesw")
    
    def place_symbol(self, row, column):
        self.player_placed = True
    




app = App()
app.mainloop()