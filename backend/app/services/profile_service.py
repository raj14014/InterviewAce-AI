from app.database import db


async def create_profile(profile_data: dict):
    """
    Create a new user profile
    """

    existing_profile = await db.profiles.find_one(
        {"email": profile_data["email"]}
    )

    if existing_profile:
        return {
            "success": False,
            "message": "Profile already exists"
        }

    result = await db.profiles.insert_one(profile_data)

    return {
        "success": True,
        "message": "Profile created successfully",
        "id": str(result.inserted_id)
    }