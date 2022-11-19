def find_short(s):
    return min(len(x) for x in s.split())
    
if __name__=="__main__":
    print(find_short("Let's travel abroad shall we"))
