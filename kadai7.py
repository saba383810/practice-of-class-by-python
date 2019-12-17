# クラスの定義
class Unit:
    #コンストラクタ
    def __init__(self,name,job,power):
        self.__name = name
        self.__job = job
        self.__hp = 100
        self.__power = power
        print("ユニットを作成しました。")
    def getName(self):
        return self.__name
    def getJob(self):
        return self.__job
    def getHP(self):
        return self.__hp
    def getPower(self):
        return self.__power
    def show(self):
        print("名前 : ",self.getName(),"\n職業 : ",self.getJob(),"\nHP   : ",self.getHP(),"\n力   : ",self.getPower())

#インスタンス化
unit = Unit("ああああ","ゆうしゃ",50)

# カプセル化された値を取り出すためにクラスの中の関数を使って表示させる。
unit.show()