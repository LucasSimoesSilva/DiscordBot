from discord.ext import commands
from util.util import time_until
import datetime as datetime
from collections import OrderedDict
from util.db_actions import *
from util.db_session import *

FILE_BIRTHDAYS = "./files/birthdays.txt"


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
                                  'Example:.add_date Lucas 21-12'
                                  'Return:Lucas birthday was added to the database')
    async def add_date(self, ctx, name, date):
        exists = add_birthday(name, date)
        if exists:
            await ctx.send(f'Name: {name} already exists in database')
        else:
            await ctx.send(f'{name} birthday was added to the database')

    @commands.command(description='Description: Remove the person from database\n'
                                  'Example:.remove_date Lucas'
                                  'Return:Lucas birthday was deleted from database')
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


def convert_date_to_sort(data):
    return datetime.datetime.strptime(data, '%d-%m-%Y')


def add_birthday(name, date):
    if check_name(name):
        file_birthdays = open(FILE_BIRTHDAYS, "a")
        file_birthdays.write(f'\n{name} = {date}')
        file_birthdays.close()
        print('Birthday registered')
        return False
    else:
        print('Name already exists in database')
        return True


def remove_birthday(name):
    with open(FILE_BIRTHDAYS, 'r') as file:
        lines = file.readlines()

    found = False
    for line in lines:
        if name in line[:line.find('=') - 1]:
            lines.remove(line)
            found = True

    if not found:
        print(f"Name: {name} don't exists in the database")
        file.close()
        return True
    else:
        with open(FILE_BIRTHDAYS, 'w') as file:
            lines[-1] = lines[-1].replace('\n', '')
            file.writelines(lines)
            file.close()
        print(f"Name: {name} removed from database")
        return False


def check_name(name):
    all_birthdays = get_all_birthdays()
    if name in all_birthdays:
        return False
    return True
