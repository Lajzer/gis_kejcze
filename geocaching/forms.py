from .models import GeocachingUser, Package, Comment

class NotepadUserCreationForm(UserCreationForm):

    class Meta:
        model = NotepadUser
        fields = ('username', 'email')

class NotepadUserChangeForm(UserChangeForm):

    class Meta:
        model = NotepadUser
        fields = ('username', 'email')
