import array as arr

array_num = arr.array('i',[1,3,5,3,7,9,3])
print ("the original array :"+str(array_num ))

print ("number of occerance of number 3 in said array:"
+str(array_num.count(3)))

array_num .reverse()
print ("reverse the order of items:")
print (str(array_num))