import helpers
import tag_all

import random

def get_sentiment_per_review(review_list):

	interests, analysis = ['HDFC','ICICI','SBI','Canara'], []

	for v in review_list:

		op = tag_all.get_sentiment_and_tag(v)
		sentiment, tags = op[0], op[1]

		bank = ''
		for item in interests:
			if item in v.split() or item.lower() in v.lower().split():
				bank = item
				break

		analysis.append([v, sentiment, tags, bank])

	return analysis

def get_promotions(review_list):

	analysis = get_sentiment_per_review(review_list)

	promotions, notifs = [], {}

	for item in analysis:

		# print(item)

		s, t, focus = item[1], item[2], item[3]

		if len(t) != 0 and len(focus) != 0:

			promotion = ''


			if s == 'positive':

				promotion+= '{} is now better than ever! Home Loans starting at {:.1f}%'.format(focus, random.uniform(5, 7))

				promotions.append(promotion)


				if focus not in notifs:
					notifs[focus] = ['{} is now offering stand in coupons! Avail them at the nearest {} center'.format(focus, t[0])]
				else:
					notifs[focus].append('{} is offering a discount'.format(focus))

			else:

				promotion+='\n\n{} {} is now equipped to serve you better , taking your grievances into account. We are sorry you were dissatisfied with the service.'.format(focus, t[0])

				promotions.append(promotion)

				# if focus not in notifs:
				# 	notifs[focus] = [promotion]
				# else:
				# 	notifs[focus].append(promotion)


	# print(notifs)

	# return promotions, notifs - use to get all
	return notifs

# review_list = ['The service at the hdfc yelehanka branch is really good',
# 			   'The security at ICICI bank is pretty bad',
# 			   'The ac does not work near the hdfc bank',
# 			   'I loved the security near vvpuram, best for night time atm'
# 			   ]

# get_promotions(review_list)

