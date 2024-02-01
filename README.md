# telegram-message-forwarder
A simple tool to forward a message (or multiple) from one channel to another.

To install, simply download python and the telethon module.
```
pip install telethon
```

Open up `main.py` and put your account's credentials in. After that is done, head to `assets/data.json`, this is where the data for your channels is stored. Currently, it has the following format:
```
{
    "channel_link": {
        "message_id": ["forward_channel", "forward_channel"]
    }
}
```
Please keep in mind the following:
* channel_link: the channel of which you want to forward a message from.
* message_id: the message you want to forward from that channel to another.
* forward_channel: channel id (supports topics too) you want to forward your message to.

For topics, use `<channel_id>/<topic_id>`, an example is included inside `data.json`.

## USE THE TOOL AT YOUR OWN RISK, NEVER SHARE YOUR CREDENTIALS WITH ANYONE!
### THERE'S A HIGH CHANCE THIS CAN BAN YOUR ACCOUNT (/SUSPEND FROM SENDING MESSAGES TO GROUPS).
