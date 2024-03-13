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