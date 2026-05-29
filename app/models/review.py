from datetime import datetime, timezone
from typing import Optional
import uuid
from sqlalchemy import UUID, DateTime, ForeignKey, Text,SmallInteger,CheckConstraint
from sqlalchemy.orm import Mapped,mapped_column,relationship
from app.db.base import Base

class Review(Base):

    __tablename__ = "reviews"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key = True,
        default = uuid.uuid4
    )   

    consultation_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("consultations.id"),
        unique=True,
        nullable = False
    )

    rating: Mapped[int] = mapped_column(
        SmallInteger,
        CheckConstraint("rating >= 1 AND rating <= 5", name="rating_check"),
        nullable=False
        
    )

    comment: Mapped[Optional[str]] = mapped_column(
        Text,
        nullable = True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default =lambda: datetime.now(timezone.utc),
        nullable = False 
    )

    consultation = relationship(
        "Consultation",
        back_populates="review"
    )