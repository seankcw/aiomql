<a id="aiomql.symbol"></a>

# aiomql.symbol

<a id="aiomql.symbol.Symbol"></a>

## Symbol Objects

```python
class Symbol(SymbolInfo)
```

Helper class with general properties and methods of a financial instrument.
You can inherit from this class and add your own properties and methods.
This class subclass of SymbolInfo which contains all symbol properties.
All methods of this class accept keyword only arguments.

**Arguments**:

- `mt5` - Platform, defaults to the MetaTrader5 class.
  

**Attributes**:

- `tick` _Tick_ - Price tick object for instrument
  

**Notes**:

  Full properties are on the SymbolInfo Object.
  Make sure Symbol is always initialized with a name argument

<a id="aiomql.symbol.Symbol.info_tick"></a>

#### info\_tick

```python
async def info_tick(*, name: str = "") -> Tick
```

Get Price Tick of the financial instrument

**Arguments**:

- `name` - if name is supplied get price tick of that financial instrument
  

**Returns**:

- `Tick` - Returns a Custom Tick Object

<a id="aiomql.symbol.Symbol.symbol_select"></a>

#### symbol\_select

```python
async def symbol_select(*, enable: bool = True) -> bool
```

Select a symbol in the MarketWatch window or remove a symbol from the window.
Update the select property

**Arguments**:

- `enable` _bool_ - Switch. Optional unnamed parameter. If 'false', a symbol should be removed from the MarketWatch window.
  Otherwise, it should be selected in the MarketWatch window. A symbol cannot be removed if open charts with this symbol are currently
  present or positions are opened on it.
  

**Returns**:

- `bool` - True if successful, otherwise – False.

<a id="aiomql.symbol.Symbol.info"></a>

#### info

```python
async def info() -> SymbolInfo | None
```

Get data on the specified financial instrument and update the symbol object properties

**Returns**:

- `bool` - True if successful else False

<a id="aiomql.symbol.Symbol.init"></a>

#### init

```python
async def init() -> bool
```

Initialized the symbol by pulling properties from the terminal

**Returns**:

- `bool` - Returns True if symbol info was successful initialized

<a id="aiomql.symbol.Symbol.copy_rates_from"></a>

#### copy\_rates\_from

```python
async def copy_rates_from(*, timeframe: TimeFrame, date_from: datetime | int,
                          count: int) -> DataFrame | None
```

Get bars from the MetaTrader 5 terminal starting from the specified date.

**Arguments**:

- `timeframe` _TimeFrame_ - Timeframe the bars are requested for. Set by a value from the TimeFrame enumeration. Required unnamed parameter.
  
- `date_from` _datetime | int_ - Date of opening of the first bar from the requested sample. Set by the 'datetime' object or as a number
  of seconds elapsed since 1970.01.01. Required unnamed parameter.
  
- `count` _int_ - Number of bars to receive. Required unnamed parameter.
  

**Returns**:

- `DateFrame` - Rates as pandas DataFrame object
- `None` - Return None if there is an error

<a id="aiomql.symbol.Symbol.copy_rates_from_pos"></a>

#### copy\_rates\_from\_pos

```python
async def copy_rates_from_pos(*,
                              timeframe: TimeFrame,
                              count: int = 500,
                              start_position: int = 0) -> DataFrame
```

Get bars from the MetaTrader 5 terminal starting from the specified index.

**Arguments**:

- `timeframe` _TimeFrame_ - TimeFrame value from TimeFrame Enum. Required keyword only parameter
  
- `count` _int_ - Number of bars to return. Keyword argument defaults to 500
  
- `start_position` _int_ - Initial index of the bar the data are requested from. The numbering of bars goes from present to past.
  Thus, the zero bar means the current one. Keyword argument defaults to 0.
  

**Returns**:

- `DataFrame` - Returns a Pandas DataFrame object of bars
- `None` - Return None if there is an error

<a id="aiomql.symbol.Symbol.copy_ticks_from"></a>

#### copy\_ticks\_from

```python
async def copy_ticks_from(*,
                          date_from: datetime | int,
                          count: int = 100,
                          flags: CopyTicks = CopyTicks.INFO) -> DataFrame
```

Get ticks from the MetaTrader 5 terminal starting from the specified date.

**Arguments**:

- `date_from` _datetime | int_ - Date the ticks are requested from. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01.
  
- `count` _int_ - Number of requested ticks. Defaults to 100
  
- `flags` _CopyTicks_ - A flag to define the type of the requested ticks from CopyTicks enum. INFO is the default
  

**Returns**:

- `DataFrame` - Returns a Pandas DataFrame object of ticks
- `None` - Return None if there is an error

<a id="aiomql.symbol.Symbol.copy_rates_range"></a>

#### copy\_rates\_range

```python
async def copy_rates_range(*, timeframe: TimeFrame, date_from: datetime | int,
                           date_to: datetime | int) -> DataFrame | None
```

Get bars in the specified date range from the MetaTrader 5 terminal.

**Arguments**:

- `timeframe` _TimeFrame_ - Timeframe the bars are requested for. Set by a value from the TimeFrame enumeration. Required unnamed parameter.
  
- `date_from` _datetime | int_ - Date the bars are requested from. Set by the 'datetime' object or as a number of seconds
  elapsed since 1970.01.01. Bars with the open time >= date_from are returned. Required unnamed parameter.
  
- `date_to` _datetime | int_ - Date, up to which the bars are requested. Set by the 'datetime' object or as a number of
  seconds elapsed since 1970.01.01. Bars with the open time <= date_to are returned. Required unnamed parameter.
  

**Returns**:

- `DataFrame` - Rates as pandas DataFrame object
- `None` - Return None if there is an error

<a id="aiomql.symbol.Symbol.copy_ticks_range"></a>

#### copy\_ticks\_range

```python
async def copy_ticks_range(*,
                           date_from: datetime | int,
                           date_to: datetime | int,
                           flags: CopyTicks = CopyTicks.INFO)
```

Get ticks for the specified date range from the MetaTrader 5 terminal.

**Arguments**:

- `date_from` - Date the bars are requested from. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Bars with
  the open time >= date_from are returned. Required unnamed parameter.
  
- `date_to` - Date, up to which the bars are requested. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Bars
  with the open time <= date_to are returned. Required unnamed parameter.
  
  flags (CopyTicks):
  

**Returns**:

- `DataFrame` - Rates as pandas DataFrame object
- `None` - Return None if there is an error

