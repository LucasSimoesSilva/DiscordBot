from discord.ext import commands
from util.util import time_until
from collections import OrderedDict
from util.db_actions import *
from util.db_session import *
from util import env_exporter

admin_role = env_exporter.get_admin_role()
all_roles = env_exporter.get_all_roles()


class Birthday(commands.Cog):

    def __int__(self, bot):
        self.bot = bot

    @commands.command(aliases=['birth'], description='Description: Shows the name of all registered birthday people and'
                                                     ' how far until their birthday\n'
                                                     'Return: Lucas: 128 days until your birthday')
    async def birthday(self, ctx):
        all_birthdays = get_all_birthdays()
        for key_all, value_all in all_birthdays.items():

            current_date = datetime.date.today()

            value_date = value_all.replace(year=current_date.year)

            value_all = value_date

            if value_date < current_date:
                value_all = value_all.replace(year=current_date.year + 1)

            all_birthdays[key_all] = value_all

        birthdays = OrderedDict(sorted(all_birthdays.items(), key=lambda item: item[1]))
        result_message = ''
        for key, value in birthdays.items():
            result_message += f'`{key}`: {time_until(value)}\n'

        await ctx.send(result_message)

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
