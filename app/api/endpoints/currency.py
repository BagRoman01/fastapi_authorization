import logging
from fastapi import APIRouter, Depends
from app.api.dependencies import currency_service_dep
from app.api.endpoints.authentication import authorize
from app.models.schemas.currency import ExchangeCurrency, HistoryExchangeCurrency

##from fastapi_cache.decorator import cache

currency = APIRouter(prefix='/currency', tags=['currency'])
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


@currency.get('/all')
async def get_currencies(
        cur_service: currency_service_dep,
        user: str = Depends(authorize),
        currencies: str = None
):
    return await cur_service.get_currencies(currencies)


@currency.post('/exchange')
# @cache(expire=5)
async def exchange_currency(
        cur_service: currency_service_dep,
        exchange: ExchangeCurrency,
        user: str = Depends(authorize)
):
    return await cur_service.exchange_currency(exchange)


@currency.post('/history_exchange')
# @cache(expire=5)
async def exchange_currency(
        cur_service: currency_service_dep,
        exchange: HistoryExchangeCurrency,
        user: str = Depends(authorize)
):
    return await cur_service.history_exchange_currency(exchange)

