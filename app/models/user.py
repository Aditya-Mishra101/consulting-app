from app.db.base import Base
from sqlalchemy import String, Enum,UUID
from datetime import datetime, timezone
import uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship
import enum


class UserRole(str, enum.Enum):
    client     = "client"
    consultant = "consultant"
    admin      = "admin"

class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    name: Mapped[str] = mapped_column(String(50), nullable=False)

    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)

    password: Mapped[str] = mapped_column(String, nullable=False)

    role: Mapped[UserRole] = mapped_column(
        Enum(UserRole, name="user_roles"),
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(timezone.utc),
        nullable=False
    )

    client_consultations = relationship(
        "Consultation",
        foreign_keys="Consultation.client_id",
        back_populates="client"
    )

    consultant_consultations = relationship(
        "Consultation",
        foreign_keys="Consultation.consultant_id",
        back_populates="consultant"
    )

    messages = relationship(
        "ChatMessage",
        back_populates="user"
    )