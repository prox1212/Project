import customtkinter
import packaging

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("700x500")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady = 20, padx = 60, fill = "both", expand = True)

root.mainloop()