"""
Bir classdan istifadə edərək 2 metod yazın.
İlk metodda dəyər olaraq bir list içərisində rəqəmləri alın  və onu bir listə əlavə edin ( bu şəkildə olacaq: mylist=[1,2,3,4,5])
Daha sonra bir metod daha yazın. Bu metodda isə bizim bir argumentimiz olacaq (Hədəf rəqəm). Burada ilk metodda aldığımız listin 
dəyərləri içərisində hər hansı 2 rəqəmin cəmi verilmiş hədəf rəqəmə bərabərdirsə həmin rəqəmlərin indexlərini qaytarın. Əgər belə
rəqəmlər yoxdursa -1 cavabı qaytarın. 

Əlavə olaraq argumentləri hansı metodunuzda istifadə etmək istədiyiniz barəsində sərbəstsiniz və əlavə arqumentlərdən istifadə edəbilərsiniz."""




class Taskfive:
    def __init__(self):
        self.mylist = []

    def first_add(self, eded):
        self.mylist = eded

    def secondmet(self, target):
        yer = []
        for i in range(len(self.mylist)):
            for e in range(i + 1, len(self.mylist)):
                if self.mylist[i] + self.mylist[e] == target:
                    yer.append((i, e))
        return yer if yer else -1

defcr = Taskfive()
defcr.first_add([1, 2, 3, 4, 5])
print(defcr.secondmet(8))  
print(defcr.secondmet(14)) 




         
             
     