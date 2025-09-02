# 0001: Database Choice and User Roles

## Context
I am building a SaaS Analytics Dashboard to collect, store, and analyze event data for different clients.  
Each client should only see their own data, while admins can see everything.  
The system must be secure, scalable, and flexible enough to handle many events over time.

## Decision
- **Database:** PostgreSQL  
- **Roles:**  
  - **Admin:** Full access to all data and system management  
  - **Client:** Can only see their own organization’s data  
  - **End user:** Generates events, linked to their client  

## Alternatives
- **SQLite:** Too simple, not production-ready  
- **MySQL:** Weaker JSON support and fewer advanced features  

## Outcome
- Data isolation per client will be handled in Django queries  
- JSON fields allow flexible storage of event metadata  
- PostgreSQL gives better scalability for analytics queries  

## Notes
- In production, database-level security and audit logging may be added
