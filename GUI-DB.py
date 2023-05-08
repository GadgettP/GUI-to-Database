import tkinter 
import customtkinter
import psycopg2

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.title("This is the ewy GUI")
app.geometry("500x350")

def login():
    username = entry1.get()
    password = entry2.get()
    if username and password:
        print("its happening")
        conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="")

        cur = conn.cursor()

        cur.execute("INSERT INTO account (username, password) VALUES (%s, %s)", (username, password))

        conn.commit()
        cur.close()
        conn.close()

        print(f"Username: {username} | Password: {password}")

frame = customtkinter.CTkFrame(master=app)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Login System", font=("Roboto", 24))
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)
entry1.bind("<Return>", login)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry2.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me")
checkbox.pack(pady=12, padx=10)

app.mainloop()

