import json
import hashlib


class Transaction:

    def __init__(self, tx_type, fromAddress, toAddress, amount, fee=0):
        self.tx_type = tx_type
        self.fromAddress = fromAddress
        self.toAddress = toAddress
        self.amount = amount
        self.fee = fee
        self.thash = None
        self.sign = None

    @property
    def txhash(self) -> bytes:
        return self.get_data_hash()

    def as_dict(self):
        # Возвращает представление объекта в виде словаря
        return {
            'tx_type': self.tx_type,
            'fromAddress': self.fromAddress,
            'toAddress': self.toAddress,
            'amount': self.amount,
            'fee': self.fee
        }

    def to_json(self):
        # Сериализует объект в строку JSON
        d = self.as_dict()
        return json.dumps(d)

    @classmethod
    def from_json(cls, json_str):
        # Создает и возвращает экземпляр класса из строки JSON
        data = json.loads(json_str)
        return cls(**data)

    def get_data_hash(self) -> bytes:
        """
        This method returns the hashes of the transaction data.
        """
        return hashlib.sha256(self.to_json().encode())

    def make_hash(self):
        """ Идентификатор транзакции """
        self.hash = self.get_data_hash().hexdigest()

    def sign_from_str(self, sign_str):
        """  требуется серилизация """
        self.sign = sign_str

if __name__ == '__main__':
    """ """

    t = Transaction("coinbase", "1", "2", "100")
    t.make_hash()
    # print(t.get_data_hash().hexdigest())
    print(t.txhash)
