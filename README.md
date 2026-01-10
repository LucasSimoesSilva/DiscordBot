
# Discord Bot
- A Discord bot with various functionalities, with its main purpose being to record birthdays.
- Bot commands are executed by typing . followed by the command.
    - Commands:
        - `.help` -> Displays available commands.
        - `.help` 'command name' -> Shows what a specific command does.

## Technologies Used
- Language: Python 3.10
- Library: discord.py
- Database: PostgreSQL 16
- Containerization: Docker & Docker Compose

---

# How to Run the Program

There are two supported ways to run the bot:

1. Docker Compose (recommended)
2. Local Python + Postgres via Docker (for development/debug)

## Option 1 — Run with Docker Compose (Recommended)

### Requirements
- Docker
- Docker Compose
- Discord account

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/LucasSimoesSilva/Discord-bot
   cd Discord-bot
   ```

2. Create your `.env` file based on the example:
   ```bash
   cp .env.example .env
   ```

3. Edit `.env` and fill **at least** the following values:
   - `DISCORD_TOKEN`
   - `ADMIN_ROLE`
   - `POSTGRES_PASSWORD`

4. Build and start the application:
   ```bash
   docker compose up -d --build
   ```

### Stop containers
```bash
docker compose down
```

### Remove database data (⚠ irreversible)
```bash
docker compose down -v
```

### Accessing the Database (optional)
If the Postgres service exposes the port:

```yaml
ports:
  - "5432:5432"
```

You can connect using tools like **DBeaver** or **psql**:
- Host: `localhost`
- Port: `5432`
- Database: `appdb`
- User: `appuser`
- Password: value from `.env`

## Option 2 — Run Locally (Python) + Postgres via Docker

Useful for debugging and development.

### Steps

1. Start only the database:
   ```bash
   docker compose up -d db
   ```

2. Configure your `.env` for local access:
   ```env
   DATABASE_URL=postgresql+psycopg2://appuser:POSTGRES_PASSWORD@localhost:5432/appdb
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python main.py
   ```

---

## Mandatory requirements to run the application
- Python 3.10. Official website [python](https://www.python.org/downloads/)
- Discord account. Official website [Discord](https://discord.com/)

---

## Steps to run the code:

1. Clone the repository https://github.com/LucasSimoesSilva/Discord-bot;

2. Go to the Discord development website: https://discord.com/developers/applications;
    - Note: You need a Discord account for this step.

3. Create a new application by clicking the `New Application button`.
    <img src="/assets/ApplicationButton.png">

4. Fill in the initial information as desired.

5. Click on the `Bot` tab on the left menu.
    1. Click the `Reset Token` button and save the given token somewhere.
    2. In the `Privileged Gateway Intents` area, enable all permissions.
        <img src="/assets/ResetToken.png">
        <img src="/assets/PrivilegedIntents.png">

6. Click on the left menu on `OAuth2` and then on `URL Generator`.

7. In the scope options, check the `bot` and `applications.commands` options.
    <img src="/assets/Scopes.png">

8. In the permission options, check the following:
    - **GENERAL PERMISSIONS** column: `Read Messages/View Channels`
    - **TEXT PERMISSIONS** column: `Send Messages`, `Manage Messages`, `Manage Threads`, `Embed Links`, `Attach Files`, `Read Message History`, `Mention Everyone`, `Use External Emojis`, `Use External Stickers`, `Add Reactions`, `Use Slash Commands`, `Use Embedded Activities`
    - **VOICE PERMISSIONS** column: `Use Embedded Activities`
    <img src="/assets/BotPermissions.png">

9. Copy the URL created at the end of the page and paste it into your preferred browser.
    - Log in with your Discord account and choose the server you want to add the bot to.

10. Set up the Environment Variables

11. Start your bot

---

## Environment Variables

The application is configured via environment variables.

### Required
```env
DISCORD_TOKEN=CHANGE_ME
ADMIN_ROLE=CHANGE_ME

POSTGRES_DB=appdb
POSTGRES_USER=appuser
POSTGRES_PASSWORD=CHANGE_ME
DATABASE_URL=postgresql+psycopg2://appuser:CHANGE_ME@db:5432/appdb

# Optional (custom messages)
BIRTHDAY_MESSAGE=Happy birthday to you
NO_DM_PERMISSION_MESSAGE=You don't have permission to send birthday DMs.
```

- **EXTRA**: Remember that the bot must have access to the text channel where you will execute the commands.
