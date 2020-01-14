import numpy as np

G = 6.67e-11
PI = 3.1415

print("Stellar Calculator (Semi-major axis and planet radius)")
print("This calculator uses transit photometry data to calculate the semi-major axis and planet radius of a star-exoplanet system. It takes in the following values:")
print("  T (seconds):   Orbital period")
print("  M (kilograms): Stellar mass")
print("  R_S (metres):  Stellar radius")
print("  t:             transit depth")
print("The program produces the following values: ")
print("  a (metres):    Semi-major axis")
print("  R_P (metres):  Planet radius")
print("")
print("Enter the following values: (sigma is the uncertainty, enter 0 if none recorded.")
print("")

T = float(input("[        T] "))
sigma_T = float(input("[  sigma_T] "))
M = float(input("[        M] "))
sigma_M = float(input("[  sigma_M] "))
R_S = float(input("[      R_S] "))
sigma_R_S = float(input("[sigma_R_S] "))
t = float(input("[        t] "))
sigma_t = float(input("[  sigma_t] "))

def r(T, M):
    global G, PI
    left = (G * M) / (4 * PI * PI)
    value = left * T*T
    return pow(value, 1/3)

def dr_dM(T, M):
    global G, PI
    top = G * T*T
    bottom = 12 * PI*PI * r(T, M)**2
    return top / bottom

def dr_dT(T, M):
    global G, PI
    top = G * M * T
    bottom = 6 * PI*PI * r(T, M)**2
    return top / bottom

def sigma_r(T, sigma_T, M, sigma_M):
    value = (dr_dT(T, M) * sigma_T)**2 + (dr_dM(T, M) * sigma_M)**2
    return np.sqrt(value)

def R_P(R_S, t):
    return R_S * np.sqrt(t)

def dR_P_dR_S(R_S, t):
    return np.sqrt(t)

def dR_P_dt(R_S, t):
    return R_S / np.sqrt(4 * t)

def sigma_R_P(R_S, sigma_R_S, t, sigma_t):
    value = (dR_P_dR_S(R_S, t) * sigma_R_S)**2 + (dR_P_dt(R_S, t) * sigma_t)**2
    return np.sqrt(value)

print("The following values have been calculated. They are presented in the form value (error).")
print("[        a] " + ("%E" % r(T, M)) + " (" + ("%E" % sigma_r(T, sigma_T, M, sigma_M)) + ")")
print("[      R_P] " + ("%E" % R_P(R_S, t)) + " (" + ("%E" % sigma_R_P(R_S, sigma_R_S, t, sigma_t)) + ")")
