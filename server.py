from flask import Flask, jsonify, request
from flask_cors import CORS
import urllib

app = Flask(__name__)
CORS(app)

@app.route('/article')
def hello():
	# REPLACE THIS LINE
	# request.args['url'] is how you get url of the article the user is on
	print(urllib.unquote(request.args['url']))

	# Response should be an array of objects
	# Each object should have the title, the url, and the image url
	# We can decide how many articles to output later
	sample_response = [
		{
			'title': 'Premier Doug Ford is holding a weekend House session to try to save the Toronto council cut legislation',
			'url': 'https://www.thestar.com/news/queenspark/2018/09/14/new-pc-government-absolutely-not-panicking-over-toronto-council-downsizing.html',
			'image': 'https://images.thestar.com/oZ8SAZb-kJ4rgydw3UAdDbvwuDg=/1086x724/smart/filters:cb(1536998770695)/https://www.thestar.com/content/dam/thestar/news/queenspark/2018/09/14/new-pc-government-absolutely-not-panicking-over-toronto-council-downsizing/doug_ford.jpg'
		},
		{
			'title': 'In ridings ‘being torn apart,’ incumbents must decide where to run',
			'url': 'https://www.thestar.com/news/gta/2018/09/15/in-ridings-being-torn-apart-incumbents-must-decide-where-to-run.html',
			'image': 'https://images.thestar.com/aNHBQdxMctX_UESstYM0YXUhtnY=/1200x872/smart/filters:cb(1537024214255)/https://www.thestar.com/content/dam/thestar/news/gta/2018/09/15/in-ridings-being-torn-apart-incumbents-must-decide-where-to-run/mike_layton_file_photo.jpg'
		},
		{
			'title': '‘Spunky and tenacious’ orca fighting to keep up with her endangered family was an inspiration to researchers',
			'url': 'https://www.thestar.com/vancouver/2018/09/14/young-orca-declared-dead-leaving-behind-her-critically-endangered-family.html',
			'image': 'https://images.thestar.com/QmVcVicKGJOW8ROY2XAEJj6HuIE=/1086x526/smart/filters:cb(1536979978857)/https://www.thestar.com/content/dam/thestar/vancouver/2018/09/14/young-orca-declared-dead-leaving-behind-her-critically-endangered-family/se201_1230_2014_144608.jpg'
		},

	]
	return jsonify(sample_response)

