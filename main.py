import json
from web3 import Web3, HTTPProvider

from scan import Scan

if __name__ == '__main__':

  # connect to the node
  w3 = Web3(Web3.HTTPProvider('https://node.cheapeth.org/rpc'))
  DAI_ADDRESS = '0x6B175474E89094C44Da98b954EedeAC495271d0F'
  ABI = json.load(open('dai_abi.json'))

  # instantiate Scan
  scan = Scan(DAI_ADDRESS, ABI['result'], w3)

  # search for holders between 11818959 and the latest block
  #holders = scan.get_holders(11818959, w3.eth.get_block_number())
  holders = scan.get_holders(11818959, 11818964)

  # save holders into a file
  scan.save_holders('holders.json')
