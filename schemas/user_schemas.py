from pydantic import BaseModel

class CreatedUserResponse(BaseModel):
    """
🧩 Pydantic models for response validation (User Schemas)

This module defines data schemas used to validate the structure of API responses.

Purpose:
- Ensure that the actual API response matches expected fields and types
- Add robustness to the tests by catching unexpected changes in API contracts

Current Schemas:
- CreatedUserResponse: schema for POST /users
- UpdatedUserResponse: schema for PUT /users

📌 Notes for contributors:
- Feel free to extend these models or create new ones for additional endpoints
- Fields are based on reqres.in API and may require adjustment if the API changes
- All schemas inherit from pydantic.BaseModel for auto-validation and type hints
"""

    id: str
    createdAt: str

class UpdatedUserResponse(BaseModel):
    """
🧩 Pydantic models for response validation (User Schemas)

This module defines data schemas used to validate the structure of API responses.

Purpose:
- Ensure that the actual API response matches expected fields and types
- Add robustness to the tests by catching unexpected changes in API contracts

Current Schemas:
- CreatedUserResponse: schema for POST /users
- UpdatedUserResponse: schema for PUT /users

📌 Notes for contributors:
- Feel free to extend these models or create new ones for additional endpoints
- Fields are based on reqres.in API and may require adjustment if the API changes
- All schemas inherit from pydantic.BaseModel for auto-validation and type hints
"""

    updatedAt: str

