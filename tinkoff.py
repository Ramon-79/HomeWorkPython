class Bank:
    BALANCE = 0
    MIN = 50
    MAX = 5000000
    COMMISSION = 0.015
    BONUS = 0.03
    TAX = 0.10
    OPERATION: int
    OPERATIONS: list[str]

    def __init__(self):
        self.OPERATION = 0
        self.OPERATIONS = dict()

    def replenishment(self, cash: int, tax: int) -> tuple[int, int] | None:
        if cash % self.MIN == 0:
            self.BALANCE += cash + tax
            self.OPERATION += 1
            self.OPERATIONS[f'+ {cash + tax}'] = 'Пополнение'
            return self.BALANCE, self.OPERATION
        else:
            return None

    def out(self, cash: int, commission: int, tax: int) -> tuple[int, int] | None:
        if cash % self.MIN == 0 and self.BALANCE > 0 and self.BALANCE - (cash + commission + tax) >= 0:
            self.BALANCE -= cash + commission + tax
            self.OPERATION += 1
            self.OPERATIONS[f'- {cash + commission + tax}'] = 'Снятие'
            return self.BALANCE, self.OPERATION
        else:
            return None

    def commission(self, cash: int) -> int:
        sum_commission = cash * self.COMMISSION
        _MAX = 600
        _MIN = 30
        if sum_commission > _MAX:
            sum_commission = _MAX
        elif sum_commission < _MIN:
            sum_commission = _MIN
        else:
            sum_commission = int(sum_commission)
        return sum_commission

    def tax(self, cash: int) -> int:
        if cash >=self.MAX:
            print(f'\nУплата налога на богатство в размере {cash * self.TAX}')
            return cash * self.TAX
        else:
            return 0

    def exit(self):
        return "Всего доброго, приходите к нам еще."

    def bonus(self):
            self.BALANCE += self.BALANCE * self.BONUS
            return f'Бонус за каждую 3-юю операцию в нашем банке . ' \
                   f'На ваш счет было зачислено: {int(self.BALANCE * self.BONUS)}\n'

    def operations(self) -> None:
        for summ, op in self.OPERATIONS.items():
            print(f'{summ} - {op}')

    def start(self, mode: str, cash: int = 0) -> str:
        if self.OPERATION % 3 == 0:
             print(self.bonus())
        tax = self.tax(cash)
        match mode:
            case "in":
                self.replenishment(cash=cash, tax=tax)
                return f"Зачисление средств, сумма: {cash}, баланс: {int(self.BALANCE)}"
            case "out":
                commission = self.commission(cash=cash)
                data = self.out(cash=cash, commission=commission, tax=tax)
                if data:
                    return f"Выполнено, сумма: {cash}, коммисия: {commission}, " \
                           f"баланс: {int(self.BALANCE)}"
                else:
                    return "Нехватает средств"

            case "show":
                self.operations()

            case "exit":
                return self.exit()


# bank = Bank()
# print(bank.start(mode='in', cash=4000000))
# print(bank.start(mode='in', cash=100000))
# print(bank.start(mode='out', cash=100000))
# print(bank.start(mode='in', cash=100000))
# print(bank.start(mode='in', cash=1000000))
# print(bank.start(mode='in', cash=2000000))
# print(bank.start(mode='out', cash=5000000))
# print(bank.start(mode='show'))
