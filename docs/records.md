<a id="aiomql.records"></a>

# aiomql.records

<a id="aiomql.records.Records"></a>

## Records Objects

```python
class Records()
```

This utility class read trade records from csv files, and update them based on their closing positions

**Arguments**:

- `records_dir` _Path_ - Path to directory containing record of placed trades.
  

**Attributes**:

- `config` - Config object
  
- `records_dir(Path)` - Path to directory containing record of placed trades, If not given takes the default from the config

<a id="aiomql.records.Records.get_records"></a>

#### get\_records

```python
async def get_records()
```

get trade records from records_dir folder

<a id="aiomql.records.Records.read_record"></a>

#### read\_record

```python
async def read_record(file: Path)
```

Read and update trade records

**Arguments**:

- `file` - Trade record file
  

<a id="aiomql.records.Records.update_record"></a>

#### update\_record

```python
async def update_record(rows: Iterable) -> Iterable[dict]
```

Get update of trades in the record file.

**Arguments**:

- `rows` - rows of recorded trade in a particular file
  
- `Returns` - return rows of updated trades as an iterable of dicts

<a id="aiomql.records.Records.update_trade_records"></a>

#### update\_trade\_records

```python
async def update_trade_records()
```

Update trade records

<a id="aiomql.records.Records.update_trade_record"></a>

#### update\_trade\_record

```python
async def update_trade_record(file: Path | str)
```



