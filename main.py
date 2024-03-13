import json
import sys
import config
from node import Node
from tools import reversed_script_hash
from cryptos import *

# Style
class colors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    HEADER = '\033[95m'
    END = '\033[0m'

def printc(str):
    print(str + colors.END)

# Public functions
def get_utxo_healthy(amount):
    percentage = get_usage_percentage(amount)

    if (percentage >= config.DEATH_UTXO_PERCETAGE):
        return "DEATH";
    elif (percentage >= config.BAD_UTXO_PERCETAGE):
        return "BAD";
    elif (percentage >= config.REGULAR_UTXO_PERCETAGE):
        return "REGULAR";
    else:
        return "GOOD";

def get_utxo_color(amount):
    percentage = get_usage_percentage(amount)

    if (percentage >= config.DEATH_UTXO_PERCETAGE):
        return "";
    elif (percentage >= config.BAD_UTXO_PERCETAGE):
        return colors.RED;
    elif (percentage >= config.REGULAR_UTXO_PERCETAGE):
        return colors.YELLOW;
    else:
        return colors.GREEN;

def get_usage_percentage(amount):
    current_fee = round(config.SIMPLE_PAYMENT_VBYTES * config.CURRENT_FEE_SATS);
    return current_fee/amount * 100;

def generate_healthy_report(wallet, address_type = 'RECEIVE'):
    addresses_with_balance = 0;
    consecutive_empty_addresses = 0;

    while consecutive_empty_addresses <= config.MAX_DEPTH:
        consecutive_empty_addresses += 1;

        try:
            if (address_type == 'RECEIVE'):
                address = wallet.new_receiving_address();
            else:
                address = wallet.new_change_address();
        except:
            printc(colors.RED + 'Provided xpub not valid.\n')
            sys.exit(0)

        scripthash = reversed_script_hash(address);

        raw_utxos = node.get_utxos(scripthash);
        utxos = json.loads(raw_utxos);

        if (len(utxos['result']) > 0):
            consecutive_empty_addresses = 0
            printc(colors.BOLD + '[ ' + address + ': ' + str(len(utxos['result'])) + ' UTXO(s) ]');
            for x in utxos['result']:
                addresses_with_balance += 1;
                printc( get_utxo_color(x['value']) + '> ' + x['tx_hash'] + ':' + str(x['tx_pos']) + ' - ' + str(x['value']) + ' sats [ ' + get_utxo_healthy(x['value']) + ' | ' + str(round(get_usage_percentage(x['value']),2)) + '%' +' ]');

    print('[ Total UTXOs: ' + str(addresses_with_balance) + ' ]');

# Main
if __name__ == '__main__':

    printc(colors.BLUE + 'Connecting to node...\n')

    node = Node(config.SERVER_ADDRESS, config.SERVER_PORT)
    
    if (not node.ping()):
        printc(colors.RED + 'Unable to connect to electrs / fulcrum node. Check address and port. :(\n')
        sys.exit(0)

    printc(colors.GREEN + '¡Connected to ' + config.SERVER_ADDRESS + '!\n')

    xpub = input("Enter your XPUB: ")
    print();

    network = Bitcoin(testnet=config.TESTNET)
    wallet = network.watch_electrum_p2wpkh_wallet(xpub)

    printc(colors.HEADER + '## Cheking up to ' + str(config.MAX_DEPTH) + ' empty receive addresses... ##');
    generate_healthy_report(wallet);
    printc(colors.HEADER + '## Finished receiving addresses check ##\n');

    if (config.CHECK_CHANGE_ADDRESSES):
        printc(colors.HEADER + '## Cheking up to ' + str(config.MAX_DEPTH) + ' empty change addresses... ##');
        generate_healthy_report(wallet, 'CHANGE');
        printc(colors.HEADER + '## Finished change addresses check ##\n');

