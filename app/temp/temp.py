import random
import string
import time


# this method create genarates random alpha numeric key
def get_key():
    key = ''
    chars = string.lowercase + string.digits + string.uppercase
    size = 8
    key = ''.join((random.choice(chars)) for x in range(size))
    current_time = str(int(round(time.time(), 0)))
    key = key + current_time
    print key


if __name__ == '__main__':
    get_key()


@blueprint.route('/<user_id>/tpid/<tpid>/submit', methods=['GET'])
def submit(user_id, tpid):
    tp = test_paper_dao.get_tp_by_id(tpid)
    tp_urs = user_dao.get_responce(user_id, tpid)
    questions = tp['data']
    for question in questions:
        sno = question['sno']
        if tp_urs[str(sno)]:
            mark_obtained = evaluate_responce(question, tp_urs[str(sno)])
            data = tp_urs[str(sno)]
            data['mark_obtained'] = mark_obtained
            user_dao.update_responce(user_id, tpid, data)
        else:
            data = {'question_no': str(sno), 'not_attempted': 'y', 'mark_obtained': 0}
            user_dao.update_responce(user_id, tpid, data)
    return jsonify({'message': 'submit'})
