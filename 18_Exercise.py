#raise error example 2
class mobile:
    def __init__(self, name):
        self.name=name


class MObileStore:
    def __init__(self):
        self.mobile = []


    def add_mobile(self,new_mobile):
         if isinstance(new_mobile,mobile):
           self.mobile.append(new_mobile)
         else:
             raise TypeError('new mobile shuold be object of mobile class  ')
oneplus=mobile('one plus 6')
samsung='samsug galaxy s8 '
MoboStore= MObileStore()
# print(MobolStore.mobile)
MoboStore.add_mobile(oneplus)
# print(MoboStore.mobile)
mobo_phones=MoboStore.mobile
print(mobo_phones[0].name)