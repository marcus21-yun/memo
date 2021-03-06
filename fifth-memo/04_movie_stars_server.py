from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta


# HTML을 주는 부분
@app.route('/')
def home():
    return render_template('movie_stars.html')

# REST HTTP Method <=> Database 연관시켜서 정해놨다.

# METHOD
# Create -> POST
# Read -> GET
# Update -> PUT
# Delete -> Delete

# 1. 내가 저장해놨던 스타들의 데이터를 좋아요 순으로 Like 숫자 보여준다.
# DB 에 모든 스타들의 데이터를 내려주는데, 이떄 순서를 Like 순서로 내려주면
# 오름차순 -> 1,2,3,9,10 sort('like',1)
# 내림차순 -> 10,9,3,2,1 sort('like',-1)
# db.mystar.find({},{'_id':0}).sort('like',-1)
# 2. 요청시 보내주는 이름의 스타를 좋아한다. 즉 Like 숫자를 추가해준다.
# type : PUT
# data : Name
# 3. 요청시 보내주는 이름의 스타를 삭제한다. 아예 날려버린다.
# type : DELETE
# data : Name

# API 역할을 하는 부분
@app.route('/api/list', methods=['GET'])
def stars_list():
    # 1. mystar 목록 전체를 검색합니다. ID는 제외하고 like 가 많은 순으로 정렬합니다.
    my_stars = list(db.mystar.find({}, {'_id': False}).sort('like', -1))
    # 참고) find({},{'_id':False}), sort()를 활용하면 굿!
    # 2. 성공하면 success 메시지와 함께 stars_list 목록을 클라이언트에 전달합니다.
    return jsonify({'result': 'success', 'msg': 'list 연결되었습니다!', 'starts_list': my_stars})


@app.route('/api/like', methods=['PUT'])
def star_like(my_star=None):
    # 1. 클라이언트가 전달한 name_give를 name_receive 변수에 넣습니다.
    name_receive = request.form['name_give']
    # 2. mystar 목록에서 find_one으로 name이 name_receive와 일치하는 star를 찾습니다.
    my_star = db.mystar.find_one({"name": name_receive})
    # 3. star의 like 에 1을 더해준 new_like 변수를 만듭니다.
    updated_like = my_star['like'] + 1

    # 4. mystar 목록에서 name이 name_receive인 문서의 like 를 new_like로 변경합니다.
    db.mystar.update_one({"name": name_receive}, {'$set': {"like": updated_like}})
    # 5. 성공하면 success 메시지를 반환합니다.
    return jsonify({'result': 'success', 'msg': 'like 연결되었습니다!'})

@app.route('/api/delete', methods=['DELETE'])
def star_delete():
    # 1. 클라이언트가 전달한 name_give를 name_receive 변수에 넣습니다.
    name_receive = request.form['name_give']

    # 2. mystar 목록에서 delete_one으로 name이 name_receive와 일치하는 star를 제거합니다.
    my_star = db.mystar.delete_one({"name": name_receive})

    # 3. 성공하면 success 메시지를 반환합니다.
    return jsonify({'result': 'success', 'msg': 'delete 연결되었습니다!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
