<a id="aiomql.core.meta_trader"></a>

# aiomql.core.meta\_trader

<a id="aiomql.core.meta_trader.MetaTrader"></a>

## MetaTrader Objects

```python
class MetaTrader(Platform)
```

<a id="aiomql.core.meta_trader.MetaTrader.login"></a>

#### login

```python
async def login(login: int,
                password: str,
                server: str,
                timeout: int = 60000) -> bool
```



<a id="aiomql.core.meta_trader.MetaTrader.initialize"></a>

#### initialize

```python
async def initialize(path: str = "",
                     login: int = 0,
                     password: str = "",
                     server: str = "",
                     timeout: int = 60000,
                     portable=False) -> bool
```



<a id="aiomql.core.meta_trader.MetaTrader.shutdown"></a>

#### shutdown

```python
async def shutdown()
```



<a id="aiomql.core.meta_trader.MetaTrader.version"></a>

#### version

```python
async def version() -> tuple[int, int, str] | None
```



<a id="aiomql.core.meta_trader.MetaTrader.account_info"></a>

#### account\_info

```python
async def account_info() -> Platform.platform.AccountInfo
```



