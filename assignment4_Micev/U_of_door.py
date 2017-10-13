def U_door (Rdoor_table,thickness,time_of_year):
    Rins=0.12
    Rdoor=Rdoor_table*thickness/25 #thickness must be in mm 
    if time_of_year=="summer":
        U=1/(Rdoor+Rins+0.044)
    if time_of_year=="winter":
        U=1/(Rdoor+Rins+0.03)
    else:
        print "ERROR"
    return U
U_door(1,1,"summer")