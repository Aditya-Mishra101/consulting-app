from decimal import Decimal
from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column,relationship
from sqlalchemy import ForeignKey, UUID,Enum, Numeric,String,DateTime
from app.db.base import Base 
import uuid
from datetime import datetime
import enum


class TransactionStatus(str, enum.Enum):
    pending = "pending"
    paid = "paid"
    refunded = "refunded"
    failed = "failed"

class Transaction(Base):
    __tablename__ = "transactions"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    consultation_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("consultations.id"),
        nullable=False
    )

    consultation = relationship(
        "Consultation",
        back_populates="transactions"
    )

    amount : Mapped[Decimal] = mapped_column(
        Numeric(10,2),
        nullable=False
        )
    
    currency : Mapped[str] = mapped_column(
        String(3),
        nullable=False,
        default="USD"
        )
    
    status : Mapped[TransactionStatus] = mapped_column(
        Enum(TransactionStatus, name="transaction_status"),
        nullable=False,
        default=TransactionStatus.pending
        )

    paid_at :Mapped[Optional[datetime]] = mapped_column(
          DateTime(timezone=True),
          nullable=True
     )