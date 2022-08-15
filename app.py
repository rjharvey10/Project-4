from flask import Flask, render_template, Response, request
# from config import app_key
import requests
import pandas as pd
import pickle
from sqlalchemy import create_engine
app = Flask(__name__)


# create my own API from the data stored in Postgres database
@app.route('/get_marvel_dc')
def hello():
    engine = create_engine("postgresql://jqzzrfsdewgljj:e5fb494866ce503b8bced245afe5c2068f1c7a94a9a242a8b41413def015f15c@ec2-54-157-16-196.compute-1.amazonaws.com:5432/d4k7shgqb7gn6i")
    df = pd.read_sql_table("marveldc",con=engine)
    return Response(df.to_json(orient="records"), mimetype='application/json')
# load the index.html when requesting the https://localhost:5000

@app.route('/', methods =["GET","POST"])
def gfg():
    if request.method == "POST":
        id = request.form.get("id")
        hair = request.form.get("hair")
        sex = request.form.get("sex")
        gsm = request.form.get("gsm")
        eye = request.form.get("eye")
        studio = request.form.get("studio")
        print(id,hair,sex,gsm,eye,studio)
        input_data = [id,hair,sex,gsm,eye,studio]
        df = pd.DataFrame(columns=['ID_Identity Unknown', 'ID_Known to Authorities Identity',\
       'ID_No Dual Identity', 'ID_Public Identity', 'ID_Secret Identity',\
       'EYE_Amber Eyes', 'EYE_Auburn Hair', 'EYE_Black Eyeballs',\
       'EYE_Black Eyes', 'EYE_Blue Eyes', 'EYE_Brown Eyes',\
       'EYE_Compound Eyes', 'EYE_Gold Eyes', 'EYE_Green Eyes', 'EYE_Grey Eyes',\
       'EYE_Hazel Eyes', 'EYE_Magenta Eyes', 'EYE_Multiple Eyes',\
       'EYE_No Eyes', 'EYE_One Eye', 'EYE_Orange Eyes',\
       'EYE_Photocellular Eyes', 'EYE_Pink Eyes', 'EYE_Purple Eyes',\
       'EYE_Red Eyes', 'EYE_Silver Eyes', 'EYE_Variable Eyes',\
       'EYE_Violet Eyes', 'EYE_White Eyes', 'EYE_Yellow Eyeballs',\
       'EYE_Yellow Eyes', 'HAIR_Auburn Hair', 'HAIR_Bald', 'HAIR_Black Hair',\
       'HAIR_Blond Hair', 'HAIR_Blue Hair', 'HAIR_Bronze Hair',\
       'HAIR_Brown Hair', 'HAIR_Gold Hair', 'HAIR_Green Hair',\
       'HAIR_Grey Hair', 'HAIR_Light Brown Hair', 'HAIR_Magenta Hair',\
       'HAIR_No Hair', 'HAIR_Orange Hair', 'HAIR_Orange-brown Hair',\
       'HAIR_Pink Hair', 'HAIR_Platinum Blond Hair', 'HAIR_Purple Hair',\
       'HAIR_Red Hair', 'HAIR_Reddish Blond Hair', 'HAIR_Reddish Brown Hair',\
       'HAIR_Silver Hair', 'HAIR_Strawberry Blond Hair', 'HAIR_Variable Hair',\
       'HAIR_Violet Hair', 'HAIR_White Hair', 'HAIR_Yellow Hair',\
       'SEX_Agender Characters', 'SEX_Female Characters',\
       'SEX_Genderfluid Characters', 'SEX_Genderless Characters',\
       'SEX_Male Characters', 'SEX_Transgender Characters', 'SEX_Unknown',\
       'GSM_Bisexual Characters', 'GSM_Genderfluid Characters',\
       'GSM_Heterosexual', 'GSM_Homosexual Characters',\
       'GSM_Pansexual Characters', 'GSM_Transgender Characters', 'STUDIO_DC',\
       'STUDIO_MARVEL'])
        df.loc[0] = 0
        print(df)
        for column_name in df.columns:
            for c in input_data:
                if c in column_name:
                    df.loc[0, column_name] = 1
        print(df)   
        pickled_model = pickle.load(open('MarvelDCmodel.pkl', 'rb'))
        outcome = pickled_model.predict(df)
        print(outcome)
        if outcome[0] == 1:
            result = "Good Character"
        else:
            result = "Bad Character"
    return render_template('index.html',text=result)

if __name__ == '__main__':
    app.run(debug=True)