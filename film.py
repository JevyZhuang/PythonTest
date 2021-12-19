class TVshow:
    list_film=['1','2','3']
    def __init__(self,show):
        self.__show=show
    @property
    def show(self):
        return self.__show
    @show.setter    #设置setter方法，让属性可修改
    def show(self,value):
        if value in TVshow.list_film:
            self.__show="你选择了《"+value+"》,稍后将播放"
        else:
            self.__show="您点播的电影不存在"
tvshow=TVshow('1')
print("正在播放",tvshow.show)
print("你可以从",tvshow.list_film,"选择")
tvshow.show='2'
print(tvshow.show)
