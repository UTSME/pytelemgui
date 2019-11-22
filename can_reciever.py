# 01_sendReceiveSingleCanMsg.py
from canlib import canlib, Frame


def setUpChannel(channel=0,
                 openFlags=canlib.Open.ACCEPT_VIRTUAL,
                 bitrate=canlib.canBITRATE_1M,
                 outputControl=canlib.Driver.NORMAL):
    ch = canlib.openChannel(channel, openFlags)
    print("Using channel: %s, EAN: %s" % (
        canlib.ChannelData(channel).channel_name,
        canlib.ChannelData(channel).card_upc_no))
    ch.setBusOutputControl(outputControl)
    ch.setBusParams(bitrate)
    ch.busOn()
    return ch


def tearDownChannel(ch):
    ch.busOff()
    ch.close()


print("canlib dll version:", canlib.dllversion())

ch0 = setUpChannel(channel=0)

frame = Frame(id_=100, data=[1, 2, 3, 4], flags=canlib.MessageFlag.EXT)

while True:
    try:
        frame = ch0.read()
        print(frame)
    except (canlib.canNoMsg) as ex:
        pass
    except (canlib.canError) as ex:
        print(ex)

tearDownChannel(ch0)

