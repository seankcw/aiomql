<a id="aiomql.bot_builder"></a>

# aiomql.bot\_builder

<a id="aiomql.bot_builder.Bot"></a>

## Bot Objects

```python
class Bot()
```

Bot builder class

**Arguments**:

- `market` _Market_ - Financial Market containing the instruments you wish to trade on
  

**Arguments**:

- `market` _Market_ - Financial Market containing the instruments you wish to trade on
- `mt5` - MetaTrade class
- `account` _Account_ - Account object
  

**Attributes**:

- `account` _Account_ - Account Object
- `executor` - Bot Executor
- `market` _Market_ - Financial Market containing the instruments you wish to trade on
- `mt5` - MetaTrade class
- `config` - Config Object
- `remove_bad_symbols` _bool_ - If true remove symbols that were not successfully initialized

<a id="aiomql.bot_builder.Bot.add_single"></a>

#### add\_single

```python
def add_single(*, strategy: Strategy)
```

Add a single standalone strategy without any market object

**Arguments**:

- `strategy` _Strategy_ - Strategy
  

<a id="aiomql.bot_builder.Bot.add_strategy"></a>

#### add\_strategy

```python
def add_strategy(strategy: type(Strategy))
```

Add a strategy to the executor

**Arguments**:

- `strategy` - Strategy to run on bot
  

**Returns**:

  
- `Notes` - Make sure the symbol has been added to the market

<a id="aiomql.bot_builder.Bot.add_strategies"></a>

#### add\_strategies

```python
def add_strategies(strategies: list[type(Strategy)])
```

Add multiple strategies at the same time

**Arguments**:

- `strategies` - A list of strategies
  

<a id="aiomql.bot_builder.Bot.add_strategy_all"></a>

#### add\_strategy\_all

```python
def add_strategy_all(*, strategy: Type[Strategy], params: dict | None = None)
```

Use this to run a strategy on all available instruments in the market using the default parameters a one parameters for all symbols

**Arguments**:

- `strategy` - Strategy class
  
- `params` - A dictionary of parameters for the strategy
  

<a id="aiomql.bot_builder.Bot.add_strategy_many"></a>

#### add\_strategy\_many

```python
def add_strategy_many(*,
                      strategy: Type[Strategy],
                      symbols: Sequence[str],
                      params: dict | None = None)
```

Multiple strategies at once

**Arguments**:

  strategy:
  symbols:
  params:
  

