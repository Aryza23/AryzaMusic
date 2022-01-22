from pyrogram.types import InlineKeyboardButton


def check_markup(user_name, user_id, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"Group's Playlist",
                callback_data=f"playlist_check {user_id}|Group|{videoid}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"{user_name[:8]}'s Playlist",
                callback_data=f"playlist_check {user_id}|Personal|{videoid}",
            ),
        ],
        [InlineKeyboardButton(text="🗑 Close Menu", callback_data="close")],
    ]
    return buttons


def playlist_markup(user_name, user_id, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"Group's Playlist",
                callback_data=f"show_genre {user_id}|Group|{videoid}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"{user_name[:8]}'s Playlist",
                callback_data=f"show_genre {user_id}|Personal|{videoid}",
            ),
        ],
        [InlineKeyboardButton(text="🗑 Close Menu", callback_data="close")],
    ]
    return buttons


def play_genre_playlist(user_id, type, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"Indonesia",
                callback_data=f"play_playlist {user_id}|{type}|indonesia",
            ),
            InlineKeyboardButton(
                text=f"Hollywood",
                callback_data=f"play_playlist {user_id}|{type}|hollywood",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"Party",
                callback_data=f"play_playlist {user_id}|{type}|party",
            ),
            InlineKeyboardButton(
                text=f"Lofi",
                callback_data=f"play_playlist {user_id}|{type}|lofi",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"Sad",
                callback_data=f"play_playlist {user_id}|{type}|sad",
            ),
            InlineKeyboardButton(
                text=f"Rock",
                callback_data=f"play_playlist {user_id}|{type}|rock",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"Pop",
                callback_data=f"play_playlist {user_id}|{type}|pop",
            ),
            InlineKeyboardButton(
                text=f"Others",
                callback_data=f"play_playlist {user_id}|{type}|others",
            ),
        ],
        [
            InlineKeyboardButton(
                text="⬅️ Back",
                callback_data=f"main_playlist {videoid}|{type}|{user_id}",
            ),
        ],
    ]
    return buttons


def add_genre_markup(user_id, type, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"✚ Rock",
                callback_data=f"add_playlist {videoid}|{type}|rock",
            ),
            InlineKeyboardButton(
                text=f"✚ Sad",
                callback_data=f"add_playlist {videoid}|{type}|sad",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"✚ Party",
                callback_data=f"add_playlist {videoid}|{type}|party",
            ),
            InlineKeyboardButton(
                text=f"✚ Lofi",
                callback_data=f"add_playlist {videoid}|{type}|lofi",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"✚ Indonesia",
                callback_data=f"add_playlist {videoid}|{type}|indonesia",
            ),
            InlineKeyboardButton(
                text=f"✚ Hollywood",
                callback_data=f"add_playlist {videoid}|{type}|hollywood",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"✚ Pop",
                callback_data=f"add_playlist {videoid}|{type}|pop",
            ),
            InlineKeyboardButton(
                text=f"✚ Others",
                callback_data=f"add_playlist {videoid}|{type}|Others",
            ),
        ],
        [
            InlineKeyboardButton(
                text="⬅️ Back", callback_data=f"goback {videoid}|{user_id}"
            ),
        ],
    ]
    return buttons


def check_genre_markup(type, videoid, user_id):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"Rock", callback_data=f"check_playlist {type}|rock"
            ),
            InlineKeyboardButton(
                text=f"Sad", callback_data=f"check_playlist {type}|sad"
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"Party", callback_data=f"check_playlist {type}|party"
            ),
            InlineKeyboardButton(
                text=f"Lofi", callback_data=f"check_playlist {type}|lofi"
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"Indonesia",
                callback_data=f"check_playlist {type}|indonesia",
            ),
            InlineKeyboardButton(
                text=f"Hollywood",
                callback_data=f"check_playlist {type}|hollywood",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"Pop",
                callback_data=f"check_playlist {type}|pop",
            ),
            InlineKeyboardButton(
                text=f"Others", callback_data=f"check_playlist {type}|others"
            ),
        ],
        [InlineKeyboardButton(text="🗑 Close Menu", callback_data="close")],
    ]
    return buttons


def third_playlist_markup(user_name, user_id, third_name, userid, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"Group's Playlist",
                callback_data=f"show_genre {user_id}|Group|{videoid}",
            ),
            InlineKeyboardButton(
                text=f"{user_name[:8]}'s Playlist",
                callback_data=f"show_genre {user_id}|Personal|{videoid}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"{third_name[:16]}'s Playlist",
                callback_data=f"show_genre {userid}|third|{videoid}",
            ),
        ],
        [InlineKeyboardButton(text="🗑 Close", callback_data="close")],
    ]
    return buttons


def paste_queue_markup(url):
    buttons = [
        [
            InlineKeyboardButton(text="▶️", callback_data=f"resumecb"),
            InlineKeyboardButton(text="⏸️", callback_data=f"pausecb"),
            InlineKeyboardButton(text="⏭️", callback_data=f"skipcb"),
            InlineKeyboardButton(text="⏹️", callback_data=f"stopcb"),
        ],
        [InlineKeyboardButton(text="Checkout Queued Playlist", url=f"{url}")],
        [InlineKeyboardButton(text="🗑 Close Menu", callback_data=f"close")],
    ]
    return buttons


def fetch_playlist(user_name, type, genre, user_id, url):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"Play {user_name[:10]}'s {genre} Playlist",
                callback_data=f"play_playlist {user_id}|{type}|{genre}",
            ),
        ],
        [InlineKeyboardButton(text="Checkout Playlist", url=f"{url}")],
        [InlineKeyboardButton(text="🗑 Close Menu", callback_data=f"close")],
    ]
    return buttons


def delete_playlist_markuup(type, genre):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"Yes! Delete",
                callback_data=f"delete_playlist {type}|{genre}",
            ),
            InlineKeyboardButton(text="No!", callback_data=f"close"),
        ],
    ]
    return buttons
