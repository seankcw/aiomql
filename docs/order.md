<a id="aiomql.order"></a>

# aiomql.order

<a id="aiomql.order.Order"></a>

## Order Objects

```python
class Order(TradeRequest)
```

Trade order related functions and properties. Subclass of TradeRequest.

**Arguments**:

- `mt5` _MetaTrader_ - The Meta trader object for connecting to the terminal. Default Keyword Argument
- `kwargs` - Arguments for initializing the order object
  

**Attributes**:

- `action` _TradeAction_ - Trading operation type from TradeAction Enum
  
- `type_time` _OrderTime_ - Order type by expiration from OrderTime
  
- `type_filling` _OrderFilling_ - Order filling type from OrderFilling Enum
  

**Notes**:

  Other order properties are defined in the TradeRequest Object

<a id="aiomql.order.Order.orders_total"></a>

#### orders\_total

```python
async def orders_total()
```

Get the number of active orders. Update the total property

**Returns**:

- `int` - Number of active orders

<a id="aiomql.order.Order.orders_get"></a>

#### orders\_get

```python
async def orders_get(*, symbol="", group="", ticket=0)
```

Get active orders with the ability to filter by symbol or ticket. There are three call options.
Call without parameters. Return active orders on all symbols

**Arguments**:

- `symbol` _str_ - Symbol name. Optional named parameter. If a symbol is specified, the ticket parameter is ignored.
  
- `group` _str_ - The filter for arranging a group of necessary symbols. Optional named parameter. If the group is specified, the function
  returns only active orders meeting a specified criteria for a symbol name.
  
- `ticket` _int_ - Order ticket (ORDER_TICKET). Optional named parameter.
  

**Returns**:

- `list[TradeOrder]` - A list of active trade orders as TradeOrder objects

<a id="aiomql.order.Order.check"></a>

#### check

```python
async def check() -> OrderCheckResult
```

Check funds sufficiency for performing a required trading operation

**Returns**:

- `(OrderCheckResult)` - Returns OrderCheckResult object

<a id="aiomql.order.Order.send"></a>

#### send

```python
async def send() -> OrderSendResult
```

Send a request to perform a trading operation from the terminal to the trade server.

**Returns**:

- `OrderSendResult` - Returns OrderSendResult object

<a id="aiomql.order.Order.calc_margin"></a>

#### calc\_margin

```python
async def calc_margin() -> float | None
```

Return margin in the account currency to perform a specified trading operation.

**Returns**:

- `float` - Returns float value if successful
- `None` - If not successful

<a id="aiomql.order.Order.calc_profit"></a>

#### calc\_profit

```python
async def calc_profit() -> float | None
```

Return profit in the account currency for a specified trading operation.

**Returns**:

- `float` - Returns float value if successful
- `None` - If not successful

