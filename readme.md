# README

## Requirements

* Electrum indexer node

## Install dependences

1. `python3 -m pip install cryptos`

## Configuration

```
SERVER_ADDRESS      = "testnet.nunchuk.io"  # Electrum indexer IP
SERVER_PORT         = 50001                 # Electrum indexer port
TESTNET             = True                  # True to check TESTNET netwok | False to check MAINNET
MAX_DEPTH           = 25                    # Max empty addresses to check
CURRENT_FEE_SATS    = 20                    # Current mempool fee amount in sats   

DEATH_UTXO_PERCETAGE    = 100               # UTXO percentage usage in the fee in order to be considered as non-transferable
BAD_UTXO_PERCETAGE      = 5                 # UTXO percentage usage in the fee in order to be considered as bad to transfer
REGULAR_UTXO_PERCETAGE  = 1                 # UTXO percentage usage in the fee in order to be considered as neutral to transfer

SIMPLE_PAYMENT_VBYTES   = 140               # Fee in vbytes for 1 input and 2 outputs

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
¡Connected to node!

Enter your XPUB: xpub6CUGRUonZSQ4TWtTMmzXdrXDtypWKiKrhko4egpiMZbpiaQL2jkwSB1icqYh2cfDfVxdx4df189oLKnC5fSwqPfgyP3hooxujYzAu3fDVmz

## Cheking up to 25 empty receive addresses... ##
[ bc1q36z7qxr0gjgm3uky0n08qnxh2zuzfh73vmhspx: 1 UTXO(s) ]
> a64fa7166be163ca0b50cd359a498f369d763e7b180a4f461727862bfd795b2a:1 - 950 sats [ DEATH | 294.74% ]
[ Total UTXOs: 1 ]
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
