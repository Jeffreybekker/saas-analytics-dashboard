# 0003: API architecture and endpoint structure


## Context  
I am building an API for a project that relies on its endpoints. So well structured documentation is essential.  


## Options considered  
There are three options to be considered:  
- Function Based Views  
- Class Based Views  
- ViewSets (+ Routers)  

They have their pros and cons.  
1. Function Based Views  
Pros:  
- Simple and straightforward to implement.  
- Easy to understand for small APIs or single endpoints.  

Cons:  
- Harder to maintain and extend for larger APIs.  
- Lots of repeating, because you often use similar logic.  
- Hard to integrate with automatic API documentation (like Swagger/OpenAPI).  

2. Class Based Views  
Pros:  
- Has more structure than Function Based Views.  
- Easier to extend when using mixins.  

Cons:  
- Overkill for simple endpoints.  
- Slightly harder to learn than Function Based Views.  
- Still requires defining URL patterns manually for each view.  

3. ViewSets and Routers  
Pros:  
- Automatically generates CRUD endpoints based on the ViewSets.  
- Routers can handle URL routing automatically too, so it is cleaner code and a more consistent API structure.  
- Works absolutely great with API documentation tools (like Swagger/OpenAPI).  
- Best practice for RESTful APIs and using versions.  

Cons:  
- It takes more time to fully understand how it works between routers and ViewSets.  
- Less flexible for customized or unusual endpoints.  


## Decision  
The best option is to use ViewSets with Routers, because this gives a clear structure and works well with API documentation tools. Since the project depends on APIs, good documentation with Swagger/OpenAPI is very important. ViewSets make this easier to set up and maintain.  


## Consequences  

Positive: API endpoints automatically and OpenAPI/Swagger works great together with ViewSets + Routers.  
Negative: Slightly harder to learn and understand if you're new to it.  


## References  
https://www.django-rest-framework.org/api-guide/views/  
https://www.django-rest-framework.org/tutorial/3-class-based-views/  
https://www.django-rest-framework.org/api-guide/viewsets/  
https://www.django-rest-framework.org/api-guide/routers/  
