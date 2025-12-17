class Solution(object):
    def reformatNumber(self, number):
        # Extract digits only
        nl = []
        for i in number:
            if i.isdigit():
                nl.append(i)

        s = ""
        ln = len(nl)
        i = 0

        while ln > 0:
            if ln > 4:
                s += nl[i] + nl[i+1] + nl[i+2] + "-"
                i += 3
                ln -= 3
            elif ln == 4:
                s += nl[i] + nl[i+1] + "-" + nl[i+2] + nl[i+3]
                break
            else:
                s += "".join(nl[i:i+ln])
                break

        return s
