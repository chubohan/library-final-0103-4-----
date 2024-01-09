from django import forms

class BorrowForm(forms.Form):
    user_name = forms.CharField(label='你的暱稱', max_length=50, initial='daniel')
    book_name = forms.CharField(label='書名', max_length=50)
    borrow_date=forms.CharField(label='借書日期', max_length=50)
    return_date=forms.CharField(label='還書日期', max_length=50)
    statue=forms.BooleanField(label='狀態')