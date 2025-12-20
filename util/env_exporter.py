from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

admin_role = os.getenv('ADMIN_ROLE')
bot_token = os.getenv('BOT_TOKEN')

if not admin_role or not bot_token:
    raise EnvironmentError("The ADMIN_ROLE and BOT_TOKEN environment variables must be defined.")

def get_admin_role():
    return admin_role

def get_bot_token():
    return bot_token

def get_all_roles():
    return [
        value
        for key, value in os.environ.items()
        if key.endswith("_ROLE")
    ]