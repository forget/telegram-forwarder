A simple tool to forward a message (or multiple) from one channel to another. To install, simply download python and the telethon module:
```
pip install telethon
```

Open `main.py` and put your account's credentials in. After that is done, head to `assets/data.json` (this is where the data for your channels is stored). The format is the following:
```
{
    "channel_link": {
        "message_id": ["forward_channel", "forward_channel"]
    }
}
```
If you do not understand it, here is a little more detail:
* channel_link: the channel of which you want to forward a message from.
* message_id: the message you want to forward from that channel to another.
* forward_channel: channel id (supports topics too) you want to forward your message to.

For topics, use `<channel_id>/<topic_id>`, an example is included inside `data.json`.

## It's very likely that you'll get suspended, so use at your own risk.
