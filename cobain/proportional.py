#Implementing Proportional Controller with python
#define parameter Kp
#define error
#define set_point

def proportional (Kp,SP):
    last_error = 0
    while True:
        PV = yield last_error
        e = SP - PV
        last_error = Kp*e

controller_1 = proportional(10,5)
controller_1.send(None)

controller_2 = proportional(1,5)
controller_2.send(None)

#konstanta PV
PV = 10

print("Controller 1: MV= ",controller_1.send(PV))
print("Controller 2: MV= ", controller_2.send(PV))
