from ast import For
import uuid
import enum
from datetime import datetime,timezone
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import UUID, VARCHAR,Enum, ForeignKey,Text, DateTime
from app.db.base import Base

class Role(str,enum.Enum):
    user = "user"
    assistant = "assistant"



class ChatMessage(Base):
    __tablename__ = "chat_message"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key= True,
        default=uuid.uuid4
    )

    user_id: Mapped[uuid.UUID] = mapped_column(
       ForeignKey("users.id")
    )

    role: Mapped[Role] = mapped_column(
        Enum(Role,name="chat_role"),
        nullable=False
    )

    content:Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    intent:Mapped[str] = mapped_column(
        VARCHAR(80),
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default =lambda: datetime.now(timezone.utc),
        nullable = False 
    )

