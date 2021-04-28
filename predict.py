from mlib import predict

def create_payload():
    while True:
        try:
            age = float(input("Input age (int): "))
            break
        except AssertionError:
            print("Incorrect Value")
    
    while True:
        try:
            hypertension = float(input("Hypertension? (0/1): "))
            assert(hypertension in [0,1])
            break
        except AssertionError:
            print("Incorrect Value")
    
    while True:
        try:
            heart_disease = float(input("Heart Disease? (0/1)"))
            assert (heart_disease) in [0,1]
            break
        except AssertionError:
            print("Incorrect Value")
      
    while True:
        try:
            avg_glucose_level = float(input('Input avg glucose lvl (float): '))
            break
        except AssertionError:
            print("Incorrect Value")
        
    while True:
        try:
            bmi = float(input('Input bmi (float): '))
            break
        except AssertionError:
            print("Incorrect Value")
    
    male = 0
    female = 0
    other = 0
    while True:
        try:
            gender = float(input('Input gender (male:0 | female:1 | other:2)\n'))
            assert (gender in [0,1,2])
            if gender == 0:
                male = 1
            elif gender == 1:
                female = 1
            elif gender == 2:
                other = 1
            break
        except AssertionError:
            print("Incorrect value")
            
    while True:
        try:
            ever_married_yes = float(input('Ever married? (No:0 | Yes:1): '))
            assert (ever_married_yes in [0,1])
            if ever_married_yes == 1:
                ever_married_no = 0
            elif ever_married_yes == 0:
                ever_married_no = 1
            break
        except AssertionError:
            print("Incorrect value")
        
        
    govt_job = 0
    never_worked = 0
    private_work = 0
    self_employed = 0
    at_home_parent = 0
    while True:
        try:
            work_type = float(input('Input work type:\nGovt Job: 1\nNever worked: 2\nPrivate company: 3\nSelf employed: 4\nStay at home parent: 5\n'))
            assert (work_type in [1,2,3,4,5])
            if work_type == 1:
                govt_job = 1
            elif work_type == 2:
                never_worked = 1
            elif work_type == 3:
                private_work = 1
            elif work_type == 4:
                self_employed = 1
            elif work_type == 5:
                at_home_parent = 5
            break
        except AssertionError:
            print("Incorrect value")
    
    rural = 0
    urban = 0
    while True:
        try:
            residence_type = float(input('Input residence type\nRural: 0\nUrban: 1\n'))
            assert (residence_type in [0,1])
            if residence_type == 0:
                rural = 1
            elif residence_type ==1:
                urban = 1
            break
        except AssertionError:
            print("Incorrect value")
    
    smoke_unknown = 0
    former_smoker = 0
    never_smoked = 0
    smoker = 0
    while True:
        try:
            smoking_status = float(input('Input smoking status:\nUnknown: 0\nFormer Smoker: 1\nNever Smoked: 2\nSmoker: 3\n'))
            assert (smoking_status in [0,1,2,3])
            if smoking_status == 0:
                smoke_unknown = 1
            elif smoking_status == 1:
                former_smoker = 1
            elif smoking_status == 2:
                never_smoked = 1
            elif smoking_status == 3:
                smoker = 1
            break
        except AssertionError:
            print("Incorrect value")
            
    payload = {
    "age": {"0": age},
    "hypertension": {"0": hypertension},
    "heart_disease": {"0": heart_disease},
    "avg_glucose_level": {"0": avg_glucose_level},
    "bmi": {"0": bmi
    },
    "gender_Female": {"0": female},
    "gender_Male":{"0": male},
    "gender_Other":{"0": other},
    "ever_married_No": {"0": ever_married_no},
    "ever_married_Yes": {"0": ever_married_yes},
    "work_type_Govt_job": {"0": govt_job},
    "work_type_Never_worked": {"0": never_worked},
    "work_type_Private": {"0": private_work},
    "work_type_Self-employed": {"0": self_employed},
    "work_type_children": {"0": at_home_parent},
    "Residence_type_Rural": {"0": rural},
    "Residence_type_Urban": {"0": urban},
    "smoking_status_Unknown": {"0": smoke_unknown},
    "smoking_status_formerly smoked": {"0": former_smoker},
    "smoking_status_never smoked": {"0": never_smoked},
    "smoking_status_smokes": {"0": smoker}
    }
    return payload

if __name__ == "__main__":
    load = create_payload()
    result = predict(load)
    print(result)
