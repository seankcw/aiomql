<a id="aiomql.strategy"></a>

# aiomql.strategy

<a id="aiomql.strategy.Entry"></a>

## Entry Objects

```python
@dataclass
class Entry()
```

A helper class for capturing entry positions.

**Attributes**:

- `time` _float_ - Time of the bar
  
- `trend` _str_ - The trend of the chart. Can be either of "notrend", "uptrend", "downtrend".
  
- `new` _bool_ - Shows if an entry position has been seen before.
  
- `type` _OrderType_ - OrderType for placing trade order
  
- `points` _float_ - points to trade.

<a id="aiomql.strategy.Strategy"></a>

## Strategy Objects

```python
class Strategy(ABC)
```

The base class for creating strategies.

**Arguments**:

- `symbol` _Symbol_ - The Financial Instrument as a Symbol Object
- `**kwargs` - Optional Keyword Arguments
  

**Attributes**:

- `Candle` _Type[Candle]_ - Can be a subclass of the Candle class specific to the strategy and analysis carried out on it.
  
- `Candles` _Type[Candles]_ - Candles class for the strategy can be the same or a subclass of the "candle.Candles" class.
  
- `name` _str_ - A name for the strategy. You can initialize a new name for the strategy that will replace the one defined as class parameter

<a id="aiomql.strategy.Strategy.get_ema"></a>

#### get\_ema

```python
async def get_ema(*,
                  time_frame: TimeFrame,
                  period: int,
                  count: int = 500) -> type(Candles)
```

Helper method that gets the ema of the bars.

**Arguments**:

- `time_frame` _TimeFrame_ - Timeframe of the bars returned
  
- `period` _int_ - Period of the ema
  
- `count` _int_ - Number of objects to be returned
  
- `Returns` - A Candles Object

<a id="aiomql.strategy.Strategy.sleep"></a>

#### sleep

```python
@staticmethod
async def sleep(secs: float)
```

Sleep for the needed amount of seconds between requests to the terminal

**Arguments**:

- `secs` _float_ - The time period of the requests, eg. when trading on the 5 minute time frame the value will be 300 secs
  
- `Returns` - None.

<a id="aiomql.strategy.Strategy.trade"></a>

#### trade

```python
@abstractmethod
async def trade()
```

Place trades using this method

