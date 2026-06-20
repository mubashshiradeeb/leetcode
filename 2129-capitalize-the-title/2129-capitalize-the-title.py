class Solution(object):
    def capitalizeTitle(self, title):
        a=title.lower().split(" ")
        b=[]
        for i in a:
            if len(i)>2:
                b.append(i.capitalize())
            else:
                b.append(i)
        return " ".join(b)
        
        