# you need to import wallHeatTransfer from wallCalculation Script
from wallCalculation import wallHeatTransfer

#two versions of the function, called 1 and 2.
#the first one returns simply a dictionary.
#the second one returns a list of dictionaries.
def materialSensitivity1(material_List,resistanceListSeries,resistanceListParallel,resistanceConv_internal,resistanceConv_external, T_inside,T_outside):
    result={}
    for material in material_List:
        R4["k"]=material["k"]
        heatTransfer = wallHeatTransfer(resistanceListSeries,resistanceListParallel,resistanceConv_internal,resistanceConv_external, T_inside,T_outside)
        
        result[material["name"]]=heatTransfer

    #return result
    return result
    #output is like this: result_sensitivity=  {"glass":253,"brick": 350,... } 

def materialSensitivity2(material_List,resistanceListSeries,resistanceListParallel,resistanceConv_internal,resistanceConv_external, T_inside,T_outside):
    i=0
    Result=range(0,len(material_List))
    for material in material_List:
        R4["k"]=material["k"]
        heatTransfer = wallHeatTransfer(resistanceListSeries,resistanceListParallel,resistanceConv_internal,resistanceConv_external, T_inside,T_outside)
        
        
        Result[i]={"name":material["name"],"heatTransfer":heatTransfer}
        i=i+1
    #return Result
    return Result
    #ouput is a list of dictionaries [{"name":"glass","HeatTransfer" : 253},{"name":"brick","HeatTransfer" : 352}]   

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
tOut=10

# create dictionary with different values of k for the brick object
#input dictionary  
glassProp = {"name":"glass", "k":0.9}
brickProp = {"name":"brick", "k": 0.87}
cement = {"name":"cement", "k": 1.5}
material_list = [ glassProp,brickProp,cement]


alg1=materialSensitivity1(material_list,serieSet,parallelSet,Ri,Ro,tIn,tOut)
alg2=materialSensitivity2(material_list,serieSet,parallelSet,Ri,Ro,tIn,tOut)