
# Copyright (C) 2020 Yusuf Usta.
# Copyright (C) 2020 RaphielGang.
# Copyright (C) 2020 AsenaUserBot.


import os
import asyncio
import random
import shutil
import time
from telethon.tl import functions
from telethon.tl.types import InputMessagesFilterDocument

from userbot import CMD_HELP, AUTO_PP, ASYNC_POOL
from userbot.events import register

@register(outgoing=True, pattern="^.auto ?(.*)")
async def auto(event):
    metod = event.pattern_match.group(1).lower()
    
    if str(metod) != "isim" and str(metod) != "bio":
        await event.edit(f"Bilinmeyen tür. Var olan türler: `isim`, `bio` {metod}")
        return

    if metod in ASYNC_POOL:
        await event.edit(f"`Görünüşe göre {metod} zaten otomatik olarak değişiyor.`")
        return

    await event.edit(f"`{metod} ayarlanıyor ...`")
    if metod == "isim":
        HM = time.strftime("%H:%M")

        await event.client(functions.account.UpdateProfileRequest(  # pylint:disable=E0602
            last_name=f"⏰{HM}"
        ))
    elif metod == "bio":
        DMY = time.strftime("%d.%m.%Y")
        HM = time.strftime("%H:%M")

        Bio = f"📅 Tarih: {DMY} | ⌚️ Saat: {HM} | @AsenaUserBot"
        await event.client(functions.account.UpdateProfileRequest(  # pylint:disable=E0602
            about=Bio
        ))


    await event.edit(f"`{metod} ayarlandı :)`")

    ASYNC_POOL.append(metod)

    while metod in ASYNC_POOL:
        try:
            if metod == "isim":
                HM = time.strftime("%H:%M")

                await event.client(functions.account.UpdateProfileRequest(  # pylint:disable=E0602
                    last_name=f"⏰{HM}"
                ))
            elif metod == "bio":
                DMY = time.strftime("%d.%m.%Y")
                HM = time.strftime("%H:%M")

                Bio = f"📅 Tarih: {DMY} | ⌚️ Saat: {HM} | @AsenaUserBot"
                await event.client(functions.account.UpdateProfileRequest(  # pylint:disable=E0602
                    about=Bio
                ))

            await asyncio.sleep(60)
        except:
            return


CMD_HELP.update({"auto": ".auto isim (ya da) bio Kullanım: Otomatik saate göre değiştirir",})