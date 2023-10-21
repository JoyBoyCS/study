#erhu  piano   violin
class Instrument(object):
    def __init__(self,name):
        self.name=name
        
    def play(self):
        print(f'{self.name}在演奏')
        
if __name__ == '__main__':
    erhu=Instrument('二胡')
    piano=Instrument('钢琴')
    violin=Instrument('小提琴')
    
    erhu.play()
    piano.play()
    violin.play()