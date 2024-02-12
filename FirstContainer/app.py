from python_LLM_Code import intialize_chain
from flask import Flask, request, jsonify

app = Flask(__name__)

model=intialize_chain()


@app.route('/recommendation', methods=['POST'])
def recommendation():

    input=request.get_json()
    sentence=input['sentence']
    # print("Inside recommendation")
    # print("The input we get is ->")
    # print("Input is->")
    # print(input)
    # print("Input type is->"+str(type(input)))

    # return jsonify({'recommendation':sentence+"POgPOgPOgPOgPOgPOgPOgPOg"})
    output=model.run(sentence)
    return jsonify({'recommendation':output})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


