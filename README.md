A simple tool to forward a message (or multiple) from one channel to another. 

First install python with pip, then install the needed dependencies:
```
pip install telethon
```

Open `bot.py` and put your account's credentials in. After that is done, head to `assets/data.json` (this is where the data for your channels is stored). The format is the following:
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

For topics, use `<channel_id>/<topic_id>`, an example is included inside `data.json`. Feel free to play with the delays, currently it forwards all messages with a `300 seconds` (5 minutes) interval and it restarts the process every `12 000 seconds` (3.33 hours). Some channels have slow-mode enabled at 5 minutes, others at 1 hour so make sure you check before you run the script so it does not break.

You must be member of the channels you are forwarding from/to.

## It's very likely that you'll get suspended, so use it at your own risk.
