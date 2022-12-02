<a id="aiomql.terminal"></a>

# aiomql.terminal

<a id="aiomql.terminal.Terminal"></a>

## Terminal Objects

```python
class Terminal(TerminalInfo)
```

Terminal related functions and properties

**Arguments**:

- `mt5` _MetaTrader_ - The Meta trader object for connecting to the terminal. Default Keyword Argument
  

**Attributes**:

- `version` - Namedtuple of terminal version values
  

**Notes**:

  Other attributes are defined in the TerminalInfo Class

<a id="aiomql.terminal.Terminal.initialize"></a>

#### initialize

```python
async def initialize(*,
                     path: str = "",
                     login: int = 0,
                     password: str = "",
                     server: str = "",
                     timeout: int = 60000,
                     portable=False) -> bool
```

Establish a connection with the MetaTrader 5 terminal. There are three call options.
Call without parameters. The terminal for connection is found automatically.
Call specifying the path to the MetaTrader 5 terminal we want to connect to. word path as a keyword argument
Call specifying the trading account path and parameters i.e login, password, server, as keyword arguments, path can be omitted.

**Arguments**:

- `path(str)` - Path to the metatrader.exe or metatrader64.exe file. Optional unnamed parameter. It is indicated first without a parameter name.
  If the path is not specified, the module attempts to find the executable file on its own.
  
- `login` _int_ - Trading account number. Optional named parameter. If not specified, the last trading account is used.
  
- `password` _str_ - Trading account password. Optional named parameter. If the password is not set, the password for a specified trading account
  saved in the terminal database is applied automatically.
  
- `server` _str_ - Trade server name. Optional named parameter. If the server is not set, the server for a
  specified trading account saved in the terminal database is applied automatically.
  
- `timeout` _int_ - Connection timeout in milliseconds. Optional named parameter. If not specified, the value of
  60 000 (60 seconds) is applied.
  
- `portable` _bool_ - Flag of the terminal launch in portable mode. Optional named parameter. If not specified, the value of False is used.
  

**Returns**:

- `(bool)` - True if successful else False

<a id="aiomql.terminal.Terminal.shutdown"></a>

#### shutdown

```python
async def shutdown()
```

Close the previously established connection to the MetaTrader 5 terminal.

Returns: None

<a id="aiomql.terminal.Terminal.version"></a>

#### version

```python
@property
async def version()
```

Get the MetaTrader 5 terminal version.
This method returns the terminal version, build and release date as a tuple of three values

**Returns**:

- `Version` - version of tuple as Version object

<a id="aiomql.terminal.Terminal.info"></a>

#### info

```python
async def info()
```

Get the connected MetaTrader 5 client terminal status and settings. gets terminal info in the form of a named tuple structure (namedtuple).
Return None in case of an error. The info on the error can be obtained using last_error().

**Returns**:

- `(Terminal)` - Terminal status and settings as a terminal object.

<a id="aiomql.terminal.Terminal.symbols_total"></a>

#### symbols\_total

```python
async def symbols_total() -> int
```

Get the number of all financial instruments in the MetaTrader 5 terminal.

**Returns**:

- `int` - Total number of available symbols

<a id="aiomql.terminal.Terminal.symbols_get"></a>

#### symbols\_get

```python
async def symbols_get(group="") -> Iterator[SymbolInfo]
```

Get all financial instruments from the MetaTrader 5 terminal.

**Arguments**:

- `group` _str_ - The filter for arranging a group of necessary symbols. Optional parameter. If the group is specified, the function returns
  only symbols meeting a specified criteria.
  

**Returns**:

- `Iterator[Symbol]` - A generator of available symbols.
  
- `Notes` - The group parameter allows sorting out symbols by name. '*' can be used at the beginning and the end of a string. The group parameter
  can be used as a named or an unnamed one. Both options work the same way. The named option (group="GROUP") makes the code easier to read.
  The group parameter may contain several comma separated conditions. A condition can be set as a mask using '*'. The logical negation
  symbol '!' can be used for an exclusion. All conditions are applied sequentially, which means conditions of including to a group should be
  specified first followed by an exclusion condition. For example, group="*, !EUR" means that all symbols should be selected first
  and the ones containing "EUR" in their names should be excluded afterwards.

<a id="aiomql.terminal.Terminal.last_error"></a>

#### last\_error

```python
async def last_error() -> Error
```

Return data on the last error.

**Returns**:

- `ErrorCode` - Last error as ErrorCode object

