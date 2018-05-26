class Mathematical_symble:
    def __init__(self, symble, priority):
        self.symble = symble 
        self.priority = priority

    def displayMath(self):
        print "Symble :", self.symble, ", Priority: ", self.priority


# Seperate a single EEC into data and symble part
def seperate_EEC(eec, num, eec_data, eec_symble):
    EEC_Sig_data = []
    EEC_Sig_symble = []
    priority = 0
    for i, ch in enumerate(eec):
        if ch.isdigit():
            EEC_Sig_data.append(ch)
        elif ch == '(':
            priority += 100
        elif ch == ')':
            priority -= 100
            if (i != len(eec)-1 and eec[i+1] == '('):
                EEC_Sig_symble.append(Mathematical_symble('/\\', priority))
        elif ch.isspace():
            EEC_Sig_symble.append(Mathematical_symble('\/', priority))
        else:
            priority += 100
            EEC_Sig_symble.append(Mathematical_symble(ch, priority))
            priority -= 100
    eec_data.append(EEC_Sig_data)
    eec_symble.append(EEC_Sig_symble)


#Seperate all of the EEC in a MTG into the data and symble part
def seperate_MTG(mtg, eec_data, eec_symble):
    for i in range(len(mtg)):
        seperate_EEC(mtg[i], i,  eec_data, eec_symble)



#Remove the "a\/a" and "a\/NULL"
def sortHB(hb_sig_data, hb_sig_symble):

    i = 0
    while i < len(hb_sig_symble):
        if(hb_sig_symble[i].symble == '\/'):
            if (hb_sig_data[i] == "NULL"):
                hb_sig_data.pop(i)
                hb_sig_symble.pop(i)
                i -= 1
            if (hb_sig_data[i+1] == "NULL"):
                hb_sig_data.pop(i+1)
                hb_sig_symble.pop(i)
                i -= 1
        i += 1



def eec2hb(eec_sig_data, eec_sig_symble, hb_data, hb_symble):
    hb_sig_data = []
    hb_sig_symble = []
    tmp_sig_data = eec_sig_data 
    jmp = 0


    #Please look at ReadMe
    for i in range(len(eec_sig_symble)):
        if (eec_sig_symble[i].symble == '-'):
            jmp = 1
            if (i == len(eec_sig_symble) -1):
                hb_sig_data.append(tmp_sig_data[i])

        elif (eec_sig_symble[i].symble == '*'):
            jmp = 1
            tmp_sig_data[i] = "NULL"
            if (i == len(eec_sig_symble) -1):
                hb_sig_data.append(tmp_sig_data[i])

        else:
            hb_sig_symble.append(eec_sig_symble[i])
            if (jmp == 0):
                hb_sig_data.append(tmp_sig_data[i])
            else:
                hb_sig_data.append(tmp_sig_data[i-1])
                jmp = 0
            if (i == len(eec_sig_symble) -1):
                hb_sig_data.append(tmp_sig_data[i+1])



    sortHB(hb_sig_data, hb_sig_symble)
    hb_data.append(hb_sig_data)
    hb_symble.append(hb_sig_symble)

            

def MTG2HB(eec_data, eec_symble, hb_data, hb_symble):
    for i in range(len(eec_data)):
        eec2hb(eec_data[i], eec_symble[i], hb_data, hb_symble)


#Print the seperated part of MTG
def print_MTG(mtg):
    print "MTG: "
    for i in range(len(mtg)):
        print mtg[i]

    print "\nData Part"
    for i in range(len(EEC_data)):
        print EEC_data[i]

    print "\nSymble Part"
    for i in range(len(EEC_symble)):
        print "Symble EEC %d" % i
        for j in range(len(EEC_symble[i])):
            EEC_symble[i][j].displayMath()


#Print the seperated part of HB
def print_HB(hb_data, hb_symble):
    print "\nHB: "
    print "\nData Part"
    for i in range(len(hb_data)):
        print hb_data[i]

    print "\nSymble Part"
    for i in range(len(hb_symble)):
        print "Symble HB %d" % i
        for j in range(len(hb_symble[i])):
            hb_symble[i][j].displayMath()

    

    

#Initialization
EEC_data = []
EEC_symble = []
HB_data = []
HB_symble = []
mtg = []
EEC0 = "(1 1*2)(4 5-6)"
EEC1 = "(1 1*2)(2 3)(4 5-6)"
EEC2 = "(7 8*9)"
EEC3 = "(1-2)(2 3)(4)"
EEC4 = "(1-2 3)"
EEC5 = "(1*2 3)"
mtg.append(EEC0)
mtg.append(EEC1)
mtg.append(EEC2)
mtg.append(EEC3)
mtg.append(EEC4)
mtg.append(EEC5)


#Realization
seperate_MTG(mtg, EEC_data, EEC_symble)
MTG2HB(EEC_data, EEC_symble, HB_data, HB_symble)


#Output
print_HB(HB_data, HB_symble)




