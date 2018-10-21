# A collection of helper functions to help interact with Flask
def gen_response(my_dict: dict):
    """
    Helper function to generate a response object that allows CORS.
    Taken from: https://github.com/choyiny/novelty-escape/blob/master/app.py
    """
    from flask import jsonify
    response = jsonify(my_dict)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
