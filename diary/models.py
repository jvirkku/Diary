from django.db import models


class Note(models.Model):
    """A diary note added by the user"""
    IMPORTANCE_CHOICES = [
        (1, 'Low'),
        (2, 'Medium'),
        (3, 'High'),
    ]
    
    my_note=models.TextField(default="") #string is accepted
    importance=models.IntegerField(choices=IMPORTANCE_CHOICES, default=1)#by default the importance is 1=low
    public=models.BooleanField(default=False)#by default this is not chosen
    date_added=models.DateTimeField(auto_now_add=True) #adds date automatically to new reviews
    date_modified=models.DateTimeField(auto_now=True) #timestamp if review is modified
    # category=models.ForeignKey(Category, on_delete=models.CASCADE, default=1)#connects reviews to categories in database
    #                                                      #if a category is deleted, so are the notes


    def __str__(self) -> str:
        '''Return a string representation of the model.'''
        return self.my_note  #returns the note as text
    