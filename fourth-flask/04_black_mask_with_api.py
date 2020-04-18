from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.


# HTML을 주는 부분
@app.route('/')
def home():
    return render_template('black_mask.html')


# API 역할을 하는 부분
@app.route('/reviews', methods=['POST'])
def write_review():
    # name_receive 로 클라이언트가 준 name 가져오기
    # name_receive = request.form['name_give']
    # print(name_receive)
    # return jsonify({'result': 'success', 'msg': '이 요청은 POST!','name_receive': name_receive})

    # # quantity_receive로 클라이언트가 준 quantity 가져오기
    # quantity_receive = request.form['quantity_give']
    # # address_receive로 클라이언트가 준 address 가져오기
    # address_receive = request.form['address_give']
    # # phone_receive로 클라이언트가 준 phone 가져오기
    # phone_receive = request.form['phone_give']
    #
    # # DB에 삽입할 order_list 만들기
    # order_list = {
    #     'name': name_receive,
    #     'quantity': quantity_receive,
    #     'address': address_receive,
    #     'phone': phone_receive
    # }
    #
    # # orders 에 order_list 저장하기
    # db.orders.insert_one(order_list)

    return jsonify({'result': 'success', 'msg': '이 요청은 POST!'})
    # 성공 여부 & 성공 메시지 반환
    # return jsonify({'result': 'success', 'msg': '리뷰가 성공적으로 작성되었습니다.'})

    # print(order_list)
    # return jsonify({'result': 'success', 'msg': '이 요청은 POST!','title_receive': order_list})


@app.route('/reviews', methods=['GET'])
def read_reviews():
    return jsonify({'result': 'success', 'msg': '이 요청은 GET!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
