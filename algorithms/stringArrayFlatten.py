
def auxFlatten(array,result):
	for element in array:
		if isinstance(element,list):
			auxFlatten(element,result)
		
		else:
			result.append(str(element))
	return result


def arrayFlatten(array):
	return auxFlatten(array,[])


"""P.S : I was not sure if the function should or no deny any tipe of input that did not contain
only strings and lists so my script accepts anything that can me casted into a string"""
