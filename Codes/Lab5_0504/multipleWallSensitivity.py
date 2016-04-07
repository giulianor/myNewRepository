# -*- coding: utf-8 -*-
# you need to import wallHeatTransfer from wallCalculation Script
#I also put costs. I did just a list with apparently possible prices for m^3. and i put those as key of dictionary
from wallCalculation import wallHeatTransfer

def multipleMaterialSensitivity(material_List,sizeList,matCost,resistanceListSeries,resistanceListParallel,resistanceConv_internal,resistanceConv_external, T_inside,T_outside):
    result={}
    i=0
    for material in material_List:
        R4["k"]=material["k"]
        
        for size in sizeList:
            #I will change all parallel sizes/thicknesses!
            R4["length"]=size
            R3["length"]=size
            R5["length"]=size
            heatTransfer = wallHeatTransfer(resistanceListSeries,resistanceListParallel,resistanceConv_internal,resistanceConv_external, T_inside,T_outside)
            varCost=matCost[i]*size*R4["area"]+(R5["area"]+R3["area"])*size*320 #1.1 is cost/m^3 for plaster
            result["material = " + str(material["name"])+", size = "+str(size), "marginal cost = "+str(varCost)]=heatTransfer
            #or
            #inputTuple=(material["name"],size,varCost)
            #result[inputTuple]=heatTransfer
            
        i=i+1
    #return result
    return result


Ri={"name":"Ri","type":"conv","area":0.25,"hConv":10}
R1={"name":"R1","type":"cond","length":0.03,"area":0.25,"k":0.026}
R2={"name":"R2","type":"cond","length":0.02,"area":0.25,"k":0.22}
R3={"name":"R3","type":"cond","length":0.16,"area":0.015,"k":0.22}
R4={"name":"R4","type":"cond","length":0.16,"area":0.22,"k":0.72}
R5={"name":"R5","type":"cond","length":0.16,"area":0.015,"k":0.22}
R6={"name":"R6","type":"cond","length":0.02,"area":0.25,"k":0.22}
Ro={"name":"Ro","type":"conv","area":0.25,"hConv":25}

parallelSet = [R3,R4,R5]
serieSet= [R1,R2,R6]

tIn=20
tOut=-10

# create dictionary with different values of k for the brick object
#input dictionary  
glassProp = {"name":"glass", "k":0.9}
brickProp = {"name":"brick", "k": 0.87}
cement = {"name":"cement", "k": 1.5}
material_list = [ glassProp,brickProp,cement]
costList=[390,285,100] #€/m^3
sizeList=[.2,.35,.95]


alg=multipleMaterialSensitivity(material_list,sizeList,costList,serieSet,parallelSet,Ri,Ro,tIn,tOut)