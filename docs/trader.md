<a id="aiomql.trader"></a>

# aiomql.trader

<a id="aiomql.trader.Trader"></a>

## Trader Objects

```python
class Trader(ABC)
```

Helper class for creating a Trader object. Handles the initializing of an order and the placing of trades

**Arguments**:

- `symbol` _Symbol_ - Financial instrument
  
- `account` _Account_ - Trading account
  

**Attributes**:

  
- `symbol` _Symbol_ - Financial instrument class Symbol class or a subclass of it.
  
- `account` _Account_ - Trading account
  
- `order` _Order_ - Trade order

<a id="aiomql.trader.Trader.create_order"></a>

#### create\_order

```python
async def create_order(*args, **kwargs)
```

Create an order, and update the order object initialized

**Arguments**:

  *args:
  **kwargs:
  

<a id="aiomql.trader.Trader.place_trade"></a>

#### place\_trade

```python
@abstractmethod
async def place_trade(*args, **kwargs) -> TradeResult | None
```

Send trade to server

**Arguments**:

  *args:
  **kwargs:
  
- `Returns` - TradeResult if successful

