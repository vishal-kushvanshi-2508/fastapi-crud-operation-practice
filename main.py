

# check version 
# import fastapi 
# print(fastapi.__version__)

from fastapi import FastAPI, Request
from mockData import student_detail
from validation import student_detail_validation 

app = FastAPI()

#### GET method

# mack function as rout
# mack home page api 
@app.get("/student_detail")
def all_student_detail():
    return {
        "message" : "all_student_detail", 
        "data" : student_detail
    }

# path params
@app.get("/student_detail/{product_id}")
def single_student(product_id: int):
    for data in student_detail:
        if data.get("id") == product_id:
            return data
    return f"product_id does not exist"


# # query params
# @app.get("/condition_wise_student")
# def condition_wise_student_detail(name:str , roll:int):
#     for data in student_detail:
#         if data.get("name") == name and data.get("roll") ==  roll:
#             return data
#     return {
#         "message" : "this data is not available in student detail", 
#         "data" : student_detail
#     }



# query params
# get all key value using fastapi request
@app.get("/condition_wise_student")
def request_wise_student_detail(request:Request):
    print("request", request)
    query_params = dict(request.query_params)
    print("request query_params ", query_params)


    for data in student_detail:
        print(data)
        print("query_params", query_params)
        if data.get("name") == query_params.get("name") and data.get("roll") ==  int(query_params.get("roll")):
            return data
    return {
        "message" : "this data is not available in student detail", 
        "data" : student_detail
    }



#### POST method
@app.post("/create_student")
def create_student(student: student_detail_validation):
    
    python_dict = student.model_dump()
    student_detail.append(python_dict)
    return {
        "message" : "student detail add successfully", 
        "data" : student_detail
    }




#### PUT method
@app.put("/update_student/{student_id}")
def update_student(student: student_detail_validation, student_id:int):
    python_dict = student.model_dump()

    for index , data in enumerate(student_detail):
        if student_id == data.get("id"):
            student_detail[index] = python_dict
            return {
                "message" : "student detail update successfully", 
                "data" : student_detail
            }
        
    return {
        "message" : "student_id does not exist",
        "data" : student_detail
    }



#### DELETE method
@app.delete("/delete_student/{student_id}")
def delete_student(student_id:int):

    for index, data in enumerate(student_detail):
        if student_id == data.get("id"):
            delete_data = student_detail.pop(index)
            return {
                "message" : "student detail delete successfully", 
                "data" : delete_data
            }
        
    return {
        "message" : "student_id does not exist",
        "student_detail" : student_detail
    }
