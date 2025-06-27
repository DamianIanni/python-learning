# {
#     "account_id": 1,
#     "name": "John Doe",
#     "balance": 1000.0
# }

class User:
    id_autoincrement: int = 0

    def __init__(self, name: str, balance: float, country: str) -> None:
        """_summary_

        Args:
            name (str): _description_
            balance (float): _description_
        """        
        User.id_autoincrement += 1
        self.user_id =  User.id_autoincrement
        self.name = name
        self.balance = balance
        self.country = country

    def deposit_money(self, amount: float) -> None:
        """_summary_

        Args:
            amount (float): _description_
        """        
        self.balance += amount

    def withdraw_money(self, amount: float) -> None:
        """_summary_

        Args:
            amount (float): _description_
        """        
        self.balance -= amount

    def get_user_to_save_in_csv_file(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """        
        user = f"{self.name},{self.user_id},{self.balance}"
        return user

    def __str__(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """        
        to_print: str = f'User: {self.name} ({self.user_id} -> balance: {self.balance})'
        return to_print