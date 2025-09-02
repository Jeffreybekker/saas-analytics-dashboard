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
- **SQLite:** Easy to set up and fine for prototypes. Not good for production, because it has problems with many users at once and lacks advanced features.  
- **MySQL:** Stable and popular, but JSON support is weaker than PostgreSQL. It also has fewer advanced analytics features and indexing options.  
- **Other databases:** Good for flexible data, but weaker for relational queries. PostgreSQL combines both: strong relational features and JSON support in one system.  
 
## Outcome
- Data isolation per client will be handled in Django queries  
- JSON fields allow flexible storage of event metadata  
- PostgreSQL gives better scalability for analytics queries  

## Notes
- In production, database-level security and audit logging may be added
