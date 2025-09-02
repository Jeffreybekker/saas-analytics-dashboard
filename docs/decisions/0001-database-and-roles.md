# Proposal 001: Database Choice and User Roles

### Summary
I choose PostgreSQL as the database and define three roles: Admin, Client and End User.

### Context
I am building a SaaS Analytics Dashboard to collect, store, and analyze event data from users of different client organizations. Each client should only see their own data, while admins can see everything. The system needs to keep data separated and secure, and be able to handle a growing number of events without slowing down.

**The system should be:**
**Private:** Clients never see each other's data
**Scalable:** Queries should be fast, also with lots of events.
**Flexible:** Events can store different data/info using JSON.
**Analytical:** Clients must view trends and summaries.

Users and rights:
**Admins:** Full access and manage the system.
**Clients:** Can only access their data and staff can have extra permissions.
**End users:** Generate the events which is linked to their client.
