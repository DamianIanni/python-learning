# {
#     "from_account_id": 1,
#     "to_account_id": 2,
#     "amount": 500.0,
#     "timestamp": datetime.now()
# }

from datetime import datetime

class Transaction:
    def __init__(self, amount: float, from_account_id: int, to_account_id: int):
        """_summary_

        Args:
            amount (float): _description_
            from_account_id (int): _description_
            to_account_id (int): _description_
        """        
        self.amount = amount
        self.from_account_id = from_account_id
        self.to_account_id = to_account_id
        self.timestamp = datetime.now()

    def get_transaction__to_save_in_csv_file(self):
        """_summary_

        Returns:
            _type_: _description_
        """       
        transaction: str = f"{self.from_account_id},{self.to_account_id},{self.amount},{self.timestamp}"
        return transaction

    def __str__(self):
        return f"Transaction: {self.amount}"