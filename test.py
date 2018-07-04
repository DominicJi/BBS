import os
if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Auth.settings")
    import django
    django.setup()
    # def squares():
    #     return [lambda x:i**x for i in range(3)]
    # def squares():
    #     res=[]
    #     for i in range(3):
    #         def make_square(x,i):
    #             return i**x
    #         res.append(make_square)
    #     return res
    # for squares in squares():
    #     print(squares(2))
    # def solve(s):
    #     upper_num=0
    #     lower_num=0
    #     for i in s:
    #         if i.isupper():
    #             upper_num+=1
    #         elif i.islower():
    #             lower_num+=1
    #     if upper_num>lower_num:
    #         return s.upper()
    #     else:
    #         return s.lower()
    # def check_str(i):
    #     return 1 if i.islower() else -1
    #
    # def solve(s):
    #     res_num=list(map(check_str,s))
    #     return s.lower() if sum(res_num)>0 else s.upper()


    # def solve(s):
    #     upper_num=sum(l.isupper() for l in s)
    #     lower_num=sum(l.islower() for l in s)
    #     return [s.upper(),s.lower()][lower_num>=upper_num]
    #
    #
    # s=[1,1,1,2,3,3,9,4,4]
    # a=filter(lambda x:s.count(x)==1,s)
