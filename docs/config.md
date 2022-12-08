<a id="aiomql.config"></a>

# aiomql.config

<a id="aiomql.config.Config"></a>

## Config Objects

```python
class Config()
```

Set config variables for your bot

**Arguments**:

- `file` _str_ - config file
- `record_trades` _bool_ - If true record trade in a csv file defaults to True
- `filename` _str_ - Name of config file, defaults to "mt5.json"
- `executor` - Type of pool executor, can be thread or process defaults to thread
- `records_dir(str)` - Name of directory for saving trades, defaults to trade records
- `win_percentage` _float_ - Percentage of expected profit that counts as a win
- `base_dir` _str | Path_ - Base directory for saving outputs.
  

**Attributes**:

  file (str):
  record_trades (bool):
  filename (str):
  executor (str):
  records_dir (str):
  win_percentage (float):
  base_dir (str | Path):
- `account_number` _int_ - Broker account number for
- `password` _str_ - Broker password
- `server` _str_ - Broker server
- `path` _str_ - Path to terminal file

<a id="aiomql.config.Config.set_attributes"></a>

#### set\_attributes

```python
def set_attributes(**kwargs)
```

Add attributes to the config object

**Arguments**:

- `**kwargs` - Set attributes as keyword arguments
  

