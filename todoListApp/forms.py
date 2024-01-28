from django import forms
from .models import Task


class TaskForm (forms.ModelForm):
    title = forms.CharField(label=" Title ",strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Title'}))
    description = forms.CharField(label=" description ",strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Description'}))
    status = forms.ChoiceField(choices=Task.STATUS,widget=forms.Select(attrs={'class':'form-control'}))

    class Meta:
        model = Task
        fields = ('title','description','status','date')
        
        widgets={
            'date' : forms.DateInput(attrs={'class':'form-control','type':'date'}),
        }

    def __init__(self, *args, **kwargs):
        
        super(TaskForm, self).__init__(*args, **kwargs)

        for i in self.fields :
            self.fields[i].required = False
        
        self.fields['title'].required = True
        self.fields['status'].required = True
        self.fields['date'].required = True
