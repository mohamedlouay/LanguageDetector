import tkinter as tk
import pickle
import pandas as pd



def languageDetector(inputText):
    import string
    import pickle
    global bestModel
    global resultatFrame

    
    #remove noise
    inputText =inputText.replace('[0-9]', ' ')
    inputText=inputText.replace('['+string.punctuation+']', ' ')
    inputText=inputText.lower()
    
    #predection
    predectedLanguage = bestModel.predict([inputText])
    probability = bestModel.predict_proba([inputText])
    allProb= pd.DataFrame(probability, columns=bestModel.classes_)
    
    #dispaly resultat
    
    for child in resultatFrame.winfo_children():
        child.destroy()

    
    predResult_label = tk.Label(resultatFrame,fg="#12183d",bg='#f5f5f5',font=("Arial", 15),
                           padx=50,pady=50,
                           text="this text is written in "+predectedLanguage)
    
    predResult_label.pack()

    resultatFrame.pack()
    
    
#load saved model
saveModel =open('myModel.pckl','rb')
bestModel = pickle.load(saveModel)
saveModel.close()    

#windows
app = tk.Tk()
app.title("Language Detector")
app.minsize(1020, 700)
width_value = app.winfo_screenwidth()
height_value = app.winfo_screenheight()
app.geometry(str(width_value) + "x" + str(height_value))
app.configure(bg='#f5f5f5')


#frames
middleFrame = tk.Frame(app, background='#f5f5f5', width=700, height=height_value)

title_label = tk.Label(middleFrame,fg="#12183d",bg='#f5f5f5',font=("Arial", 15),padx=50,pady=50, text="Welcome to our Language Detector \n Our model support 5 languages (en,es,fr,it,de)")
title_label.pack()

# Create text widget and specify size.
textArea = tk.Text(middleFrame, height = 10, width = 70)
textArea.pack()

# Create button for detect text.
btnDetect = tk.Button(middleFrame, text = "Detect",bg="#6378ff",fg="white",font=("Arial", 15),pady=5,width = 50 ,command= lambda: languageDetector(textArea.get("1.0",'end-1c')))
btnDetect.pack(pady=10)
#resultat frame
resultatFrame =tk.Frame(middleFrame)



middleFrame.pack()


app.mainloop()


