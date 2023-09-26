import tkinter
import tkinter.messagebox
import customtkinter
import mouse

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):

    WIDTH = 520
    HEIGHT = 580




    def __init__(self):
        super().__init__()
        self.title("ClickerCounter")
       # self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        self.minsize(520, 580)

        self.resizable(False, False)

        # ============ create two frames ============

        self.frame_left = customtkinter.CTkFrame(master=self, width=140, height=580, corner_radius=0)
        self.frame_left.grid_propagate(False) #damit bleibt der Frame immer gleich groß
        self.frame_left.grid(row=0, column=0)

        self.frame_left.grid_rowconfigure(4, weight=1)  # empty row as spacing


        self.button_1 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Klickzähler",
                                                command=self.button_event,
                                                width=100
                                                )
        self.button_1.grid(row=1, column=0, pady=10, padx=20)

        self.button_2 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Graph",
                                                command=self.button_event,
                                                width=100
                                                )
        self.button_2.grid(row=2, column=0, pady=10, padx=20)
        self.button_3 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Mäuse",
                                                command=self.button_event,
                                                width=100
                                                )
        self.button_3.grid(row=3, column=0, pady=10, padx=20)
        self.button_4 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Einstellungen",
                                                command=self.button_event,
                                                width=100
                                                )
        self.button_4.grid(row=5, column=0, pady=10, padx=20)


        self.frame_right = customtkinter.CTkFrame(master=self, width=340, height=540)
        self.frame_right.grid_propagate(False)  # damit bleibt der Frame immer gleich groß
        self.frame_right.grid(row=0, column=1,  padx=20, pady=20)
        self.button_mauswahl = customtkinter.CTkButton(master=self.frame_right,
                                                text="Mausauswahl",
                                                command=self.button_event,
                                                height=4, width=8
                                                )
        self.button_mauswahl.grid(row=0, column=0, pady=10, padx=20)

        self.label_mittelklick = customtkinter.CTkLabel(master=self.frame_right,
                                              text="Mitte")
        # text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_mittelklick.grid(row=2, column=0, pady=10, padx=10)

        self.label_linkssklick = customtkinter.CTkLabel(master=self.frame_right,
                                                        text="Links")
        # text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_linkssklick.grid(row=3, column=0, pady=10, padx=10)

        self.label_rechtsklick = customtkinter.CTkLabel(master=self.frame_right,
                                                        text="Rechts")
        # text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_rechtsklick.grid(row=4, column=0, pady=10, padx=10)

        global leftclickamount

        mouse.on_click(self.onleftclick)
        mouse.on_right_click(self.onrightclick)
        mouse.on_middle_click(self.onmiddleclick)



        '''
        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_left ============

        # configure grid layout (1x11)
        self.frame_left.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(4, weight=1)  # empty row as spacing
        self.frame_left.grid_rowconfigure(8, minsize=20)    # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing

        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="Klickzähler")
                                              #text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_1.grid(row=1, column=0, pady=10, padx=10)

        self.button_1 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Graph",
                                                command=self.button_event)
        self.button_1.grid(row=2, column=0, pady=10, padx=20)

        self.button_2 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Mäuse",
                                                command=self.button_event)
        self.button_2.grid(row=3, column=0, pady=10, padx=20)

        self.button_3 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Options",
                                                command=self.button_event)
        self.button_3.grid(row=10, column=0, pady=10, padx=20, sticky="w")

        #self.label_mode = customtkinter.CTkLabel(master=self.frame_left, text="Appearance Mode:")
        #self.label_mode.grid(row=9, column=0, pady=0, padx=20, sticky="w")

        #self.optionmenu_1 = customtkinter.CTkOptionMenu(master=self.frame_left,
        #                                                values=["Light", "Dark", "System"],
        #                                                 command=self.change_appearance_mode)
        #self.optionmenu_1.grid(row=10, column=0, pady=10, padx=20, sticky="w")

        # ============ frame_right ============

        # configure grid layout (3x7)
        self.frame_right.rowconfigure(1, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)

        # ============ frame_right ============

        self.label_info_1 = customtkinter.CTkLabel(master=self.frame_right,
                                                   text="CTkLabel: Lorem ipsum dolor sit,\n" +
                                                        "amet consetetur sadipscing elitr,\n" +
                                                        "sed diam nonumy eirmod tempor" ,
                                                   height=100,
                                                   corner_radius=6,  # <- custom corner radius
                                                   fg_color=("white", "gray38"),  # <- custom tuple-color
                                                   justify=tkinter.LEFT)
        self.label_info_1.grid(column=0, row=0, sticky="nwe", padx=15, pady=15)

        #self.progressbar = customtkinter.CTkProgressBar(master=self.frame_info)
        #self.progressbar.grid(row=1, column=0, sticky="ew", padx=15, pady=15)

'''




    def button_event(self):
        print("Button pressed")

    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def on_closing(self, event=0):
        self.destroy()

    def onrightclick(self):
        rightclickamount += 1
        print("right: " + str(rightclickamount))
        self.label_rechtsklick.configure(text=f'Rightclicked: {rightclickamount} times!!!')

    def onleftclick(self):
        leftclickamount += 1
        print("left: " + str(leftclickamount))
        self.label_linkssklick.configure(text=f'Leftclicked: {leftclickamount} times!!!')

    def onmiddleclick(self):
        middleclickamount += 1
        print("left: " + str(middleclickamount))
        self.label_mittelklick.configure(text=f'middleclick: {middleclickamount} times!!!')


if __name__ == "__main__":


    app = App()
    app.mainloop()