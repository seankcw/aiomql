<a id="aiomql.executor"></a>

# aiomql.executor

<a id="aiomql.executor.Executor"></a>

## Executor Objects

```python
class Executor()
```

Executor class for running multiple strategies and instruments concurrently.

**Attributes**:

- `executor` _ThreadPoolExecutor, ProcessPoolExecutor_ - Executor object.
- `workers` _list_ - List of strategies.

<a id="aiomql.executor.Executor.add_workers"></a>

#### add\_workers

```python
def add_workers(strategies: Sequence[type(Strategy)])
```

Add multiple strategies at once

**Arguments**:

- `strategies` _Sequence[Strategy]_ - A sequence of strategies.
  

<a id="aiomql.executor.Executor.remove_workers"></a>

#### remove\_workers

```python
def remove_workers(*symbols: Sequence[Symbol])
```

Remove worker if the symbol of the strategy did not initialize successfully

<a id="aiomql.executor.Executor.add_worker"></a>

#### add\_worker

```python
def add_worker(strategy: type(Strategy))
```

Add a strategy object to the list of workers

**Arguments**:

- `strategy` _Strategy_ - A strategy object
  

<a id="aiomql.executor.Executor.run"></a>

#### run

```python
@staticmethod
def run(strategy: type(Strategy))
```

Wrap the coroutine in asyncio.run for each thread.

**Arguments**:

- `strategy` _Strategy_ - A strategy object
  

<a id="aiomql.executor.Executor.execute"></a>

#### execute

```python
def execute(workers: int = 0)
```

Add workers to pool executors.

**Arguments**:

- `workers` - Number of workers to use in executor pool. Defaults to zero
  

