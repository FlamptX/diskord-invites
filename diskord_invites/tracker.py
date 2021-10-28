from diskord import Client, Member, TextChannel, VoiceChannel
from diskord.ext.commands import Bot, Cog
from typing import Union, Callable, Awaitable
from asyncio import sleep, get_event_loop, iscoroutinefunction

class Tracker(Cog):
    def __init__(self, bot: Union[Bot, Client]):
        self.bot = bot
        self.funcs = []
        self.invites = []

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
        if not iscoroutinefunction(coro):
            raise TypeError(f"{coro} is not a coroutine")
        self.funcs.append(coro)
        return coro
