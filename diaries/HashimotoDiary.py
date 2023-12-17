from diaries.AbstractDiary import AbstractDiary
class HashimotoDiary(AbstractDiary):
    def get_date(self):
        return "2021-12-17"
    
    def get_summary(self):
        return """他の教科の課題が多かった"""
    
    def get_author(self):
        return "Hashimoto"