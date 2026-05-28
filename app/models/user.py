from db.base import Base
from sqlalchemy import Column, String, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from uuid import uuid4
import enum


class UserRole(str, enum.Enum):
    client     = "client"
    consultant = "consultant"
    admin      = "admin"

class User(Base):
    """
    Core identity table.
    Stores all platform users — clients, consultants, and admins.
    """
    __tablename__ = "users"

    id         = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name       = Column(String(120), nullable=False)
    email      = Column(String, unique=True, nullable=False)
    role       = Column(Enum(UserRole, name="user_role"), nullable=False)
    created_at = Column(TIMESTAMPTZ, nullable=False, server_default=func.now())

    consultations_as_client = relationship(
        "Consultation",
        foreign_keys="Consultation.client_id",
        back_populates="client",
    )
 
    consultations_as_consultant = relationship(
        "Consultation",
        foreign_keys="Consultation.consultant_id",
        back_populates="consultant",
    )
    chat_messages = relationship("ChatMessage", back_populates="user")

    def __repr__(self) -> str:
        return f"<User id={self.id} email={self.email!r} role={self.role}>"