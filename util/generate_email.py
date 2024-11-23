import random
import string
import uuid

def generate_email():
    name_length = 8
    name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=name_length))

    domains = ["example.com", "testmail.com", "mailservice.com"]
    domain = random.choice(domains)

    # Add a unique identifier
    unique_id = uuid.uuid4().hex[:6]  # Short unique identifier

    email = f"{name}_{unique_id}@{domain}"
    return email
