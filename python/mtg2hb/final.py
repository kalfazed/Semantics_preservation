class MTG:
    def __init__(self, mtg, eec_data, eec_symble):
        self.mtg = mtg
        self.eec_data = eec_data
        self.eec_symble = eec_symble

class HB:
    def __init__(self, hb_data, hb_symble):
        self.hb_data = hb_data 
        self.hb_symble = hb_data


class Mathematical_symble:
    def __init__(self, symble, priority):
        self.symble = symble 
        self.priority = priority

    def displayMath(self):
        print "Symble :", self.symble, ", Priority: ", self.priority




#Seperate all of the EEC in a MTG into the data and symble part
def seperate_MTG(mtg):
    for i in range(len(mtg)):
        seperate_EEC(mtg[i])
        EEC_Sig_data = []
        EEC_Sig_symble = []
