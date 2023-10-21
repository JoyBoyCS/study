def get_count(s,ch):
    count = 0
    for item in s:
        if ch.upper() == item or ch.lower()==item:
            count+=1
    return count

if __name__ == '__main__':
    s='hellopython,Hellojava,hellojango'
    ch=input('请输入要统计的字符：')
    count=get_count(s,ch)
    print(count)