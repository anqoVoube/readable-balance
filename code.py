class ReadableBalance:
    def __init__(self, balance: float) -> str:
        self.balance = balance
        self.return_balance = str(balance)

    def decimal_digits(self, length: int = 2):
        format_length = f".{length}f"
        self.return_balance = format(self.balance, format_length)
        return self

    def commas(self):
        if self.return_balance.find('.') != -1:
            int_decimal_sep =  self.return_balance.split('.')
            value_wout_decimals = int(int_decimal_sep[0])
            self.return_balance = f'{value_wout_decimals:,}' + '.' + str(int_decimal_sep[1])
        else:
            self.return_balance = f'{self.balance:,}'
        
        return self.return_balance

    @property
    def display(self):
        return self.return_balance


#x = ReadableBalance(5000)
#print(x.decimal_digits().display)

