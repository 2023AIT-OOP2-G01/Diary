from diaries.AbstractDiary import AbstractDiary 
class ReoDiary(AbstractDiary):

    def get_date(self):
        return "2021-12-15"
    def get_summary(self):
        return "共同作業って難しいね"
    def get_author(self):
        return "Reo"