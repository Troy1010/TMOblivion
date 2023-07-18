# Bleed equation
* This alternative equation would allow for a CurvatureConstant (CC)
y = (x / SBV)
z = {
	if CC == 0: y
	if CC >  0: y^(1+CC)
	if CC <  0: 1 - (1 - y)^(1+abs(CC))
}
t = z * SUD