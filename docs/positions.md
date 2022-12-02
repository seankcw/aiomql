<a id="aiomql.positions"></a>

# aiomql.positions

<a id="aiomql.positions.Positions"></a>

## Positions Objects

```python
class Positions()
```

Hold open positions related properties and objects

**Arguments**:

- `mt5` _MetaTrader_ - The Meta trader object for connecting to the terminal. Default Keyword Argument
- `symbol` _str_ - Financial instrument name
- `group` _str_ - The filter for arranging a group of necessary symbols. Optional named parameter. If the group is specified, the function returns
  only positions meeting a specified criteria for a symbol name.
- `ticket` _int_ - Position ticket
  

**Attributes**:

- `symbol` _str_ - Financial instrument name
  
- `group` _str_ - The filter for arranging a group of necessary symbols. Optional named parameter. If the group is specified, the function returns
  only positions meeting a specified criteria for a symbol name.
  
- `ticket` _int_ - Position ticket
  
- `positions` _list[TradePosition]_ - A list of trade positions
  
  total_positions (int):

<a id="aiomql.positions.Positions.positions_total"></a>

#### positions\_total

```python
async def positions_total() -> int
```

Get open positions with the ability to filter by symbol or ticket.
Returns (int): Return integer value

<a id="aiomql.positions.Positions.positions_get"></a>

#### positions\_get

```python
async def positions_get()
```

Get open positions with the ability to filter by symbol or ticket.

**Returns**:

- `list[TradePosition]` - A list of open trade positions

<a id="aiomql.positions.Positions.close_all"></a>

#### close\_all

```python
async def close_all() -> int
```

Close all open positions
Returns (int): Return number of open positions

