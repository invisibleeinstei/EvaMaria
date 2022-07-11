class script(object):
    START_TXT = """<b>𝐇𝐞𝐲 {},
𝐌𝐲 𝐍𝐚𝐦𝐞 𝐢𝐬 <a href=https://t.me/{}>{}</a>,𝐈'𝐦 𝐅𝐚𝐬𝐭 𝐅𝐢𝐥𝐭𝐞𝐫 𝐁𝐨𝐭 𝐖𝐢𝐭𝐡 𝐀𝐝𝐯𝐚𝐧𝐜𝐞𝐝 𝐅𝐮𝐧𝐜𝐭𝐢𝐨𝐧𝐬.. 🐥🌳</b>

𝙰𝚕𝚠𝚊𝚢𝚜 𝚂𝚒𝚖𝚙𝚕𝚎 𝙰𝚗𝚍 𝙵𝚊𝚜𝚝  𝙰𝚕𝚕 𝗔𝗟 𝗞𝗨𝗣𝗣𝗜𝗬𝗔 𝚋𝚘𝚝𝚜...🐣🌳
©️𝙰𝚕𝚕 𝚛𝚒𝚐𝚑𝚝𝚜 𝚛𝚎𝚜𝚎𝚛𝚟𝚎𝚍 𝗔𝗟 𝗞𝗨𝗣𝗣𝗜𝗬𝗔 𝚃𝚎𝚊𝚖. 🌳"""
    HELP_TXT = """𝐇𝐞𝐞𝐞.{} 👻
𝐇𝐞𝐫𝐞 𝐢𝐬 𝐭𝐡𝐞 𝐡𝐞𝐥𝐩 𝐟𝐨𝐫 𝐦𝐲 𝐜𝐨𝐦𝐦𝐚𝐧𝐝𝐬."""
    ABOUT_TXT = """✯ ᴍʏ ɴᴀᴍᴇ: {} 
✯ ᴅᴇᴠᴇʟᴏᴘᴇʀ: <a href=https://t.me/invisible_einstein>ɪɴᴠɪꜱɪʙʟᴇ ᴇɪɴꜱᴛᴇɪɴ |ᴵᴱ ⚡️</a>
✯ ᴘʀᴏɢʀᴀᴍ ʟɪʙʀᴀʀʏ: 𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦 🔥
✯ ʟᴀɴɢᴜᴀɢᴇ: 𝐏𝐲𝐭𝐡𝐨𝐧𝟑 🌟
✯ ᴅᴀᴛᴀʙᴀꜱᴇ: 𝐆𝐨𝐨𝐠𝐥𝐞 𝐕𝐏𝐒 🚀
✯ ʙᴏᴛ ꜱᴇʀᴠᴇʀ: 𝐆𝐨𝐨𝐠𝐥𝐞 𝐕𝐏𝐒 🚧
<b>𝙰𝚕𝚠𝚊𝚢𝚜 𝚂𝚒𝚖𝚙𝚕𝚎 𝙰𝚗𝚍 𝙵𝚊𝚜𝚝  𝙰𝚕𝚕 𝗔𝗟 𝗞𝗨𝗣𝗣𝗜𝗬𝗔 𝚋𝚘𝚝𝚜...🐣🌳</b>
©️𝙰𝚕𝚕 𝚛𝚒𝚐𝚑𝚝𝚜 𝚛𝚎𝚜𝚎𝚛𝚟𝚎𝚍 𝗔𝗟 𝗞𝗨𝗣𝗣𝗜𝗬𝗔 𝚃𝚎𝚊𝚖. 🌳"""
    SOURCE_TXT = """𝐎𝐨𝐨𝐩𝐬.𝐒𝐨𝐫𝐫𝐲 𝐈 𝐚𝐦 𝐧𝐨𝐭 𝐚 𝐨𝐩𝐞𝐧 𝐬𝐨𝐮𝐫𝐜𝐞 𝐩𝐫𝐨𝐣𝐞𝐜𝐭.𝐩𝐥𝐞𝐚𝐬𝐞 𝐏𝐌 𝐌𝐲 𝐟𝐚𝐭𝐡𝐞𝐫.<a href=https://t.me/invisible_einstein>ɪɴᴠɪꜱɪʙʟᴇ ᴇɪɴꜱᴛᴇɪɴ |ᴵᴱ ⚡️</a>
  
<b>DEVS:</b>
- <a href=https://t.me/invisible_einstein>Invisible Einstein⚡️</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and I will respond whenever a keyword is found the message

<b>NOTE:</b>
1. I should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- I will Support a both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Me supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/...)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn (😶) and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of I

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """★ 𝐓𝐨𝐭𝐚𝐥 𝐅𝐢𝐥𝐞𝐬: <code>{}</code> 🚧
★ 𝐓𝐨𝐭𝐚𝐥 𝐔𝐬𝐞𝐫𝐬: <code>{}</code>🙋🏻‍♂️
★ 𝐓𝐨𝐭𝐚𝐥 𝐂𝐡𝐚𝐭𝐬: <code>{}</code>💁🏻‍♂️🎈
★ 𝐔𝐬𝐞𝐛 𝐒𝐭𝐨𝐫𝐚𝐠𝐞: <code>{}</code>🔥 
★ 𝐑𝐞𝐦𝐚𝐢𝐧𝐢𝐧𝐠 𝐒𝐩𝐚𝐜𝐞: <code>{}</code>🚀"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
