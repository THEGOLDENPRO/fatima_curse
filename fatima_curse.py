import GoldyBot
from GoldyBot.utility.commands import send, mention
import nextcord
from nextcord.ext.commands import Context

database:GoldyBot.Database = GoldyBot.cache.main_cache_dict["database"]
mcf_database = database.new_instance("mcf_data")

client:nextcord.Client = GoldyBot.cache.main_cache_dict["client"]

class FatimaCurse(GoldyBot.Extension):
    def __init__(self):
        self.curse_enabled = False
        super().__init__(self)
    
    def loader(self):

        @client.event
        async def on_message(message:GoldyBot.nextcord.Message):
            if self.curse_enabled:
                member = GoldyBot.Member(ctx=None, member_object=message.author)

                if member.member_id == "303480386271313921": # Fatima's Discord ID 🤓
                    await message.add_reaction("🤓")
        
        @GoldyBot.command(help_des="A command that curses fatima whenever she talks.", required_roles=["bot_dev"], slash_cmd_only=True)
        async def fatima_curse(self:FatimaCurse, ctx):
            return True

        @fatima_curse.sub_command()
        async def enable(self:FatimaCurse, ctx:Context):
            self.curse_enabled = True
            await send(ctx, f"💚 {mention(GoldyBot.Member(ctx))} Curse Enabled. 💀 *Have fun!*")

        @fatima_curse.sub_command()
        async def disable(self:FatimaCurse, ctx:Context):
            self.curse_enabled = False
            await send(ctx, f"🤎 {mention(GoldyBot.Member(ctx))} Curse disabled.")

            
def load():
    FatimaCurse()