from flask import Flask, request, jsonify
from flask_cors import CORS
from bardapi import Bard, BardCookies
import requests
import os
from dotenv import load_dotenv

app = Flask(__name__)
CORS(app)
load_dotenv()
#token = os.getenv("BARD_API_KEY")
token = "dQhdekeGC9PoIRCb_rdRTLQphr0yzfoTmhMoh8gcCYHmseWIEvW3Gm_ko-vEN-ixOLtuMA."
print(token)

cookie_dict = {
    "__Secure-1PSID": "dwhdevbryMc6gg3OI8eEi5iDWkTpagJGwG6szZ_QSrAIM2TTSR4B7RHfB3-ej5O6B_CybQ.",
    "__Secure-1PSIDTS": "sidts-CjIBPVxjSr-pwHsjyx_4F4khFD3p-CghabmZavuGEiAgje6mTdelNw1Z5Rl751UxM0WlpBAA",
    # Any cookie values you want to pass session object.
}

bard = BardCookies(cookie_dict=cookie_dict)


#session = requests.Session()
#session.cookies.set("__Secure-1PSID", "bard __Secure-1PSID dQhdekeGC9PoIRCb_rdRTLQphr0yzfoTmhMoh8gcCYHmseWIEvW3Gm_ko-vEN-ixOLtuMA.")
#session.cookies.set( "__Secure-1PSIDCC", "bard __Secure-1PSIDCC ACA-OxOJ6_eOrZYeh9paKqUwYKJjGPsPFNJmKE81coWhXDjA-dfmdlquUnj12GFxtWpsLckXeA")
#session.cookies.set("__Secure-1PSIDTS", "bard __Secure-1PSIDTS sidts-CjIBPVxjSovkdTEkMb0snKdlWxA_LRtXWYNJ9IPMU-sMnaQLH3lONQjZ6uivdbefdAi3mhAA")
#session.headers = {
#        "Host": "bard.google.com",
#        "X-Same-Domain": "1",
#        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.4472.114 Safari/537.36",
#        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
#        "Origin": "https://bard.google.com",
#        "Referer": "https://bard.google.com/",
# }


@app.route('/api/query', methods=['POST'])
def query_bard():
    data = request.get_json()
    query = data['query']

    #bard = Bard(token=token)
    result = bard.get_answer(query)
    print(result)
    return jsonify({'content': result['content']})

if __name__ == '__main__':
    app.run(debug=True, port=5173)  # Run on port 5173