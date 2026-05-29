from datetime import datetime
import enum
from typing import Optional
import uuid

from sqlalchemy import UUID, DateTime, ForeignKey,Enum
from sqlalchemy.orm import mapped_column,Mapped

from app.db.base import Base

class consultation_status(str,enum.Enum):
    pending = "pending"
    confirmed = "confirmed"
    completed = "completed"
    cancelled = "cancelled"

class consultations(Base):
    __tablename__ = "consultations"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    client_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    consultant_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    scheduled_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )

    status:Mapped[consultation_status] = mapped_column(
        Enum(consultation_status,name="consultation_status"),
        nullable=False,
        default=consultation_status.pending
    )

    notes:Mapped[Optional[str]] = mapped_column(
        "User",
        nullable=True
    )

    
