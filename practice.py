import matplotlib.pyplot as plt 
import pandas as pd


def test_mat():
 fig=plt.figure()
 plt.title("Matplotlib Practice")
 plt.xlabel("x-axis")
 plt.ylabel("y-axis")
 x=[1,2,3,4,5] 
 y=[1,2,3,4,5] 
 y2=[1.5,2.5,3.5,4.5,5.5]
 #plt.plot(x,y,color='black',linestyle='--',marker='o')
 #plt.bar(x,y)
 #plt.scatter(x,y2,color='red')

 plt.plot(x, y, label="Squared")
 plt.plot(x, y2, label="Squared")

 plt.show()

def test_pand():
 data = {
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
    "Product_A": [200, 250, 180, 300, 280],
    "Product_B": [150, 220, 210, 260, 290]
 }

 df = pd.DataFrame(data)

 df.plot(x="Day")
 plt.show()

test_pand() 