# Create a Book class with a private attribute _title.
# Use a getter to return the title and a setter to update it. 
# Ensure the title cannot be an empty string.

class ttle:

    def __init__(self) -> None:
        self._title=0

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self,t):

        if len(t)>0:
            if t.istitle():
                self._title=t

            else:
                raise ValueError("\n\nEach latter of title should be capital.")

        else:
            raise ValueError("\nTitle cant be empty string.")
        

a=ttle()
a.title=input("\n\n\nEnter Title of book : ").title()

