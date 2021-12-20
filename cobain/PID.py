#Implementing PID Controller with python
#define Kp, Ki, Kd, last_error
#define PID
#define error


def PID (Kp, Ki, Kd, last_error=0):
    e_prev = 0
    I = 0
    time_prev = 0
    MV = last_error
    
    while True:
        t, SP, PV = MV

        #Formula PID
        e = SP - PV

        P = Kp*e
        I = Ki*e*(t-time_prev)
        D = Kd*(e-e_prev)/(t-time_prev)

        MV = last_error+P+I+D

        e_prev = e
        time_prev = t













