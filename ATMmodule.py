class ATM:
    def __init__(self, account_holder, balance=0):
        """Initialize the ATM with an account holder and an initial balance."""
        self.account_holder = account_holder
        self.balance = balance
        self.transactions = []  

    def check_balance(self):
        """Display the current balance."""
        print(f"Account Holder: {self.account_holder}")
        print(f"Current Balance: ${self.balance:.2f}")
        print("-" * 30)

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited: ${amount:.2f}") 
            print(f"${amount:.2f} has been deposited into your account.")
        else:
            print("Invalid deposit amount. Must be greater than zero.")
        print("-" * 30)

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount <= 0:
            print("Invalid withdrawal amount. Must be greater than zero.")
        elif amount > self.balance:
            print("Insufficient funds. Cannot withdraw this amount.")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrew: ${amount:.2f}") 
            print(f"${amount:.2f} has been withdrawn from your account.")
        print("-" * 30)

    def show_transaction_history(self):
        """Show the transaction history."""
        print("Transaction History:")
        if self.transactions:
            for transaction in self.transactions:
                print(transaction)
        else:
            print("No transactions yet.")
        print("-" * 30)
