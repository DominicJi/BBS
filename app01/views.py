from django.shortcuts import render,redirect,HttpResponse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from app01 import forms
from app01 import models
from geetest import GeetestLib
# Create your views here.



#正常图片验证码
def login(request):
    form_obj=forms.UserForm()
    if request.method=='POST':
        ret={'code':0}
        username=request.POST.get('username')
        password=request.POST.get('password')
        v_code=request.POST.get('v_code','')
        if v_code.upper()==request.session.get('v_code',''):
            #自动校验用户名和密码对不对
            user=auth.authenticate(username=username,password=password)
            if user:
                # 内置的login方法
                # 1. 生成Session数据，存一下user_id 然后把sessionid写入Cookie
                # 后续每一次请求来的时候，AuthenticationMiddleware中的process_request方法中
                # 会自动帮我们取到user_id，然后到数据库中拿出user对象,然后添加到request.user属性中 --> request.user = user
                # 后续我们都可以通过request.user拿到当前的登陆用户对象
                auth.login(request,user)
                ret['data']='/home/'
            else:
                ret['code']=1
                ret['data']='用户名或密码错误'
        else:
            ret['code']=1
            ret['data']='验证码错误'
        return JsonResponse(ret)
    return render(request,'login.html',{'form_obj':form_obj})

def v_code(request):
    from PIL import Image,ImageDraw,ImageFont
    import random
    #定义一个生成随机颜色代码的内部函数,返回值对应RGB()里面的三个参数值
    def get_color():
        return random.randint(0,255),random.randint(0,255),random.randint(0,255)
    #生成一个图片对象
    img_obj=Image.new(
        'RGB',
        (250,35),
        color=(144,144,144)
    )
    #在图片中加文字
    #生成一个画笔对象
    draw_obj=ImageDraw.Draw(img_obj)
    #加载字体文件
    font_obj=ImageFont.truetype('static/font/kumo.ttf',size=35)
    #for循环五次，每次写一个随机的字符
    tmp_list=[]
    for i in range(5):
        n=str(random.randint(0,9))
        l=chr(random.randint(97,122))
        u=chr(random.randint(65,90))
        r=random.choice([n,l,u])
        tmp_list.append(r)
        draw_obj.text(
            (i*48+20,0),#验证码在图片区的位置
            r,          #内容
            get_color(),#颜色
            font=font_obj
        )
    #得到生成的随机验证码
    v_code_str=''.join(tmp_list)
    #不能使用全局的变量保存验证码，会被覆盖
    #每个请求都应该对应自己的验证码
    request.session['v_code']=v_code_str.upper()
    #加干扰线
    # width = 250  # 图片宽度（防止越界）
    # height = 35
    # for i in range(2):
    #     x1 = random.randint(0, width)
    #     x2 = random.randint(0, width)
    #     y1 = random.randint(0, height)
    #     y2 = random.randint(0, height)
    #     draw_obj.line((x1, y1, x2, y2), fill=get_color())
    #
    # # 加干扰点
    # for i in range(2):
    #     draw_obj.point([random.randint(0, width), random.randint(0, height)], fill=get_color())
    #     x = random.randint(0, width)
    #     y = random.randint(0, height)
    #     draw_obj.arc((x, y, x+4, y+4), 0, 90, fill=get_color())

    # 第一版： 将生成的图片保存到文件中
    # with open("xx.png", "wb") as f:
    #     img_obj.save(f, "png")
    # print("图片已经生成！")
    # with open("xx.png", "rb") as f:
    #     return HttpResponse(data, content_type="image/png")

    #将图片直接在内存中保存
    from io import BytesIO
    tmp=BytesIO()#生成一个io对象
    img_obj.save(tmp,'png')
    data=tmp.getvalue()
    return HttpResponse(data,content_type='image/png')


# s使用滑动验证码登录
pc_geetest_id = "b46d1900d0a894591916ea94ea91bd2c"
pc_geetest_key = "36fc3fe98530eea08dfc6ce76e3d24c4"

def pcgetcaptcha(request):
    user_id = 'test'
    gt = GeetestLib(pc_geetest_id, pc_geetest_key)
    status = gt.pre_process(user_id)
    request.session[gt.GT_STATUS_SESSION_KEY] = status
    request.session["user_id"] = user_id
    response_str = gt.get_response_str()
    return HttpResponse(response_str)

def login2(request):
    form_obj=forms.UserForm()
    if request.method=='POST':
        gt = GeetestLib(pc_geetest_id, pc_geetest_key)
        challenge = request.POST.get(gt.FN_CHALLENGE, '')
        validate = request.POST.get(gt.FN_VALIDATE, '')
        seccode = request.POST.get(gt.FN_SECCODE, '')
        status = request.session[gt.GT_STATUS_SESSION_KEY]
        user_id = request.session["user_id"]
        if status:
            result = gt.success_validate(challenge, validate, seccode, user_id)
        else:
            result = gt.failback_validate(challenge, validate, seccode)
        # 如果验证码正确
        if result:
            ret={'code':0}
            username=request.POST.get('username')
            password=request.POST.get('password')
            #自动校验用户名和密码对不对
            user=auth.authenticate(username=username,password=password)
            if user:
            # 内置的login方法
            # 1. 生成Session数据，存一下user_id 然后把sessionid写入Cookie
            # 后续每一次请求来的时候，AuthenticationMiddleware中的process_request方法中
            # 会自动帮我们取到user_id，然后到数据库中拿出user对象,然后添加到request.user属性中 --> request.user = user
            # 后续我们都可以通过request.user拿到当前的登陆用户对象
                auth.login(request,user)
                ret['data']='/home/'
            else:
                ret['code']=1
                ret['data']='用户名或密码错误'
            return JsonResponse(ret)
    return render(request,'login2.html',{'form_obj':form_obj})

@login_required
def home(request):
    return render(request,'home.html')

def logout(request):
    #直接调用auth内置的注销方法
    #拿到request中含有的用户id字段，到数据库里面删除对应的session
    auth.logout(request)
    return redirect('/login/')

@login_required
def set_password(request):
    form_obj=forms.Set_password()
    if request.method=='POST':
        ret = {'flag': 0}
        form_obj=forms.Set_password(request.POST)
        if form_obj.is_valid():
            old_password=request.POST.get('raw_password')
            new_password=request.POST.get('new_password')
            #调用auth提供的自动校验密码的方法先校验原来的密码对不对
            user_obj=request.user
            if user_obj.check_password(old_password):
                #原来的密码正确后，在去校验两次修改的密码对不对
                # if new_password==confirm_password:
                    #两次密码一致，则去数据库修改密码
                user_obj.set_password(new_password)
                #保存修改
                user_obj.save()
                ret['data']='/login/'
            else:
                ret['flag']=1
                ret['data']='原密码错误'
        else:
            ret['flag']=2
            ret['data']=form_obj.errors
        return JsonResponse(ret)
    return render(request,'set_password.html',{'form_obj':form_obj})

def middle(request):
    return render(request,'middle.html')


#form表单版注册数据
def register(request):
    form_obj=forms.UserForm()
    if request.method=='POST':
        form_obj=forms.UserForm(request.POST)
        if form_obj.is_valid():
            avatar_obj=request.FILES.get('avatar')
            form_obj.cleaned_data.pop('confirm_password','')
            #创建用户
            models.UserInfo.objects.create_user(avatar=avatar_obj,**form_obj.cleaned_data)
            #创建超级用户
            # User.objects.create_superuser(username=,password=,email=)
            return redirect('/middle/')
    return render(request,'register.html',{'form_obj':form_obj})


#ajax版提交注册数据
def reg(request):
    form_obj=forms.UserForm()
    if request.method=='POST':
        ret={'flag':0}
        form_obj=forms.UserForm(request.POST)
        if form_obj.is_valid():
            avatar_obj=request.FILES.get('avatar')
            form_obj.cleaned_data.pop('confirm_password','')
            models.UserInfo.objects.create_user(avatar=avatar_obj,**form_obj.cleaned_data)
            ret['data']='/middle/'
        else:
            ret['flag']=1
            ret['data']=form_obj.errors
        return JsonResponse(ret)
    return render(request,'reg.html',{'form_obj':form_obj})