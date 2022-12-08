<a id="aiomql.ticks"></a>

# aiomql.ticks

<a id="aiomql.ticks.Tick"></a>

## Tick Objects

```python
class Tick(Base)
```

Price Tick of Financial Instrument

<a id="aiomql.ticks.Ticks"></a>

## Ticks Objects

```python
class Ticks()
```

Container data class for price ticks. Arrange in chronological order.
Supports iteration, slicing and assignment

**Arguments**:

- `data` _DataFrame | tuple[tuple]_ - Dataframe of price ticks or a tuple of tuples
  

**Arguments**:

- `flip` _bool_ - If flip is True reverse data argument.
  

**Attributes**:

- `_data` - Dataframe Object holding the ticks

