import asyncio
import importlib

from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pytgcalls import idle
from rich.console import Console
from youtubesearchpython import VideosSearch

from config import (
    LOG_GROUP_ID,
    LOG_SESSION,
    STRING1,
    STRING2,
    STRING3,
    STRING4,
    STRING5,
)
from Yukki import (
    ASS_CLI_1,
    ASS_CLI_2,
    ASS_CLI_3,
    ASS_CLI_4,
    ASS_CLI_5,
    ASSID1,
    ASSID2,
    ASSID3,
    ASSID4,
    ASSID5,
    ASSNAME1,
    ASSNAME2,
    ASSNAME3,
    ASSNAME4,
    ASSNAME5,
    BOT_ID,
    BOT_NAME,
    LOG_CLIENT,
    OWNER_ID,
    app,
)
from Yukki.Core.Clients.cli import LOG_CLIENT
from Yukki.Core.PyTgCalls.Yukki import (
    pytgcalls1,
    pytgcalls2,
    pytgcalls3,
    pytgcalls4,
    pytgcalls5,
)
from Yukki.Database import (
    get_active_chats,
    get_active_video_chats,
    get_sudoers,
    is_on_off,
    remove_active_chat,
    remove_active_video_chat,
)
from Yukki.Plugins import ALL_MODULES

loop = asyncio.get_event_loop()
console = Console()


async def initiate_bot():
    with console.status(
        "[magenta] Finalizing Booting...",
    ) as status:
        try:
            chats = await get_active_video_chats()
            for chat in chats:
                chat_id = int(chat["chat_id"])
                await remove_active_video_chat(chat_id)
        except Exception:
            pass
        try:
            chats = await get_active_chats()
            for chat in chats:
                chat_id = int(chat["chat_id"])
                await remove_active_chat(chat_id)
        except Exception:
            pass
        status.update(status="[bold blue]Scanning for Plugins", spinner="earth")
        console.print("Found {} Plugins".format(len(ALL_MODULES)) + "\n")
        status.update(
            status="[bold red]Importing Plugins...",
            spinner="bouncingBall",
            spinner_style="yellow",
        )
        for all_module in ALL_MODULES:
            imported_module = importlib.import_module("Yukki.Plugins." + all_module)
            if hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__:
                imported_module.__MODULE__ = imported_module.__MODULE__
            #    if (
            #        hasattr(imported_module, "__HELP__")
            #        and imported_module.__HELP__
            #    ):
            #        HELPABLE[
            #            imported_module.__MODULE__.lower()
            #        ] = imported_module
            console.print(
                f">> [bold cyan]Successfully imported: [green]{all_module}.py"
            )
        console.print("")
        status.update(
            status="[bold blue]Importation Completed!",
        )
    console.print(
        "[bold green]Congrats!! Idzeroid Music Bot has started successfully!\n"
    )
    try:
        await app.send_message(
            LOG_GROUP_ID,
            "<b>Congrats!! Music Bot has started successfully!</b>",
        )
    except Exception:
        print(
            "\nBot has failed to access the log Channel. Make sure that you have added your bot to your log channel and promoted as admin!"
        )
        console.print(f"\n[red]Stopping Bot")
        return
    a = await app.get_chat_member(LOG_GROUP_ID, BOT_ID)
    if a.status != "administrator":
        print("Promote Bot as Admin in Logger Channel")
        console.print(f"\n[red]Stopping Bot")
        return
    console.print(f"\n┌[red] Bot Started as {BOT_NAME}!")
    console.print(f"├[green] ID :- {BOT_ID}!")
    if STRING1 != "None":
        try:
            await ASS_CLI_1.send_message(
                LOG_GROUP_ID,
                "<b>Congrats!! Assistant Client 1  has started successfully!</b>",
            )
        except Exception:
            print(
                "\nAssistant Account 1 has failed to access the log Channel. Make sure that you have added your Assistant to your log channel and promoted as admin!"
            )
            console.print(f"\n[red]Stopping Bot")
            return
        try:
            await ASS_CLI_1.join_chat("idzeroid")
            await ASS_CLI_1.join_chat("satanicsociety")
        except:
            pass
        console.print(f"├[red] Assistant 1 Started as {ASSNAME1}!")
        console.print(f"├[green] ID :- {ASSID1}!")
    if STRING2 != "None":
        try:
            await ASS_CLI_2.send_message(
                LOG_GROUP_ID,
                "<b>Congrats!! Assistant Client 2 has started successfully!</b>",
            )
        except Exception:
            print(
                "\nAssistant Account 2 has failed to access the log Channel. Make sure that you have added your Assistant to your log channel and promoted as admin!"
            )
            console.print(f"\n[red]Stopping Bot")
            return
        try:
            await ASS_CLI_2.join_chat("idzeroid")
            await ASS_CLI_2.join_chat("satanicsociety")
        except:
            pass
        console.print(f"├[red] Assistant 2 Started as {ASSNAME2}!")
        console.print(f"├[green] ID :- {ASSID2}!")
    if STRING3 != "None":
        try:
            await ASS_CLI_3.send_message(
                LOG_GROUP_ID,
                "<b>Congrats!! Assistant Client 3 has started successfully!</b>",
            )
        except Exception:
            print(
                "\nAssistant Account 3 has failed to access the log Channel. Make sure that you have added your Assistant to your log channel and promoted as admin!"
            )
            console.print(f"\n[red]Stopping Bot")
            return
        try:
            await ASS_CLI_3.join_chat("idzeroid")
            await ASS_CLI_3.join_chat("satanicsociety")
        except:
            pass
        console.print(f"├[red] Assistant 3 Started as {ASSNAME3}!")
        console.print(f"├[green] ID :- {ASSID3}!")
    if STRING4 != "None":
        try:
            await ASS_CLI_4.send_message(
                LOG_GROUP_ID,
                "<b>Congrats!! Assistant Client 4 has started successfully!</b>",
            )
        except Exception:
            print(
                "\nAssistant Account 4 has failed to access the log Channel. Make sure that you have added your Assistant to your log channel and promoted as admin!"
            )
            console.print(f"\n[red]Stopping Bot")
            return
        try:
            await ASS_CLI_4.join_chat("idzeroid")
            await ASS_CLI_4.join_chat("satanicsociety")
        except:
            pass
        console.print(f"├[red] Assistant 4 Started as {ASSNAME4}!")
        console.print(f"├[green] ID :- {ASSID4}!")
    if STRING5 != "None":
        try:
            await ASS_CLI_5.send_message(
                LOG_GROUP_ID,
                "<b>Congrats!! Assistant Client 5 has started successfully!</b>",
            )
        except Exception:
            print(
                "\nAssistant Account 5 has failed to access the log Channel. Make sure that you have added your Assistant to your log channel and promoted as admin!"
            )
            console.print(f"\n[red]Stopping Bot")
            return
        try:
            await ASS_CLI_5.join_chat("idzeroid")
            await ASS_CLI_5.join_chat("satanicsociety")
        except:
            pass
        console.print(f"├[red] Assistant 5 Started as {ASSNAME5}!")
        console.print(f"├[green] ID :- {ASSID5}!")
    if LOG_SESSION != "None":
        try:
            await LOG_CLIENT.send_message(
                LOG_GROUP_ID,
                "<b>Congrats!! Logger Client has started successfully!</b>",
            )
        except Exception:
            print(
                "\nLogger Client has failed to access the log Channel. Make sure that you have added your Logger Account to your log channel and promoted as admin!"
            )
            console.print(f"\n[red]Stopping Bot")
            return
        try:
            await LOG_CLIENT.join_chat("idzeroid")
            await LOG_CLIENT.join_chat("satanicsociety")
        except:
            pass
    console.print(f"└[red] Idzeroid Music Bot Boot Completed.")
    if STRING1 != "None":
        await pytgcalls1.start()
    if STRING2 != "None":
        await pytgcalls2.start()
    if STRING3 != "None":
        await pytgcalls3.start()
    if STRING4 != "None":
        await pytgcalls4.start()
    if STRING5 != "None":
        await pytgcalls5.start()
    await idle()
    console.print(f"\n[red]Stopping Bot")


@app.on_message(filters.command("start") & filters.private)
async def start_command(_, message):
    if len(message.text.split()) > 1:
        name = (message.text.split(None, 1)[1]).lower()
        if name[0] == "s":
            sudoers = await get_sudoers()
            text = "⭐️<u> **Owners:**</u>\n"
            sex = 0
            for x in OWNER_ID:
                try:
                    user = await app.get_users(x)
                    user = user.first_name if not user.mention else user.mention
                    sex += 1
                except Exception:
                    continue
                text += f"{sex}➤ {user}\n"
            smex = 0
            for count, user_id in enumerate(sudoers, 1):
                if user_id not in OWNER_ID:
                    try:
                        user = await app.get_users(user_id)
                        user = user.first_name if not user.mention else user.mention
                        if smex == 0:
                            smex += 1
                            text += "\n⭐️<u> **Sudo Users:**</u>\n"
                        sex += 1
                        text += f"{sex}➤ {user}\n"
                    except Exception:
                        continue
            if not text:
                await message.reply_text("No Sudo Users")
            else:
                await message.reply_text(text)
            if await is_on_off(5):
                sender_id = message.from_user.id
                sender_name = message.from_user.first_name
                umention = f"[{sender_name}](tg://user?id={int(sender_id)})"
                return await LOG_CLIENT.send_message(
                    LOG_GROUP_ID,
                    f"{message.from_user.mention} has just started bot to check <code>SUDOLIST</code>\n\n**USER ID:** {sender_id}\n**USER NAME:** {sender_name}",
                )
        if name[0] == "i":
            m = await message.reply_text("🔎 Fetching Info!")
            query = (str(name)).replace("info_", "", 1)
            query = f"https://www.youtube.com/watch?v={query}"
            results = VideosSearch(query, limit=1)
            for result in results.result()["result"]:
                title = result["title"]
                duration = result["duration"]
                views = result["viewCount"]["short"]
                thumbnail = result["thumbnails"][0]["url"].split("?")[0]
                channellink = result["channel"]["link"]
                channel = channel = result["channel"]["name"]
                link = result["link"]
                published = result["publishedTime"]
            searched_text = f"""
🔍__**Video Track Information**__

❇️**Title:** {title}

⏳**Duration:** {duration} Mins
👀**Views:** `{views}`
⏰**Published Time:** {published}
🎥**Channel Name:** {channel}
📎**Channel Link:** [Visit From Here]({channellink})
🔗**Video Link:** [Link]({link})

⚡️ __Searched Powered By {BOT_NAME}__"""
            key = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="🎥 Watch Youtube Video", url=f"{link}"
                        ),
                        InlineKeyboardButton(text="🔄 Close", callback_data="close"),
                    ],
                ]
            )
            await m.delete()
            await app.send_photo(
                message.chat.id,
                photo=thumbnail,
                caption=searched_text,
                parse_mode="markdown",
                reply_markup=key,
            )


if __name__ == "__main__":
    loop.run_until_complete(initiate_bot())
