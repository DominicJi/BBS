from django import forms
from django.core.validators import RegexValidator
from django.core.validators import ValidationError


class UserForm(forms.Form):
    username=forms.CharField(
        max_length=16,
        min_length=3,
        label='用户名',
        error_messages={
            'required':'用户名不能为空',
            'min_length':'用户名最少三位',
            'max_length':'用户名最多16位'
        },
        widget=forms.widgets.TextInput(attrs={'class':'form-control'})
    )
    password=forms.CharField(
        max_length=16,
        min_length=8,
        label='密码',
        error_messages={
            'required': '密码不能为空',
            'min_length': '密码最少8位',
            'max_length': '密码最多16位',
        },
        widget=forms.widgets.PasswordInput(render_value=True,attrs={'class':'form-control'}),
        #校验的列表内不仅可以是正则，也可以是自定义的校验函数
        # validators=[RegexValidator(r'\d','密码必须包含数字'),RegexValidator(r'[a-zA-Z]','密码必须包含字母')]
    )
    confirm_password=forms.CharField(
        max_length=16,
        min_length=8,
        label='确认密码',
        error_messages={
            'required': '密码不能为空',
            'min_length': '密码最少8位',
            'max_length': '密码最多16位',
        },
        widget=forms.widgets.PasswordInput(render_value=True,attrs={'class':'form-control'}),
    )
    phone=forms.CharField(
        max_length=11,
        min_length=11,
        label='手机号',
        error_messages={
            'min_length': '手机号只能是11位',
            'max_length': '手机号只能是11位',
            'required':'手机号不能为空',
        },
        validators=[RegexValidator(r'^[0-9].*','手机号只能是数字'),RegexValidator(r'^1[356789][0-9]{9}$','请填写正确的手机号格式')],
        widget = forms.widgets.TextInput(attrs={'class': 'form-control'})
    )
    # email=forms.CharField(
    #     label='邮箱',
    #     required=False,
    #     # error_messages={
    #     #     'required': '邮箱不能为空',
    #     # },
    #     widget=forms.widgets.EmailInput(attrs={'class':'form-control'})
    # )
    # gender=forms.ChoiceField(
    #     choices=((1,'男'),(2,'女'),(3,'保密')),
    #     label='性别',
    #     required=False,
    #     initial=3,
    #     widget=forms.widgets.RadioSelect
    # )
    # hobby=forms.MultipleChoiceField(
    #     choices=((1,'篮球'),(2,'足球'),(3,'斯诺克'),(4,'美女'),(5,'游戏'),(6,'电影'),(7,'漫画')),
    #     label='爱好',
    #     required=False,
    #     initial=[1,3],
    #     widget=forms.widgets.SelectMultiple(attrs={'class':'form-control '})
    # )
    #局部钩子函数
    #利用form组件给我们提供的钩子函数实现，数据验证
    def clean_username(self):
        #从form组件中拿出符合我字段定义的基本要求数据用户名
        value=self.cleaned_data.get('username')
        #判断输入的用户名中是否含有JBY字段，有就抛出提示信息
        if 'JBY' in value:
            raise ValidationError('不能用爸爸的姓名拼音')
        else:
            #没有则将数据返回给form组件
            return value
    #全局钩子函数
    #利用钩子函数，自定义方法实现密码一致性的校验
    def clean(self):
        #此时通过校验的数据都保存在self.cleaned_data中
        password=self.cleaned_data.get('password')
        confirm_password=self.cleaned_data.get('confirm_password')
        #取出两次用户输入的密码
        if password==confirm_password and password:
            # 将用户输入的所有数据再次返回给form组件
            return self.cleaned_data
        #不一致，向confirm_password字段中添加错误信息
        self.add_error('confirm_password','两次密码不一致')
        #抛出异常
        raise ValidationError('两次密码不一致')


class Set_password(forms.Form):
    raw_password = forms.CharField(
        max_length=16,
        min_length=8,
        label='原密码',
        error_messages={
            'required': '密码不能为空',
            'min_length': '密码最少8位',
            'max_length': '密码最多16位',
        },
        widget=forms.widgets.PasswordInput(render_value=True, attrs={'class': 'form-control'}),
        # 校验的列表内不仅可以是正则，也可以是自定义的校验函数
        # validators=[RegexValidator(r'\d','密码必须包含数字'),RegexValidator(r'[a-zA-Z]','密码必须包含字母')]
    )
    new_password = forms.CharField(
        max_length=16,
        min_length=8,
        label='新密码',
        error_messages={
            'required': '新密码不能为空',
            'min_length': '新密码最少8位',
            'max_length': '新密码最多16位',
        },
        widget=forms.widgets.PasswordInput(render_value=True, attrs={'class': 'form-control'}),
        # 校验的列表内不仅可以是正则，也可以是自定义的校验函数
        # validators=[RegexValidator(r'\d','密码必须包含数字'),RegexValidator(r'[a-zA-Z]','密码必须包含字母')]
    )
    confirm_password = forms.CharField(
        max_length=16,
        min_length=8,
        label='确认密码',
        error_messages={
            'required': '密码不能为空',
            'min_length': '密码最少8位',
            'max_length': '密码最多16位',
        },
        widget=forms.widgets.PasswordInput(render_value=True, attrs={'class': 'form-control'}),
        # 校验的列表内不仅可以是正则，也可以是自定义的校验函数
        # validators=[RegexValidator(r'\d','密码必须包含数字'),RegexValidator(r'[a-zA-Z]','密码必须包含字母')]
    )

    def clean(self):
        new_password=self.cleaned_data.get('new_password')
        confirm_password=self.cleaned_data.get('confirm_password')
        if new_password and new_password==confirm_password:
            return self.cleaned_data
        else:
            self.add_error('confirm_password','两次密码不一致')
            raise ValidationError('两次密码不一致')
