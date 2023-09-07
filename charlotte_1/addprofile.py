import customtkinter
import button 
import sqlite3
import hashlib 

class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("500x400")
        self.title("Добавить профиль")


        self.entry_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.entry_frame.grid(sticky="nsew")

        self.tabview = customtkinter.CTkTabview(self.entry_frame, corner_radius=3)
        self.tabview.grid(sticky="nsew")
        self.tabview.add("Сервер")
        self.tabview.add("Кластер")
        self.tabview.tab("Сервер").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("Кластер").grid_columnconfigure(0, weight=1)

        self.entry = customtkinter.CTkEntry(self.tabview.tab("Сервер"),
                                            placeholder_text="Название(не обязательно)",
                                            corner_radius=3)
        self.entry.grid(row=0,
                        column=0,
                        padx=(10, 10),
                        pady=(10, 10),
                        sticky="nsew")

        self.ip_adress = customtkinter.CTkEntry(self.tabview.tab("Сервер"),
                                               placeholder_text="IP-адрес",
                                               corner_radius=3)
        self.ip_adress.grid(row=1,
                        column=0,
                        padx=(10, 10),
                        pady=(10, 10),
                        sticky="nsew")

        self.user = customtkinter.CTkEntry(self.tabview.tab("Сервер"), 
                                           placeholder_text="Пользователь",
                                           corner_radius=3)
        self.user.grid(row=2,
                        column=0,
                        padx=(10, 10),
                        pady=(10, 10),
                        sticky="nsew")

        self.password = customtkinter.CTkEntry(self.tabview.tab("Сервер"),
                                               placeholder_text="Пароль",
                                               corner_radius=3)
        self.password.grid(row=3,
                           column=0,
                           padx=(10, 10),
                           pady=(10, 10),
                           sticky="nsew")


        #Фрейм окна с кнопками
        self.button_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.button_frame.grid(padx=10, pady=10, sticky="nsew")

        self.main_button_1 = button.AcessButton(self.button_frame,
                                                text="Принять",
                                                command=self.add_profile)
        self.main_button_1.grid(row=4,
                                column=3,
                                padx=(10, 10),
                                pady=(10, 10),
                                sticky="nsew")

        self.main_button_2 = button.CancelButton(self.button_frame,
                                                 text="Отмена",
                                                 command=self.cancel)
        self.main_button_2.grid(row=4,
                                column=4,
                                padx=(10, 10),
                                pady=(10, 10),
                                sticky="nsew")


        self.main_button_3 = button.OwnButton(self.button_frame,
                                              text="Тест")
        self.main_button_3.grid(row=4,
                                column=5,
                                padx=(10, 10),
                                pady=(10, 10),
                                sticky="nsew")



    def generate_token(self):
        return secrets.token_hex(16)

    def add_profile(self):
        # подключаемся к базе данных
        self.conn = sqlite3.connect('Charlotte')
        self.cursor = self.conn.cursor()            

        self.ip_adress = self.ip_adress.get()
        self.user = self.user.get()
        self.password = self.password.get()
        self.hashed_password = hashlib.sha256(self.password.encode()).hexdigest()

        # добавляем новую запись в таблицу
        self.cursor.execute("INSERT INTO users (ip_adress, login, password) VALUES (?, ?, ?)", (self.ip_adress, self.user, self.hashed_password))
        self.token = generate_token()
        self.cursor.execute("INSERT INTO sessions (token) VALUES (?)", (token))
        self.conn.commit()

        # закрываем соединение с базой данных
        self.conn.close()

    def cancel(self):
        self.destroy()