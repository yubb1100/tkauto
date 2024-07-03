import tkinter as tk
from tkinter import ttk
import customtkinter as ctk

# Setting up appearance mode and default color theme
ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Selection Form")
        self.geometry(f"{800}x{600}")

        # configure grid layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(5, weight=1)

        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="Selection Form", font=ctk.CTkFont(size=16, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # Height Selection
        self.height_label = ctk.CTkLabel(self.sidebar_frame, text="Select Height:")
        self.height_label.grid(row=1, column=0, padx=20, pady=10)
        self.height_var = tk.StringVar(self)
        self.height_dropdown = ttk.Combobox(self.sidebar_frame, textvariable=self.height_var, values=["Short", "Medium", "Tall"])
        self.height_dropdown.grid(row=2, column=0, padx=20, pady=10)
        self.height_dropdown.current(0)

        # Class Selection
        self.class_label = ctk.CTkLabel(self.sidebar_frame, text="Select Class:")
        self.class_label.grid(row=3, column=0, padx=20, pady=10)
        self.class_var = tk.StringVar(self)
        self.class_dropdown = ttk.Combobox(self.sidebar_frame, textvariable=self.class_var, values=["A", "B", "C"])
        self.class_dropdown.grid(row=4, column=0, padx=20, pady=10)
        self.class_dropdown.current(0)

        # Anchor Checkbox
        self.anchor_var = tk.BooleanVar(self)
        self.anchor_checkbox = ctk.CTkCheckBox(self.sidebar_frame, text="Anchor", variable=self.anchor_var)
        self.anchor_checkbox.grid(row=5, column=0, padx=20, pady=10)

        # Transformer Checkbox and Type Selection
        self.transformer_var = tk.BooleanVar(self)
        self.transformer_checkbox = ctk.CTkCheckBox(self.sidebar_frame, text="Transformer", variable=self.transformer_var, command=self.toggle_transformer_dropdown)
        self.transformer_checkbox.grid(row=6, column=0, padx=20, pady=10)

        self.transformer_type_label = ctk.CTkLabel(self.sidebar_frame, text="Select Transformer Type:")
        self.transformer_type_label.grid(row=7, column=0, padx=20, pady=10)
        self.transformer_type_var = tk.StringVar(self)
        self.transformer_type_dropdown = ttk.Combobox(self.sidebar_frame, textvariable=self.transformer_type_var, values=["Type 1", "Type 2", "Type 3"])
        self.transformer_type_dropdown.grid(row=8, column=0, padx=20, pady=10)
        self.transformer_type_dropdown.config(state='disabled')

        # Framing Options
        self.framing_label = ctk.CTkLabel(self.sidebar_frame, text="Select Framing Option:")
        self.framing_label.grid(row=9, column=0, padx=20, pady=10)
        self.framing_var = tk.StringVar(self)
        self.framing_dropdown = ttk.Combobox(self.sidebar_frame, textvariable=self.framing_var, values=["Option 1", "Option 2", "Option 3"])
        self.framing_dropdown.grid(row=10, column=0, padx=20, pady=10)
        self.framing_dropdown.current(0)

        # Submit Button
        self.submit_button = ctk.CTkButton(self.sidebar_frame, text="Submit", command=self.submit_form)
        self.submit_button.grid(row=11, column=0, padx=20, pady=10)

        # create main entry and button
        self.entry = ctk.CTkEntry(self, placeholder_text="Main Entry")
        self.entry.grid(row=3, column=1, padx=20, pady=(20, 20), sticky="nsew")

        self.main_button_1 = ctk.CTkButton(self, text="Main Button", command=self.main_button_event)
        self.main_button_1.grid(row=3, column=2, padx=20, pady=(20, 20), sticky="nsew")

    def toggle_transformer_dropdown(self):
        if self.transformer_var.get():
            self.transformer_type_dropdown.config(state='readonly')
        else:
            self.transformer_type_dropdown.config(state='disabled')
            self.transformer_type_var.set("")  # Reset selection

    def submit_form(self):
        height = self.height_var.get()
        class_type = self.class_var.get()
        is_anchor = self.anchor_var.get()
        is_transformer = self.transformer_var.get()
        transformer_type = self.transformer_type_var.get()
        framing_option = self.framing_var.get()

        print(f"Height: {height}")
        print(f"Class: {class_type}")
        print(f"Anchor: {'Yes' if is_anchor else 'No'}")
        print(f"Transformer: {'Yes' if is_transformer else 'No'}")
        if is_transformer:
            print(f"Transformer Type: {transformer_type}")
        print(f"Framing Option: {framing_option}")

    def main_button_event(self):
        print("Main Button Clicked")

if __name__ == "__main__":
    app = App()
    app.mainloop()