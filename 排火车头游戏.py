# encoding: utf-8
# 小时候玩的排火车头游戏
import random,time

class paihuoche(object):
    def __init__(self):
        
        #大小王
        big = small = 0
        #四花色
        spring = summer = autumn = winter = [1,2,3,4,5,6,7,8,9,10,11,12,13]

        #扑克装盒
        self.puke=[]
        self.puke.append(big)
        self.puke.append(small)
        self.puke +=spring+summer+autumn+winter

        #洗牌
        self.puke_daluan = self.puke.copy()
        random.shuffle(self.puke_daluan)
        
        #玩家个数
        self.geshu=3
        #分牌
        self.players = self.fund()

        #打印目前玩家的手牌
        print("#########################################") 
        for i,pai in enumerate(self.players):
            print("palyer{}的牌{}【{}】".format(i,pai,len(pai)))
        print("#########################################")
        
        #火车
        self.huoche=[]
        #出局的玩家
        self.chuju=[]
        
    #开始干
    def start(self):
        
        #如果出局人数小于总人数-1就一直玩下去
        while(len(self.chuju)<(self.geshu-1)):

            #依次排火车
            for i in range(self.geshu):
                if i not in self.chuju:
                    self.dapai(i)
            #休息1秒
            time.sleep(1)
            
            #打印目前玩家的手牌
            print("#########################################") 
            for i,pai in enumerate(self.players):
                print("palyer{}的牌{}【{}】".format(i,pai,len(pai)))
            print("#########################################") 
        #如果出局人数==总人数-1，就结束了    
        print("结束")
        
    #按玩家个数分牌   
    def fund(self):
        n = int(len(self.puke_daluan)/self.geshu)
        resules = []
        for i in range(0, len(self.puke_daluan), n):
            temp = self.puke_daluan[i:i + n]
            resules.append(temp)
        return resules

    #出牌
    def dapai(self,i):
        
        #出牌人永远是出第一张牌
        chupai = self.players[i][0]
        print("palyer{}出牌{}".format(i,chupai))
        
        #如果出的牌在火车中有
        if chupai not in self.huoche:
            self.huoche.append(chupai) #火车中加入这张牌
            print("当前火车{}【{}】".format(self.huoche,len(self.huoche))) #打印当前火车情况
            self.players[i].pop(0) #玩家手牌删除第一张 
            if(len(self.players[i])==0): #如果玩家没有手牌了，出局
                print("palyer{}出局".format(i))
                self.chuju.append(i) #吧出局数据组加入该出局的人
            
        #如果出的牌在火车中有
        else:
            self.huoche.append(chupai) #火车中加入这张牌
            self.players[i].pop(0) #玩家手牌删除第一张 
            paiIndex = self.huoche.index(chupai) #或者火车站这张牌的第一次出现的位置
            winPai = self.huoche[paiIndex:] #截取这个位置到最后 为赢的牌
            print("palyer{}赢牌{}".format(i,winPai))
            self.huoche = self.huoche[:paiIndex] #火车剩余的牌
            print("当前火车{}【{}】".format(self.huoche,len(self.huoche)))
            self.players[i]+=winPai #玩家在自己手牌加入赢的牌
            self.dapai(i) #当前玩家迭代发牌
        
        
dapai = paihuoche()
dapai.start()

            
