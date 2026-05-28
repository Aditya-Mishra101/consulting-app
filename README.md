# Consulting Platform Backend

Production-style monolithic backend service for a consulting marketplace platform.

This system connects:
- Clients
- Consultants
- Admin

and supports:
- Paid 1:1 consultation sessions
- Payment tracking
- Post-session reviews
- Natural-language chatbot querying platform data

---

# Current Project Status

## Overall Status
Project initialization phase.

## Current Progress
No implementation has been completed yet.

The repository currently contains:
- planning documents
- Cursor AI configuration

No application code exists yet.

---

# Core Requirements

The backend must provide:

## Functional Features

### Authentication
- User registration
- User login
- JWT authentication
- Role-based access control

### Consultation System
- Consultant profile management
- Consultant availability
- Booking consultations
- Consultation status tracking

### Payments
- Track transactions/payments
- Associate payments with consultations
- Payment status handling

### Reviews
- Clients can review completed consultations
- Ratings + feedback storage

### Chatbot
Natural-language chatbot endpoint capable of:
- answering booking questions
- answering payment questions
- answering consultant availability questions
- querying PostgreSQL-backed data
- storing conversation history

---

# Database Tables

The project contain these primary tables:

1. `users`
2. `consultations`
3. `transactions`
4. `reviews`
5. `chat_messages`

---

# Tech Stack

## Backend
- FastAPI
- Python 3.14.5

## Database
- PostgreSQL

## ORM
- SQLAlchemy 2.0

## Migration Tool
- Alembic

## Validation
- Pydantic v2

## Authentication
- JWT
- bcrypt/passlib

## Containerization
- Docker
- Docker Compose

---

# Architecture Requirements

The application must follow production-style backend architecture.

## Architecture Style
Monolithic modular backend.

## Pattern Requirements
- Repository pattern
- Service layer
- Dependency injection
- Separation of concerns


# Database Design Plan

## users
Stores:
- clients
- consultants
- admins

Possible fields:
- id
- name
- email
- role
- created_at

---

## consultations
Stores booked sessions.

Possible fields:
- id
- client_id
- consultant_id
- scheduled_at
- status
- notes

---

## transactions
Stores payment records.

Possible fields:
- id
- consultation_id
- amount
- currency
- status
- paid_at

---

## reviews
Stores post-session feedback.

Possible fields:
- id
- consultation_id
- rating
- comment
- created_at

---

## chat_messages
Stores chatbot conversations.

Possible fields:
- id
- user_id
- role
- content
- created_at
=======
