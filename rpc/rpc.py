import requests

payload = {
  "jsonrpc": "2.0",
    "method": "eth_getBalance",
      "params": [
          "0xDf1B72FC1bA5a77DD6c038DC2bc70746fFCA5caA",
              "latest"
                ],
                  "id": 0
                  }
r = requests.post('https://node.cheapeth.org/rpc', json=payload)

print(r.json())
