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