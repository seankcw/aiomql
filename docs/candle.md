<a id="aiomql.candle"></a>

# aiomql.candle

<a id="aiomql.candle.Candle"></a>

## Candle Objects

```python
class Candle(Base)
```

A class representing rates from the charts as Japanese Candlesticks.
Subclass this class to add needed properties.

**Attributes**:

- `Index` _int_ - Position of the candle in the chart. Zero represents the most recent
- `time` _int_ - Period start time.
- `open` _int_ - Open price
- `high` _float_ - The highest price of the period
- `low` _float_ - The lowest price of the period
- `close` _float_ - Close price
- `tick_volume` _float_ - Tick volume
- `real_volume` _float_ - Trade volume
- `spread` _float_ - Spread
- `ema` _float, optional_ - ema

<a id="aiomql.candle.Candle.mid"></a>

#### mid

```python
@property
def mid() -> float
```

The mid of open and close
Returns: mid

<a id="aiomql.candle.Candle.is_bullish"></a>

#### is\_bullish

```python
def is_bullish() -> bool
```

Returns: True or Fasle

<a id="aiomql.candle.Candle.is_bearish"></a>

#### is\_bearish

```python
def is_bearish() -> bool
```

Returns: True or False

<a id="aiomql.candle.Candles"></a>

## Candles Objects

```python
class Candles()
```

A class representing a collection of rates as Candle Objects, Arranged chronologically.
Class is an iterable container

**Arguments**:

- `data` _DataFrame, tuple[tuple]_ - A pandas dataframe or a tuple of tuple as returned from the terminal
  

**Arguments**:

  candle (Type(Candle)): Type of Candle object represented by the class.
- `flip` _bool_ - If flip is True reverse data argument.
  

**Attributes**:

- `_data` - Dataframe Object holding the rates
- `Candle` - Candle class for individual objects

