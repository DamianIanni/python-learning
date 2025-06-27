from user import User
from transaction import Transaction
import csv

class Bank:
    users_list: list[User] = []
    transaction_lis: list[Transaction] = []

    def create_user(self, name: str, balance: float, country: str) -> None:
        """_summary_

        Args:
            name (str): _description_
            balance (float): _description_
        """        
        if not Bank._valid_name(name) or not Bank._valid_amount(balance) or not country.isalpha():
            return
        user: User = User(name, balance, country)
        Bank._add_user_to_list(user)

    def transfer_money(self,amount: float, sender_account_id: int, receiver_account_id: int) -> None:
        """_summary_

        Args:
            amount (float): _description_
            sender_account_id (int): _description_
            receiver_account_id (int): _description_
        """        
        if not Bank._valid_amount(amount):
            return
        Sender_user: User = Bank._get_user_by_id(sender_account_id)
        Receiver_user: User = Bank._get_user_by_id(receiver_account_id)

        has_sufficient_funds: bool = Bank._has_sufficient_funds(amount, Sender_user.balance)
        if not has_sufficient_funds:
            return

        Sender_user.withdraw_money(amount)
        Receiver_user.deposit_money(amount)
        
        transaction: Transaction = Transaction(amount, sender_account_id, receiver_account_id)
        
        Bank._add_transaction_to_list(transaction)

    def export_transactions_to_csv(self, path: str) -> None:
        """_summary_

        Args:
            path (str): _description_
        """        
        with open(path, mode="w", newline="") as file:
            writer = csv.writer(file)
            # Escribo encabezados
            writer.writerow(["from_user_id", "to_user_id", "amount", "timestamp"])
            # Escribo transacciones
            for t in self.transaction_lis:
                writer.writerow([t.from_account_id, t.to_account_id, t.amount, t.timestamp])

    def export_users_to_csv(self, path: str) -> None:
        """_summary_

        Args:
            path (str): _description_
        """        
        with open(path, mode="w", newline="") as file:
            writer = csv.writer(file)
            # Escribo encabezados
            writer.writerow(["user_id", "name", "balance", "country"])
            # Escribo usuarios
            for u in self.users_list:
                writer.writerow([u.user_id, u.name, u.balance, u.country])



    # Internal methods
    def _valid_amount(amount: float) -> bool:
        return amount > 0

    def _valid_name(name: str) -> bool:
        return len(name) > 0 and len(name) < 20 and name.isalpha()

    def _has_sufficient_funds(amount: float, user_balance: float) -> bool:
        return user_balance >= amount
            
    def _add_user_to_list(user: User) -> None:
        """_summary_

        Args:
            user (User): _description_
        """        
        Bank.users_list.append(user)

    def _add_transaction_to_list(transaction: Transaction) -> None:
        """_summary_

        Args:
            transaction (Transaction): _description_
        """        
        Bank.transaction_lis.append(transaction)

    def _get_user_by_id(account_id: int) -> User:
        """_summary_

        Args:
            account_id (int): _description_

        Raises:
            Exception: _description_

        Returns:
            User: _description_
        """        
        for user in Bank.users_list:
            if user.user_id == account_id:
                return user
        raise Exception("User not found")


    