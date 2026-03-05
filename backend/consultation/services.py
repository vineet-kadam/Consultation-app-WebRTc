from .models import User


def create_doctor(doctor_data):
    first_name = doctor_data.get("first_name", "")
    last_name  = doctor_data.get("last_name", "")

    # Safely construct username, defaulting to empty string if names are missing
    username = f"{first_name.lower().strip()}_{last_name.lower().strip()}".strip("_")

    if not username:
        # Fallback if username somehow is empty
        username = doctor_data.get("username", "default_doctor")

    doctor_available = User.objects.filter(username=username).first()
    if doctor_available:
        return doctor_available

    doctor_user = create_user({
        "username"  : username,
        "password"  : username,
        "first_name": first_name,
        "last_name" : last_name,
        "role"      : "doctor",
    })
    return doctor_user


def create_patient(patient_data):
    username = patient_data.get("username", "")

    if not username:
        raise ValueError("Username is required to create a patient")

    patient_available = User.objects.filter(username=username).first()
    if patient_available:
        return patient_available

    patient_user = create_user({
        "username"  : username,
        "password"  : patient_data.get("password", username),  # Default password to username if missing
        "first_name": patient_data.get("first_name", ""),
        "last_name" : patient_data.get("last_name", ""),
        "role"      : "patient",
    })
    return patient_user


def create_user(user_data):
    role = user_data.get("role", "patient").lower()
    user = User.objects.create_user(
        username=user_data.get("username"),
        password=user_data.get("password"),
        first_name=user_data.get("first_name", ""),
        last_name=user_data.get("last_name", ""),
        role=role
    )
    return user