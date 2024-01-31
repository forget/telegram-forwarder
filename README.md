# telegram-message-forwarder
A simple tool to forward a message (or multiple) from one channel to another.

To install, simply download python and the telethon module.
```
pip install telethon
```

Open up `main.py` and put your account's credentials in. After that is done, head to `assets/data.json`, this is where the data for your channels is stored. Currently, it has the following format:
```
{
    "channel_id": {
        "message_id": ["channel_id_to_forward_to", "channel_id_to_forward_to2"]
    }
}
```
Please keep in mind the following:
* channel_id: the channel of which you want to forward a message from.
* message_id: the message you want to forward from that channel to another.
* array: the elements are simply the channel ids where you want the message to be posted.

# NOTE: Telegram's API works like so:
* channel_id's have -100 in front of them, so if you copy the channel ID from the application, do not forget to add it at the front.
