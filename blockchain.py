class blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
    
    def new_block(self):
        # create new block and add to chain
        pass

    def new_transaction(self):
        # add new transaction and add to list of transactions
        pass

    @staticmethod
    def hash(block):
        # hashes a block
        pass

    @property
    def last_block(block):
        # returns the last block in the chain
        pass
    