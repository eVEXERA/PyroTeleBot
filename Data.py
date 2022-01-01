from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
𝙷𝙴𝙻𝙻𝙾 {}
𝚃𝙷𝙸𝚂 𝙱𝙾𝚃 𝚆𝙾𝚁𝙺𝚂 𝚃𝙾 𝙷𝙴𝙻𝙿 𝚈𝙾𝚄 𝙶𝙴𝚃 𝚂𝙴𝚂𝚂𝙸𝙾𝙽 𝚂𝚃𝚁𝙸𝙽𝙶. 
𝙼𝙰𝙽𝙰𝙶𝙴𝙳 𝙱𝚈 @TeamDeeCoDe
     """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("𝙶𝙴𝚃 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼 𝚂𝙴𝚂𝚂𝙸𝙾𝙽", callback_data="generate")],
        [InlineKeyboardButton("𝙶𝙴𝚃 𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽 𝚂𝙴𝚂𝚂𝙸𝙾𝙽", callback_data="generate")],
        [InlineKeyboardButton(text="𝙱𝙰𝙲𝙺", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("𝙶𝙴𝚃 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼 𝚂𝙴𝚂𝚂𝙸𝙾𝙽", callback_data="generate")],
        [InlineKeyboardButton("𝙶𝙴𝚃 𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽 𝚂𝙴𝚂𝚂𝙸𝙾𝙽", callback_data="generate")]
    ]
    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("𝙶𝙴𝚃 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼 𝚂𝙴𝚂𝚂𝙸𝙾𝙽", callback_data="generate")],
        [InlineKeyboardButton("𝙶𝙴𝚃 𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽 𝚂𝙴𝚂𝚂𝙸𝙾𝙽", callback_data="generate")]      
        [InlineKeyboardButton("𝙼𝙰𝙸𝙽𝚃𝙴𝙽𝙰𝙽𝙲𝙴 𝙱𝚈", url="https://t.me/TeamDeecode")],
        [
            InlineKeyboardButton("𝙷𝙾𝚆 𝚃𝙾 𝚄𝚂𝙴", callback_data="help"),
            InlineKeyboardButton("𝙰𝙱𝙾𝚄𝚃 𝙳𝙴𝙲𝙾𝙳𝙴", callback_data="about")
      ],
        [InlineKeyboardButton("𝙾𝚃𝙷𝙴𝚁 𝙳𝙴𝙲𝙾𝙳𝙴 𝙱𝙾𝚃𝚂", url="https://telegra.ph/DeCoDe-Projects-12-29")],
    ]


    # Help Message
    HELP = """
✨ **𝙰𝚅𝙰𝙸𝙻𝙰𝙱𝙻𝙴 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂** ✨ 
 /about - 𝙰𝙱𝙾𝚄𝚃 𝚃𝙷𝙸𝚂 𝙱𝙾𝚃 
 /help - 𝙷𝙾𝚆 𝚃𝙾 𝚄𝚂𝙴 𝚃𝙷𝙸𝚂 𝙱𝙾𝚃 
 /start - 𝚂𝚃𝙰𝚁𝚃 𝙱𝙾𝚃 
 /generate - 𝚂𝚃𝙰𝚁𝚃 𝙶𝙴𝙽𝙴𝚁𝙰𝚃𝙸𝙽𝙶 𝚂𝙴𝚂𝚂𝙸𝙾𝙽 
 /cancel - 𝙲𝙰𝙽𝙲𝙴𝙻 𝙿𝚁𝙾𝙲𝙴𝚂𝚂
 /restart - 𝚁𝙴𝚂𝚃𝙰𝚁𝚃 𝙿𝚁𝙾𝙲𝙴𝚂𝚂 
    """

    # About Message
    ABOUT = """
**𝙰𝙱𝙾𝚄𝚃 𝙳𝙴𝙲𝙾𝙳𝙴 𝙱𝙾𝚃𝚉**
𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙶𝚁𝙾𝚄𝙿 : [𝙳𝙴𝙲𝙾𝙳𝙴](HTTPS://T.ME/DECODESUPPORT)
𝙳𝙴𝚅𝙴𝙻𝙾𝙿𝙴𝚁 : [𝚂𝙰𝙼𝙼𝚈](https://github.com/BrayDanXD)
   
[𝙵𝙾𝙻𝙻𝙾𝚆 𝙾𝙽 𝙶𝙸𝚃𝙷𝚄𝙱](https://github.com/BRAYDNAXD)
𝙳𝙴𝙲𝙾𝙳𝙴 𝙼𝚄𝚂𝙸𝙲 : [𝙳𝙴𝙿𝙻𝙾𝚈 𝙼𝚄𝚂𝙸𝙲 𝙱𝙾𝚃](https://GitHub.com/braydanxd/promusic)
   """
   
