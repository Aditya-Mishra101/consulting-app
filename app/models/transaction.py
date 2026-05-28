from decimal import Decimal
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, UUID,Enum 
from app.db.base import Base 
from sqlalchemy import DateTime
import uuid
from datetime import datetime, timezone
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
        Decimal(10,2),
        nullable=False
        )
    
    currency : Mapped[str] = mapped_column(
        nullable=False,
        default="USD"
        )
    
    status : Mapped[TransactionStatus] = mapped_column(
        Enum(TransactionStatus, name="transaction_status"),
        nullable=False
        )

    paid_at :Mapped[datetime] = mapped_column(
          DateTime(timezone=True),
          nullable=False
     )