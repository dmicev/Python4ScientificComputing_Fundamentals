import assignment3_step2_Micev_new
import U_of_door

series_layers=["gypsum_13mm","common_brick_100mm","fiberboard_13mm","wood_bevel"]
paralel_layers=["glassfiber_90mm","woodstud_90mm"]
fraction_insulation=0.7
Area_walls=105.8 #m^2
Area_door=2.2 #m^2
Area_ceillings=200 #m^2
U_roof=0.25 #W/m^2 K
Twin=-4.8 # degree C - Winter temperature in Piacenza given in Weather data 
Tins=20 # degree C - desired temperature in a room in winter
wall_layers,Rwall_heating,Uwall_heating=assignment3_step2_Micev_new.wall_calc(series_layers,paralel_layers,fraction_insulation)
Rdoor=0.22
thickness=50
Udoor_heating=U_of_door.U_door(Rdoor,thickness,"winter")
print " Thermal conductivity of wall in winter is: "+str(Uwall_heating)+" W/m^2 K"
print " Thermal conductivity of door in winter is: "+str(Udoor_heating)+" W/m^2 K"
print " Thermal conductivity of roof in winter is: "+str(U_roof)+" W/m^2 K"
Q_wall_heating=Area_walls*Uwall_heating*(Tins-Twin)
Q_door_heating=Area_door*Udoor_heating*(Tins-Twin)
Q_roof_heating=Area_ceillings*U_roof*(Tins-Twin)
Q_total_heating=Q_wall_heating+Q_door_heating+Q_roof_heating
print " "
print " Total heat transfer through walls in winter is: " + str(Q_wall_heating)+ " W"
print " Total heat transfer through door in winter is: " + str(Q_door_heating)+ " W"
print " Total heat transfer through roof in winter is: " + str(Q_roof_heating)+ " W"
print " " 
print " Total heat transfer through opaque surfaces in winter is: "+str(Q_total_heating)+ " W."
print " That means that We should provide heat power of "+str (Q_total_heating)+" W in order to gain desired temperature of 20 (for a opaque surfaces)."
