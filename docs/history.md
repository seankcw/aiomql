<a id="aiomql.history"></a>

# aiomql.history

<a id="aiomql.history.History"></a>

## History Objects

```python
class History()
```

The history class handles trade deals and trade orders in the trading history.

**Arguments**:

- `mt5` _MetaTrader_ - The Meta trader object for connecting to the terminal. Default Keyword Argument.
  
  
- `date_from` _datetime, float_ - Date the orders are requested from. Set by the 'datetime' object or as a number of seconds elapsed since
  1970.01.01. Defaults to the current time in "utc"
  
  
- `date_to` _datetime, float_ - Date, up to which the orders are requested. Set by the 'datetime' object or as a number of
  seconds elapsed since 1970.01.01. Defaults to the current time in "utc"
  
  
- `group` _str_ - Filter for selecting history by symbols.
  
  
- `ticket` _int_ - Filter for selecting history by ticket number
  
  
- `position` _int_ - Filter for selecting history deals by position
  

**Attributes**:

- `deals` _Iterable[TradeDeal]_ - Iterable of trade deals
- `orders` _Iterable[TradeOrder]_ - Iterable of trade orders
- `total_deals` - Total number of deals
- `total_orders` _int_ - Total number orders
- `group` _str_ - Filter for selecting history by symbols.
- `ticket` _int_ - Filter for selecting history by ticket number
- `position` _int_ - Filter for selecting history deals by position
- `initialized` _bool_ - check if initial request has been sent to the terminal to get history.

<a id="aiomql.history.History.init"></a>

#### init

```python
async def init(deals=True, orders=True) -> bool
```

Get history deals and orders

**Arguments**:

- `deals` _bool_ - If true get history deals during initial request to terminal
- `orders` _bool_ - If true get history orders during initial request to terminal
  

**Returns**:

- `bool` - True if all requests were successful else False

<a id="aiomql.history.History.get_deals"></a>

#### get\_deals

```python
async def get_deals() -> list[TradeDeal]
```

Get trade deals

**Returns**:

- `list[TradeDeal]` - Iterable of trade deals

<a id="aiomql.history.History.deals_total"></a>

#### deals\_total

```python
async def deals_total() -> int
```

Get total number of deals
Returns (int): Number of Deals

<a id="aiomql.history.History.get_orders"></a>

#### get\_orders

```python
async def get_orders() -> list[TradeOrder]
```

Get trade orders

**Returns**:

- `list[TradeOrder])` - Iterable of trade orders

<a id="aiomql.history.History.orders_total"></a>

#### orders\_total

```python
async def orders_total() -> int
```

Get total number of orders
Returns (int): Number of orders

