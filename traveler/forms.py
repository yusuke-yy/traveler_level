from django import forms
from django.core.mail import EmailMessage

from .models import Photo,Diagnosis

from django.urls import reverse_lazy

class GuestDiagnosisForm(forms.Form):
    prefectures = forms.CharField(label='今までに訪れた都道府県の数',max_length=2,widget=forms.TextInput(attrs={'pattern':'^[0-9]+$'}))
    countries = forms.CharField(label='今までに訪れた国の数',max_length=3,widget=forms.TextInput(attrs={'pattern':'^[0-9]+$'}))

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.fields['prefectures'].widget.attrs['class']= 'field'
        self.fields['prefectures'].widget.attrs['placeholder']= '今まで訪れた都道府県の数をここに入力してください'
        self.fields['countries'].widget.attrs['class']= 'field'
        self.fields['countries'].widget.attrs['placeholder']= '今まで訪れた国の数をここに入力してください'

class InquiryForm(forms.Form):
    name = forms.CharField(label='お名前',max_length=30)
    email = forms.EmailField(label='メールアドレス')
    title = forms.CharField(label='タイトル',max_length=30)
    message = forms.CharField(label='メッセージ',widget=forms.Textarea) 

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.fields['name'].widget.attrs['class']= 'form-control col-9'
        self.fields['name'].widget.attrs['placeholder']= 'お名前をここに入力してください。'
        self.fields['email'].widget.attrs['class']= 'form-control col-11'
        self.fields['email'].widget.attrs['placeholder']= 'メールアドレスをここに入力してください。'
        self.fields['title'].widget.attrs['class']= 'form-control col-11'
        self.fields['title'].widget.attrs['placeholder']= 'タイトルをここに入力してください。'
        self.fields['message'].widget.attrs['class']= 'form-control col-12'
        self.fields['message'].widget.attrs['placeholder']= 'メッセージをここに入力してください。'

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        title = self.cleaned_data['title']
        message = self.cleaned_data['message']

        subject = 'お問い合わせ {}'.format(title)
        message = '送信者名: {0}\nメールアドレス: {1}\nメッセージ:\n{2}'.format(name,email,message)
        from_email = 'admin@example.com'
        to_list = [
            'test@example.com'
        ]
        cc_list = [
            email
        ]
        message = EmailMessage(subject=subject,body=message,from_email=from_email,to=to_list,cc=cc_list)
        message.send()

class PhotoCreateForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('title','photo1',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class DiagnosisForm(forms.ModelForm):
    class Meta:
        model = Diagnosis
        fields = ('prefectures','countries',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'