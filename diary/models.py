from django.db import models

class Category(models.Model):
    """A category that the user can asign to notes"""
    COLOUR_CHOICES = [
        ('#FF0000', 'Red'),
        ('#00FF00', 'Green'),
        ('#0000FF', 'Blue'),
        ('#FFFF00', 'Yellow'),
        ('#FF00FF', 'Magenta'),
        ('#00FFFF', 'Cyan'),
        ('#000000', 'Black'),
        ('#FFFFFF', 'White'),
    ]

    category_name = models.CharField(max_length=100)
    category_colour = models.CharField(max_length=7, choices=COLOUR_CHOICES, default='#FFFFFF')  #default to white

    class Meta:
        verbose_name_plural = 'Categories'  # Plural name

    def __str__(self) -> str:
        return str(self.category_name)
    
class Note(models.Model):
    """A diary note added by the user"""
    IMPORTANCE_CHOICES = [
        (1, 'Low'),
        (2, 'Medium'),
        (3, 'High'),
    ]
    
    title = models.CharField(max_length = 50, default="Untitled") # each note will have a title
    my_note=models.TextField(default="") #string is accepted
    importance=models.IntegerField(choices=IMPORTANCE_CHOICES, default=1)#by default the importance is 1=low
    public=models.BooleanField(default=False)#by default this is not chosen
    date_added=models.DateTimeField(auto_now_add=True) #adds date automatically to new reviews
    date_modified=models.DateTimeField(auto_now=True) #timestamp if review is modified
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)  # Allows null category = a note without a category
    #category=models.ForeignKey(Category, on_delete=models.CASCADE, default=1)#connects reviews to categories in database
    #                                                      #if a category is deleted, so are the notes


    def __str__(self) -> str:
        '''Return a string representation of the model.'''
        # Check if category is assigned to avoid "NoneType" errors
        category_name = self.category.category_name if self.category else "No Category"
        return f"{category_name}: {self.my_note}"  # Format as a single string