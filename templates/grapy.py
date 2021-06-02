@app.route("/home/graph")
def graph():
    user_id ="oauth2|kakao|1750600619"
    test_db = pymysql.connect(user='root', passwd='team09', host='35.180.122.212', db='mydb', charset='utf8')
    cursor = test_db.cursor(pymysql.cursors.DictCursor)

    # 이미지 부위 증상별 개수
    sqls = "SELECT distinct  face_detail.forehead, face_detail.cheek_R, face_detail.nose, face_detail.philtrum, face_detail.chin, face_detail.cheek_L, user_face.sym_id FROM face_detail JOIN user_face WHERE user_face.date = (select MAX(date) from user_face) and user_face.user_face_id = face_detail.user_face_id  limit 1" 
    cursor.execute(sqls)
    results = cursor.fetchall()

    # 증상, 원인, 주의사항 script
    sql = "SELECT distinct user_face.date, prescription_data.sym_id, prescription_data.sym_name,prescription_data.symptom, prescription_data.cause, prescription_data.caution, prescription_data.solution FROM prescription_data JOIN user_face WHERE user_face.date = (select MAX(date) from user_face) and user_face.sym_id = prescription_data.sym_id  limit 3" 
    cursor.execute(sql)
    result = cursor.fetchall()

    # 숫자 제거
    symptoms = []
    causes = []
    cautions = []
    solutions = []
    symptom = ''.join([sol for sol in result.symptom if not sol.isdigit()])  
    symptoms.append(symptom)
    cause = ''.join([sol for sol in result.cause if not sol.isdigit()])  
    causes.append(cause)
    caution = ''.join([sol for sol in result.caution if not sol.isdigit()])
    cautions.append(caution)
    solution = ''.join([sol for sol in result.solution if not sol.isdigit()]) 
    solutions.append(solution)  



    # for d in result:
    #     #date = d["date"]
    #     symptom.append(d["symptom"])
    #     cause.append(d["cause"])
    #     caution.append(d['caution'])
    #     solution.append(d['solution'])
        #date = date.split()
             


    return render_template("graph.html", result=result, symptoms=symptoms, causes=causes, cautions=cautions, solutiosn=solutions, results=results)