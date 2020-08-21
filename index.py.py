from flask import *
from scrapping import s
import pickle
import string
import nltk
from chatb import cb
import random
import re
sc = s()


d = {
		
		1 : {
				"intent":"greetings",
				"response":["Hey","hello","hello How can i help you","Hello",]
			}, 
		2 : {
				"intent":"about",
				"response":[
								"coronaviruses are a type of virus. There are many different kinds, and some cause disease. A newly identified coronavirus, SARS-CoV-2, has caused a worldwide pandemic of respiratory illness, called COVID-19.",
								"A novel coronavirus (CoV) is a new strain of coronavirus.The disease caused by the novel coronavirus first identified in Wuhan, China, has been named coronavirus disease 2019 (COVID-19) – ‘CO’ stands for corona, ‘VI’ for virus, and ‘D’ for disease.Formerly, this disease was referred to as ‘2019 novel coronavirus’ or ‘2019-nCoV.’",
								"A novel coronavirus (CoV) is a new strain of coronavirus.The disease caused by the novel coronavirus first identified in Wuhan, China, has been named coronavirus disease 2019 (COVID-19) – ‘CO’ stands for corona, ‘VI’ for virus, and ‘D’ for disease.                               Formerly, this disease was referred to as ‘2019 novel coronavirus’ or ‘2019-nCoV.’ .The COVID-19 virus is a new virus linked to the same family of viruses as Severe Acute Respiratory Syndrome (SARS) and some types of common cold.",
								"Researchers first identified a coronavirus in 1937, isolating one that was responsible for a type of bronchitis in birds that had the potential to devastate poultry stocks."

						   ]
			},
		3 : {
				"intent":"symptoms",
				"response":[
							  """Symptoms can include fever, cough and shortness of breath. In more severe cases, infection can cause pneumonia or breathing difficulties. More rarely, the disease can be fatal.""",
							  """COVID-19 symptoms include:
							  Cough
							  Fever
							  Shortness of breath
							  Muscle aches
							  Sore throat
							  Unexplained loss of taste or smell
							  Diarrhea
							  Headache""",
							  """Symptoms may include:

							  a runny nose
							  a headache
							  a cough
							  a fever
							  a sore throat
							  generally feeling unwell""",
							  """Cold- or flu-like symptoms usually set in around 2–4 days after the infection develops. Typically, the symptoms are mild, though they vary from person to person. In some people, coronavirus infections are fatal.

							  Symptoms may include:
							  
							  a runny nose
							  a headache
							  a cough
							  a fever
							  a sore throat
							  generally feeling unwell"""
						   ]
			},
		4 : {
				"intent":"precaution",
				"response":[
								"It’s crucial to practice good hygiene, respiratory etiquette and social and physical distancing",
								"Anyone planning a trip overseas should always check the travel advisory for their destination country for any restrictions on entry, quarantine requirements on entry, or other relevant travel advice.",
								" Clean your seat, armrest, touchscreen, etc. with a disinfecting wipe once inside an aircraft or other vehicle. Also use a disinfecting wipe to clean key surfaces, doorknobs, remote controls, etc at the hotel or other accommodation where you and your children are staying.",

								"While traveling, all parents should follow standard hygiene measures for themselves and their children: Wash hands frequently or use an alcohol-based sanitizer with at least 60 per cent alcohol, practice good respiratory hygiene (cover your mouth and nose with your bent elbow or tissue when you cough or sneeze and immediately dispose of the used tissue) and avoid close contact with anyone who is coughing or sneezing.",     
						   ]
			},  
		5 : {
				"intent":"animal",
				"response":[
								".",
								"",
								""
							]
			}, 
		6 : {
				"intent":"vaccine",
				"response":[
							"No vaccine is currently available for COVID-19. However, scientists have now replicated the virus. This could allow for early detection and treatment in people who have the virus but are not experiencing symptoms.",
						   ]
			}, 
		7 : {
				"intent":"Spread",
				"response":[    
								"""Researchers believe that the viruses transmit via fluids in the respiratory system, such as mucus.

								For example, a coronavirus can spread when a person:
								
								coughs or sneezes without covering their mouth, dispersing droplets into the air
								touches someone who has the infection
								touches a surface that has the virus, then touches their own nose, eyes, or mouth""",
								"The virus is transmitted through direct contact with respiratory droplets of an infected person (generated through coughing and sneezing), and touching surfaces contaminated with the virus. The COVID-19 virus may survive on surfaces for several hours, but simple disinfectants can kill it.",
								"People can catch COVID-19 from others who have the virus. The disease can spread from person to person through small droplets from the nose or mouth which are spread when a person with COVID-19 coughs or exhales. These droplets land on objects and surfaces around the person.",
								"As of now, researchers know that the new coronavirus is spread through droplets released into the air when an infected person coughs or sneezes. The droplets generally do not travel more than a few feet, and they fall to the ground (or onto surfaces) in a few seconds — this is why social and physical distancing is effective in preventing the spread.",
							]
			}, 
		8 : {
				"intent":"getinfo",
				"response":[]
			}, 
		9 : {
				"intent":"[period",
				"response":[
								"It appears that symptoms are showing up in people within 14 days of exposure to the virus.",
								"",
								""
							]
			},                                   
											
	  }


news = sc.news()

lemmer = nltk.stem.WordNetLemmatizer()
def LemTokens(tokens):
		return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def Normalize(text):
		return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

vect = pickle.load(open("D:/chatbot/ML/vect.pkl","rb"))
clf = pickle.load(open("D:/chatbot/ML/chat.pkl","rb"))

app = Flask(__name__)
app.config['SECRET_KEY'] = '959121b6ce54245c32bb1c09fae3cf16'
ch = cb()


@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html',p = sc.getc(),news = news )



@app.route("/test",methods = ['GET','POST'])
def test():
	if request.method == 'POST':
		req = request.form
		a = int(req.get("1"))
		b = int(req.get("2"))
		c = int(req.get("3"))
		d = int(req.get("4"))
		l = [a,b,c,d]
		clf = pickle.load(open("D:/chatbot/ML/test.pkl","rb"))
		pred = clf.predict([l])[0]
		if pred == 'Yes':
			flash(f'According to me you have to go for checkup','danger')
		else:
			flash(f'You are safe , so keep maintain social Distancing with others ,Stay Home','success')
		return redirect(url_for('test'))
	return render_template('test.html')


@app.route("/chat")
def abc():
	return render_template("chatbox.html")

bye = ["Bye for now But remember i'm available 24/7 if you want to know something ask me","Bye Stay Home Be safe","Bye Spread Awreness to people ..but remember Don't do mass gathering ","Bye ...Thank You!","Bye ...Be Aware of evertyhing"]
@app.route('/background_process')
def background_process():
	try:
		msg = request.args.get('msg', 0, type=str)
		print("\n\n",msg,"\n\n")
		if  bool(re.search('bye',msg.lower())):
			p =  random.choice(bye)
		elif bool(re.search('thank',msg.lower())): 
			p = "welcome it's my pleasure"
		else:
			p = ch.response(msg,clf,vect)
			p = random.choice(d[p]['response'])
		return jsonify(sent = msg,receive = p)
	except Exception as e:
		return str(e)


if __name__ == "__main__":
	app.run(debug = True)