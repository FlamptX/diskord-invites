from diskord import Member, TextChannel, VoiceChannel
from diskord.ext.commands import Bot, Cog
from typing import Union, Callable, Awaitable
from asyncio import sleep, get_event_loop, iscoroutinefunction
import time

class Tracker(Cog):
    def __init__(self, bot: Bot, fetch_invites: bool = False, suppress_logs: bool = False):
        bot.add_cog(self)

        self.bot = bot
        self.funcs = []
        self.invites = []
        self.suppress_logs = suppress_logs

        if fetch_invites:
            self.bot.add_listener(self.on_ready)

    async def _fetch_invites(self):
        t = time.time()
        for g in self.bot.guilds:
            invites = await g.invites()
            for i in invites:
                self.invites.append(i)
            await sleep(0.5)
        if not self.suppress_logs:
            print(f"All invites were fetched ({round(time.time() - t)}s).")

    async def on_ready(self):
        await self._fetch_invites()

    @Cog.listener()
    async def on_invite_create(self, invite):
        self.invites.append(invite)

    @Cog.listener()
    async def on_invite_delete(self, invite):
        await sleep(0.5)
        for i, x in enumerate(self.invites):
            if x.code == invite.code:
                del self.invites[i]

    @Cog.listener()
    async def on_member_join(self, member):
        invites = await member.guild.invites()
        for x in invites:
            for y in self.invites:
                if x.code == y.code and y.uses < x.uses:
                    loop = get_event_loop()
                    for z in self.funcs:
                        loop.create_task(z(member, x.inviter, x.channel))

    def member_join(self, coro: Callable[[Member, Member, Union[TextChannel, VoiceChannel]], Awaitable[None]]):
        """
        A decorator that listens for a member_join event

        :param coro: The coroutine passed for the decorator
        :raises TypeError: When the passed function is not a coroutine
        """
        if not iscoroutinefunction(coro):
            raise TypeError(f"{coro} is not a coroutine")
        self.funcs.append(coro)
        return coro
