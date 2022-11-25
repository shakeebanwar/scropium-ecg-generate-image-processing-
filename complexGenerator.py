import croping as cp
import sec_3 as sc
import lead1 as l1
import lead2 as l2
import lead3 as l3
import ecgremovehorizantal as line

lead1 = [1,4,7,10]
lead2 = [2,5,8,11]
lead3 = [3,6,9,12]


cp.imagecroper()
line.blackRemove()
sc.complexgenerator()
l1.preprocess(lead1,0)
l2.preprocess1(lead2,1)
l3.preprocess2(lead3,2)
l3.combine()
