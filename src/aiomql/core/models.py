import MetaTrader5 as mt5

from .constants import BookType, TradeAction, OrderType, OrderTime, OrderFilling, PositionType, PositionReason, DealType, DealEntry, DealReason, \
    SymbolChartMode, SymbolTradeMode, SymbolCalcMode, SymbolOptionMode, SymbolOrderGTCMode, SymbolOptionRight, SymbolTradeExecution, SymbolSwapMode, \
    DayOfWeek, ErrorCode, AccountTradeMode, AccountStopoutMode, AccountMarginMode

from . import Base

"""
This module hold data structures used in this library
"""


class AccountInfo(Base):
    """
    Information about account.

    Attributes:
        account_number: int
        password: str
        server: str
        trade_mode: AccountTradeMode
        balance: float
        leverage: float
        profit: float
        point: float
        amount: float = 0
        equity: float
        credit: float
        margin: float
        margin_level: float
        margin_free: float
        margin_mode: AccountMarginMode
        margin_so_mode: AccountStopoutMode
        margin_so_call: float
        margin_so_so: float
        margin_initial: float
        margin_maintenance: float
        fifo_close: bool
        limit_orders: float
        currency: str = "USD"
        trade_allowed: bool = True
        trade_expert: bool = True
        currency_digits: int
        assets: float
        liabilities: float
        commission_blocked: float
        name: str
        company: str
    """
    account_number: int
    password: str
    server: str
    trade_mode: AccountTradeMode
    balance: float
    leverage: float
    profit: float
    point: float
    amount: float = 0
    equity: float
    credit: float
    margin: float
    margin_level: float
    margin_free: float
    margin_mode: AccountMarginMode
    margin_so_mode: AccountStopoutMode
    margin_so_call: float
    margin_so_so: float
    margin_initial: float
    margin_maintenance: float
    fifo_close: bool
    limit_orders: float
    currency: str = "USD"
    trade_allowed: bool = True
    trade_expert: bool = True
    currency_digits: int
    assets: float
    liabilities: float
    commission_blocked: float
    name: str
    company: str


class TerminalInfo(Base):
    """
    Hold Terminal Information

    Attributes:
        community_account: bool
        community_connection: bool
        connected: bool
        dlls_allowed: bool
        trade_allowed: bool
        tradeapi_disabled: bool
        email_enabled: bool
        ftp_enabled: bool
        notifications_enabled: bool
        mqid: bool
        build: int
        maxbars: int
        codepage: int
        ping_last: int
        community_balance: float
        retransmission: float
        company: str
        name: str
        language: str
        path: str
        data_path: str
        commondata_path: str
    """
    community_account: bool
    community_connection: bool
    connected: bool
    dlls_allowed: bool
    trade_allowed: bool
    tradeapi_disabled: bool
    email_enabled: bool
    ftp_enabled: bool
    notifications_enabled: bool
    mqid: bool
    build: int
    maxbars: int
    codepage: int
    ping_last: int
    community_balance: float
    retransmission: float
    company: str
    name: str
    language: str
    path: str
    data_path: str
    commondata_path: str


class SymbolInfo(Base):
    """
    Holds Symbol Information

    Attributes:
        name: str
        custom: bool
        chart_mode: SymbolChartMode
        select: bool
        visible: bool
        session_deals: int
        session_buy_orders: int
        session_sell_orders: int
        volume: float
        volumehigh: float
        volumelow: float
        time: int
        digits: int
        spread: float
        spread_float: bool
        ticks_bookdepth: int
        trade_calc_mode: SymbolCalcMode
        trade_mode: SymbolTradeMode
        start_time: int
        expiration_time: int
        trade_stops_level: int
        trade_freeze_level: int
        trade_exemode: SymbolTradeExecution
        swap_mode: SymbolSwapMode
        swap_rollover3days: DayOfWeek
        margin_hedged_use_leg: bool
        expiration_mode: int
        filling_mode: int
        order_mode: int
        order_gtc_mode: SymbolOrderGTCMode
        option_mode: SymbolOptionMode
        option_right: SymbolOptionRight
        bid: float
        bidhigh: float
        bidlow: float
        ask: float
        askhigh: float
        asklow: float
        last: float
        lasthigh: float
        lastlow: float
        volume_real: float
        volumehigh_real: float
        volumelow_real: float
        option_strike: float
        point: float
        trade_tick_value: float
        trade_tick_value_profit: float
        trade_tick_value_loss: float
        trade_tick_size: float
        trade_contract_size: float
        trade_accrued_interest: float
        trade_face_value: float
        trade_liquidity_rate: float
        volume_min: float
        volume_max: float
        volume_step: float
        volume_limit: float
        swap_long: float
        swap_short: float
        margin_initial: float
        margin_maintenance: float
        session_volume: float
        session_turnover: float
        session_interest: float
        session_buy_orders_volume: float
        session_sell_orders_volume: float
        session_open: float
        session_close: float
        session_aw: float
        session_price_settlement: float
        session_price_limit_min: float
        session_price_limit_max: float
        margin_hedged: float
        price_change: float
        price_volatility: float
        price_theoretical: float
        price_greeks_delta: float
        price_greeks_theta: float
        price_greeks_gamma: float
        price_greeks_vega: float
        price_greeks_rho: float
        price_greeks_omega: float
        price_sensitivity: float
        basis: str
        category: str
        currency_base: str
        currency_profit: str
        currency_margin: Any
        bank: str
        description: str
        exchange: str
        formula: Any
        isin: Any
        name: str
        page: str
        path: str
    """
    custom: bool
    chart_mode: SymbolChartMode
    select: bool
    visible: bool
    session_deals: int
    session_buy_orders: int
    session_sell_orders: int
    volume: float
    volumehigh: float
    volumelow: float
    time: int
    digits: int
    spread: float
    spread_float: bool
    ticks_bookdepth: int
    trade_calc_mode: SymbolCalcMode
    trade_mode: SymbolTradeMode
    start_time: int
    expiration_time: int
    trade_stops_level: int
    trade_freeze_level: int
    trade_exemode: SymbolTradeExecution
    swap_mode: SymbolSwapMode
    swap_rollover3days: int  # Should use - DayOfWeek
    margin_hedged_use_leg: bool
    expiration_mode: int
    filling_mode: int
    order_mode: int
    order_gtc_mode: SymbolOrderGTCMode
    option_mode: SymbolOptionMode
    option_right: SymbolOptionRight
    bid: float
    bidhigh: float
    bidlow: float
    ask: float
    askhigh: float
    asklow: float
    last: float
    lasthigh: float
    lastlow: float
    volume_real: float
    volumehigh_real: float
    volumelow_real: float
    option_strike: float
    point: float
    trade_tick_value: float
    trade_tick_value_profit: float
    trade_tick_value_loss: float
    trade_tick_size: float
    trade_contract_size: float
    trade_accrued_interest: float
    trade_face_value: float
    trade_liquidity_rate: float
    volume_min: float
    volume_max: float
    volume_step: float
    volume_limit: float
    swap_long: float
    swap_short: float
    margin_initial: float
    margin_maintenance: float
    session_volume: float
    session_turnover: float
    session_interest: float
    session_buy_orders_volume: float
    session_sell_orders_volume: float
    session_open: float
    session_close: float
    session_aw: float
    session_price_settlement: float
    session_price_limit_min: float
    session_price_limit_max: float
    margin_hedged: float
    price_change: float
    price_volatility: float
    price_theoretical: float
    price_greeks_delta: float
    price_greeks_theta: float
    price_greeks_gamma: float
    price_greeks_vega: float
    price_greeks_rho: float
    price_greeks_omega: float
    price_sensitivity: float
    basis: str
    category: str
    currency_base: str
    currency_profit: str
    currency_margin: str
    bank: str
    description: str
    exchange: str
    formula: str
    isin: str
    name: str
    page: str
    path: str


class BookInfo(Base):
    """
    Book Info

    Attributes:
        type: BookType
        price: float
        volume: float
        volume_dbl: float
    """
    type: BookType
    price: float
    volume: float
    volume_dbl: float


class TradeOrder(Base):
    """
    Trade Order

    Attributes:
        ticket: int
        time_setup: int
        time_setup_msc: int
        time_done: int
        time_done_msc: int
        time_expiration: int
        type: int
        type_time: int
        type_filling: int
        state: int
        magic: int
        reason: int
        position_id: int
        position_by_id: int
        volume_initial: float
        volume_current: float
        price_open: float
        sl: float
        tp: float
        price_current: float
        price_stoplimit: float 
        symbol: str
        comment: str
        external_id: str
    """
    ticket: int
    time_setup: int
    time_setup_msc: int
    time_done: int
    time_done_msc: int
    time_expiration: int
    type: int
    type_time: int
    type_filling: int
    state: int
    magic: int
    reason: int
    position_id: int
    position_by_id: int
    volume_initial: float
    volume_current: float
    price_open: float
    sl: float
    tp: float
    price_current: float
    price_stoplimit: float
    symbol: str
    comment: str
    external_id: str


class TradeRequest(Base):
    """
    Trade Request

    Attributes:
        action: TradeAction
        type: OrderType
        order: int
        symbol: str
        volume: float
        sl: float
        tp: float
        price: float
        deviation: float
        stoplimit: float
        type_time: OrderTime
        type_filling: OrderFilling
        expiration: int
        position: int
        position_by: int
        comment: str
        magic: int  
    """
    action: TradeAction
    type: OrderType
    order: int
    symbol: str
    volume: float
    sl: float
    tp: float
    price: float
    deviation: float
    stoplimit: float
    type_time: OrderTime
    type_filling: OrderFilling
    expiration: int
    position: int
    position_by: int
    comment: str
    magic: int


class OrderCheckResult(Base):
    """
    Order Check Result

    Attributes:
        retcode: int
        balance: float
        equity: float
        profit: float
        margin: float
        margin_free: float
        margin_level: float
        comment: str
        request: TradeRequest
    """
    retcode: int
    balance: float
    equity: float
    profit: float
    margin: float
    margin_free: float
    margin_level: float
    comment: str
    request: mt5.TradeRequest


class OrderSendResult(Base):
    """
    Order Send Result

    Attributes:
        retcode: int
        deal: int
        order: int
        volume: float
        price: float
        bid: float
        ask: float
        comment: str
        request: TradeRequest
        request_id: int
        retcode_external: int
        profit: float
    """
    retcode: int
    deal: int
    order: int
    volume: float
    price: float
    bid: float
    ask: float
    comment: str
    request: mt5.TradeRequest
    request_id: int
    retcode_external: int
    profit: float


class TradePosition(Base):
    """
    Trade Position

    Attributes:
        ticket: int
        time: int
        time_msc: int
        time_update: int
        time_update_msc: int
        type: OrderType
        magic: float
        identifier: int
        reason: PositionReason
        volume: float
        price_open: float
        sl: float
        tp: float
        price_current: float
        swap: float
        profit: float
        symbol: str
        comment: str
        external_id: str
    """
    ticket: int
    time: int
    time_msc: int
    time_update: int
    time_update_msc: int
    type: OrderType
    magic: float
    identifier: int
    reason: PositionReason
    volume: float
    price_open: float
    sl: float
    tp: float
    price_current: float
    swap: float
    profit: float
    symbol: str
    comment: str
    external_id: str


class TradeDeal(Base):
    """
    Trade Deal

    Attributes:
        ticket: int
        order: int
        time: int
        time_msc: int
        type: DealType
        entry: DealEntry
        magic: int
        position_id: int
        reason: DealReason
        volume: float
        price: float
        commission: float
        swap: float
        profit: float
        fee: float
        sl: float
        tp: float
        symbol: str
        comment: str
        external_id: str
    """
    ticket: int
    order: int
    time: int
    time_msc: int
    type: DealType
    entry: DealEntry
    magic: int
    position_id: int
    reason: DealReason
    volume: float
    price: float
    commission: float
    swap: float
    profit: float
    fee: float
    sl: float
    tp: float
    symbol: str
    comment: str
    external_id: str


class TerminalInfo(Base):
    """
    Terminal Properties

    Attributes:
        community_account: bool
        community_connection: bool
        connected: bool
        dlls_allowed: bool
        trade_allowed: bool
        tradeapi_disabled: bool
        email_enabled: bool
        ftp_enabled: bool
        notifications_enabled: bool
        mqid: bool
        build: int
        maxbars: int
        codepage: int
        ping_last: int
        community_balance: float
        retransmission: int
        company: str
        name: str
        language: str
        path: str
        data_path: str
    """
    community_account: bool
    community_connection: bool
    connected: bool
    dlls_allowed: bool
    trade_allowed: bool
    tradeapi_disabled: bool
    email_enabled: bool
    ftp_enabled: bool
    notifications_enabled: bool
    mqid: bool
    build: int
    maxbars: int
    codepage: int
    ping_last: int
    community_balance: float
    retransmission: int
    company: str
    name: str
    language: str
    path: str
    data_path: str
    commondata_path: str


class Error:
    """
    Simple Error class

    Args:
        code (int): Error code as returned
        description (str): description of error

    Attributes:
         code (ErrorCode): Error code as ErrorCode Enum
         description (int): error description
    """

    def __init__(self, code: int, description: str):
        self.code = ErrorCode(code)
        self.description = description

    def __repr__(self):
        return f"{self.__class__.__name__}(code={self.code}, description={self.description})"

    def __str__(self):
        return f"""
        Error Code: {self.code}
        Error Description: {self.description}
        """
