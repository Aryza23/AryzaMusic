from pyrogram.types import InlineKeyboardButton


def choose_markup(videoid, duration, user_id):
    return [
        [
            InlineKeyboardButton(
                text="🎵 Play Music",
                callback_data=f"MusicStream {videoid}|{duration}|{user_id}",
            ),
            InlineKeyboardButton(
                text="🎥 Play Video",
                callback_data=f"Choose {videoid}|{duration}|{user_id}",
            ),
        ],
    ]


def livestream_markup(quality, videoid, duration, user_id):
    return [
        [
            InlineKeyboardButton(
                text="🎥  Start Live",
                callback_data=f"LiveStream {quality}|{videoid}|{duration}|{user_id}",
            ),
            InlineKeyboardButton(
                text="🗑 Close",
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]


def stream_quality_markup(videoid, duration, user_id):
    return [
        [
            InlineKeyboardButton(
                text="📽 360P",
                callback_data=f"VideoStream 360|{videoid}|{duration}|{user_id}",
            ),
            InlineKeyboardButton(
                text="📽 720P",
                callback_data=f"VideoStream 720|{videoid}|{duration}|{user_id}",
            ),
            InlineKeyboardButton(
                text="📽 480P",
                callback_data=f"VideoStream 480|{videoid}|{duration}|{user_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="⬅️ Back",
                callback_data=f"gback_list_chose_stream {videoid}|{duration}|{user_id}",
            )
        ],
    ]
