import copy

class MTG:
    def __init__(self, graph, eec_data, eec_symble):
        self.graph = graph
        self.eec_data = eec_data
        self.eec_symble = eec_symble

class HB:
    def __init__(self, hb_data, hb_symble):
        self.hb_data = hb_data 
        self.hb_symble = hb_symble

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
    tmp_sig_data = copy.copy(eec_sig_data)
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

            

def MTG2HB(mtg, hb):
    seperate_MTG(mtg.graph, mtg.eec_data, mtg.eec_symble)
    
    for i in range(len(mtg.eec_data)):
        eec2hb(mtg.eec_data[i], mtg.eec_symble[i], hb.hb_data, hb.hb_symble)

def get_data_set(hb, data_set):
    for i in range(len(hb.hb_data)):
        data_sig_set = []
        #single data
        if (len(hb.hb_data[i]) == 1):
            data_sig_set.append(hb.hb_data[i][0])
        else:
            for j in range(len(hb.hb_symble[i])):
                data_sig_set.append(hb.hb_data[i][j])
                #seperate by '/\'
                if (hb.hb_symble[i][j].symble == '/\\'):
                    data_sig_set.append('&')

                if (j == len(hb.hb_symble[i]) - 1):
                    data_sig_set.append(hb.hb_data[i][j+1])
                    

        data_set.append(data_sig_set)
                
    

#def belongs_to(hb_data, data_set)

'''
def HB_preserved(hb0, hb1):
    init = 0
    conj = 0
    preserved = True
    tmp_data_set = []
    target_data_set = []
    get_data_set(hb1, target_data_set)

    #Single data in HB_data
    if(len(hb0.hb_symble) == 0):
            belongs_to(hb0.hb_data, target_data_set)


    #Divide the HB_data into several data_set, find if the data_set belongs to the target HB_data
    for i in range(len(hb0.hb_symble)):
            if (hb0.hb_symble.symble == '/\\'):
                    tmp_data_set = copy.copy(hb0.hb_data[init, i])
                    belongs_to(tmp_data_set, target_data_set)
                    init = i + 1
                    conj = 1

    #The whole HB_data is a single data_set
    if (conj == 0):
            tmp_data_set = copy.copy(hb0.hb_data[0, i])
            belongs_to(tmp_data_set, target_data_set)

    return preserved
'''

#Print the seperated part of MTG
def print_MTG(mtg):
    print "MTG: "
    for i in range(len(mtg.graph)):
        print mtg.graph[i]

    print "\nData Part"
    for i in range(len(mtg.eec_data)):
        print mtg.eec_data[i]

    print "\nSymble Part"
    for i in range(len(mtg.eec_symble)):
        print "Symble EEC %d" % i
        for j in range(len(mtg.eec_symble[i])):
            mtg.eec_symble[i][j].displayMath()


#Print the seperated part of HB
def print_HB(hb):
    print "\nHB: "
    print "\nData Part"
    for i in range(len(hb.hb_data)):
        print hb.hb_data[i]

    print "\nSymble Part"
    for i in range(len(hb.hb_symble)):
        print "HB %d" % i
        for j in range(len(hb.hb_symble[i])):
            hb.hb_symble[i][j].displayMath()

    

    

#Initialization
EEC_list = []
EEC_list.append("(1*2 3)")
EEC_list.append("(1-2 3)")
EEC_list.append("(1 2*3)")
EEC_list.append("(1-2)(2 3)(4)")
EEC_list.append("(1 1*2)(4 5-6)")
EEC_list.append("(1 1*2)(2 3)(4 5-6)")

mtg = MTG(EEC_list, [], [])
hb = HB([], [])
data_set = []

#Realization
MTG2HB(mtg, hb)

#get data set 
get_data_set(hb, data_set)

#Output
#print_MTG(mtg)
print_HB(hb)
#print data_set




