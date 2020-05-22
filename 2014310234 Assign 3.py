

Logs = input()
RawData = Logs.split()

NumOfLogs = int(RawData[0])

RawData.remove(RawData[0])

Length = len(RawData)

IdLoc = []
for i in range(len(RawData)):
    if len(RawData[i]) == 10:
        IdLoc.append(i)


Data = []
for i in range(NumOfLogs):
    Logs = []
    Data.append(Logs)
    
for j in range(1, len(IdLoc)):
    
    for k in range(IdLoc[j-1], IdLoc[j]):
        
        Data[j-1].append(RawData[k])

for i in range(IdLoc[-1], Length):
    Data[-1].append(RawData[i])


AmPmIdx = []
for i in range(len(Data)):
    if  Data[i][-1] == 'am' or Data[i][-1] == 'pm':
        AmPmIdx.append(i)

AmPm = []
for i in AmPmIdx:
    AmPm.append(Data[i][-1])

AmNum = AmPm.count('am')

Hrs = []
for i in range(len(Data)):
    Hrs.append(int(Data[i][2].split(':')[0]))

    
Bifurcation = []
if len(AmPmIdx) == 0:
    for i in range(len(Hrs)):
        if Hrs[i] >= 12:
            Bifurcation.append(i)
    for i in range(0, Bifurcation[0]):
        Data[i].append('am')
    for j in range(Bifurcation[0], len(Data)):
        Data[j].append('pm')
elif len(AmPmIdx) != 0:
    if AmPm[0] == 'am':
        for i in range(AmPmIdx[0]):
            Data[i].append('am')
        for j in range(0, AmPmIdx[AmNum-1]):
            if Data[j][-1] != 'am':
                Data[j].append('am')
            elif Data[j][-1] == 'am':
                Data[j] == Data[j]
        for k in range(AmPmIdx[AmNum-1]+1, len(Data)):
            if Data[k][-1] != 'pm':
                Data[k].append('pm')
            elif Data[k][-1] == 'pm':
                Data[k] == Data[k]
        
    elif AmPm[0] == 'pm':
        for j in range(1, AmPmIdx[0]):
            if int(Data[j][2].split(':')[0]) < 12:
                if int(Data[j][2].split(':')[0]) <= int(Data[j-1][2].split(':')[0]) and int(Data[j][2].split(':')[0]) < int(Data[j+1][2].split(':')[0]):
                    Data[j].append('am')
                elif int(Data[j][2].split(':')[0]) <= int(Data[j-1][2].split(':')[0]) and int(Data[j][2].split(':')[0]) > int(Data[j+1][2].split(':')[0]):
                    Data[j].append('pm')
                elif int(Data[j][2].split(':')[0]) > int(Data[j-1][2].split(':')[0]):
                    Data[j].append('am')
            elif int(Data[j][2].split(':')[0]) >=12:
                Data[j].append('pm')
        for k in range(AmPmIdx[0]+1, len(Data)):
            if Data[k][-1] != 'pm':
                Data[k].append('pm')
            elif Data[k][-1] == 'pm':
                Data[k] == Data[k]
        if Data[1][-1] == 'am':
            Data[0].append('am')
        elif Data[1][-1] == 'pm':
            if int(Data[0][2].split(':')[0]) < 12:
                Data[0].append('am')
            elif int(Data[0][2].split(':')[0]) >= 12:
                Data[0].append('pm')


            
for i in range(len(Data)):
    if 'am' in Data[i][-1]:
        del Data[i][-1]
    elif 'pm' in Data[i][-1]:
        if int(Data[i][2].split(':')[0]) >= 12:
            del Data[i][-1]
        elif int(Data[i][2].split(':')[0]) < 12:
            del Data[i][-1]
            TimeTmp = Data[i][2].split(':')
            TimeTmp[0] = str(int(TimeTmp[0]) + 12)
            Data[i][2] = ":".join(TimeTmp)


def function0(List):
    global Data
    
    VisitLogs = []
    for i in range(len(List)):
        if 'V' in List[i][1]:
            VisitLogs.append(List[i])
            
    VisitHr = []
    for i in range(len(VisitLogs)):
        Hr = int(VisitLogs[i][2].split(':')[0])
        VisitHr.append(Hr)                                                  #VisitHr = [11, 12, 13, 13, 13, 14, 15]

    VisitHrHeader = list(set(VisitHr))                      #VisitHrHeader = [11, 12, 13, 14, 15]
    VisitHrHeader = sorted(VisitHrHeader)

    VisitId = []
    for i in range(len(VisitHrHeader)):
        VisitIdHr = []
        VisitId.append(VisitIdHr)

    for i in range(len(VisitId)):
        VisitId[i].append(VisitHrHeader[i])
        
    for j in range(len(VisitHrHeader)):
        for k in range(len(VisitLogs)):
            if VisitHrHeader[j] == int(VisitLogs[k][2].split(':')[0]):
                VisitId[j].append(VisitLogs[k][0])

    VisitIdwithoutDup = []
    for i in range(len(VisitId)):
        a = list(set(VisitId[i]))
        VisitIdwithoutDup.append(a)

    LogNum = []
    for i in range(len(VisitIdwithoutDup)):
        LogNum.append(len(VisitIdwithoutDup[i])-1)

                      
    MaxVisit = max(LogNum)                                          # 3

    MaxVisitIndex = LogNum.index(max(LogNum))    #2

    MaxVisitHr = VisitHrHeader[MaxVisitIndex]                       #이게 어떻게 되는거지? 시간순서라 그런가
    
    
    return MaxVisitHr, MaxVisit

a, b = function0(Data)
print(a, b)


def function1(List):
    global Data
    ExitLogs = []
    for i in range(len(List)):
        if 'E' in List[i][1]:
            ExitLogs.append(List[i])

    ExitHr = []
    for i in range(len(ExitLogs)):
        Hr = int(ExitLogs[i][2].split(':')[0])
        ExitHr.append(Hr)                                       #[14, 15, 17, 17]

    ExitHrHeader = list(set(ExitHr))                      #ExitHrHeader = [14, 15, 17]
    ExitHrHeader = sorted(ExitHrHeader)
    
    ExitId = []
    for i in range(len(ExitHrHeader)):
        ExitIdHr = []
        ExitId.append(ExitIdHr)

    for i in range(len(ExitId)):
        ExitId[i].append(ExitHrHeader[i])
        
    for j in range(len(ExitHrHeader)):
        for k in range(len(ExitLogs)):
            if ExitHrHeader[j] == int(ExitLogs[k][2].split(':')[0]):
                ExitId[j].append(ExitLogs[k][0])

    ExitIdwithoutDup = []
    for i in range(len(ExitId)):
        a = list(set(ExitId[i]))
        ExitIdwithoutDup.append(a)

    LogNum = []
    for i in range(len(ExitIdwithoutDup)):
        LogNum.append(len(ExitIdwithoutDup[i])-1)

    MaxExit = max(LogNum)                                   #2

    MaxExitIndex = LogNum.index(max(LogNum))            #1

    MaxExitHr = ExitHrHeader[MaxExitIndex]              #17

    return MaxExitHr, MaxExit

c, d = function1(Data)
print (c, d)


def function2(List):
    global Data
    VisitLogs = []
    for i in range(len(List)):
        if 'V' in List[i][1]:
            VisitLogs.append(List[i])
            
    Interval = []
    for i in range(len(VisitLogs)-1):
        if int(VisitLogs[i][2].split(':')[0]) == int(VisitLogs[i+1][2].split(':')[0]):
            TimeGap = int(VisitLogs[i+1][2].split(':')[1]) - int(VisitLogs[i][2].split(':')[1])
        elif int(VisitLogs[i][2].split(':')[0]) != int(VisitLogs[i+1][2].split(':')[0]):
            TimeGap = int(VisitLogs[i+1][2].split(':')[1]) + (60*(int(VisitLogs[i+1][2].split(':')[0]) - int(VisitLogs[i][2].split(':')[0])) - int(VisitLogs[i][2].split(':')[1]))
        Interval.append(TimeGap)

    MinInterval = min(Interval)                                 #분으로 표시
    
    
    MultiMinInterval = []                                                   #최소값이 같은게 여러개
    for i in Interval:
        if i == MinInterval:
            MultiMinInterval.append(i)

    Check = []
    if len(MultiMinInterval) == 1:
        MinIntervalIndex = Interval.index(min(Interval))
    elif len(MultiMinInterval) != 1:
        for i in range(len(Interval)):
            if MinInterval == Interval[i]:
                Check.append(i)
                for j in Check:
                    if VisitLogs[j][0] != VisitLogs[j+1][0]:
                        MinIntervalIndex = j
                             
    
    
    VisitorId1 = VisitLogs[MinIntervalIndex][0]
    VisitorId2 = VisitLogs[MinIntervalIndex+1][0]
        
    if MinInterval >= 60 and MinInterval < 120:
        Minute = MinInterval-60
        ConvertedInterval = '01:'+str(Minute)
    elif MinInterval >= 120:
        Minute = MinInterval-120
        ConvertedInterval = '02'+str(Minute)
    elif MinInterval < 60:
        if MinInterval < 10:
            ConvertedInterval = '00:0'+str(MinInterval)           #120분 이상 차이나는 경우?
        elif MinInterval >= 10:
            ConvertedInterval = '00:'+str(MinInterval)
        
    return VisitorId1, VisitorId2, ConvertedInterval

e, f, g = function2(Data)
print (e, f, g)
            

    

def function3(List):
    global Data
    ID = []
    for i in range(len(Data)):
        ID.append(Data[i][0])

    ID = list(set(ID))

    IDType = []
    for i in range(len(ID)):
        Type = []
        IDType.append(Type)

    for i in range(len(ID)):
        IDType[i].append(ID[i])
        for j in range(len(Data)):
            if ID[i] == Data[j][0]:
                IDType[i].append(Data[j][1])

    Cheat = []
    for i in range(len(IDType)):
        if IDType[i][1] == 'V':
            for j in range(1, len(IDType[i])-1):
                if IDType[i][j] == IDType[i][j+1] == 'V':
                    Cheat.append(IDType[i][0])
            
            
        
    return Cheat

for i in function3(Data):
    print(i, end=' ')

print(' ')


def function4(List):
    global Data
    ID = []
    for i in range(len(Data)):
        ID.append(Data[i][0])

    ID = list(set(ID))

    IDType = []
    for i in range(len(ID)):
        Type = []
        IDType.append(Type)

    for i in range(len(ID)):
        IDType[i].append(ID[i])
        for j in range(len(Data)):
            if ID[i] == Data[j][0]:
                IDType[i].append(Data[j][1])

    Cheat = []
    for i in range(len(IDType)):
        if IDType[i][1] == 'V':
            for j in range(1, len(IDType[i])-1):
                if IDType[i][j] == IDType[i][j+1] == 'E':
                    Cheat.append(IDType[i][0])
        elif IDType[i][1] == 'E':
            Cheat.append(IDType[i][0])
            
    return Cheat

for i in function4(Data):
    print(i, end=' ')

