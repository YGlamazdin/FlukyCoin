import time

from core.transaction import Transaction
from core.Block import Block
from core.protocol import Protocol

from net.client import Client
import random
if __name__ == '__main__':
    """ """

    t = Transaction("coinbase", random.randint(0,100000), "2", "100")
    t.make_hash()
    # print(t.get_data_hash().hexdigest())
    print(t.txhash)

    block = Block().create(0, None, time.time(),[], None )



