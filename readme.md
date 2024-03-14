# README

## Requirements

* **Electrum indexer** node.
* **Tor Browser** installed on your computer, if your **Electrum indexer** is under the Tor network.

## Dependences

### Install

* `python3 -m pip install cryptos pysocks` 

### Usage

* `cryptos`, to derive public addresses from the xpub.
* `pysocks`, to connnect to nodes under Tor network.

## Configuration

```
SERVER_ADDRESS      = "testnet.nunchuk.io"  # Electrum indexer address or IP
SERVER_PORT         = 50001                 # Electrum indexer port

TOR_PROXY_ADDRESS   = False                 # Tor proxy addresss or IP | False to disable Tor proxy
TOR_PROXY_PORT      = False                 # Tor proxy port | False to disable Tor proxy

TESTNET                 = True              # True to check TESTNET network | False to check MAINNET
MAX_DEPTH               = 25                # Max empty addresses to check
CURRENT_FEE_SATS        = 20                # Current mempool fee amount in sats
SIMPLE_PAYMENT_VBYTES   = 140               # Fee in vbytes for 1 input and 2 outputs

DEATH_UTXO_PERCETAGE    = 100               # UTXO percentage usage in the fee in order to be considered as non-transferable
BAD_UTXO_PERCETAGE      = 5                 # UTXO percentage usage in the fee in order to be considered as bad to transfer
REGULAR_UTXO_PERCETAGE  = 1                 # UTXO percentage usage in the fee in order to be considered as neutral to transfer

CHECK_CHANGE_ADDRESSES  = True              # True to check all addresses | False for NOT checking change addresses
```

Set up your own configuration values on `main.py` file.

## Run

0. Make sure to set an Electrum / Electrs node in the configuration file.
1. Run: `python3 main.py`.
2. Enter an xpub when prompted.
3. Check the results.

## Output example

```
¡Connected to testnet.nunchuk.io!

Enter your XPUB: tpubDCEqoceNVNo5tAeUf5t4Hm5K3ftLbPM9HfoBp9QSKSZ5qYkfhksuDuEDXVHooXnPodAwGfBQK45rwPnQfo7bjJmmMpTHMsxA2mWg8ADhcN6

## Cheking up to 25 empty receive addresses... ##
[ tb1qqajupdvlpzmwgmhe43rd92kjd59khcuu8h8enx: 2 UTXO(s) ]
> 4738931221205f9352fe44ae43255b9cfaf8c1590e0464e32044daca7efa3aa4:0 - 90000 sats [ REGULAR | 3.11% ]
> 58bc34a653644856f513d36a173e1ab4d8038e3b5c12a156f938fcdcffe0cb9c:0 - 10000 sats [ BAD | 28.0% ]
[ tb1qrncf7c6tsvg29s40mklmvsjd9j6shcegc6ycqj: 1 UTXO(s) ]
> 6f8d142d59798a98125d0c24296ec3a2fe040d9b5091fe9608d075cc81d587fa:0 - 500000 sats [ GOOD | 0.56% ]
[ Total UTXOs: 3 ]
## Finished receiving addresses check ##

## Cheking up to 25 empty change addresses... ##
[ Total UTXOs: 0 ]
## Finished change addresses check ##
```

# Privacy concerns

The purpose of this project is to estimate the health of the UTXOs of a wallet from the public extended key in a private way.

The extended public key is a piece of data from where all the public addresses can be derived but cannot be used to move funds. Still, it is good practice to keep this information private.

After the public addresses have been derived, it is necessary to check the UTXOs of each one of these addresses on the blockchain, for this purpose we have implemented the use of the Electrum indexer.

Technically any public electrum node can be used, but this is not recommended. To keep your privacy, it is recommended to use your own node.
