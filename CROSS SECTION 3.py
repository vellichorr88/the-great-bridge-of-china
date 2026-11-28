import math
I = 1163879.635 
y_bar = 58.757 
h = 100

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

print("max comp p")
print(max_p_comp(I, (h-y_bar)))
print("max tens p")
print(max_p_tens(I, (y_bar)))
print("max case 1 p")
print(top_4_sides(65-1.27, 1.27*2, I, (h-y_bar)))

print("max case 2 p")
print(top_3_binded(17.5+0.5*1.27, 2*1.27, I, (h-y_bar)))

print("max web buckle p")
print(web_buckle(h - y_bar - 0.5*1.27, 1.27, I, h - y_bar - 0.5*1.27 ))


print("max glue p at the top")
print(glue_shear_p(I, 20, (100*2*1.27*(h-y_bar - 1*(1.27)))))

print("max glue p at the bottom")
print(glue_shear_p(I, 20, (100*1.27*(y_bar - 0.5*(1.27)))))

print("max shear p")
print(max_shear_p(I, 2*1.27, (100*(1.27)*(y_bar-0.5*(1.27))+2*(1.27*10)*(y_bar-1.5*1.27)+2*1.27*(y_bar)*(0.5*y_bar))))