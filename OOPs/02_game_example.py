class Remote():
    pass


class Player:
    def moveright(self):
        pass
    def moveleft(self):
        pass
    def movetop(self):
        pass

# object making/instantiation (memory allocated)
remote1=Remote()
player1=Player()


if(remote1.isLeftpressed()):
    player1.moveleft()