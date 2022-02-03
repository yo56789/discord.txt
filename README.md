# discord.txt
Make a discord bot using a .txt file. Based off [discordlib](https://github.com/CodeWithSwastik/discord-lib)

## Installing
```
pip install git+https://github.com/yo56789/discord.txt
```

## Using
```python
from discordtxt import Client

client = Client("filepath")
client.run()
```

## Limitations
- No cog support
- Can only send messages
- Cant use slash commands
- Cant add reactions
