# class Solution:
#     def capitalizeTitle(self, title: str) -> str:
#         title=title.lower().split()
#         s=[]
#         for i in title:
#             if len(i)>2:
#                 s.append(i.capitalize())
#             else:
#                 s.append(i.lower())
#         return " ".join(s)
class Solution:
    def capitalizeTitle(self, title: str) -> str:
        return " ".join(
            word.capitalize() if len(word) > 2 else word.lower()
            for word in title.lower().split()
        )
            