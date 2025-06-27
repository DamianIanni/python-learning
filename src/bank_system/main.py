from bank import Bank

bank_system = Bank()

bank_system.create_user("Damian", 2500, "Argentina")
bank_system.create_user("Lautaro", 6500, "Argentina")
bank_system.create_user("Pauline", 2000, "Germany")
bank_system.create_user("Lina", 5000, "Germany")
bank_system.create_user("John", 8430, "UnitedStates")

bank_system.transfer_money(1000, 1, 2)
bank_system.transfer_money(2000, 3, 1)
bank_system.transfer_money(3000, 5, 4)
bank_system.transfer_money(3000, 5, 4)

bank_system.export_transactions_to_csv('src/bank_system/__data__/transactions.csv')
bank_system.export_users_to_csv('src/bank_system/__data__/users.csv')
