from discord import (
    Intents, 
    Game, 
    Activity, 
    Streaming,
    ActivityType,
)
from discord.ext.commands import (
    Bot,
    Command,
    Context,
)
from typing import Dict, List
from .utils import (
    parseConfig,
    parseCommands,
    parseRunLine,
    )

def build_bot_from_txt(config: Dict) -> Bot:
    """
    Only supports presence, intents, command_prefix
    """
    bot_config = {}
    bot_config["intents"] = Intents.all() if config.get("intents") == "all" else Intents.default()
    bot_config["command_prefix"] = config.get("prefix")

    presence = config.get("presence")
    if presence:
        presencetext = (config.get("presencetext")).replace("-", " ")
        if presence == "watching":
            activity = Activity(type=ActivityType.watching, name=presencetext)
        elif presence == "listening":
            activity = Activity(type=ActivityType.listening, name=presencetext)
        elif presence == "streaming":
            activity = Streaming(name=presencetext, url=config.get("presenceurl"))
        else:
            activity = Game(name=presencetext)

        bot_config["activity"] = activity
    bot = Bot(**bot_config)
    return bot

def create_command(config: Dict) -> Command:
    args = config.get("args", [])
    async def command(ctx: Context, *args):
        # for i, arg in enumerate(args):
        #     if arg.startswith("*"):
        #         setattr(ctx, arg[1:], " ".join(args[i:]))
        
        await ctx.send(config.get("message"))

    aliases = config.get("aliases", [])
    if isinstance(aliases, str):
        aliases = [aliases]
    return Command(
        command,
        name = config["name"],
        aliases = aliases,
        description = config.get("description", "")
    )

def add_all_commands(bot: Bot, config_list: List[Dict]):
    for config in config_list:
        bot.add_command(create_command(config))


class Client:
    def __init__(self, data):
        self.data = self.load(data)
        self.config = parseConfig(self.data)
        self.bot = build_bot_from_txt(self.config)

        add_all_commands(self.bot, parseCommands(self.data))

        
    def load(self, filepath) -> Dict:
        with open(filepath, "r") as f:
            filedata = f.read()
            return filedata

    def run(self):
        """Runs the bot"""
        print("bot is online")
        self.bot.run(parseRunLine(self.data))