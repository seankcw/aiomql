<a id="aiomql.market"></a>

# aiomql.market

<a id="aiomql.market.Market"></a>

## Market Objects

```python
class Market(ABC)
```

An abstract base class for handling a market properties and functions

**Arguments**:

- `mt5` _MetaTrader_ - The Meta trader object for connecting to the terminal. Default Keyword Argument
  

**Attributes**:

- `instruments` _Set[str]_ - A set of financial instruments available in a Market eg Forex Market
  
- `symbols` _Set[Symbol]_ - A set of symbols that will be made available for the current trading session.
  
- `name` _str_ - A name for the market
  
- `symbol` _Symbol_ - The Symbol subclass for instruments in this market

<a id="aiomql.market.Market.select_all"></a>

#### select\_all

```python
def select_all()
```

Make all financial instruments in market available for trading

<a id="aiomql.market.Market.add"></a>

#### add

```python
def add(*, symbol: type(Symbol))
```

Add symbol object directly to the set of symbols for the trading session

**Arguments**:

- `symbol` - Symbol Object

<a id="aiomql.market.Market.select"></a>

#### select

```python
def select(*symbols, check: (bool) = True)
```

Add financial instruments to the set of trading symbols for the session.

**Arguments**:

- `*symbols` _Iterable[str]_ - symbol(s) to be added to the set of trading symbols. i.e you can add a single symbol or multiple symbols at once
  

**Arguments**:

- `check` _bool_ - if check is true makes sure the symbol is in the list of predefined financial instruments for the market

<a id="aiomql.market.Market.book_add"></a>

#### book\_add

```python
async def book_add(symbol: str) -> bool
```

Subscribes the MetaTrader 5 terminal to the Market Depth change events for a specified symbol.
If the symbol is not in the list of instruments for the market, This method will return False

**Arguments**:

- `symbol` _str_ - financial instrument name
  
- `Returns` - True if successful, otherwise – False.

<a id="aiomql.market.Market.book_get"></a>

#### book\_get

```python
async def book_get(*, symbol: str, check: bool = True) -> BookInfo
```

Returns a tuple from BookInfo featuring Market Depth entries for the specified symbol.

**Arguments**:

- `symbol` _str_ - financial instrument name
- `check` _bool_ - check if symbol is in the set of financial instruments
  
- `Returns` _BookInfo | None_ - Returns the Market Depth content as a BookInfo Object else None
  

**Raises**:

- `ValueError` - Raises ValueError if symbol is not in the list of instruments for the market.

<a id="aiomql.market.Market.book_release"></a>

#### book\_release

```python
async def book_release(symbol: str) -> bool
```

Cancels subscription of the MetaTrader 5 terminal to the Market Depth change events for a specified symbol.

**Arguments**:

- `symbol` - financial instrument name
  

**Returns**:

- `bool` - True if successful, otherwise – False.

<a id="aiomql.market.Market.init_symbols"></a>

#### init\_symbols

```python
async def init_symbols()
```

Initialize all symbols in the market for the current session

