# -*- coding: utf-8 -*-
#
#   ____  __  ___   ___  ___  ___  _  _  __       __   ___  __
#  (_  _)(  )(  ,) (  _)(   \(  _)( )( )(  )     (  ) (  ,\(  )
#   )(   )(  )  \  ) _) ) ) )) _) )()(  )(__    /__\  ) _/ )(
#  (__) (__)(_)\_)(___)(___/(_)   \__/ (____)  (_)(_)(_)  (__)
#
#
# This file is part of Tiredful API application

from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'autocomplete': 'off'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete': 'off'}))
    grant_type = forms.CharField(widget=forms.HiddenInput(attrs={'value': 'password'}))
    client_id = forms.CharField(widget=forms.HiddenInput(attrs={'value': '5cI2vLy5RYR5cphK1KQbEG8xpTpjFbq3agcfQMkH'}))
    client_secret = forms.CharField(widget=forms.HiddenInput(attrs={
        'value': 'aFUbytyk91ihiyeOb0mBhsArZs6HYZxj5c8AlN8GmBLEjAa7lLPlL4VDDUvCQDfaFjQj1LWSHe3dmfUAVnlA7Znx8Gau5S2UW3pAQMwQBeK0c2NB89PbSYCZp1JnJ6u7'}))


class LogoutForm(forms.Form):
    token = forms.CharField(widget=forms.TextInput(attrs={'autocomplete': 'off'}))
    client_id = forms.CharField(widget=forms.HiddenInput(attrs={'value': '5cI2vLy5RYR5cphK1KQbEG8xpTpjFbq3agcfQMkH'}))
    client_secret = forms.CharField(widget=forms.HiddenInput(attrs={
        'value': 'aFUbytyk91ihiyeOb0mBhsArZs6HYZxj5c8AlN8GmBLEjAa7lLPlL4VDDUvCQDfaFjQj1LWSHe3dmfUAVnlA7Znx8Gau5S2UW3pAQMwQBeK0c2NB89PbSYCZp1JnJ6u7'}))
