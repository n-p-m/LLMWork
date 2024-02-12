
import requests


url = 'http://127.0.0.1:5000/recommendation'

customer = { 'sentence':"Give me Sleep Recommendations."}


response = requests.post(url, json=customer).json()
print(response)

# if response['churn'] == True:
#     print('sending promo email to %s' % customer_id)
# else:
#     print('not sending promo email to %s' % customer_id)