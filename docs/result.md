<a id="aiomql.result"></a>

# aiomql.result

<a id="aiomql.result.TradeResult"></a>

## TradeResult Objects

```python
class TradeResult()
```

Save result of trades made by a strategy to a csv file.

**Arguments**:

- `result` _OrderSendResult_ - OrderSendResult object of an executed trade
- `request` _Order | dict_ - Order object or a dict of trade order request properties
- `parameters` _dict_ - The parameters of the strategy placing the trade
- `time` _float_ - Timestamp of when order was placed
- `name` - Name  of strategy or any desired name for the result csv file

**Attributes**:

- `config` - The configuration object
- `result` _dict_ - Trade result as a dict
- `request` _dict_ - Trade order as a dict
- `parameters` _dict_ - The parameters of the strategy placing the trade
- `time` - Timestamp
- `time` _float_ - Timestamp of when order was placed
- `name` - Name  of strategy or any desired name for the result csv file
  

**Notes**:

  To enable saving trades as csv file. Make sure that config.record_trades is True

<a id="aiomql.result.TradeResult.data"></a>

#### data

```python
@property
@cache
def data() -> dict
```

A dict representing data to be saved in the csv file. It is a combination of the strategy parameters, the order result properties, the trade
request properties, actual profit made from trade, timestamp of when trade was placed, closed to indicate if trade has been closed and win to
indicate if trade was successful or not
Returns (dict): A dict of data to be saved

<a id="aiomql.result.TradeResult.to_csv"></a>

#### to\_csv

```python
async def to_csv()
```

Saves to csv file format

