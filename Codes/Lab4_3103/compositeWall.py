# -*- coding: utf-8 -*-
def compositeWallSeries(resistanceList):
    """This function takes as input a list of resistances, each of which is a dictionary.
    It computes the series of the resistances token as input.
    """
    R_series=0
    resistancesResults = {}
    for resistance in resistanceList:
        A = resistance["area"]
        L = resistance["length"]
        k = resistance["k"]
        R= round(L/(k*A),2)          

        R_series=R_series+R
        nameOfResistance = resistance["name"]
        resistancesResults[nameOfResistance] = round(R,2)
    R_tot=R_series
    resistancesResults["R_total"] = round(R_tot,2)  
    return resistancesResults  
    
    resistancesResults= round(R_series,2)
    return resistancesResults


def compositeWallParallel(resistanceList):
    """This function takes as input a list of resistances, each of which is a dictionary.
    It computes the parallel of the resistances token as input.
    """
    
    resistancesResults = {}
    R_tot_inv=0
    for resistance in resistanceList:
        A = resistance["area"]
        L = resistance["length"]
        k = resistance["k"]
        R= round(L/(k*A),3)
        R_inv= 1/(R)          
        R_tot_inv += R_inv
        nameOfResistance = resistance["name"]
        resistancesResults[nameOfResistance] = round(R,2)
    R_tot = 1/R_tot_inv
    resistancesResults["R_total"] = round(R_tot,2)  
    return resistancesResults  



def compositeWall(resistanceListSeries,resistanceListParallel):
    """This function takes as input two lists of resistances, each of which is a dictionary.
    It computes the series of the 1st list, the parallel of 2nd and sum it to return the total resistance given by the series of the two resistances computed.
    res={"name":"str","type":"'cond' or 'conv'","length":m,"area":m^2,"k":W/(m*deg°C)}
    resistance given is deg°C/W
    """
    composite={}
    rSeries=compositeWallSeries(resistanceListSeries)
    rParallel=compositeWallParallel(resistanceListParallel)
    rSeriesTot=rSeries["R_total"]
    rParallelTot=rParallel["R_total"]
    rTot=rSeriesTot+rParallelTot
    composite["series"]=rSeries
    composite["parallel"]=rParallel
    composite["rWall"]=rTot
    
    return composite
    

def wallConvection(resistanceConv):
    
    resistanceResult={}
    h=resistanceConv["hConv"]
    A=resistanceConv["area"]
    name=resistanceConv["name"]
    R=round(1/float(h)/float(A),2);
    resistanceResult[name]=round(R,4)    
    resistanceResult["Rconv"]=round(R,4)
    
    return resistanceResult

def wallResistance(listSeries,listParallel,convInt,convExt):
    wall=compositeWall(listSeries,listParallel)
    rWall=wall["rWall"]
    
    conv1=wallConvection(convInt)
    rConv1=conv1["Rconv"]
    
    conv2=wallConvection(convExt)
    rConv2=conv2["Rconv"]
    
    rTot=rWall+rConv1+rConv2
    
    tot={}
    tot["wall"]=wall
    tot["convInt"]=conv1
    tot["convExt"]=conv2
    tot["rTot"]=rTot
    
    return tot
    
    
    
Ri={"name":"Ri","type":"conv","area":1.25,"hConv":10}
R1={"name":"R1","type":"cond","length":0.03,"area":1.25,"k":0.026}
R2={"name":"R2","type":"cond","length":0.02,"area":1.25,"k":0.22}
R3={"name":"R3","type":"cond","length":0.16,"area":0.075,"k":0.22}
R4={"name":"R4","type":"cond","length":0.16,"area":1.1,"k":0.72}
R5={"name":"R5","type":"cond","length":0.16,"area":0.075,"k":0.22}
R6={"name":"R6","type":"cond","length":0.02,"area":1.25,"k":0.22}
Ro={"name":"Ro","type":"conv","area":1.25,"hConv":25}
series=[R1,R2,R6]
parallel=[R3,R4,R5]

a=wallResistance(series,parallel,Ri,Ro)