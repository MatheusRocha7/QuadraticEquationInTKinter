import math
import tkinter as tk



def exit():
	gui.destroy()
	
	

def calculate(a, b, c):
	try:
		aVar = int(coefficientOfA.get())
		bVar = int(coefficientOfB.get())
		cVar = int(coefficientOfC.get())
		delta = bVar**2-4*aVar*cVar
		
		if delta < 0:
			resultLabel["text"] = "This equation has no real solution"
			
		elif delta == 0:
			x = (-bVar+math.sqrt(bVar**2-4*aVar*cVar))/2*aVar
			resultLabel["text"] = "This equation has one solution: {}".format(x)
			
		else:
			x1 = (-bVar+math.sqrt((bVar**2)-(4*(aVar*cVar))))/(2*aVar)
			x2 = (-bVar-math.sqrt((bVar**2)-(4*(aVar*cVar))))/(2*aVar)
			resultLabel["text"] = "This equation has two solutions: {} or {}".format(x1, x2)
			
	except ValueError:
		resultLabel["text"] = "Value Error"



def clear():
	coefficientOfA.delete(0, tk.END)
	coefficientOfB.delete(0, tk.END)
	coefficientOfC.delete(0, tk.END)
	
	

gui = tk.Tk()
gui.title("Quadratic Equation")
gui.geometry("800x600")

abcLabel = tk.Label(gui, text = "A\nB\nC")
abcLabel.place(x = 0, y = 0)

resultLabel = tk.Label(gui, text = "Result")
resultLabel.place(x = 0, y = 230)
	
exitBt = tk.Button(gui, text = "Exit", command = exit)
exitBt.place(x = 600, y = 0)
	
coefficientOfA = tk.Entry(gui)
coefficientOfA.place(x = 30, y = 0)
	
coefficientOfB = tk.Entry(gui)
coefficientOfB.place(x = 30, y = 40)
	
coefficientOfC = tk.Entry(gui)
coefficientOfC.place(x = 30, y = 80)

calculateBt = tk.Button(gui, text = "Calculate", command = lambda: calculate(coefficientOfA, coefficientOfB, coefficientOfC))
calculateBt.place(x = 520, y = 70)

clearBt = tk.Button(gui, text = "Clear",command = clear)
clearBt.place(x = 580, y = 140)

gui["bg"] = "black"
gui.mainloop()