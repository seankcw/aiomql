import logging

from aiomql import Config
from aiomql.account import account
from aiomql.terminal import terminal
from aiomql.lib.strategies.finger_trap import FingerTrap
from aiomql import Bot, Positions
from aiomql.lib.symbols.synthetic_symbol import SyntheticSymbol
from aiomql import Records
import asyncio

fmt = "%(asctime)s : %(message)s"

logging.basicConfig(filename='example.log', format=fmt, level=logging.DEBUG)

config = Config()
config.record_trades = True
config.set_attributes(account_number=30371334, password="*********", server="Deriv-Demo")

# market = SyntheticMarket()

def bot():
    bot = Bot()
    st = FingerTrap(symbol=SyntheticSymbol(name="Volatility 25 (1s) Index"))
    bot.add_single(strategy=st)
    # bot.add_strategy_all(strategy=FingerTrap)
    bot.execute()


async def record():
    account.set_attributes(account_number=30371334, password="*******", server="Deriv-Demo")
    await terminal.initialize()
    await account.login()

    await Records().update_trade_record(file="trade_records/FingerTrap.csv")
    # await Records().update_trade_records()


async def pos():
    await terminal.initialize()
    account.set_attributes(account_number=30371334, password="*******", server="Deriv-Demo")
    await account.login()
    await Positions().close_all()


# run bot
# bot()

# run an async function
asyncio.run(record())
