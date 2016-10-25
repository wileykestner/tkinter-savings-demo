from savings import Savings
from tk_savings import TkSavings

if __name__ == "__main__":
    observer = TkSavings()
    savings_application = Savings(savings_observer=observer)
    savings_application.start()
