from datetime import datetime

from pandas import DataFrame

from .core.meta_trader import MetaTrader
from .core.constants import TimeFrame, CopyTicks
from .core.models import SymbolInfo
from .ticks import Tick


class Symbol(SymbolInfo):
    tick: Tick
    selected: bool

    def __init__(self, mt5=MetaTrader(), **kwargs):
        self.mt5 = mt5
        super().__init__(**kwargs)

    def __repr__(self):
        return f"{self.name}"

    def __eq__(self, other: "Symbol"):
        return self.name == other.name

    def __lt__(self, other: "Symbol"):
        return self.name > other.name

    def __hash__(self):
        return hash(self.name)

    async def get_tick(self, name: str = ""):
        name = name if name else self.name
        tick = await self.mt5.symbol_info_tick(name)
        self.set_attributes(tick=tick, **tick._asdict())
        return Tick(**tick._asdict())

    async def _select(self):
        self.selected = await self.mt5.symbol_select(self.name, True)

    async def get_info(self):
        info = await self.mt5.symbol_info(self.name)
        if info:
            self.set_attributes(**info._asdict())

    async def init(self) -> bool:
        await self._select()
        if self.selected:
            await self.get_info()
        return self.selected

    async def rates_from_pos(self, *, time_frame: TimeFrame, count: int = 500, start_position: int = 0) -> DataFrame:
        rates = await self.mt5.copy_rates_from_pos(self.name, time_frame, start_position, count)
        return DataFrame(rates)

    async def ticks_from_pos(self, *, date_from: datetime | int, count: int = 100, flags: CopyTicks = CopyTicks.COPY_TICKS_INFO) -> DataFrame:
        ticks = await self.mt5.copy_ticks_from(self.name, date_from, count, flags)
        return DataFrame(ticks)

    async def rates_from_range(self, *, time_frame: TimeFrame, utf_from: datetime, utc_to: datetime) -> DataFrame:
        rates = await self.mt5.copy_rates_range(self.name, time_frame, utf_from, utc_to)
        return DataFrame(rates)
