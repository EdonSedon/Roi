from tkinter import *
from tkinter import ttk

class CurrencyConverter:

    def __init__(self, root):
        self.root = root
        root.title("Currency Converter")
        
        self.mainframe = ttk.Frame(root, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        self.amount = StringVar()
        amount_entry = ttk.Entry(self.mainframe, width=7, textvariable=self.amount)
        amount_entry.grid(column=2, row=1, sticky=(W, E))

        self.result_var = StringVar()
        ttk.Label(self.mainframe, textvariable=self.result_var).grid(column=2, row=2, sticky=(W, E))

        ttk.Button(self.mainframe, text="Konverto", command=self.convert).grid(column=3, row=3, sticky=W)
        ttk.Button(self.mainframe, text="Switch", command=self.switch_currency).grid(column=2, row=3, sticky=W)

        ttk.Label(self.mainframe, text="Sasia").grid(column=3, row=1, sticky=W)
        ttk.Label(self.mainframe, text="Bejn").grid(column=1, row=2, sticky=E)
        self.label_result = ttk.Label(self.mainframe, text="Rezultati")
        self.label_result.grid(column=3, row=2, sticky=W)

        self.from_currency_to_chf = True
        self.update_labels()

        for child in self.mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        amount_entry.focus()
        root.bind("<Return>", self.convert)

    def convert(self, *args):
        try:
            value = float(self.amount.get())
            if self.from_currency_to_chf:
                result = round(1.07 * value, 2)
            else:
                result = round(value / 1.07, 2)
            self.result_var.set(result)
        except ValueError:
            pass

    def switch_currency(self):
        self.from_currency_to_chf = not self.from_currency_to_chf
        self.update_labels()

    def update_labels(self):
        conversion_direction = "CHF to Euro" if self.from_currency_to_chf else "Euro to CHF"
        self.label_result.config(text=f"Konvertimi nga ({conversion_direction})")


root = Tk()
CurrencyConverter(root)
root.mainloop()
