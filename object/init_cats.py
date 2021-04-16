class Cat:
    def __init__(self, name, color='흰색'): #항상 class 를 초기화
        self.name = name
        self.color = color

    def meow(self, name):
        print('내 이름은 {}, 색깔은 {} , 야옹'.format(self.name, self.color))
        print('속도는 ', name)

nabi = Cat("나비")
nabi.meow(100)
nero = Cat("네로","검은색")
nero.meow(200)
mimi = Cat("미미","갈색")
mimi.meow(300)