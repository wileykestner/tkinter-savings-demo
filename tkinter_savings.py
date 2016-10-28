from tkinter import Tk, StringVar, ttk, E, W, Event
from typing import Callable

from savings import SavingsObserver, PresentRequiredEarningsObserver


class TkinterSavings(SavingsObserver, PresentRequiredEarningsObserver):
    def __init__(self):
        super().__init__()

        self._tk_application = Tk()
        self._tk_application.title("After tax earnings")
        main_frame = self.get_padded_frame(tk_application=self._tk_application,
                                           west_padding=3,
                                           north_padding=3,
                                           east_padding=12,
                                           south_padding=12)
        main_frame.grid()

        desired_savings_variable = StringVar()
        tax_rate_variable = StringVar()
        need_to_earn_variable = StringVar()

        savings_pre_label = ttk.Label(master=main_frame, text="If you want to save")
        savings_entry = ttk.Entry(master=main_frame, textvariable=desired_savings_variable)
        savings_post_label = ttk.Label(master=main_frame, text="after taxes")

        tax_rate_pre_label = ttk.Label(master=main_frame, text="when the tax rate is")
        tax_rate_entry_label = ttk.Entry(master=main_frame, textvariable=tax_rate_variable)
        tax_rate_post_label = ttk.Label(master=main_frame, text="percent")

        need_to_earn_pre_label = ttk.Label(master=main_frame, text="then you need to earn")
        need_to_earn_label = ttk.Label(main_frame, textvariable=need_to_earn_variable)
        need_to_earn_post_label = ttk.Label(master=main_frame, text="before taxes")

        calculate_button = ttk.Button(main_frame, text="Calculate")

        savings_pre_label.grid(row=1, column=1, sticky=E)
        savings_entry.grid(row=1, column=2)
        savings_post_label.grid(row=1, column=3, sticky=W)

        tax_rate_pre_label.grid(row=2, column=1, sticky=E)
        tax_rate_entry_label.grid(row=2, column=2)
        tax_rate_post_label.grid(row=2, column=3, sticky=W)

        need_to_earn_pre_label.grid(row=3, column=1, sticky=E)
        need_to_earn_label.grid(row=3, column=2, sticky=(W, E))
        need_to_earn_post_label.grid(row=3, column=3, sticky=W)

        calculate_button.grid(column=3, row=4, sticky=W)

        for child in main_frame.winfo_children():
            child.grid_configure(padx=5, pady=5)

        self._need_to_earn_label = need_to_earn_label
        self._tax_rate_entry_label = tax_rate_entry_label
        self._savings_entry = savings_entry
        self._calculate_button = calculate_button
        self._desired_savings_variable = desired_savings_variable
        self._tax_rate_variable = tax_rate_variable
        self._need_to_earn_variable = need_to_earn_variable

    def register_savings_functions(self, present_required_earnings: Callable[[int,
                                                                              float,
                                                                              PresentRequiredEarningsObserver],
                                                                             None]):
        def _present_required_earnings(event: Event):
            tax_rate = int(self._tax_rate_variable.get())
            savings_string = self._desired_savings_variable.get()
            desired_savings = float(savings_string)
            present_required_earnings(tax_rate, desired_savings, self)

        self._calculate_button.bind("<Button-1>", _present_required_earnings)
        self._tk_application.bind("<Return>", _present_required_earnings)
        self._savings_entry.focus()
        self._tk_application.mainloop()

    def did_present_required_earnings(self, required_earnings: float):
        self._need_to_earn_variable.set(str(required_earnings))

    @staticmethod
    def get_padded_frame(tk_application: Tk,
                         west_padding: int,
                         north_padding: int,
                         east_padding: int,
                         south_padding: int) -> ttk.Frame:
        padding_args = [west_padding, north_padding, east_padding, south_padding]
        padding_string = "{} {} {} {}".format(*padding_args)

        return ttk.Frame(tk_application, padding=padding_string)
