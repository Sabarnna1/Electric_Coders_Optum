from csv_files import *

def count_allergies():

    allergies = df_allergies['DESCRIPTION'].value_counts().to_dict()
    allergies = {'allergies':[{'allergy':x,'count':allergies[x]} for x in allergies]}
    allergies.update({'number of allergies':len(allergies['allergies'])})
    return (allergies)

def count_conditions():

    conditions = df_conditions['DESCRIPTION'].value_counts().to_dict()
    conditions = {'conditions':[{'conditions':x,'count':conditions[x]} for x in conditions]}
    conditions.update({'number of conditions':len(conditions['conditions'])})
    return (conditions)

def count_immunizer():

    immunizations = df_immunizations['DESCRIPTION'].value_counts().to_dict()
    immunizations = {'immunizations':[{'immunizer':x,'count':immunizations[x]} for x in immunizations]}
    immunizations.update({'number of immunizer':len(immunizations['immunizations'])})
    return (immunizations)

def count_procedures():

    procedures = df_procedures['DESCRIPTION'].value_counts().to_dict()
    procedures = {'procedures':[{'procedures':x,'count':procedures[x]} for x in procedures]}
    procedures.update({'number of procedures':len(procedures['procedures'])})
    return (procedures)

def count_medicine():

    medicine = df_medications['DESCRIPTION'].value_counts().to_dict()
    medicine = {'medicine':[{'medicine':x,'count':medicine[x]} for x in medicine]}
    medicine.update({'number of medicine':len(medicine['medicine'])})
    return (medicine)

def insurance():

    medications = df_medications['PAYER'].value_counts().to_dict()
    medications = [{'Id':x,'count':medications[x]} for x in medications]
    payers = df_payers[['Id','NAME']].to_dict('records')
    res = []
    for x in medications:
        for y in payers:
            if x['Id']==y['Id']:
                res.append({'Id':x['Id'],'NAME':y['NAME'],'count':x['count']})
                break
    return (res)

def prefered_insurance():

    data = insurance()

    for x in data:
        if x['NAME'] == 'NO_INSURANCE':
            data.remove(x)
            break

    df = pd.DataFrame(data)
    df = df.sort_values(by=['count'], ascending=False)
    df['percent'] = (df['count'] / df['count'].sum()) * 100
    del df['count']

    return({'prefered_insurances':df.to_dict('records')})


def used_insurance():

    data = insurance()
    res = []

    for x in data:
        if x['NAME'] == 'NO_INSURANCE':
            res.append({'insurance':'not_used','count':x['count']})
            data.remove(x)
            break

    res.append({'insurance':'used','count':pd.DataFrame(data)['count'].sum()})
    df = pd.DataFrame(res)
    df['percent'] = (df['count'] / df['count'].sum()) * 100
    del df['count']
    
    return({'insurance_transactions':df.to_dict('records')})

# print(used_insurance())

def patient_health_issue_count():

    res = {"patient_health_issue": [
        {
            "factor": "allergies",
            "message": "patients suffering from allergies.",
            "count": int(len(list(set(list(df_allergies['PATIENT'])))))
        },

        {
            "factor": "immunizations",
            "message": "patients taken immunizations.",
            "count": int(len(list(set(list(df_immunizations['PATIENT'])))))
        },

        {
            "factor": "conditions",
            "message": "patients suffering from health conditions.",
            "count": int(len(list(set(list(df_conditions['PATIENT'])))))
        },

        {
            "factor": "medications",
            "message_1": "patients not taking medications.-'count_1'",
            "message_2": "patients taking medications.-'count_2'",
            "count_1": int(len(list(set(list(df_medications['PATIENT']))))),
            "count_2":int(len(list(set(list(df_patients['Id'])))) - len(list(set(list(df_medications['PATIENT'])))))
        },

        {
            "factor": "medications",
            "message": "patients under went procedures.",
            "count": int(len(list(set(list(df_procedures['PATIENT'])))))
        },

        {
            "factor": "alive status",
            "message_1": "patients not dead.- 'count_1'",
            "message_2": "patients dead.- 'count_2'",
            "count_1": int(df_patients['DEATHDATE'].isnull().sum()),
            "count_2":int(df_patients['Id'].unique().shape[0] - df_patients['DEATHDATE'].isnull().sum())
        }
    ]
    }
    return(res)
