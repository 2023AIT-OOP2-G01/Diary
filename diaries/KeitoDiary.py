from diaries.AbstractDiary import AbstractDiary 
class KeitoDiary(AbstractDiary):
    def get_date(self):
        return "2021-12-18"
    def get_summary(self):
        return "とても寒かった。冬みたいに寒かった"
    def get_author(self):
        return "Keito"