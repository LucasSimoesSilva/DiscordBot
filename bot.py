from typing import Mapping, Optional, List, Any
from util import env_exporter

import discord
import os
from discord.ext import commands
from discord.ext.commands import Cog, Command, Group

help_message = 'Use `.help [command]` for more information on a command.\n\n'

admin_role = int(env_exporter.get_admin_role())
bot_token = env_exporter.get_bot_token()

class CustomHelpCommand(commands.HelpCommand):

    def __init__(self):
        super().__init__()

    # .help
    async def send_bot_help(self, mapping: Mapping[Optional[Cog], List[Command[Any, ..., Any]]], /):
        await self.get_destination().send('----------------------------------------------------')
        await self.get_destination().send(f'{help_message}')
        for cog in mapping:
            await self.get_destination().send(
                f'**{cog.qualified_name}**\nCommands: {[command.name for command in mapping[cog]]}'
                .replace('[', '').replace('\'', '').replace(']', ''))

    # .help 'cog'
    async def send_cog_help(self, cog: Cog, /) -> None:
        return await super().send_cog_help(cog)

    # .help 'group'
    async def send_group_help(self, group: Group[Any, ..., Any], /) -> None:
        return await super().send_group_help(group)

    # .help 'command'
    async def send_command_help(self, command: Command[Any, ..., Any], /) -> None:
        await self.get_destination().send(f'----------------------------------------------------\nName: `{command.name}`')
        if command.aliases:
            for alias in command.aliases:
                await self.get_destination().send(f'`Alias: {alias}`')

        await self.get_destination().send(f'\n{command.description}')
        await self.get_destination().send('----------------------------------------------------')


async def run_discord_bot():
    TOKEN = bot_token
    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix=".", help_command=CustomHelpCommand(), intents=intents)

    @bot.event
    async def on_ready():
        print('Bot is online.')

    cogs_commands(bot)

    async with bot:
        await load_extensions(bot)
        await bot.start(TOKEN)


def cogs_commands(bot):
    @bot.command()
    @commands.has_role(admin_role)
    async def load(ctx, ex):
        await bot.load_extension(f'cogs.{ex}')

    @bot.command()
    @commands.has_role(admin_role)
    async def unload(ctx, ex):
        await bot.unload_extension(f'cogs.{ex}')


async def load_extensions(bot):
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")
