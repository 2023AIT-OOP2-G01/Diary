from diaries.DiarySample import DiarySample
from diaries.ArenDiary import ArenDiary
from diaries.ReoDiary import ReoDiary
from diaries.MizunoDiary import MizunoDiary
from diaries.HashimotoDiary import HashimotoDiary
from diaries.KeitoDiary import KeitoDiary
from diaries.ShoriDiary import ShoriDiary
from diaries.YamadaDiary import YamadaDiary
# ↓のリストには、メンバーの各日記が格納されます。 
diaries = [
    DiarySample(), 
    ArenDiary(),
    ReoDiary(),
    MizunoDiary(),
    HashimotoDiary(),
    KeitoDiary(),
    ShoriDiary(),
    YamadaDiary()
]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
