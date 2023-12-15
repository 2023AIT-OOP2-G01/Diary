from diaries.DiarySample import DiarySample
from diaries.ArenDiary import ArenDiary
from diaries.ReoDiary import ReoDiary
# ↓のリストには、メンバーの各日記が格納されます。 
diaries = [
    DiarySample(), 
    ArenDiary(),
    ReoDiary(),
]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
