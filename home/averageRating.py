class AverageRating:
    title = ""
    pos_rate = 0
    neg_rate = 0

    def __init__(self, title, pos_rate, neg_rate):
        self.title = title
        self.pos_rate = pos_rate
        self.neg_rate = neg_rate
        
    def getAverage(self):
        if int(self.pos_rate) ==0 and int(self.neg_rate) == 0:
            return 0
        elif int(self.pos_rate) == 0 and int(self.neg_rate) > 0:
            #return int(self.neg_rate)
            return 0
        elif int(self.pos_rate) >0 and int(self.neg_rate) ==0:
            #return int(self.pos_rate)
            return 100
        elif self.pos_rate is None:
            return 0
        elif self.neg_rate is None:
            return 0
        else:
            if int(self.pos_rate) < int(self.neg_rate):
                temp = int(self.pos_rate) - int(self.neg_rate)
                temp = temp*-1
                temp = temp / int(self.pos_rate)
                return temp * 100
                #return 100 - int(self.pos_rate) / int(self.neg_rate)
            elif int(self.pos_rate) > int(self.neg_rate):
                temp = int(self.pos_rate) - int(self.neg_rate)
                temp = temp / int(self.pos_rate)
                return temp * 100
                #return 100 - int(self.neg_rate) / int(self.pos_rate)

class OnlyAverage:
    title = ""
    average = 0

    def __init__(self, title, average):
        self.title = title
        self.average = average
        
