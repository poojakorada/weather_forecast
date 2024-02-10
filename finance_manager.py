import tkinter as tk
from tkinter import messagebox

class FinanceManagerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Personal Finance Manager")
        self.master.geometry("500x500")
        self.master.configure(bg="lightgray")

        self.add_expense_button = tk.Button(master, text="Add Expense", command=self.add_expense, bg="lightblue")
        self.add_expense_button.pack(pady=10)

        self.view_expenses_button = tk.Button(master, text="View Expenses", command=self.view_expenses, bg="lightgreen")
        self.view_expenses_button.pack(pady=10)

        self.set_budget_button = tk.Button(master, text="Set Budget", command=self.set_budget, bg="lightyellow")
        self.set_budget_button.pack(pady=10)

        self.generate_report_button = tk.Button(master, text="Generate Report", command=self.generate_report, bg="lightcoral")
        self.generate_report_button.pack(pady=10)

        self.quit_button = tk.Button(master, text="Quit", command=master.quit, bg="lightsalmon")
        self.quit_button.pack(pady=10)

    def add_expense(self):
        expense_window = tk.Toplevel(self.master)
        expense_window.title("Add Expense")
        expense_window.configure(bg="lightgray")

        label_category = tk.Label(expense_window, text="Category:", bg="lightgray")
        label_category.grid(row=0, column=0)
        self.category_entry = tk.Entry(expense_window)
        self.category_entry.grid(row=0, column=1)

        label_amount = tk.Label(expense_window, text="Amount:", bg="lightgray")
        label_amount.grid(row=1, column=0)
        self.amount_entry = tk.Entry(expense_window)
        self.amount_entry.grid(row=1, column=1)

        add_button = tk.Button(expense_window, text="Add", command=self.save_expense, bg="lightblue")
        add_button.grid(row=2, columnspan=2)

    def save_expense(self):
        category = self.category_entry.get()
        amount = self.amount_entry.get()
        try:
            amount = float(amount)
            with open("expenses.txt", "a") as file:
                file.write(f"{category},{amount}\n")
            messagebox.showinfo("Success", "Expense added successfully!")
        except ValueError:
            messagebox.showerror("Error", "Invalid amount")

    def view_expenses(self):
        expenses_window = tk.Toplevel(self.master)
        expenses_window.title("View Expenses")
        expenses_window.configure(bg="lightgray")

        scrollbar = tk.Scrollbar(expenses_window)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        expenses_text = tk.Text(expenses_window, wrap=tk.WORD, yscrollcommand=scrollbar.set, bg="lightyellow")
        expenses_text.pack()

        with open("expenses.txt", "r") as file:
            expenses = file.readlines()
            for expense in expenses:
                expenses_text.insert(tk.END, expense)

        scrollbar.config(command=expenses_text.yview)

    def set_budget(self):
        budget_window = tk.Toplevel(self.master)
        budget_window.title("Set Budget")
        budget_window.configure(bg="lightgray")

        label_category = tk.Label(budget_window, text="Category:", bg="lightgray")
        label_category.grid(row=0, column=0)
        self.category_entry = tk.Entry(budget_window)
        self.category_entry.grid(row=0, column=1)

        label_amount = tk.Label(budget_window, text="Amount:", bg="lightgray")
        label_amount.grid(row=1, column=0)
        self.amount_entry = tk.Entry(budget_window)
        self.amount_entry.grid(row=1, column=1)

        set_button = tk.Button(budget_window, text="Set", command=self.save_budget, bg="lightblue")
        set_button.grid(row=2, columnspan=2)

    def save_budget(self):
        category = self.category_entry.get()
        amount = self.amount_entry.get()
        try:
            amount = float(amount)
            with open("budgets.txt", "a") as file:
                file.write(f"{category},{amount}\n")
            messagebox.showinfo("Success", "Budget set successfully!")
        except ValueError:
            messagebox.showerror("Error", "Invalid amount")

    def generate_report(self):
        # Your report generation logic here
        messagebox.showinfo("Report", "Report generated successfully!")


if __name__ == "__main__":
    root = tk.Tk()
    app = FinanceManagerApp(root)
    root.mainloop()
