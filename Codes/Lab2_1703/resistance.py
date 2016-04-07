A=raw_input("area: ");
mat=raw_input("material: ");
Type=raw_input("type: ");

if mat=="glass":
    k=str(.96);
    if Type=="window":
        L=str(.004);
    else:
        L=raw_input("lenght:: ")
        
if mat=="brick":
    k=str(.04);
    if Type=="wall":
        L=str(.76);
    else:
        L=raw_input("length:: ")


else:
    k=raw_input("conductivity: ")
    L=raw_input("length:: ")
    
R=str(float(k)/float(L)/float(A))

print ("love is our resistance: "+R)