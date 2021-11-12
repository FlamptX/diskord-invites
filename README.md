<div>
  <h1 align='center'>
    diskord-invites
  </h1>
</div>
<div>
  <p align='center'>
    <img src=https://img.shields.io/pypi/dm/diskord-invites?color=success&label=PyPi%20Downloads&style=flat-square>
    <img src=https://shields.io/github/issues-raw/FlamptX/diskord-invites?color=success&label=Active%20Issues&style=flat-square>
    <img src=https://img.shields.io/pypi/v/diskord-invites>
  </p>
  <p align='center'>
    Python library for simple invites tracking.
  </p>
</div>
<br>

## Features
- Very easy to use
- Uses [diskord](https://github.com/diskord-dev/diskord)
- Actively maintained
## Links
- **[PyPi](https://pypi.org/project/diskord-invites)**
## Installation
You can easily install it using the python package manager `pip`

```
pip install diskord-invites
```
## Quickstart
Example usage (bot is diskord.ext.commands.Bot)
```python
from diskord_invites import Tracker

tracker = Tracker(bot)

@tracker.member_join
async def member_join(member, inviter, channel):
    await channel.send(f"{member.name} was invited by {inviter.name}")
```

## Contributions
Feel free to open pull requests and improve the library. If you find any issues, please report it.
