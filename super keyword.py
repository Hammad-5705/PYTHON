class parent:
    def employee(self,name,id):
        self._name=name
        self._id=id


class child(parent):
        def programmer(self,name,id,lang):
            self._lang=lang
            super().employee(name,id)
            




a=child()
a.programmer("Ali",5656,"Python")
print(a._name,a._lang,a._id)
