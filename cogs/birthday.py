from discord.ext import commands
from discord.ext.commands import Context

from util.util import time_until
from collections import OrderedDict
from util.db_actions import *
from util.db_session import *
from util import env_exporter
import logging

admin_role = int(env_exporter.get_admin_role())
all_roles = [int(role) for role in env_exporter.get_all_roles()]


class Birthday(commands.Cog):

    def __int__(self, bot):
        self.bot = bot

    @staticmethod
    def _has_dm_role(ctx: Context) -> bool:
        if not ctx.guild:
            return False
        role = ctx.guild.get_role(int(admin_role))
        return role is not None and role in ctx.author.roles

    @commands.command(aliases=['birth'], description='Description: Shows the name of all registered birthday people and'
                                                     ' how far until their birthday\n'
                                                     'Return: Lucas: 128 days until your birthday')
    async def birthday(self, ctx: Context, option: str | None = None):
        send_dm = (option or "").lower() == "dm"

        all_birthdays = get_all_birthdays()
        current_date = datetime.date.today()

        adjusted = {}
        for name, date_value in all_birthdays.items():
            next_birthday = date_value.replace(year=current_date.year)
            if next_birthday < current_date:
                next_birthday = next_birthday.replace(year=current_date.year + 1)
            adjusted[name] = next_birthday

        birthdays = OrderedDict(sorted(adjusted.items(), key=lambda item: item[1]))

        db = None
        try:
            db = SessionLocal()
            user_list = list_users(db)
        finally:
            db.close()

        users_by_name = {u.name: u for u in user_list}

        result_lines = []
        birthday_today = []

        for name, date_value in birthdays.items():
            user = users_by_name.get(name)
            user_disc_id = user.user_disc_id if user else None

            result_lines.append(f'`{name}`: {time_until(date_value, user_disc_id)}')

            if (
                    send_dm
                    and user_disc_id
                    and date_value == current_date
            ):
                birthday_today.append(user_disc_id)

        await ctx.send("\n".join(result_lines))

        if not send_dm:
            return

        if not self._has_dm_role(ctx):
            await ctx.send("You don't have permission to send birthday DMs.")
            return

        for disc_id in birthday_today:
            try:
                user = await ctx.bot.fetch_user(int(disc_id))
                await user.send("Lucas te deseja um felizissimo demais e incrível aniversário :birthday: :tada::tada::tada::tada::tada:")
            except Exception as e:
                logging.exception(e)
                pass

    @commands.command(description='Description: Add the person and his birthday in the database\n'
                                  'Example:.add_date Lucas 21-12\n'
                                  'Return:Lucas birthday was added to the database')
    @commands.has_any_role(*all_roles)
    async def add_date(self, ctx, name, date):
        exists = add_birthday(name, date)
        if exists:
            await ctx.send(f'Name: {name} already exists in database')
        else:
            await ctx.send(f'{name} birthday was added to the database')

    @commands.command(description='Description: Remove the person from database\n'
                                  'Example:.remove_date Lucas\n'
                                  'Return:Lucas birthday was deleted from database')
    @commands.has_role(admin_role)
    async def remove_date(self, ctx, name):
        exists = remove_birthday(name)
        if exists:
            await ctx.send(f"Name: {name} don't exists in the database")
        else:
            await ctx.send(f"Name: {name} removed from database")


async def setup(bot):
    await bot.add_cog(Birthday(bot))


def get_all_birthdays():
    db = None
    birthdays = {}
    try:
        db = SessionLocal()
        user_list = list_users(db)
    finally:
        db.close()

    for user in user_list:
        birthdays[str(user.name)] = user.date

    return birthdays


def convert_date_to_sort(date: str):
    d = datetime.datetime.strptime(date, "%d-%m")
    return datetime.date(2000, d.month, d.day)


def add_birthday(name, date):
    date = convert_date_to_sort(date)

    db = None
    try:
        db = SessionLocal()
    finally:
        db.close()

    if not user_exists(db, name):
        create_user(db, name, date)
        print(f'Birthday registered: {name} {date}')
        return False
    else:
        print(f'Name ({name}) already exists in database')
        return True


def remove_birthday(name):
    db = None
    try:
        db = SessionLocal()
    finally:
        db.close()

    if delete_user_by_name(db, name):
        print(f"Name: {name} removed from database")
        return False
    else:
        print(f"Name: {name} don't exists in the database")
        return True
