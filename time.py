import asyncio
from datetime import datetime
import pytz
from telethon import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest

# بيانات API مالك من https://my.telegram.org
API_ID = 17400306
API_HASH = "fbc295e7bd64178a0755626eff0682de"
SESSION = "time_session"

# توقيت بغداد
TZ = "Asia/Baghdad"

# ستايل الأرقام fullwidth
style = str.maketrans("0123456789", "０１２３４５６７８９")

def fancy_time(t: str) -> str:
    return t.translate(style)

async def main():
    client = TelegramClient(SESSION, API_ID, API_HASH)
    await client.start()

    me = await client.get_me()
    print(f"شغال ✅ بحساب: {me.first_name}")

    while True:
        now = datetime.now(pytz.timezone(TZ)).strftime("%H:%M")
        fancy = fancy_time(now)
        try:
            await client(UpdateProfileRequest(
                last_name=f"⏰ {fancy}"   # يظهر ⏰ １４:３７ مثلاً
            ))
            print("تم تحديث:", fancy)
        except Exception as e:
            print("خطأ:", e)

        await asyncio.sleep(60)

if __name__ == "__main__":
    asyncio.run(main())
