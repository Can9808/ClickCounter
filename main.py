import tkinter
import tkinter.messagebox
import customtkinter
import mouse
from datetime import datetime
from CTkMessagebox import CTkMessagebox
from PIL import Image

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

rightclickamount = 0
leftclickamount = 0
middleclickamount = 0
is_running = False
elapsed_time = 0
session_started = False

class App(customtkinter.CTk):
    def __init__(self):
        farbe_label = "grey30"

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
                                                command=self.switch_frame_to_clickcounter,
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
                                                command=self.switch_frame_to_mouse,
                                                width=100
                                                )
        self.button_3.grid(row=3, column=0, pady=10, padx=20)
        self.button_4 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Einstellungen",
                                                command=self.button_event,
                                                width=100
                                                )
        self.button_4.grid(row=5, column=0, pady=10, padx=20)

        self.frame_right_mouse = customtkinter.CTkFrame(master=self, width=340, height=540)
        self.frame_right_mouse.grid_propagate(False)  # damit bleibt der Frame immer gleich groß
        self.frame_right_mouse.grid(row=0, column=2, padx=20, pady=20)


        self.frame_right = customtkinter.CTkFrame(master=self, width=340, height=540)
        self.frame_right.grid_propagate(False)  # damit bleibt der Frame immer gleich groß
        self.frame_right.grid(row=0, column=2,  padx=20, pady=20)


        self.label_new = customtkinter.CTkLabel(master=self.frame_right_mouse, text="HELLO WORLD!")
        self.label_new.place(x=340 / 2, y=40 / 2, anchor="center")


        #TOP
        frame_right_mid_width = 340
        frame_right_mid_height = 40

        self.frame_right_top = customtkinter.CTkFrame(master=self.frame_right, width=frame_right_mid_width, height=frame_right_mid_height, bg_color="white")
        self.frame_right_top.grid_propagate(False)  # damit bleibt der Frame immer gleich groß
        self.frame_right_top.grid(row=0, column=0)

        self.button_mauswahl = customtkinter.CTkButton(master=self.frame_right_top,
                                                text="Mausauswahl",
                                                command=self.button_event,
                                                height=25, width=(frame_right_mid_width / 3)
                                                )
        self.button_mauswahl.grid(row=0, column=0, pady=10, padx=20)

        #MittelKlick - Zähler
        self.frame_right_mid = customtkinter.CTkFrame(master=self.frame_right, width=frame_right_mid_width, height=frame_right_mid_height, bg_color="white")
        self.frame_right_mid.grid_propagate(False)  # damit bleibt der Frame immer gleich groß
        self.frame_right_mid.grid(row=2, column=0)
        self.label_mittelklickCounter = customtkinter.CTkLabel(master=self.frame_right_mid, text="0",width=150,
                                                                fg_color=farbe_label,
                                                                corner_radius=900)
        self.label_mittelklickCounter.place(x=frame_right_mid_width / 2, y=frame_right_mid_height / 2, anchor="center")


        #ClickZähler
        self.frame_right_clickCounter = customtkinter.CTkFrame(master=self.frame_right, width=frame_right_mid_width,
                                                      height=frame_right_mid_height, bg_color="white")
        self.frame_right_clickCounter.grid_propagate(False)  # damit bleibt der Frame immer gleich groß
        self.frame_right_clickCounter.grid(row=3, column=0)

        self.label_linkssklickCounter = customtkinter.CTkLabel(master=self.frame_right_clickCounter, text="0", width=150,
                                                                fg_color=farbe_label,
                                                                corner_radius=900)
        self.label_linkssklickCounter.grid(row=4, column=0, pady=10, padx=10)

        self.label_rechtsklickCounter = customtkinter.CTkLabel(master=self.frame_right_clickCounter, text="0", width=150,
                                                                fg_color=farbe_label,
                                                                corner_radius=900)
        self.label_rechtsklickCounter.grid(row=4, column=1, pady=10, padx=10)

        mouse.on_click(self.onleftclick)
        mouse.on_right_click(self.onrightclick)
        mouse.on_middle_click(self.onmiddleclick)

        # Session Label
        self.frame_right_session_top = customtkinter.CTkFrame(master=self.frame_right, width=frame_right_mid_width , height=40, bg_color="white")
        self.frame_right_session_top.grid_propagate(False)  # damit bleibt der Frame immer gleich groß

        self.frame_right_session_top.grid(row=5, column=0)
        self.frame_right.grid_rowconfigure(4, weight=1)
        self.label_session = customtkinter.CTkLabel(master=self.frame_right_session_top, text="Session",
                                                                width=150,
                                                                fg_color=farbe_label, #TODO IDK welche Farbe
                                                                corner_radius=900)
        self.label_session.place( x=frame_right_mid_width / 2, y=frame_right_mid_height / 2, anchor="center")

        img = customtkinter.CTkImage(dark_image=Image.open("./icon/diskette_dark.png"), size=(20, 20))
        self.button_save = customtkinter.CTkButton(master=self.frame_right_session_top,
                                                text="",
                                                command=self.safe_data,
                                                width=16,
                                                height=16,
                                                image=img
                                                )
        self.button_save.place(x=310, y=frame_right_mid_height / 2, anchor="center")



        #session Neu
        self.frame_right_session_bot = customtkinter.CTkFrame(master=self.frame_right, width=frame_right_mid_width, bg_color="white")
        self.frame_right_session_bot.grid_propagate(False)  # damit bleibt der Frame immer gleich groß

        self.frame_right_session_bot.grid(row=6, column=0)

        self.button_session_new = customtkinter.CTkButton(master=self.frame_right_session_bot,
                                                       text="Neu",
                                                       command=self.session_new,
                                                       width=150
                                                       )
        self.button_session_new.grid(row=0, column=0, pady=10, padx=10)

        #session start/stop
        self.button_session_start = customtkinter.CTkButton(master=self.frame_right_session_bot,
                                                       text="Start",
                                                       command=self.start_timer,
                                                       width=150
                                                       )
        self.button_session_start.grid(row=1, column=0, pady=10, padx=10)
        self.button_session_stop = customtkinter.CTkButton(master=self.frame_right_session_bot,
                                                       text="Stop",
                                                       command=self.stop_timer,
                                                       width=150
                                                       )
        self.button_session_stop.grid(row=1, column=1, pady=10, padx=10)

        #session timestamp Start

        self.label_session_start_time = customtkinter.CTkLabel(master=self.frame_right_session_bot, text="Session Start:",
                                                    width=150)
        self.label_session_start_time.grid(row=2, column=0, pady=(10,0))

        self.label_session_start_timestamp = customtkinter.CTkLabel(master=self.frame_right_session_bot,
                                                                text="DD/HH/YY HH:MM:SS",
                                                                width=150,
                                                                fg_color=farbe_label,
                                                                corner_radius=900)
        self.label_session_start_timestamp.grid(row=3, column=0, pady=0)

        # session Laufzeit

        self.label_session_running_time = customtkinter.CTkLabel(master=self.frame_right_session_bot,
                                                               text="Laufzeit",
                                                               width=150)
        self.label_session_running_time.grid(row=2, column=1, pady=(10, 0))

        self.label_session_running_timestamp = customtkinter.CTkLabel(master=self.frame_right_session_bot,
                                                                text="00:00:00:00",
                                                                width=150,
                                                                fg_color=farbe_label,
                                                                corner_radius=900)
        self.label_session_running_timestamp.grid(row=3, column=1, pady=0)


    def switch_frame_to_clickcounter(self):
        print("Klickzähler")
        self.frame_right_mouse.grid_remove()
        self.frame_right.grid(row=0, column=2, padx=20, pady=20)

    def switch_frame_to_mouse(self):
        print("Mäuse")
        #self.frame_right.forget()
        self.frame_right.grid_remove()
        self.frame_right_mouse.grid(row=0, column=2, padx=20, pady=20)

    def button_event(self):
        print("Button pressed")

    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def on_closing(self, event=0):
        self.destroy()


    def onrightclick(self):
        global rightclickamount
        if is_running:
            rightclickamount += 1
            print("right: " + str(rightclickamount))
            self.label_rechtsklickCounter.configure(text=f'{rightclickamount:,}'.replace(',','.'))

    def onleftclick(self):
        global leftclickamount
        if is_running:
            leftclickamount += 1
            print("left: " + str(leftclickamount))
            self.label_linkssklickCounter.configure(text=f'1.000.000.00{leftclickamount}')
            self.label_linkssklickCounter.configure(text=f'{leftclickamount:,}'.replace(',','.'))


    def onmiddleclick(self):
        global middleclickamount
        if is_running:
            middleclickamount += 1
            print("middle: " + str(middleclickamount))

            self.label_mittelklickCounter.configure(text=f'{middleclickamount:,}'.replace(',','.'))

    def update_time(self): #DD:HH:MM:SS
        if is_running:
            global elapsed_time
            elapsed_time += 1
            days = elapsed_time // 86400
            hours = elapsed_time // 3600
            hours = hours % 24
            minutes = elapsed_time // 60
            minutes = minutes % 60
            seconds = elapsed_time % 60

            time_str = f"{days:02d}:{hours:02d}:{minutes:02d}:{seconds:02d}"
            self.label_session_running_timestamp.configure(text=time_str)
            app.after(1000, self.update_time)

    def start_timer(self):
        if session_started:
            global is_running
            is_running = True
            self.update_time()
        else:
            self.show_warning("Starte erst eine Session!")

    def stop_timer(self): #TODO Speichere die Session
        global is_running
        if session_started & is_running:
            is_running = False
        else:
            self.show_warning("Starte erst eine Session!")


    def session_new(self):
        global session_started
        global elapsed_time
        if is_running:
            self.show_warning("Stoppe den Timer!")
        else:
            print(elapsed_time)
            if elapsed_time != 0:
                print("speichere...")
            elapsed_time = 0
            global rightclickamount
            rightclickamount = 0
            global leftclickamount
            leftclickamount = 0
            global middleclickamount
            middleclickamount = 0
            self.label_session_running_timestamp.configure(text="00:00:00:00")
            self.label_rechtsklickCounter.configure(text="0")
            self.label_linkssklickCounter.configure(text="0")
            self.label_mittelklickCounter.configure(text="0")
            session_started = True
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            print("date and time =", dt_string)
            self.label_session_start_timestamp.configure(text=dt_string)


    def safe_data(self):
        if session_started and not is_running and elapsed_time != 0:
            print("speichere...")
        elif not session_started:
            self.show_warning("Starte zuerst eine Session!")
        elif is_running:
            self.show_warning("Stoppe zuerst die Session!")



    def show_warning(self, message):
        # Show some retry/cancel warnings
        CTkMessagebox(title="Warnung!", message=message,
                            icon="warning", option_1="OK")



if __name__ == "__main__":


    app = App()
    app.mainloop()