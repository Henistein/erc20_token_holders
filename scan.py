import json
from web3 import Web3, HTTPProvider
from web3._utils.filters import construct_event_filter_params
from tqdm import trange, tqdm


class Scan:
  def __init__(self, token_address, token_abi, w3):
    self.w3 = w3
    self.token = self._load_token(token_address, token_abi)
    self.collected = dict()

  def _load_token(self, token_address, token_abi):
    return self.w3.eth.contract(address=token_address, abi=token_abi)
  
  def _get_balance(self, address):
    return self.token.functions.balanceOf(address).call()

  def _add_address(self, address):
    if address not in self.collected.keys():
      balance = self._get_balance(address)
      if balance != 0:
        self.collected[address] = round(balance / 1e+18, 10)

  def save_holders(self, path):
    # save all_addresses set into json
    json.dump(self.collected, open(path, 'w'))
    
  def get_holders(self, fromBlock, toBlock):
    for i in (t := trange(fromBlock, toBlock)):
      # get block transactions
      block_txs = self.w3.eth.getBlock(i)['transactions']

      # collect 'to' and 'from' addresses
      for tx in tqdm(block_txs, leave=True):
        transaction = self.w3.eth.getTransaction(tx)
        # check if addresses have balance, if so add them to set
        if transaction['to'] is not None:
          self._add_address(transaction['to'])
        if transaction['from'] is not None:
          self._add_address(transaction['from'])
            
      t.set_description('Collected: %d' % len(self.collected)) 
    return self.collected

