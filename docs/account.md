<a id="aiomql.account"></a>

# aiomql.account

<a id="aiomql.account.Account"></a>

## Account Objects

```python
class Account(AccountInfo)
```

Properties and methods of the current trading account. Subclass of AccountInfo

**Arguments**:

- `mt5` _MetaTrader_ - The Meta trader object for connecting to the terminal. Default Keyword Argument
- `kwargs` - Arguments for AccountInfo attributes
  

**Attributes**:

- `risk` _float_ - Percentage of account to risk
- `risk_to_reward` _float_ - ratio of risk to reward
  connected (float):
  

**Notes**:

  Other Account properties are defined in the AccountInfo Object
  Since bot can only use one account at a time use the account class as a module style singleton object by importing the account object declared
  in this module instead of creating a new object.

<a id="aiomql.account.Account.refresh"></a>

#### refresh

```python
async def refresh()
```

Update the account info object with latest values from the terminal

**Returns**:

- `Account` - The Account Object with updated properties

<a id="aiomql.account.Account.login"></a>

#### login

```python
async def login()
```

Make sure account_number, password and server attributes have been initialized
Returns: True if login was successful else False

