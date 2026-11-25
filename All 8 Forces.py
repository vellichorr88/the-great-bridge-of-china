import math
# hi
def flex_stress(I, y):
    return (1236.7478399999993*y/I)

def shear_stress(I, b, Q):
    return ((4.9124*Q)/(I*b))

def sigma_crit(k, b, t):
    return ((k * math.pi**2 * 4000) / (12 * (1-0.2**2))) * (t/b)**2

def max_p_comp(I, y_comp):
    return (6/flex_stress(I, y_comp))

def max_p_tens(I, y_tens):
    return(30/flex_stress(I, y_tens))

def max_shear_p(I, b_web, Q_mid):
    return (4/shear_stress(I, b_web, Q_mid))

def glue_shear_p(I, b_glue, Q_glue):
    return (2/shear_stress(I, b_glue, Q_glue))

def top_4_sides(b, t, I, y_comp):
    return sigma_crit(4, b, t)/flex_stress(I, y_comp)

def top_3_binded(b, t, I, y_comp):
    return sigma_crit(0.425, b, t)/flex_stress(I, y_comp)

def web_buckle(b_comp_web, t, I, y_web_top):
    """Case 3: Web under flexural compression (k = 6).
    y_web_top: distance from neutral axis to the top of the web (not top of flange).
    b_comp_web: height of the compressed portion of the web.
    """
    return sigma_crit(6, b_comp_web, t)/flex_stress(I, y_web_top)

def max_p_web_shear_buckle(h, a, w, I, b_web, Q_mid):
    tau = ((5*math.pi**2*4000)/((12 * (1-0.2**2))))*((w/h)**2 + (w/a)**2)
    return tau/(shear_stress(I, b_web, Q_mid))


