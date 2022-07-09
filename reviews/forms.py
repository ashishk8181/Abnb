from django import forms
from . import models

class CreateReviewForm(forms.ModelForm):
    cleanliness = forms.IntegerField(max_value=5, min_value=1)
    accuracy = forms.IntegerField(max_value=5, min_value=1)
    communication = forms.IntegerField(max_value=5, min_value=1)
    location = forms.IntegerField(max_value=5, min_value=1)
    check_in = forms.IntegerField(max_value=5, min_value=1)
    value = forms.IntegerField(max_value=5, min_value=1)

    class Meta:
        model = models.Review
        fields = (
            "review",
            "cleanliness",
            "accuracy",
            "communication",
            "location",
            "check_in",
            "value",
        )
    
    def save(self):
        review = super().save(commit=False)
        return review