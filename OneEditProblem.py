def oneEdit(s1, s2):
    s1 = list(s1)
    s2 = list(s2)
    if len(s2) > len(s1) + 1:
        return False
    elif len(s2) < len(s1) - 1:
        return False
    elif len(s2) > len(s1):
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                dif = s1[i]
                s1[i] = s2[i]
                if s1 == s2:
                    return True
                s1[i] = dif
                if s2[:i] == s1[:i] and s2[(i+1):] == s1[i:]:
                    return True
        s1.append(s2[-1])
        if s1 == s2:
            return True
        else:
            return False
    else:
        for i in range(len(s2)):
            if s1[i] != s2[i]:
                dif = s2[i]
                s2[i] = s1[i]
                if s1 == s2:
                    return True
                s2[i] = dif
                if s1[:i] == s2[:i] and s1[(i+1):] == s2[i:]:
                    return True
        s2.append(s1[-1])
        if s2 == s1:
            return True
        else:    
            return False 


print(oneEdit("pale", "pale"))
