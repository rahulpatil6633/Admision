import numpy as np
import config 
import pickle

class Admission():
    def __init__(self,GRE_Score,TOEFL_Score,University_Rating,SOP,LOR,CGPA,Research):
        self.GRE_Score=GRE_Score
        self.TOEFL_Score=TOEFL_Score
        self.University_Rating=University_Rating
        self.SOP=SOP
        self.LOR=LOR
        self.CGPA=CGPA
        self.Research=Research
        
    def load_model(self):
        with open (config.MODEL_FILE_PATH,'rb')as f :
            self.linear_model=pickle.load(f)    
            
        with open (config.STD_SCALER_FILE_PATH,'rb')as f :
            self.std_scaler=pickle.load(f) 
            
    def get_admission(self):
        self.load_model()
        test_array=np.array([self.GRE_Score,self.TOEFL_Score,self.University_Rating,self.SOP,self.LOR,self.CGPA,self.Research])
        
        result=self.std_scaler.transform([test_array])
        final=self.linear_model.predict(result)[0]
        return final
        
        
                 