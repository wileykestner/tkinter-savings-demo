from savings import Savings
from tkinter_savings import TkinterSavings

if __name__ == "__main__":
    observer = TkinterSavings()
    savings_application = Savings(savings_observer=observer)
    savings_application.start()
