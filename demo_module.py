from math import factorial
from pprint import pprint as pp
from bittrex import Bittrex as Bx


key = "136798590cf24b45a2c2a455c35061b4"
private = "d4758d357cc049279b8289ef8c50b0d6"

my_bittrex = Bx(api_key=key, api_secret=private)


if __name__ == '__main__':
    mark = my_bittrex.get_markets()
    wallets = my_bittrex.get_balances()
    pp(mark)
    pp(wallets)
