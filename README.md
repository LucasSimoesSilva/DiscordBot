
# Discord Bot
- A Discord bot with various functionalities, with its main purpose being to record birthdays.
- Bot commands are executed by typing . followed by the command.
    - Commands:
        - `.help` -> Displays available commands.
        - `.help` 'command name' -> Shows what a specific command does.

## Technologies Used
- Language: Python 3.10.13
- IDE: PyCharm 2023.2.3 (Professional Edition)
- Used API: discord.py

<hr>

# How to Run the Program

<br>

## Mandatory requirements to run the application
- Python 3.10. Official website [python](https://www.python.org/downloads/)
- Discord account. Official website [Discord](https://discord.com/)

<hr>

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

10. Open the `DiscordBot` folder with your favorite Python editor.

11. Inside the folder, create a file named `.env`.
    - In the file, you will add two variables, the Token that you obtained in the step 5 and the role admin, that is the name of the role in your serve that you want to have access to the 'clear command'
      - At the moment, you can have only one role admin

Example:
```text
ADMIN_ROLE=The dragons
BOT_TOKEN=AAAAAAAAAAAAABBBBBBBBBBBBBBBBCCCCCCCCCCCDDDDDDDDDDD
```

12. In a terminal of your choice inside the `DiscordBot` folder, use the command `pip install -r requirements.txt`.

13. Now you can run the `main.py` file using an IDE or in the terminal with the command `python main.py`, and your bot will be operational to perform its functions within the server.

- **EXTRA**: Remember that the bot must have access to the text channel where you will execute the commands.
