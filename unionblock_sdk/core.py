from dataclasses import dataclass
from typing import List, Optional

class OTCApiException(Exception):
    pass

@dataclass
class OTCApiOrder:
    order_id: str
    base_token: str
    quote_token: str
    quantity: str
    side: str
    buy_price: str
    sell_price: str
    final_price: str
    market_price: str
    risk_rate: str
    canceled_at: str
    filled_at: str
    expire_at: str
    created_at: str
    status: str

    @classmethod
    def from_json(cls, json_data):
        if isinstance(json_data, list):
            return [cls.from_json(item) for item in json_data]
        else:
            return cls(
                order_id=json_data.get('order_id'),
                base_token=json_data.get('base_token'),
                quote_token=json_data.get('quote_token'),
                quantity=json_data.get('quantity'),
                side=json_data.get('side'),
                buy_price=json_data.get('buy_price'),
                sell_price=json_data.get('sell_price'),
                final_price=json_data.get('final_price'),
                market_price=json_data.get('market_price'),
                risk_rate=json_data.get('risk_rate'),
                canceled_at=json_data.get('canceled_at'),
                filled_at=json_data.get('filled_at'),
                expire_at=json_data.get('expire_at'),
                created_at=json_data.get('created_at'),
                status=json_data.get('status'),
            )

@dataclass
class OTCApiDeposit:
    tx_id: str
    token: str
    quantity: str
    from_address: str
    status: str
    to_address: str
    created_at: str

    @classmethod
    def from_json(cls, json_data):
        if isinstance(json_data, list):
            return [cls.from_json(item) for item in json_data]
        else:
            return cls(
                tx_id=json_data.get('tx_id'),
                token=json_data.get('token'),
                quantity=json_data.get('quantity'),
                from_address=json_data.get('from_address'),
                status=json_data.get('status'),
                to_address=json_data.get('to_address'),
                created_at=json_data.get('created_at'),
            )

@dataclass
class OTCApiWithdrawal:
    id: str
    bank: str
    wallet_id: str
    confirmation_id: str
    updated_at: str
    created_at: str

    @classmethod
    def from_json(cls, json_data):
        if isinstance(json_data, list):
            return [cls.from_json(item) for item in json_data]
        else:
            return cls(
                id=json_data.get('id'),
                bank=json_data.get('bank'),
                wallet_id=json_data.get('wallet_id'),
                confirmation_id=json_data.get('confirmation_id'),
                updated_at=json_data.get('updated_at'),
                created_at=json_data.get('created_at'),
            )

@dataclass
class OTCApiTransaction:
    id: str
    order: OTCApiOrder
    deposits: List[OTCApiDeposit]
    withdrawal: Optional[OTCApiWithdrawal]
    status: str
    updated_at: str
    created_at: str

    @classmethod
    def from_json(cls, json_data):
        if isinstance(json_data, list):
            return [cls.from_json(item) for item in json_data]
        else:
            return cls(
                id=json_data.get('id'),
                order=OTCApiOrder.from_json(json_data.get('order')),
                deposits=[OTCApiDeposit.from_json(deposit) for deposit in json_data.get('deposits', [])],
                withdrawal=OTCApiWithdrawal.from_json(json_data.get('withdrawal')) if json_data.get('withdrawal') else None,
                status=json_data.get('status'),
                updated_at=json_data.get('updated_at'),
                created_at=json_data.get('created_at'),
            )
